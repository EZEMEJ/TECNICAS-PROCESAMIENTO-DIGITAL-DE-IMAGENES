# TRABAJO PRÁCTICO INTEGRADOR N°1: Sistema de Análisis de Documentos Digitalizados

## Objetivo

Desarrollar un sistema básico de análisis automático de documentos digitalizados que integre las técnicas de procesamiento de imágenes estudiadas en el curso.

## Estructura del Trabajo

Este proyecto está organizado en las siguientes partes:

1.  **Fundamentos Teóricos:** Discute las diferencias metodológicas entre el desarrollo de software tradicional y la investigación en IA/Ciencias de Datos, y las ventajas de usar cuadernos interactivos.
2.  **Setup del Entorno:** Configuración del entorno de trabajo, incluyendo importaciones de librerías y funciones utilitarias para el manejo de imágenes.
3.  **Análisis de Imágenes:** Carga, inspección visual y análisis de un dataset de 3 imágenes de documentos con diferentes características.
4.  **Preprocessing Básico:** Aplicación de técnicas de preprocessing como segmentación, corrección de perspectiva y mejora de calidad a las imágenes del dataset.

## Dataset

El proyecto requiere un dataset de 3 imágenes de documentos con diferentes características:
- Buena calidad (bien iluminada, recta)
- Rotada o inclinada
- Con problemas (oscura, borrosa, o con sombras)

Estas imágenes deben colocarse en una carpeta llamada `dataset/` en la misma ubicación que el notebook principal.

## Setup del Entorno

Para ejecutar este notebook, necesitarás tener instaladas las siguientes librerías de Python:

- `numpy`
- `pandas` (aunque no se usa activamente en las partes visibles, está importada)
- `matplotlib`
- `seaborn` (aunque no se usa activamente en las partes visibles, está importada)
- `ipywidgets` (aunque no se usa activamente en las partes visibles, está importada)
- `PIL` (Pillow)
- `opencv-python` (`cv2`)
- `scikit-image` (`skimage`)
- `scikit-learn` (`sklearn`) (aunque no se usa activamente en las partes visibles, está importada)

