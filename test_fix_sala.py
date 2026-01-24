#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para verificar el fix de búsqueda en Salas
Prueba el expediente 615/2019 en NOVENA SALA PENAL ORAL
"""

import json

# Crear un archivo JSON de prueba solo con el expediente problemático
test_expedientes = {
    "expedientes": [
        {
            "comentario": "TEST FIX - Expediente que antes fallaba",
            "numero": "615/2019",
            "juzgado": "NOVENA SALA PENAL ORAL"
        }
    ]
}

# Guardar archivo de prueba
with open('expedientes_test.json', 'w', encoding='utf-8') as f:
    json.dump(test_expedientes, f, indent=2, ensure_ascii=False)

print("✅ Archivo expedientes_test.json creado")
print("\nPara probar el fix, ejecuta:")
print("  python3 buscar_expedientes.py expedientes_test.json")
print("\nDebería encontrar los 14 registros del expediente 615/2019")
