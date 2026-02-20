"""
Resumen de Intervenciones de Mantenimiento Vial
Unidad de Mantenimiento Vial (UMV), 2017-2018
"""

import pandas as pd

print("=" * 60)
print("  MANTENIMIENTO VIAL - UMV")
print("=" * 60)

# Cargar datos
df = pd.read_excel("Historico_UMV.xlsx")

print(f"\n📋 Total de intervenciones: {len(df):,}")

# 1. Top localidades
print("\n🏘️  TOP 10 LOCALIDADES CON MÁS INTERVENCIONES:")
top_loc = df['Nombre Localidad'].value_counts().head(10)
for i, (loc, cant) in enumerate(top_loc.items(), 1):
    pct = (cant / len(df)) * 100
    barra = "█" * int(pct)
    print(f"   {i:2}. {loc:20} {cant:4} ({pct:5.1f}%) {barra}")

# 2. Tipo de malla vial
print("\n🛣️  INTERVENCIONES POR TIPO DE MALLA VIAL:")
# Limpiar espacios en la columna
col_malla = ' Tipo Malla Vial '
malla = df[col_malla].str.strip().value_counts()
for tipo, cant in malla.items():
    pct = (cant / len(df)) * 100
    print(f"   {tipo:5} → {cant:4} intervenciones ({pct:.1f}%)")

# 3. Métricas de área y longitud
print("\n📐 MÉTRICAS DE INTERVENCIÓN:")
# Nota: las columnas tienen caracteres especiales
col_area = [c for c in df.columns if 'rea' in c.lower() and 'segmento' in c.lower()][0]
col_long = 'Longitud Segmento (ML)'

area_total = df[col_area].sum()
long_total = df[col_long].sum()

print(f"   Área total intervenida:    {area_total:,.0f} m²")
print(f"   Equivalente a:             {area_total/10000:.1f} hectáreas")
print(f"   Longitud total:            {long_total:,.0f} metros")
print(f"   Equivalente a:             {long_total/1000:.1f} km")

# 4. Tipo de actividad (mostrando problema de calidad de datos)
print("\n🔧 TIPO DE ACTIVIDAD (observa la inconsistencia en los datos):")
actividades = df['Tipo de Actividad'].value_counts().head(8)
for act, cant in actividades.items():
    print(f"   '{act}': {cant}")

print("\n   ⚠️  Nota: Hay variantes del mismo valor (Parcheo, parcheo, ' Parcheo ')")
print("   Esto es un problema común de calidad de datos.")

print("\n" + "=" * 60)
print("  ✅ Resumen completado")
print("=" * 60)
