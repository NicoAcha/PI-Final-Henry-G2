# Data Model – PRISMA Retail Analytics

El modelo fue diseñado siguiendo un enfoque de Star Schema para facilitar el análisis comercial, de inventario y rentabilidad.

## Tablas de hechos
- Fact_Sales: contiene las transacciones de ventas.
- Fact_Inventory_Snapshot: estado del inventario en el tiempo.
- Fact_Purchase_Details: compras por producto.

## Dimensiones
- Dim_Product
- Dim_Store
- Dim_Date

## Objetivo del modelo
Permitir un análisis integrado entre ventas, inventario y compras para mejorar la toma de decisiones en retail.
