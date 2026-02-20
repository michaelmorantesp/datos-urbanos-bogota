"""
Exploración de datos de calidad del aire - PM10
Bogotá, 2012-2023
"""

import pandas as pd

print("=" * 60)
print("  ANÁLISIS DE CALIDAD DEL AIRE - PM10")
print("=" * 60)

# Cargar el archivo Excel
df = pd.read_excel("Historico_PM10.xlsx")

# 1. Información básica
print("\n📋 INFORMACIÓN BÁSICA")
print(f"   Número de filas: {df.shape[0]}")
print(f"   Número de columnas: {df.shape[1]}")

# 2. Ver las columnas
print("\n📑 COLUMNAS DEL DATASET:")
for i, col in enumerate(df.columns, 1):
    print(f"   {i}. {col}")

# 3. Primeras filas
print("\n📄 PRIMERAS 5 FILAS:")
print(df.head())

# 4. Estadísticas de la concentración de PM10
print("\n📊 ESTADÍSTICAS DE conc_pm10 (µg/m³):")
print(f"   Mínimo:           {df['conc_pm10'].min()}")
print(f"   Máximo:           {df['conc_pm10'].max()}")
print(f"   Media:            {df['conc_pm10'].mean():.2f}")
print(f"   Mediana:          {df['conc_pm10'].median()}")
print(f"   Desv. Estándar:   {df['conc_pm10'].std():.2f}")

# 5. Años disponibles
print("\n📅 AÑOS EN EL DATASET:")
df['anio'] = pd.to_datetime(df['fecha_ini']).dt.year
print(f"   Desde: {df['anio'].min()}")
print(f"   Hasta: {df['anio'].max()}")
print(f"   Total años: {df['anio'].nunique()}")

print("\n" + "=" * 60)
print("  ✅ Exploración completada")
print("=" * 60)