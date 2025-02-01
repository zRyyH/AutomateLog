from google.cloud import vision
from PIL import Image
import io
import os


# Configuração da API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "chave.json"

# Inicializar o cliente da Vision API
client = vision.ImageAnnotatorClient()

x_inicial = 618
y_inicial = 998
x_final = 1032
y_final = 1409


def position_sem_parar(image_path="screenshot.png"):
    # Abrir e cortar a imagem usando Pillow
    with Image.open(image_path) as img:
        # Coordenadas do corte: (x_inicial, y_inicial, x_final, y_final)
        cropped_img = img.crop((x_inicial, y_inicial, x_final, y_final))

        # Salvar a imagem cortada em memória
        buffer = io.BytesIO()
        cropped_img.save(buffer, format="PNG")
        content = buffer.getvalue()

    # Criar objeto de imagem para enviar à API
    image = vision.Image(content=content)

    # Realizar a análise (detecção de texto)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    for text in texts:
        if text.description.upper() == "SEM":
            # Extraindo as coordenadas dos vértices
            vertices = [
                {"x": vertex.x, "y": vertex.y} for vertex in text.bounding_poly.vertices
            ]

            # Cálculo da média de x e y
            avg_x = sum(vertex["x"] for vertex in vertices) / len(vertices)
            avg_y = sum(vertex["y"] for vertex in vertices) / len(vertices)

            return {"x": int(x_inicial + avg_x), "y": int(y_inicial + avg_y)}

    # Tratamento de erros
    if response.error.message:
        raise Exception(f"Ocorreu um erro: {response.error.message}")