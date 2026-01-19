#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para descubrir IDs de Salas en el sistema de Estrados Electrónicos
TSJ Quintana Roo

Uso: python3 descubrir_ids_salas.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def probar_id_sala(driver, id_sala, nombre_sala):
    """Prueba si un ID de sala es válido"""
    url = f"https://www.tsjqroo.gob.mx/estrados/buscador_primera.php?int={id_sala}&metodo=1&findexp=1/2025"

    try:
        driver.get(url)
        time.sleep(2)

        # Verificar si la página cargó correctamente
        page_source = driver.page_source.lower()

        # Buscar señales de que el ID es válido
        if "error" in page_source or "no encontrado" in page_source:
            return None

        # Buscar el nombre del juzgado/sala en la página
        if any(palabra.lower() in page_source for palabra in nombre_sala.split()):
            print(f"✅ ID {id_sala}: {nombre_sala} - ENCONTRADO")
            return id_sala
        else:
            # Intentar extraer el nombre real del juzgado de la página
            try:
                # Aquí puedes agregar lógica para extraer el nombre del juzgado
                print(f"⚠️  ID {id_sala}: Responde pero no coincide con '{nombre_sala}'")
            except:
                pass
            return None

    except Exception as e:
        print(f"❌ ID {id_sala}: Error - {e}")
        return None

def main():
    print("=" * 70)
    print("🔍 Descubridor de IDs de Salas - TSJ Quintana Roo")
    print("=" * 70)
    print()

    # Salas a buscar (según la lista proporcionada)
    salas_a_buscar = [
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
        "SALA CONSTITUCIONAL",
    ]

    # Iniciar navegador
    print("Iniciando Chrome...")
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Descomenta para modo invisible
    driver = webdriver.Chrome(options=options)

    resultados = {}

    try:
        print("\nProbando IDs comunes para Salas de Segunda Instancia...")
        print("(Esto puede tomar varios minutos)\n")

        # Probar rangos comunes de IDs para salas
        # Las salas suelen tener IDs en rangos específicos
        rangos_a_probar = [
            range(1, 30),      # IDs bajos comunes para salas
            range(98, 105),    # Rango antes de juzgados de Cancún
            range(116, 131),   # Rango entre juzgados
            range(138, 144),   # Otro rango intermedio
            range(167, 188),   # Rango alto
            range(189, 210),   # Rango muy alto
        ]

        for rango in rangos_a_probar:
            for id_sala in rango:
                print(f"Probando ID {id_sala}...", end='\r')

                url = f"https://www.tsjqroo.gob.mx/estrados/buscador_primera.php?int={id_sala}&metodo=1&findexp=1/2025"
                driver.get(url)
                time.sleep(1.5)

                # Intentar extraer el nombre del órgano jurisdiccional
                try:
                    page_source = driver.page_source

                    # Buscar patrones que indiquen que es una sala
                    if "SALA" in page_source.upper():
                        # Intentar extraer el nombre exacto
                        print(f"\n🎯 ID {id_sala}: Posible SALA encontrada")
                        print(f"   URL: {url}")

                        # Guardar screenshot para revisión manual
                        driver.save_screenshot(f"sala_id_{id_sala}.png")
                        print(f"   Screenshot guardado: sala_id_{id_sala}.png")

                        resultados[id_sala] = "SALA - Revisar manualmente"

                except Exception as e:
                    pass

        print("\n")
        print("=" * 70)
        print("📊 RESULTADOS")
        print("=" * 70)

        if resultados:
            print("\nPosibles IDs de Salas encontrados:")
            for id_sala, nombre in resultados.items():
                print(f"  ID {id_sala}: {nombre}")
            print(f"\nRevisa los screenshots generados (sala_id_XXX.png)")
            print("para identificar qué sala corresponde a cada ID.\n")
        else:
            print("\n⚠️  No se encontraron IDs de Salas en los rangos probados.")
            print("Intenta buscar manualmente en el sistema de estrados.\n")

        print("\n💡 MÉTODO MANUAL para encontrar IDs:")
        print("1. Abre: https://www.tsjqroo.gob.mx/estrados/main.php")
        print("2. Click en 'Segunda Instancia'")
        print("3. Click en cada sala")
        print("4. En la URL verás: buscador_primera.php?int=XXX")
        print("5. El número XXX es el ID de esa sala")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

    finally:
        input("\n⏸️  Presiona ENTER para cerrar...")
        driver.quit()

if __name__ == "__main__":
    main()
