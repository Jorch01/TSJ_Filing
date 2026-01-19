# 🔍 Cómo Encontrar los IDs de las Salas

## Método 1: Manual (RECOMENDADO) ⭐

Este es el método más rápido y confiable:

### Pasos:

1. **Abre el navegador** y ve a:
   ```
   https://www.tsjqroo.gob.mx/estrados/main.php
   ```

2. **Haz click en "Segunda Instancia"** en el menú lateral

3. **Para cada Sala que aparezca:**
   - Haz click en el nombre de la Sala
   - Observa la **URL en la barra de direcciones**
   - Verás algo como: `buscador_primera.php?int=123&...`
   - El número después de `int=` es el **ID de la Sala**

4. **Anota los IDs** con sus nombres:
   ```
   ID: 123 → PRIMERA SALA CIVIL, MERCANTIL Y FAMILIAR
   ID: 124 → SEGUNDA SALA CON COMPETENCIA EN EL SISTEMA PENAL ORAL
   etc.
   ```

5. **Actualiza los archivos:**
   - Edita `buscar_expedientes.py` en la sección `JUZGADOS` (línea ~92)
   - Edita `expedientes.json` en la sección `juzgados_disponibles`

---

## Método 2: Script Automático

Si prefieres automatizar la búsqueda:

```bash
python3 descubrir_ids_salas.py
```

El script:
- ✅ Probará automáticamente diferentes IDs
- ✅ Guardará screenshots cuando encuentre una Sala
- ✅ Te mostrará los resultados al final

**Nota:** Este método puede tomar 5-10 minutos.

---

## Método 3: Inspeccionar Código HTML

Para usuarios avanzados:

1. Abre https://www.tsjqroo.gob.mx/estrados/main.php
2. Presiona `F12` para abrir DevTools
3. Ve a la pestaña "Network"
4. Haz click en "Segunda Instancia"
5. Busca la petición que carga el menú (probablemente `sidebar.php` o similar)
6. Revisa la respuesta - deberías ver un array con IDs y nombres

---

## 📝 Plantilla para Actualizar

Una vez que tengas los IDs, agrega esto a `buscar_expedientes.py`:

```python
# ===== SALAS DE SEGUNDA INSTANCIA =====
'PRIMERA SALA CIVIL MERCANTIL Y FAMILIAR': XXX,  # ← Reemplaza XXX con el ID real
'SEGUNDA SALA PENAL ORAL': XXX,
'TERCERA SALA PENAL ORAL': XXX,
'CUARTA SALA CIVIL MERCANTIL Y FAMILIAR': XXX,
'QUINTA SALA CIVIL MERCANTIL Y FAMILIAR': XXX,
'SEXTA SALA CIVIL MERCANTIL Y FAMILIAR': XXX,
'SEPTIMA SALA PENAL TRADICIONAL': XXX,
'OCTAVA SALA PENAL ORAL': XXX,
'NOVENA SALA PENAL ORAL': XXX,
'DECIMA SALA CIVIL MERCANTIL Y FAMILIAR PLAYA': XXX,
'SALA CONSTITUCIONAL': XXX,
```

Y actualiza `expedientes.json`:

```json
"SEGUNDA_INSTANCIA": [
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
```

---

## ⚡ Necesitas Ayuda?

Si encuentras los IDs, envíamelos y yo actualizo los archivos por ti.

Formato:
```
PRIMERA SALA CIVIL MERCANTIL Y FAMILIAR = 123
SEGUNDA SALA PENAL ORAL = 124
etc.
```
