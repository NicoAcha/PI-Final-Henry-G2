1. Carga e Inspección Inicial:
Se cargó el dataset BegInvFINAL12312016.csv conteniendo el inventario inicial. Se detectaron 206529 filas y 9 columnas. La estructura general es consistente, identificando las columnas clave como InventoryId, Store y Brand.

2. Conversión de Tipos:

Fechas: La columna startDate se encontraba en formato texto (object) y fue convertida exitosamente a datetime64[ns] para permitir análisis temporales y evitar errores de formato.

Numéricos: onHand (enteros) y Price (flotantes) se detectaron con los tipos correctos, por lo que no requirieron conversión.


3. Validación de Integridad (Nulos):
Se realizó un escaneo de valores nulos y se confirmó que el dataset se encuentra íntegro (0 nulos) en todas sus columnas.

Nota de Automatización: Se incluyó en el script una lógica de imputación condicional para la columna City. Aunque no fue necesaria en esta ejecución, se mantiene activa en el código para asegurar la robustez del ETL ante futuras ingestas de datos que podrían llegar incompletos.


4. Resultado Final:
Se generó un dataset limpio y consistente, sin valores nulos en campos críticos y con los formatos de fecha estandarizados, exportado como BegInvFINAL12312016_clean.csv, listo para su ingesta en la base de datos automatizada.