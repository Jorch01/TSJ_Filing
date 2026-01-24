# 🔍 Solución: "No se encontraron resultados"

## Guía para cuando el bot reporta "Sin publicaciones"

---

## 🐛 ACTUALIZACIÓN IMPORTANTE - v6.2 (24 enero 2026)

**Si estás usando una versión anterior a v6.2**, actualiza AHORA. Se corrigió un bug crítico:

### ✅ FIX IMPLEMENTADO:
Las búsquedas en **Salas de Segunda Instancia** ahora funcionan correctamente. Versiones anteriores usaban el endpoint incorrecto, causando que expedientes válidos mostraran "Sin publicaciones".

**Si tu versión es v6.2 o superior, este problema está resuelto.**

---

## ❓ ¿Por qué aparece "Sin publicaciones"?

Cuando el bot reporta "Sin publicaciones" significa que el **sistema de estrados del TSJ** no tiene registros para ese expediente en ese juzgado/sala específico.

**Esto NO es un error del bot** - el bot está funcionando correctamente y reportando lo que el sistema muestra.

---

## 🔍 Causas Comunes

### 1. **Expediente en otro juzgado/sala**

El expediente puede estar radicado en:
- Otra sala de segunda instancia
- Primera instancia (antes de apelar)
- Otra materia (civil vs familiar vs penal)

### 2. **Número de expediente incorrecto**

Verifica:
- ✅ Formato correcto: `615/2019` vs `0615/2019` vs `615-2019`
- ✅ Año correcto: `615/2019` vs `615/2020` vs `615/2018`
- ✅ Dígitos completos: A veces faltan ceros iniciales

### 3. **Expediente muy antiguo**

Los expedientes anteriores a cierta fecha pueden no estar digitalizados en estrados electrónicos.

### 4. **Expediente aún no publicado**

Si el expediente es muy reciente, puede que aún no tenga publicaciones en estrados.

### 5. **Expediente archivado**

Expedientes concluidos hace tiempo pueden haber sido archivados.

---

## ✅ Solución 1: Búsqueda Manual en Navegador

### Verifica manualmente en el sistema:

```
https://www.tsjqroo.gob.mx/estrados/main.php
```

1. Selecciona el juzgado/sala
2. Ingresa el número de expediente
3. Busca

Si ves "No se encontró ningun resultado", confirma que no está ahí.

---

## ✅ Solución 2: Buscar en Múltiples Ubicaciones

### Opción A: Usar el script buscar_multiple.py

```bash
python3 buscar_multiple.py 615/2019 PENAL
```

Esto genera JSON para buscar en **todas las salas penales**:
- SEGUNDA SALA PENAL ORAL
- TERCERA SALA PENAL ORAL
- SEPTIMA SALA PENAL TRADICIONAL
- OCTAVA SALA PENAL ORAL
- NOVENA SALA PENAL ORAL

### Categorías disponibles:

```bash
# Buscar en todas las salas penales
python3 buscar_multiple.py 615/2019 PENAL

# Buscar en todos los juzgados civiles
python3 buscar_multiple.py 123/2024 CIVIL

# Buscar en todos los juzgados familiares
python3 buscar_multiple.py 2358/2025 FAMILIAR

# Buscar en todas las salas de segunda instancia
python3 buscar_multiple.py 456/2024 TODAS_SALAS
```

Copia el JSON generado y pégalo en `expedientes.json`, luego ejecuta el bot.

---

## ✅ Solución 3: Probar Variantes del Número

Agrega múltiples variantes del mismo expediente:

```json
{
  "expedientes": [
    {"numero": "615/2019", "juzgado": "NOVENA SALA PENAL ORAL"},
    {"numero": "0615/2019", "juzgado": "NOVENA SALA PENAL ORAL"},
    {"numero": "615/2018", "juzgado": "NOVENA SALA PENAL ORAL"},
    {"numero": "615/2020", "juzgado": "NOVENA SALA PENAL ORAL"}
  ]
}
```

---

## ✅ Solución 4: Búsqueda por Nombre

Si conoces el nombre de las partes, busca por nombre en lugar de expediente:

```json
{
  "nombre": "JUAN PEREZ LOPEZ",
  "juzgado": "NOVENA SALA PENAL ORAL"
}
```

---

## 🎯 Ejemplo Práctico: Expediente 615/2019

### Caso de Uso Real

El expediente `615/2019` no aparece en la NOVENA SALA PENAL ORAL.

### Pasos recomendados:

#### 1. Buscar en todas las salas penales:

```bash
python3 buscar_multiple.py 615/2019 PENAL
```

#### 2. Agregar al expedientes.json:

```json
{
  "expedientes": [
    {
      "comentario": "Búsqueda múltiple en salas penales",
      "numero": "615/2019",
      "juzgado": "SEGUNDA SALA PENAL ORAL"
    },
    {
      "comentario": "Búsqueda múltiple en salas penales",
      "numero": "615/2019",
      "juzgado": "TERCERA SALA PENAL ORAL"
    },
    {
      "comentario": "Búsqueda múltiple en salas penales",
      "numero": "615/2019",
      "juzgado": "OCTAVA SALA PENAL ORAL"
    }
  ]
}
```

#### 3. Ejecutar el bot:

```bash
python3 buscar_expedientes.py
```

#### 4. Revisar el Excel:

Busca en el Excel cuál sala tiene `Estado: "Con publicaciones"` para ese expediente.

---

## 📊 Interpretando el Reporte Excel

| Estado | Significado |
|--------|-------------|
| **Sin publicaciones** | El expediente no existe en ese juzgado/sala |
| **Con publicaciones** | ✅ El expediente SÍ existe y tiene acuerdos |

Si **TODAS** las búsquedas dicen "Sin publicaciones":
- Verifica el número de expediente con el tribunal
- Confirma que está en el sistema de estrados
- Considera que puede ser muy antiguo o reciente

---

## 🛠️ Herramientas Disponibles

### 1. `buscar_multiple.py`
Genera JSON para buscar en múltiples ubicaciones

```bash
python3 buscar_multiple.py <expediente> <categoria>
```

### 2. GUI
Agrega manualmente cada variante desde la interfaz gráfica

```bash
./iniciar_gui.sh
```

### 3. Edición manual de expedientes.json
Para control total sobre las búsquedas

---

## 💡 Mejores Prácticas

### ✅ DO:
- Buscar en múltiples salas si no estás seguro
- Probar variantes del número (con/sin ceros)
- Verificar manualmente en el navegador primero
- Contactar al tribunal si no aparece en ningún lado

### ❌ DON'T:
- Asumir que el bot tiene un error
- Buscar solo en una ubicación
- Ignorar el formato del número de expediente
- No verificar el año del expediente

---

## 📞 Contacto con el Tribunal

Si después de todas estas búsquedas no encuentras el expediente:

1. **Contacta al tribunal** que supuestamente tiene el caso
2. **Verifica** el número exacto de expediente
3. **Pregunta** si está en estrados electrónicos
4. **Solicita** el estatus actual del expediente

---

## 🎓 Ejemplo Completo

### Situación:
Buscas el expediente `615/2019` en NOVENA SALA PENAL ORAL pero aparece "Sin publicaciones"

### Solución paso a paso:

```bash
# 1. Generar búsquedas múltiples
python3 buscar_multiple.py 615/2019 PENAL

# 2. Abrir expedientes.json y pegar el JSON generado

# 3. Ejecutar el bot
python3 buscar_expedientes.py

# 4. Revisar resultados_expedientes.xlsx

# 5. Buscar filas con "Con publicaciones"
```

### Resultado esperado:
El Excel mostrará qué sala tiene el expediente:

| Búsqueda | Juzgado | Estado |
|----------|---------|--------|
| 615/2019 | SEGUNDA SALA... | Sin publicaciones |
| 615/2019 | TERCERA SALA... | ✅ Con publicaciones |
| 615/2019 | NOVENA SALA... | Sin publicaciones |

**Conclusión**: El expediente está en la TERCERA SALA, no en la NOVENA.

---

## 🎯 Resumen

1. ✅ **El bot funciona correctamente** - reporta lo que el sistema muestra
2. 🔍 **Busca en múltiples ubicaciones** - usa `buscar_multiple.py`
3. 📝 **Prueba variantes** del número de expediente
4. 🌐 **Verifica manualmente** en el navegador
5. 📊 **Revisa el Excel** para encontrar dónde SÍ aparece
6. 📞 **Contacta al tribunal** si no aparece en ningún lado

---

**Recuerda**: "Sin publicaciones" NO es un error - es información valiosa que te dice dónde NO está el expediente.
