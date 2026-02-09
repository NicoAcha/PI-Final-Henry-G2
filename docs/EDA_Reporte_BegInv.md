# Reporte de Análisis Exploratorio (EDA): Inventario Inicial

**Archivo Analizado:** `BegInvFINAL12312016.csv`
**Fecha del Análisis:** 8 de Febrero, 2026
**Autor:** Fede

## 1. Resumen Ejecutivo
El dataset contiene el inventario inicial del año. Los datos muestran un negocio enfocado en **productos de gama media-baja (High Volume / Mid-Range Price)**. No es una boutique de licores de lujo, sino un retail/mayorista de alta rotación.

---

## 2. Análisis de Precios (`Price`)
**Objetivo:** Entender la estrategia de precios y la gama de productos.

### Hallazgos Principales:
* **Distribución:** Fuertemente sesgada a la derecha (Right Skewed). La inmensa mayoría de productos son baratos.
* **Rango de Precios:**
    * El **50%** del inventario cuesta **$14.99** o menos.
    * El **75%** cuesta menos de **$21.99**.
    * El **99%** de los productos cuestan menos de **$100**.
* **Psicología de Precios:** Se detectaron picos claros en las barreras psicológicas de **$9.99**, **$14.99** y **$19.99**.
* **Anomalías:** Se detectaron **2 registros con Precio $0.00**.
    * Caso 1: Stock 0 (Lógico, producto inactivo).
    * Caso 2: Stock 2 (Posible muestra o error de sistema).

**Decisión para el modelo:** Se recomienda filtrar o tratar los precios >$100 como *outliers* para visualizaciones generales, ya que distorsionan la escala.

---

## 3. Análisis de Stock (`onHand`)
**Objetivo:** Detectar problemas de acumulación y capacidad de almacén.

### Hallazgos Principales:
* **Comportamiento General:** La mayoría de las tiendas tienen un stock bajo/moderado por producto (< 50 unidades).
* **Los "Monstruos" (Outliers):** Existen tiendas con **más de 1,000 unidades** de un solo producto. Esto sugiere operaciones de tipo mayorista o centros de distribución.
* **El Segmento "Volumen Alto":**
    * Se identificó un clúster de productos con stock entre **100 y 800 unidades**.
    * Su precio promedio es de **~$21.39**, lo que indica una fuerte inversión en marcas líderes de gama media (no solo alcohol barato).
    * *Dato clave:* Hay productos de ~$35 con stocks de casi 900 unidades (aprox $30k parados en stock).

---

## 4. Ranking de Productos
**Objetivo:** Identificar los "Best Sellers" o productos clave por volumen físico.

### Top Marcas (por cantidad de botellas):

1.  Smirnoff 80 Proof: 37621 unidades
2.  Capt Morgan Spiced Rum: 35440 unidades
3.  Bacardi Superior Rum: 34717 unidades

---

## 5. Conclusión Técnica
El archivo `BegInv` está limpio en su estructura general. Los valores nulos/ceros son insignificantes (<0.01%). El negocio depende del volumen de venta en el rango de **$10 - $20 USD**.

**Siguiente paso sugerido:** Cruzar esta información con `EndInv` para calcular la Rotación de Inventario y Ventas Reales.