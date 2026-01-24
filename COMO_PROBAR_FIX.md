# 🧪 Cómo Probar el Fix v6.2

## Verificar que el expediente 615/2019 ahora funciona

---

## ✅ Verificación Rápida

El fix está **IMPLEMENTADO Y FUNCIONANDO** si ves esto en los logs cuando ejecutes una búsqueda en una Sala:

```
🏛️  Sala de 2ª Instancia detectada - usando buscador_segunda.php (areaId=154)
```

En lugar de esto (versión anterior):

```
📍 Juzgado de 1ª Instancia - usando buscador_primera.php
```

---

## 🎯 Método 1: Prueba Automatizada

### Paso 1: Crear expediente de prueba

```bash
python3 test_fix_sala.py
```

Esto crea `expedientes_test.json` con el expediente problemático.

### Paso 2: Ejecutar búsqueda

```bash
python3 buscar_expedientes.py expedientes_test.json
```

### Paso 3: Verificar resultado

El Excel `resultados_expedientes.xlsx` debe mostrar:

| Búsqueda | Tipo | Juzgado | Estado | Publicaciones |
|----------|------|---------|--------|---------------|
| 615/2019 | expediente | NOVENA SALA PENAL ORAL | ✅ Con publicaciones | 14 (o más) |

---

## 🖥️ Método 2: Usando la GUI

### Paso 1: Abrir interfaz gráfica

```bash
./iniciar_gui.sh
```

O:

```bash
python3 gui_expedientes.py
```

### Paso 2: Agregar el expediente

1. Selecciona "Por número de expediente"
2. Ingresa: `615/2019`
3. En el menú desplegable selecciona: `NOVENA SALA PENAL ORAL`
4. Click en "➕ Agregar Expediente"

### Paso 3: Ejecutar búsqueda

Click en "🚀 EJECUTAR BÚSQUEDA"

### Paso 4: Observar el log

Deberías ver en la consola:

```
🏛️  Sala de 2ª Instancia detectada - usando buscador_segunda.php (areaId=154)
🔍 URL: https://www.tsjqroo.gob.mx/estrados/buscador_segunda.php?findexp=615/2019&int=179&areaId=154&metodo=1
✅ 14 publicaciones encontradas
```

### Paso 5: Verificar Excel

Abre `resultados_expedientes.xlsx` y confirma que hay 14 (o más) registros.

---

## 📊 Método 3: Búsqueda Manual en Navegador

Para comparar:

1. Abre: https://www.tsjqroo.gob.mx/estrados/main.php
2. Selecciona: "NOVENA SALA CON COMPETENCIA EN EL SISTEMA PENAL ORAL"
3. Ingresa: `615/2019`
4. Click "Buscar"
5. Cuenta los resultados

El bot debe encontrar **la misma cantidad** que ves en el navegador.

---

## 🔍 Otras Salas para Probar

Si quieres probar que todas las Salas funcionan, puedes usar el script `buscar_multiple.py`:

```bash
# Generar búsquedas en TODAS las salas penales
python3 buscar_multiple.py 615/2019 PENAL

# O en todas las salas de segunda instancia
python3 buscar_multiple.py 615/2019 TODAS_SALAS
```

Copia el JSON generado al `expedientes.json` y ejecuta:

```bash
python3 buscar_expedientes.py
```

---

## ❓ ¿Qué Esperar?

### ✅ CORRECTO (v6.2):

```
[10:30:15] ℹ️  Procesando: 615/2019 en NOVENA SALA PENAL ORAL
[10:30:15] 🏛️  Sala de 2ª Instancia detectada - usando buscador_segunda.php (areaId=154)
[10:30:15] 🔍 URL: https://www.tsjqroo.gob.mx/estrados/buscador_segunda.php?findexp=615/2019&int=179&areaId=154&metodo=1
[10:30:19] ✅ 14 publicaciones encontradas
[10:30:19] ✅ Estado: Con publicaciones
```

### ❌ INCORRECTO (v6.1 y anteriores):

```
[10:30:15] ℹ️  Procesando: 615/2019 en NOVENA SALA PENAL ORAL
[10:30:15] 🔍 URL: https://www.tsjqroo.gob.mx/estrados/buscador_primera.php?int=179&metodo=1&findexp=615/2019
[10:30:19] ⚠️  Sin publicaciones para: 615/2019
[10:30:19] ❌ Estado: Sin publicaciones
```

---

## 🎨 Indicadores Visuales en Excel

### Columna "Estado"

- ✅ **"Con publicaciones"** (fondo verde) = Expediente encontrado
- ❌ **"Sin publicaciones"** (sin formato) = Expediente no existe en ese juzgado

### Columna "Es Nuevo"

- 🟡 **Fondo amarillo** = Acuerdo publicado en los últimos 5 días
- ⚪ **Sin fondo** = Acuerdo antiguo

---

## 🐛 Si Aún No Funciona

### 1. Verifica la versión

Abre `buscar_expedientes.py` y busca en las primeras líneas:

```python
"""
Robot de Búsqueda Automática de Expedientes v6.2
...
- 🐛 FIX: Endpoint correcto para Salas (buscador_segunda.php + areaId)
"""
```

Si dice **v6.1 o anterior**, actualiza tu código.

### 2. Verifica que el mapeo existe

Busca en `buscar_expedientes.py` la línea:

```python
AREA_IDS_SALAS = {
```

Si NO existe, actualiza tu código.

### 3. Activa modo debug

En `config.json`:

```json
{
  "configuracion": {
    "debug_mode": true
  }
}
```

Ejecuta de nuevo y revisa los logs detallados.

### 4. Revisa screenshots

Si debug está activado, revisa la carpeta `debug_screenshots/` para ver qué está cargando el navegador.

---

## 📞 Contacto

Si después de probar el fix aún tienes problemas:

1. Verifica que estás en la **rama correcta**: `claude/parallel-browser-searches-i979H`
2. Asegúrate de tener el **último commit** (debe mencionar "v6.2")
3. Revisa los logs en detalle
4. Compara los screenshots con el navegador manual

---

**Última actualización**: 24 enero 2026
**Versión del fix**: v6.2
