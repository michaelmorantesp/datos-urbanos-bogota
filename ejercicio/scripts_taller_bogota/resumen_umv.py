"""
📊 Resumen de Intervenciones de Mantenimiento Vial (UMV)
"""

import pandas as pd

print("=" * 60)
print("🚧 INTERVENCIONES DE MANTENIMIENTO VIAL - UMV")
print("=" * 60)

# Cargar datos
df = pd.read_excel("Historico_UMV.xlsx")

print(f"\n📋 Total de intervenciones: {len(df)}")

# Intervenciones por localidad
print("\n🏘️ TOP 5 LOCALIDADES CON MÁS INTERVENCIONES:")
top_localidades = df['Nombre Localidad'].value_counts().head(5)
for loc, cantidad in top_localidades.items():
    print(f"   • {loc}: {cantidad} intervenciones")

# Tipo de malla vial
print("\n🛣️ INTERVENCIONES POR TIPO DE MALLA VIAL:")
malla = df[' Tipo Malla Vial '].value_counts()
for tipo, cantidad in malla.items():
    porcentaje = (cantidad / len(df)) * 100
    print(f"   {tipo.strip()}: {cantidad} ({porcentaje:.1f}%)")

# Área total intervenida
area_total = df['Área\nSegmento (m2)'].sum()
print(f"\n📐 ÁREA TOTAL INTERVENIDA: {area_total:,.0f} m²")
print(f"   Equivalente a {area_total/10000:.1f} hectáreas")

# Longitud total
long_total = df['Longitud Segmento (ML)'].sum()
print(f"\n📏 LONGITUD TOTAL: {long_total:,.0f} metros")
print(f"   Equivalente a {long_total/1000:.1f} kilómetros")

print("\n" + "=" * 60)
print("✅ Resumen completado")
print("=" * 60)
