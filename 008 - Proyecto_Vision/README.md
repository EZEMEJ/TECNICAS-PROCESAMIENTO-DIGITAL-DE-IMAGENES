---
title: Clasificador Orgánico vs Reciclable
emoji: 🔍
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

# CLASIFICADOS ORGÁNICO/RECICLABLE

## Descripción

Una aplicación de clasificación de imágenes que distingue entre objetos orgánicos y reciclables.

## Modelo utilizado

- **Modelo preentrenado**: openai/clip-vit-base-patch32
- **Tarea**: [clasificación/detección]
- **Framework**: Transformers (Hugging Face)

## Categorías

- Objeto orgánico
- Objeto reciclable

## Cómo usar

1. Subí una imagen o usá tu cámara
2. Presioná "Clasificar"
3. Observá los resultados

## Desarrollo

Proyecto desarrollado para la materia **Procesamiento Digital de Imágenes y Visión por Computadora**.

**Autor**: MEJIAS IAIR EZEQUIEL
**Año**: 2025  
**Institución**: IFTS24

## Instalación local

```bash
# Clonar repositorio
git clone https://huggingface.co/spaces/iem143/Clasificador_Organico_vs_Reciclable

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python app.py

## Comparación de Modelos

### Modelo Preentrenado (CLIP)

**Ventajas**:
- Alto rendimiento sin necesidad de entrenamiento adicional.
- Capacidad para reconocer una amplia variedad de objetos y conceptos.

**Desventajas**:
- Menor precisión en tareas específicas.
- No se adapta al dominio particular.

**Resultados en mi dataset**:
- Precisión aproximada: [completá con tus resultados]
- Casos donde funciona bien: [describí]
- Casos donde falla: [describí]

### Modelo Personalizado (Teachable Machine)

**Ventajas**:
- Personalizable según las necesidades específicas del proyecto.
- Fácil de usar y entrenar.
- Permite adaptar el modelo a contextos locales.

**Desventajas**:
- Requiere datos representativos y bien etiquetados para funcionar correctamente..
- Generaliza mal fuera del dominio entrenado.

**Resultados en mi dataset**:
- Precisión aproximada: [completá con tus resultados]
- Tamaño del dataset de entrenamiento: 2000 imagenes en total - 1000 imágenes de objetos orgánicos y 1000 imágenes de objetos reciclables.
- Mejora respecto a CLIP: [porcentaje o descripción]

## Conclusiones

[Reflexioná sobre:
- Cuándo conviene usar modelos preentrenados vs personalizados
- Qué aprendiste del proceso de desarrollo
- Posibles mejoras futuras
- Aplicaciones reales de tu proyecto]