# Guardianes del Petén — Entrega 4

**Estudiante:** Axel Samuel López Ortiz  
**Carné:** 202504785  
**Grupo:** Grupo 2 – LISCC-L  
**Fecha:** 8 de noviembre de 2026

## Ejecución

Con Python 3 instalado, abre una terminal en esta carpeta y ejecuta:

```bash
python main.py
```

Al terminar, presiona ENTER para cerrar.

## Diagrama de clases actualizado

```mermaid
classDiagram
    class Animal {
      <<abstract>>
      +codigo
      +nombre
      +edad
      +habitat
      +mostrar_info()
      +alimentarse()
      +desplazarse()
      +describir()*
    }
    class Jaguar {
      +fuerza_mordida
      +cazar()
      +alimentarse()
      +describir()
    }
    class Tapir {
      +peso
      +buscar_frutas()
      +alimentarse()
      +describir()
    }
    class GuacamayaRoja {
      +envergadura
      +volar()
      +alimentarse()
      +describir()
    }
    class CocodriloDePantano {
      +longitud
      +nadar()
      +alimentarse()
      +describir()
    }
    class Alerta {
      +codigo
      +prioridad
      +hora
      +descripcion
    }
    class SistemaGuardianes {
      +animales
      +alertas
      +agregar_animal()
      +agregar_alerta()
      +ordenar_alertas()
      +ordenar_animales_por_codigo()
      +buscar_animal(codigo)
    }
    Animal <|-- Jaguar
    Animal <|-- Tapir
    Animal <|-- GuacamayaRoja
    Animal <|-- CocodriloDePantano
    SistemaGuardianes o-- Animal
    SistemaGuardianes o-- Alerta
```

## Evidencia de ejecución

![Ejecución de main.py](evidencia_ejecucion.png)

Las alertas se ordenan por **alta antes de media** y luego por **hora ascendente**, con selección manual. Los animales se ordenan por `codigo` también mediante selección, y se buscan con **búsqueda binaria**.
