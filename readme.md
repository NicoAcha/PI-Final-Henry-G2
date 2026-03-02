📊 Prisma Analytics – Optimización de Inventarios y Rentabilidad

👥 Equipo

Facundo Spellanzon – Data Analyst

Federico Acosta – Data Analyst

Diego Muller – Data Analyst

Martina Iara Guerberoff – Project Manager

Pedro Nicolás Acha – Lead Project Manager

🎯 Objetivo del proyecto

Desarrollar un modelo analítico orientado a mejorar la gestión de inventarios y la rentabilidad en una empresa del sector retail, integrando múltiples fuentes de datos para facilitar la toma de decisiones estratégicas.

El foco principal fue detectar oportunidades de mejora en:

Rotación de productos

Niveles de stock

Rentabilidad por sucursal

Eficiencia operativa

🚀 Alcance del proyecto

Limpieza y estandarización de datasets de inventario, compras y ventas

Integración de fuentes en un pipeline unificado

Diseño de un modelo dimensional (esquema estrella)

Análisis exploratorio de datos (EDA)

Automatización de la actualización de ventas

Construcción de dashboards ejecutivos en Power BI

Soporte a la toma de decisiones basada en datos

🧠 Principales hallazgos

El sobrestock y la baja rotación impactan significativamente en la rentabilidad

Existen diferencias relevantes en desempeño entre sucursales

La segmentación de productos permite optimizar compras y niveles de stock

La visibilidad de costos y ventas mejora la planificación comercial

⚙️ Tecnologías utilizadas

Python (Jupyter Notebook)

BigQuery

Power BI

SQL

🗂️ Estructura del repositorio
/notebooks

limpieza_*.ipynb → limpieza individual por dataset

00_master_pipeline.ipynb → integración de datos

/docs

ERD_model.md → explicación del modelo dimensional

notas_limpieza.md → decisiones de transformación

/scripts_ETL

Scripts de automatización para actualización de ventas y mantenimiento del modelo.

🏗️ Modelo de datos

El proyecto utiliza un esquema estrella compuesto por:

Dimensiones

Product

Vendor

Branch

Date

Tablas de hechos

Fact_Sales → ingresos y cantidades vendidas

Fact_Purchases → costos y volúmenes de compra

Fact_InventorySnapshot → estado de stock por fecha

🔄 Pipeline

Limpieza de datasets

Generación de datos estandarizados

Integración en pipeline

Validación de calidad

Carga a BigQuery

Actualización automática de ventas

📊 Dashboard en Power BI

El archivo principal se encuentra en la carpeta /powerbi.

Nombre: dapt10_g2_PF.pbix

Permite analizar:

Rentabilidad por sucursal

Gestión de inventarios

Rotación de productos

Desempeño comercial

Para visualizar:

Descargar el archivo

Abrir en Power BI Desktop
