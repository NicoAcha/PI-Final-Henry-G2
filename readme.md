# Proyecto final - Data Analytics Henry

## Equipo
- Facundo Spellanzon - Data Analyst
- Federico Acosta - Data Analyst
- Diego Muller - Data Analyst
- Martina Iara Guerberoff - Proyect Manager
- Pedro Nicolás Acha - Lead Proyect Manager

## Objetivo
Análisis y optimización de inventarios utilizando:
- Python (Jupyter)
- BigQuery
- Power BI

## Alcance del proyecto
- Limpieza y estandarización de 6 datasets de inventario, compras y ventas  
- Integración en un pipeline único  
- Modelado dimensional (star schema)  
- Análisis exploratorio (EDA)  
- Carga y explotación en BigQuery y Power BI

## Estructura del repositorio
/notebooks

limpieza_*.ipynb → limpieza individual por dataset

00_master_pipeline.ipynb → integrador de datos

/docs

ERD_model.md → explicación del modelo estrella

notas_limpieza.md → decisiones por dataset

## Modelo de datos
El proyecto utiliza un **esquema estrella** compuesto por:

**Dimensiones**
- Product  
- Vendor  
- Branch  
- Date  

**Tablas de hechos**
- Fact_Sales → cantidades e ingresos por venta  
- Fact_Purchases → costos y volúmenes de compra  
- Fact_InventorySnapshot → estado de stock por fecha

## Pipeline actual
1. Limpieza individual de cada CSV  
2. Generación de `_clean.csv`  
3. Integración en `00_master_pipeline.ipynb`  
4. Validación de nulos y duplicados  
5. Próximo: carga a BigQuery

## Próximos pasos
- Definir llaves de unión entre datasets  
- Construir tablas fact/dim en BigQuery  
- Desarrollo de métricas (margen, rotación, cobertura)  
- Dashboard en Power BI
