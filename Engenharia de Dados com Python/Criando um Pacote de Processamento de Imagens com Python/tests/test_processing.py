# tests/test_processing.py

import os
from image_processing import convert_to_grayscale

def test_convert_to_grayscale():
    input_image = 'test_input.jpg'
    output_image = 'test_output.jpg'
    
    # Crie uma imagem de teste
    with open(input_image, 'wb') as f:
        f.write(os.urandom(1024))  # Cria um arquivo de 1KB aleatório
    
    convert_to_grayscale(input_image, output_image)
    
    assert os.path.exists(output_image)
    
    os.remove(input_image)
    os.remove(output_image)
