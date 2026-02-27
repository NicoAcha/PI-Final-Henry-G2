import sqlite3
from pathlib import Path
from dotenv import load_dotenv
from google.cloud import bigquery
import os

load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

DB_PATH = Path("database") / "ventas.db"

def create_db_file():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.close()

def create_sales_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            InventoryId TEXT,
            Store INTEGER,
            Brand INTEGER,
            Description TEXT,
            Size TEXT,
            SalesQuantity INTEGER,
            SalesDollars REAL,
            SalesPrice REAL,
            SalesDate TEXT,
            Volume INTEGER,
            Classification INTEGER,
            ExciseTax REAL,
            VendorNo INTEGER,
            VendorName TEXT,
            row_hash TEXT UNIQUE
        );
    """)

    conn.commit()
    conn.close()

import pandas as pd

INPUT_DIR = Path("input")

def get_input_files():
    return sorted(INPUT_DIR.glob("*.csv"))

def read_sales_csv(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(file_path, sep=";")
    return df

EXPECTED_COLUMNS = [
    "InventoryId","Store","Brand","Description","Size","SalesQuantity","SalesDollars",
    "SalesPrice","SalesDate","Volume","Classification","ExciseTax","VendorNo","VendorName"
]

def validate_columns(df: pd.DataFrame):
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    extra = [c for c in df.columns if c not in EXPECTED_COLUMNS]

    if missing or extra:
        raise ValueError(f"Columnas inválidas. Faltan: {missing} | Sobran: {extra}")

def parse_sales_date(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["SalesDate"] = pd.to_datetime(df["SalesDate"], errors="coerce")
    return df

import hashlib

def add_row_hash(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Convertimos todo a string consistente y armamos una firma por fila
    def row_signature(row):
        parts = []
        for col in EXPECTED_COLUMNS:
            val = row[col]
            if pd.isna(val):
                parts.append("")
            else:
                parts.append(str(val).strip())
        return "|".join(parts)

    df["row_hash"] = df.apply(lambda r: hashlib.sha256(row_signature(r).encode("utf-8")).hexdigest(), axis=1)
    return df

def insert_sales(df: pd.DataFrame) -> int:
    conn = sqlite3.connect(DB_PATH)

    # Armamos el df con el orden de columnas como en la tabla
    out = df.copy()
    out["SalesDate"] = out["SalesDate"].dt.strftime("%Y-%m-%d")  # guardamos como texto ISO

    cols = EXPECTED_COLUMNS + ["row_hash"]
    out = out[cols]

    # Insertamos fila por fila para poder ignorar duplicados por row_hash UNIQUE
    inserted = 0
    cur = conn.cursor()

    sql = """
        INSERT OR IGNORE INTO sales (
            InventoryId, Store, Brand, Description, Size,
            SalesQuantity, SalesDollars, SalesPrice, SalesDate,
            Volume, Classification, ExciseTax, VendorNo, VendorName,
            row_hash
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """
    for _, row in out.iterrows():
        cur.execute(sql, tuple(row.values))
        inserted += cur.rowcount  # 1 si insertó, 0 si ignoró (duplicado)

    conn.commit()
    conn.close()
    return inserted

def load_to_bigquery(df: pd.DataFrame):
    client = bigquery.Client()

    table_id = "etl-ventas.ventas_ds.sales_test"

    df_bq = df.copy()
    df_bq["SalesDate"] = df_bq["SalesDate"].dt.date

    print("BQ DF rows:", len(df_bq))
    print("BQ unique hashes:", df_bq["row_hash"].nunique())
    job = client.load_table_from_dataframe(df_bq, table_id)
    job.result()

    print("Datos cargados en BigQuery.")



import shutil

PROCESSED_DIR = Path("processed")
ERROR_DIR = Path("error")

def move_to_processed(file_path: Path):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PROCESSED_DIR / file_path.name
    shutil.move(str(file_path), str(dest))


import smtplib
from email.message import EmailMessage

def send_email_notification(inserted_rows):
    user = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_APP_PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = "ETL Ventas - Ejecución Exitosa"
    msg["From"] = user
    msg["To"] = user
    msg.set_content(f"La ejecución del ETL finalizó correctamente.\nRegistros insertados: {inserted_rows}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(user, password)
        smtp.send_message(msg)









if __name__ == "__main__":
    create_db_file()
    create_sales_table()
    print("OK: DB y tabla sales creadas/verificadas.")
    files = get_input_files()
    print("Archivos encontrados:", len(files))

    df = read_sales_csv(files[0])
    print("Primer archivo:", files[0].name)
    print("Filas:", len(df))
    print("Columnas:", list(df.columns))
    validate_columns(df)
    print("OK: columnas válidas.")

    df = parse_sales_date(df)
    print("SalesDate nulos tras parseo:", df["SalesDate"].isna().sum())

    df = add_row_hash(df)
    print("Hash ejemplo:", df["row_hash"].iloc[0])
    print("Hashes únicos:", df["row_hash"].nunique())

    inserted = insert_sales(df)
    print("Insertadas:", inserted)
    load_to_bigquery(df)
    send_email_notification(inserted)

    move_to_processed(files[0])
    print("OK: movido a processed.")

