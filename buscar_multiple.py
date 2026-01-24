#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Buscador Múltiple de Expedientes
Busca un expediente en múltiples juzgados/salas automáticamente
"""

import json
import sys

def buscar_expediente_multiple(numero_expediente, categoria_juzgados):
    """
    Genera entradas JSON para buscar un expediente en múltiples juzgados

    Args:
        numero_expediente: Número del expediente (ej: "615/2019")
        categoria_juzgados: "PENAL", "CIVIL", "FAMILIAR", "MERCANTIL", "TODAS_SALAS"
    """

    categorias = {
        "PENAL": [
            "SEGUNDA SALA PENAL ORAL",
            "TERCERA SALA PENAL ORAL",
            "SEPTIMA SALA PENAL TRADICIONAL",
            "OCTAVA SALA PENAL ORAL",
            "NOVENA SALA PENAL ORAL"
        ],
        "CIVIL": [
            "JUZGADO PRIMERO CIVIL CANCUN",
            "JUZGADO SEGUNDO CIVIL CANCUN",
            "JUZGADO TERCERO CIVIL CANCUN",
            "JUZGADO CUARTO CIVIL CANCUN",
            "JUZGADO ORAL CIVIL CANCUN",
            "JUZGADO PRIMERO CIVIL PLAYA",
            "JUZGADO SEGUNDO CIVIL PLAYA",
            "JUZGADO ORAL CIVIL PLAYA",
            "JUZGADO CIVIL CHETUMAL",
            "JUZGADO CIVIL ORAL CHETUMAL"
        ],
        "FAMILIAR": [
            "JUZGADO PRIMERO FAMILIAR ORAL CANCUN",
            "JUZGADO SEGUNDO FAMILIAR ORAL CANCUN",
            "JUZGADO SEGUNDO DE LO FAMILIAR CANCUN",
            "JUZGADO FAMILIAR DE PRIMERA INSTANCIA CANCUN",
            "JUZGADO FAMILIAR ORAL PLAYA",
            "JUZGADO FAMILIAR PRIMERA INSTANCIA PLAYA",
            "JUZGADO FAMILIAR ORAL CHETUMAL",
            "JUZGADO FAMILIAR PRIMERA INSTANCIA CHETUMAL"
        ],
        "MERCANTIL": [
            "JUZGADO PRIMERO MERCANTIL CANCUN",
            "JUZGADO SEGUNDO MERCANTIL CANCUN",
            "JUZGADO TERCERO MERCANTIL CANCUN",
            "JUZGADO ORAL MERCANTIL CANCUN",
            "JUZGADO MERCANTIL PLAYA",
            "JUZGADO MERCANTIL CHETUMAL"
        ],
        "TODAS_SALAS": [
            "PRIMERA SALA CIVIL MERCANTIL Y FAMILIAR",
            "SEGUNDA SALA PENAL ORAL",
            "TERCERA SALA PENAL ORAL",
            "CUARTA SALA CIVIL MERCANTIL Y FAMILIAR",
            "QUINTA SALA CIVIL MERCANTIL Y FAMILIAR",
            "SEXTA SALA CIVIL MERCANTIL Y FAMILIAR",
            "SEPTIMA SALA PENAL TRADICIONAL",
            "OCTAVA SALA PENAL ORAL",
            "NOVENA SALA PENAL ORAL",
            "DECIMA SALA CIVIL MERCANTIL Y FAMILIAR PLAYA",
            "SALA CONSTITUCIONAL"
        ]
    }

    if categoria_juzgados not in categorias:
        print(f"❌ Categoría inválida. Usa: {', '.join(categorias.keys())}")
        return

    juzgados = categorias[categoria_juzgados]

    print(f"🔍 Buscando expediente {numero_expediente} en {len(juzgados)} ubicaciones")
    print(f"📋 Categoría: {categoria_juzgados}\n")
    print("Copia este JSON y pégalo en expedientes.json:\n")
    print("```json")

    for juzgado in juzgados:
        expediente = {
            "comentario": f"Búsqueda múltiple: {numero_expediente}",
            "numero": numero_expediente,
            "juzgado": juzgado
        }
        print(json.dumps(expediente, indent=2, ensure_ascii=False) + ",")

    print("```\n")
    print(f"✅ {len(juzgados)} búsquedas generadas")
    print("\n💡 Después de ejecutar el bot, revisa el Excel para ver dónde aparece.")


def main():
    print("=" * 70)
    print("🔍 Buscador Múltiple de Expedientes")
    print("    TSJ Quintana Roo")
    print("=" * 70)
    print()

    if len(sys.argv) < 3:
        print("Uso:")
        print("  python3 buscar_multiple.py <numero_expediente> <categoria>")
        print()
        print("Categorías disponibles:")
        print("  PENAL          - Busca en todas las salas penales")
        print("  CIVIL          - Busca en todos los juzgados civiles")
        print("  FAMILIAR       - Busca en todos los juzgados familiares")
        print("  MERCANTIL      - Busca en todos los juzgados mercantiles")
        print("  TODAS_SALAS    - Busca en todas las salas de segunda instancia")
        print()
        print("Ejemplos:")
        print("  python3 buscar_multiple.py 615/2019 PENAL")
        print("  python3 buscar_multiple.py 2358/2025 FAMILIAR")
        print("  python3 buscar_multiple.py 123/2024 TODAS_SALAS")
        print()
        sys.exit(1)

    numero = sys.argv[1]
    categoria = sys.argv[2].upper()

    buscar_expediente_multiple(numero, categoria)


if __name__ == "__main__":
    main()
