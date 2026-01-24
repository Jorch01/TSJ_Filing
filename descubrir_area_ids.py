#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para descubrir los areaId de las Salas de Segunda Instancia
Prueba diferentes combinaciones para encontrar los areaId correctos
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def probar_area_id(driver, id_sala, nombre_sala, area_id_inicial=150, area_id_final=200):
    """
    Prueba diferentes areaIds para una Sala específica
    """
    print(f"\n{'='*70}")
    print(f"🔍 Probando: {nombre_sala}")
    print(f"   ID Sala (int): {id_sala}")
    print(f"{'='*70}")

    base_url = "https://www.tsjqroo.gob.mx/estrados"
    expediente_prueba = "1/2024"  # Expediente de prueba

    for area_id in range(area_id_inicial, area_id_final + 1):
        try:
            # Construir URL con buscador_segunda.php
            url = f"{base_url}/buscador_segunda.php?findexp={expediente_prueba}&int={id_sala}&areaId={area_id}&metodo=1"

            driver.get(url)
            time.sleep(2)

            # Verificar si la página cargó correctamente
            page_source = driver.page_source

            # Verificar si NO hay error de página o redirección
            if "error" not in page_source.lower() and "not found" not in page_source.lower():
                # Verificar si hay una tabla de resultados (aunque esté vacía)
                if "table" in page_source.lower() or "tbody" in page_source.lower():
                    print(f"   ✅ areaId={area_id} - Página válida (tiene tabla)")

                    # Verificar si hay resultados o mensaje de "no resultados"
                    if "No se encontr" in page_source or "ningun resultado" in page_source.lower():
                        print(f"      → Sin resultados para expediente {expediente_prueba}")
                    else:
                        # Intentar contar filas
                        try:
                            filas = driver.find_elements(By.CSS_SELECTOR, "tr.odd, tr.even")
                            if len(filas) > 0:
                                print(f"      → ¡ENCONTRÓ {len(filas)} RESULTADOS! ✨")
                        except:
                            pass

                    return area_id  # Retorna el primer areaId válido

        except Exception as e:
            # Silenciar errores, solo nos interesan los areaIds que funcionan
            pass

    print(f"   ❌ No se encontró areaId válido en rango {area_id_inicial}-{area_id_final}")
    return None


def main():
    print("=" * 70)
    print("🔍 DESCUBRIDOR DE AREA IDs")
    print("   Salas de Segunda Instancia - TSJ Quintana Roo")
    print("=" * 70)
    print()

    # Configurar Chrome
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Ejecutar sin interfaz gráfica
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=chrome_options)

    # Diccionario de Salas a probar
    salas = {
        'PRIMERA SALA CIVIL MERCANTIL Y FAMILIAR': 170,
        'SEGUNDA SALA PENAL ORAL': 171,
        'TERCERA SALA PENAL ORAL': 173,
        'CUARTA SALA CIVIL MERCANTIL Y FAMILIAR': 183,
        'QUINTA SALA CIVIL MERCANTIL Y FAMILIAR': 175,
        'SEXTA SALA CIVIL MERCANTIL Y FAMILIAR': 176,
        'SEPTIMA SALA PENAL TRADICIONAL': 177,
        'OCTAVA SALA PENAL ORAL': 178,
        'NOVENA SALA PENAL ORAL': 179,  # Ya sabemos que areaId=154
        'DECIMA SALA CIVIL MERCANTIL Y FAMILIAR PLAYA': 172,
        'SALA CONSTITUCIONAL': 184,
    }

    resultados = {}

    try:
        for nombre_sala, id_sala in salas.items():
            area_id = probar_area_id(driver, id_sala, nombre_sala)
            if area_id:
                resultados[nombre_sala] = {
                    'int': id_sala,
                    'areaId': area_id
                }

    finally:
        driver.quit()

    # Mostrar resultados finales
    print("\n" + "=" * 70)
    print("📊 RESULTADOS FINALES")
    print("=" * 70)
    print()
    print("Copia este diccionario en buscar_expedientes.py:")
    print()
    print("AREA_IDS_SALAS = {")
    for nombre, datos in resultados.items():
        print(f"    {datos['int']}: {datos['areaId']},  # {nombre}")
    print("}")
    print()
    print("=" * 70)


if __name__ == "__main__":
    main()
