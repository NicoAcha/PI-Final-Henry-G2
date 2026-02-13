CREATE TABLE henry-pf-g2.pf_inventory.dim_product (
  product_id INT64,
  description STRING,
  size STRING,
  volume FLOAT64,
  classification STRING,
  );

CREATE TABLE henry-pf-g2.pf_inventory.dim_vendor (
  vendor_id INT64,
  vendor_name STRING
  );

CREATE TABLE henry-pf-g2.pf_inventory.dim_date (
  date_id DATE,
  year INT64,
  month INT64,
  day INT64,
  week INT64,
  quarter INT64
  );

CREATE TABLE henry-pf-g2.pf_inventory.dim_branch (
  branch_id INT64,
  branch_name STRING
  );

CREATE TABLE henry-pf-g2.pf_inventory.dim_purchase_order (
  po_number INT64,
  order_date DATE,
  vendor_id INT64,
  branch_id INT64
  );

CREATE TABLE henry-pf-g2.pf_inventory.fact_sales (
  sales_id INT64,
  date_id DATE,
  product_id INT64,
  branch_id INT64,
  sales_qty INT64,
  sales_dollars FLOAT64,
  sales_price FLOAT64
  );

CREATE TABLE henry-pf-g2.pf_inventory.fact_inventory_snapshot (
  snapshot_id INT64,
  date_id DATE,
  product_id INT64,
  branch_id INT64,
  onhand_qty INT64,
  onhand_value FLOAT64
  );

CREATE TABLE henryf-g2.pf_inventory.fact_purchase_details (
  po_number INT64,
  product_id INT64,
  purchase_qty INT64,
  purchase_dollars FLOAT64,
  unit_purchase_price FLOAT64
  )
