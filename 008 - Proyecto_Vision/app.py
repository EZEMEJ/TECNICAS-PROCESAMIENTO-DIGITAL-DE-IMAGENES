# app.py
import gradio as gr
from transformers import pipeline
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# ===========================
# RUTAS DE MODELOS Y ETIQUETAS
# ===========================
RUTA_MODELO_TM = "models/keras_model.h5"
RUTA_LABELS_TM = "models/labels.txt"

# ===========================
# CARGAR MODELO TEACHABLE MACHINE
# ===========================
print("🔹 Cargando modelo Teachable Machine...")
modelo_tm = load_model(RUTA_MODELO_TM, compile=False)

# Cargar etiquetas
with open(RUTA_LABELS_TM, "r") as f:
    etiquetas_tm = [line.strip() for line in f.readlines()]

print(f"✅ Modelo TM cargado con {len(etiquetas_tm)} clases")

# ===========================
# CARGAR MODELO CLIP
# ===========================
print("🔹 Cargando modelo CLIP...")
modelo_clip = pipeline(
    "zero-shot-image-classification",
    model="openai/clip-vit-base-patch32"
)

# Definir categorías de CLIP (igual que etiquetas TM o personalizar)
CATEGORIAS_CLIP = etiquetas_tm  # Por simplicidad, usar mismas categorías

# ===========================
# FUNCIONES DE PREPROCESAMIENTO
# ===========================
def preprocesar_tm(imagen: Image.Image):
    """Preprocesa imagen para Teachable Machine"""
    img = imagen.resize((224, 224))
    arr = np.asarray(img, dtype=np.float32)
    arr = arr.reshape(1, 224, 224, 3)
    arr = (arr / 127.5) - 1  # Normalizar [-1, 1]
    return arr

# ===========================
# FUNCIONES DE CLASIFICACIÓN
# ===========================
def clasificar_tm(imagen: Image.Image):
    if imagen is None:
        return {"Error": 1.0}
    try:
        x = preprocesar_tm(imagen)
        pred = modelo_tm.predict(x)
        resultados = {etiquetas_tm[i]: float(pred[0][i]) for i in range(len(etiquetas_tm))}
        # Ordenar por probabilidad descendente
        resultados = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))
        return resultados
    except Exception as e:
        print(f"Error TM: {e}")
        return {"Error": 1.0}

def clasificar_clip(imagen: Image.Image):
    if imagen is None:
        return {"Error": 1.0}
    try:
        resultados = modelo_clip(imagen, candidate_labels=CATEGORIAS_CLIP)
        return {r['label']: float(r['score']) for r in resultados}
    except Exception as e:
        print(f"Error CLIP: {e}")
        return {"Error": 1.0}

# ===========================
# INTERFAZ GRADIO
# ===========================
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    # Clasificador de Imágenes con IA
    Comparación entre modelo preentrenado (CLIP) y modelo personalizado (Teachable Machine)
    """)

    with gr.Row():
        imagen_input = gr.Image(
            type="pil",
            label="Imagen a clasificar",
            sources=["upload", "webcam"]
        )

    with gr.Row():
        boton_tm = gr.Button("Clasificar con TM", variant="primary")
        boton_clip = gr.Button("Clasificar con CLIP", variant="secondary")

    with gr.Row():
        with gr.Column():
            resultado_tm = gr.Label(label="Teachable Machine", num_top_classes=len(etiquetas_tm))
        with gr.Column():
            resultado_clip = gr.Label(label="CLIP", num_top_classes=len(CATEGORIAS_CLIP))

    gr.Markdown("""
    ---
    **Modelos**
    - **Teachable Machine (TM)**: Modelo personalizado entrenado.
    - **CLIP**: Modelo general de OpenAI.
    """)

    # Conectar botones con funciones
    boton_tm.click(fn=clasificar_tm, inputs=imagen_input, outputs=resultado_tm)
    boton_clip.click(fn=clasificar_clip, inputs=imagen_input, outputs=resultado_clip)

if __name__ == "__main__":
    demo.launch()
