## Automatización de actualización de ventas

Se implementó un script de ETL (`scripts_ETL/...py`) para automatizar la actualización de ventas.

**Flujo:**
1. Lee archivos nuevos de ventas desde `input/`.
2. Valida el esquema de columnas.
3. Normaliza fechas (`SalesDate`).
4. Genera `row_hash` por registro para evitar duplicados.
5. Inserta en una base local SQLite como staging (idempotente).
6. Carga la información a BigQuery.
7. Envía notificación por email al finalizar.
8. Mueve el archivo procesado a `processed/`.

**Requisitos de ejecución (local):**
- Variables de entorno en `.env` (credenciales de BigQuery y Gmail).
- Dependencias: pandas, python-dotenv, google-cloud-bigquery.

**Nota:**
La deduplicación está garantizada mediante `row_hash` en la capa de staging. Como mejora futura, se puede consolidar una tabla final en BigQuery deduplicada por `row_hash` mediante MERGE/SELECT DISTINCT.
