# image_processing/processing.py

from PIL import Image
import numpy as np

def convert_to_grayscale(image_path, output_path):
    """
    Converte uma imagem para escala de cinza e salva no caminho especificado.

    :param image_path: Caminho da imagem de entrada.
    :param output_path: Caminho para salvar a imagem em escala de cinza.
    """
    image = Image.open(image_path).convert('L')
    image.save(output_path)
