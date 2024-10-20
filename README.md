# Criando-um-Pacote-de-Processamento-de-Imagens-com-Python

Image Processing Package
Um pacote de processamento de imagens em Python.

# Instalação
pip install .

# Uso
from image_processing import read_image, save_image, resize_image, convert_to_grayscale, blur_image

image = read_image('path/to/image.jpg')
gray_image = convert_to_grayscale(image)
save_image('path/to/gray_image.jpg', gray_image)

# Testes
python -m unittest discover tests
