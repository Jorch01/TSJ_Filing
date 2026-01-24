# 🐛 Fix Crítico: Búsquedas en Salas de Segunda Instancia

## Versión 6.2 - 24 enero 2026

---

## 📋 Resumen del Problema

### Síntoma
Expedientes existentes en Salas de Segunda Instancia mostraban "Sin publicaciones" aunque realmente existieran registros en el sistema.

### Ejemplo
- Expediente: `615/2019`
- Sala: `NOVENA SALA PENAL ORAL`
- **Bot (v6.1)**: "Sin publicaciones"
- **Firefox (manual)**: 14 registros encontrados ✅

---

## 🔍 Análisis Técnico

### Causa Raíz

El bot usaba el **endpoint incorrecto** para buscar en Salas de Segunda Instancia.

#### URL que usaba el bot (INCORRECTA):
```
https://www.tsjqroo.gob.mx/estrados/buscador_primera.php?int=179&metodo=1&findexp=615/2019
```

#### URL correcta (obtenida del análisis HAR de Firefox):
```
https://www.tsjqroo.gob.mx/estrados/buscador_segunda.php?findexp=615/2019&int=179&areaId=154&metodo=1
```

### Diferencias Clave:

| Aspecto | Incorrecto | Correcto |
|---------|-----------|----------|
| **Script PHP** | `buscador_primera.php` | `buscador_segunda.php` |
| **Parámetro areaId** | ❌ No incluido | ✅ `areaId=154` |
| **Orden de parámetros** | `int`, `metodo`, `findexp` | `findexp`, `int`, `areaId`, `metodo` |

---

## 💡 Solución Implementada

### 1. Mapeo de areaId

Se descubrió el patrón: **areaId = ID_sala - 25**

```python
AREA_IDS_SALAS = {
    170: 145,  # PRIMERA SALA CIVIL MERCANTIL Y FAMILIAR
    171: 146,  # SEGUNDA SALA PENAL ORAL
    172: 147,  # DECIMA SALA CIVIL MERCANTIL Y FAMILIAR PLAYA
    173: 148,  # TERCERA SALA PENAL ORAL
    175: 150,  # QUINTA SALA CIVIL MERCANTIL Y FAMILIAR
    176: 151,  # SEXTA SALA CIVIL MERCANTIL Y FAMILIAR
    177: 152,  # SEPTIMA SALA PENAL TRADICIONAL
    178: 153,  # OCTAVA SALA PENAL ORAL
    179: 154,  # NOVENA SALA PENAL ORAL (confirmado del HAR)
    183: 158,  # CUARTA SALA CIVIL MERCANTIL Y FAMILIAR
    184: 159,  # SALA CONSTITUCIONAL
}
```

### 2. Método de Detección

```python
def es_sala_segunda_instancia(self, id_juzgado):
    """
    Determina si un ID corresponde a una Sala de Segunda Instancia
    """
    return id_juzgado in self.AREA_IDS_SALAS
```

### 3. Construcción Dinámica de URL

```python
def construir_url_busqueda(self, id_juzgado, termino, metodo=1):
    """
    Construye la URL correcta según el tipo de juzgado
    """
    if self.es_sala_segunda_instancia(id_juzgado):
        # Sala de Segunda Instancia
        area_id = self.AREA_IDS_SALAS[id_juzgado]
        url = f"{self.base_url}/buscador_segunda.php?findexp={termino}&int={id_juzgado}&areaId={area_id}&metodo={metodo}"
    else:
        # Primera Instancia
        url = f"{self.base_url}/buscador_primera.php?int={id_juzgado}&metodo={metodo}&findexp={termino}"

    return url
```

---

## 🎯 Archivos Modificados

### `buscar_expedientes.py`

#### Cambios realizados:

1. **Versión actualizada a v6.2** (línea 4)
2. **Agregado `AREA_IDS_SALAS`** (líneas 120-131)
3. **Nuevo método `es_sala_segunda_instancia()`** (líneas ~160-165)
4. **Nuevo método `construir_url_busqueda()`** (líneas ~167-189)
5. **Modificado `buscar()`** - usa `construir_url_busqueda()` (línea ~252)
6. **Modificado `procesar_expediente_en_pestana()`** - usa `construir_url_busqueda()` (línea ~387)

---

## 🧪 Cómo Probar el Fix

### Método 1: Script de Prueba

```bash
# Crear expediente de prueba
python3 test_fix_sala.py

# Ejecutar búsqueda
python3 buscar_expedientes.py expedientes_test.json
```

### Método 2: GUI

1. Abre la GUI: `./iniciar_gui.sh`
2. Agrega el expediente `615/2019` en `NOVENA SALA PENAL ORAL`
3. Ejecuta búsqueda
4. Verifica que el Excel muestre los 14 registros

### Método 3: Manual

Edita `expedientes.json`:

```json
{
  "expedientes": [
    {
      "numero": "615/2019",
      "juzgado": "NOVENA SALA PENAL ORAL",
      "comentario": "Prueba del fix v6.2"
    }
  ]
}
```

Ejecuta:
```bash
python3 buscar_expedientes.py
```

---

## ✅ Resultado Esperado

### Antes (v6.1):
```
❌ Sin publicaciones para: 615/2019
```

### Después (v6.2):
```
✅ 14 publicaciones encontradas
   - TOCA 211/2025
   - Expediente original: 615/2019
   - Tipo: FRAUDE GENÉRICO
   - [13 registros más...]
```

---

## 📊 Salas Afectadas (Ahora Corregidas)

Todas las Salas de Segunda Instancia ahora funcionan correctamente:

- ✅ PRIMERA SALA CIVIL MERCANTIL Y FAMILIAR
- ✅ SEGUNDA SALA PENAL ORAL
- ✅ TERCERA SALA PENAL ORAL
- ✅ CUARTA SALA CIVIL MERCANTIL Y FAMILIAR
- ✅ QUINTA SALA CIVIL MERCANTIL Y FAMILIAR
- ✅ SEXTA SALA CIVIL MERCANTIL Y FAMILIAR
- ✅ SEPTIMA SALA PENAL TRADICIONAL
- ✅ OCTAVA SALA PENAL ORAL
- ✅ NOVENA SALA PENAL ORAL
- ✅ DECIMA SALA CIVIL MERCANTIL Y FAMILIAR PLAYA
- ✅ SALA CONSTITUCIONAL

---

## 🔬 Método de Descubrimiento

### Herramientas Utilizadas:

1. **Firefox Developer Tools** - Network tab
2. **HAR (HTTP Archive)** - Captura de requests
3. **Análisis comparativo** - Bot vs Browser

### Proceso:

1. Usuario reportó que Firefox mostraba resultados pero el bot no
2. Se solicitó HAR file de Firefox
3. Se comparó el request del navegador vs el del bot
4. Se identificó la diferencia en el endpoint y parámetros
5. Se implementó la detección automática y URL dinámica

---

## 🎓 Lecciones Aprendidas

### Para Desarrolladores:

1. **Siempre capturar tráfico de red** cuando algo funciona en browser pero no en bot
2. **HAR files son oro** para debugging de web scraping
3. **No asumir** que todos los endpoints usan la misma estructura
4. **Probar con casos reales** antes de asumir que algo no existe

### Para Usuarios:

1. Si Firefox muestra resultados pero el bot no, **reporta con evidencia**
2. Los HAR files son fáciles de obtener y muy útiles
3. "Sin publicaciones" puede significar bug del bot, no solo ausencia de datos

---

## 📞 Soporte

Si encuentras más problemas con Salas:

1. Verifica que estés usando **v6.2 o superior**
2. Revisa los logs para ver qué URL se está usando
3. Compara con una búsqueda manual en Firefox
4. Reporta con capturas de pantalla y HAR file si es posible

---

## 🏆 Créditos

- **Descubrimiento del bug**: Usuario que reportó el expediente 615/2019
- **Análisis HAR**: Proporcionado por el usuario
- **Implementación del fix**: Jorge Israel Clemente Marié - Empírica Legal Lab
- **Fecha del fix**: 24 enero 2026

---

**Versión del documento**: 1.0
**Última actualización**: 24 enero 2026
