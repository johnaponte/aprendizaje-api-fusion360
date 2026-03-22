# Curso PRO: Fusion 360 API con Python

## Introducción
Este es un curso práctico orientado a crear herramientas reales en Fusion 360 usando Python.
No es teórico: cada sesión incluye código, ejercicio guiado y errores típicos.

---

# SEMANA 1 — FUNDAMENTOS

## Sesión 1 — Primer script

### Objetivo
Entender cómo ejecutar código dentro de Fusion.

### Teoría (links)
- Creating Scripts and Add-Ins: https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-9701BBA7-EC0E-4016-A9C8-964AA4838954
- Basic API Concepts: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/BasicConcepts_UM.htm

### Código base
```python
"""This file acts as the main module for this script."""

import traceback
import adsk.core
import adsk.fusion
# import adsk.cam

# Initialize the global variables for the Application and UserInterface objects.
app = adsk.core.Application.get()
ui  = app.userInterface


def run(_context: str):
    """This function is called by Fusion when the script is run."""

    try:
        # Your code goes here.
        doc = app.activeDocument
        ui.messageBox(f"Hello, World!\nDocumento activo: {doc.name}")
    except Exception as e:  
        app.log(f'Error: {e}\nFailed to execute script.\n{traceback.format_exc()}')

```

### Ejercicio
- Ejecuta el script
- Cambia el mensaje
- Intenta acceder a un documento inexistente

### Error típico
- `NoneType object` → no hay documento activo

---

## Sesión 2 — Acceder al diseño

### Objetivo
Entender cómo ejecutar código dentro de Fusion.

### Teoría (links)
- Basic API Concepts: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/BasicConcepts_UM.htm
- Application and Design objects: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Application.htm

### Código base
```python
design = adsk.fusion.Design.cast(app.activeProduct)
root = design.rootComponent
```

### Ejercicio
- Imprimir nombre del root component

### Error típico
- activeProduct no es Design

---

## Sesión 3 — Componentes

### Código
```python
for comp in design.allComponents:
    print(comp.name)
```

### Teoría (links)
- Components and Occurrences: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Components.htm

### Ejercicio
- Contar componentes

---

## Sesión 4 — Colecciones

### Código
```python
sketches = root.sketches
print(sketches.count)
```

### Teoría (links)
- Object Model and Collections: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Collection.htm

---

## Sesión 5 — Debug

### Código
```python
try:
    x = None.name
except:
    print(traceback.format_exc())
```

### Teoría (links)
- Python Specific Issues: https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-C1545D80-D804-4CF3-886D-9B5C54B2D7A2

---

# SEMANA 2 — GEOMETRÍA

## Sesión 6 — Sketch

```python
sketch = root.sketches.add(root.xYConstructionPlane)
lines = sketch.sketchCurves.sketchLines
lines.addTwoPointRectangle(
    adsk.core.Point3D.create(0,0,0),
    adsk.core.Point3D.create(5,5,0)
)
```

### Teoría (links)
- Sketch API: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Sketches.htm

---

## Sesión 7 — Extrusión

```python
profile = sketch.profiles.item(0)
extrudes = root.features.extrudeFeatures
extInput = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
extInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(5))
extrudes.add(extInput)
```

### Teoría (links)
- Extrude Feature: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/ExtrudeFeatureSample_Sample.htm

---

## Sesión 8 — Parámetros

```python
width = 10
height = 5
```

### Teoría (links)
- Parameters and Units: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Units_UM.htm

Ejercicio: usa variables en lugar de valores fijos.

---

## Sesión 9 — Agujeros

### Teoría (links)
- Sketch Circles: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/SketchCircles.htm

- Añadir círculos en sketch
- Cortar con extrude cut

---

## Sesión 10 — Proyecto

### Teoría (links)
- Combining Features: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Features.htm

Crear placa con:
- dimensiones variables
- agujeros

---

# SEMANA 3 — UI

## Sesión 11 — Botón

```python
cmdDef = ui.commandDefinitions.addButtonDefinition(
    'cmdId',
    'Mi comando',
    'Descripción'
)
```

### Teoría (links)
- User Interface API: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/UserInterface.htm

---

## Sesión 12 — Inputs

```python
inputs = cmd.commandInputs
inputs.addValueInput('width', 'Width', 'cm', adsk.core.ValueInput.createByReal(5))
```

### Teoría (links)
- Command Inputs: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/CommandInputs_UM.htm

---

## Sesión 13 — Evento execute

```python
def notify(args):
    print("Ejecutado")
```

### Teoría (links)
- Events: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Events_UM.htm

---

## Sesión 14 — Integración

- UI + geometría

### Teoría (links)
- Commands Overview: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Commands_UM.htm

---

## Sesión 15 — Validación

- impedir valores negativos

### Teoría (links)
- Error Handling (Python): https://docs.python.org/3/tutorial/errors.html

---

# SEMANA 4 — ADD-IN

## Sesión 16 — Estructura

```
addin/
  entry.py
  commands/
  lib/
```

### Teoría (links)
- Add-in Structure: https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-DF32F126-366B-45C0-88B0-CEB46F5A9BE8

---

## Sesión 17 — Modularización

Separar:
- lógica
- UI

### Teoría (links)
- Python Modules: https://docs.python.org/3/tutorial/modules.html

---

## Sesión 18 — Selección

```python
sel = ui.selectEntity("Selecciona cara", "Faces")
```

### Teoría (links)
- Selection API: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/UserSelections_UM.htm

---

## Sesión 19 — Proyecto final

Opciones:
- generador de caja
- exportador STL

### Teoría (links)
- Export Manager: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/ExportManager.htm

---

## Sesión 20 — Refinamiento

Checklist:
- código limpio
- errores controlados
- UI clara

### Teoría (links)
- Best Practices: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/BestPractices.htm

---

# ERRORES TÍPICOS

- No entender rootComponent
- No validar inputs
- Hardcodear valores

---

# REGLA FINAL

Si no puedes explicar el flujo:
Application → Design → Component → Feature

NO HAS APRENDIDO.
