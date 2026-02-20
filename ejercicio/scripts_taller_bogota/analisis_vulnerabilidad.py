"""
Análisis de Índice de Vulnerabilidad por Localidad
Bogotá, 2007-2023
"""

import pandas as pd

print("=" * 60)
print("  ÍNDICE DE VULNERABILIDAD POR LOCALIDAD")
print("=" * 60)

# Cargar datos
df = pd.read_excel("Historico_IV.xlsx")

print(f"\n📋 Datos cargados: {len(df)} registros")
print(f"   Período: {df['FECHA_INICIO'].min().year} - {df['FECHA_FIN'].max().year}")

# 1. Distribución del índice de vulnerabilidad
print("\n📊 DISTRIBUCIÓN DEL ÍNDICE DE VULNERABILIDAD:")
conteo = df['INDICE_VULNERABILIDAD'].value_counts()
total = len(df)

for nivel, cantidad in conteo.items():
    porcentaje = (cantidad / total) * 100
    barra = "█" * int(porcentaje / 2)
    print(f"   {nivel:12} {cantidad:4} ({porcentaje:5.1f}%) {barra}")

# 2. Localidades
print(f"\n🗺️  LOCALIDADES ({df['LocNombre'].nunique()} en total):")
localidades = sorted(df['LocNombre'].unique())
for i, loc in enumerate(localidades, 1):
    print(f"   {i:2}. {loc}")

# 3. Análisis por localidad actual (último año)
ultimo_anio = df['FECHA_FIN'].max().year
df_actual = df[df['FECHA_FIN'].dt.year == ultimo_anio]

print(f"\n📈 VULNERABILIDAD EN {ultimo_anio}:")
for _, row in df_actual.iterrows():
    print(f"   {row['LocNombre']:20} → {row['INDICE_VULNERABILIDAD']}")

print("\n" + "=" * 60)
print("  ✅ Análisis completado")
print("=" * 60)
