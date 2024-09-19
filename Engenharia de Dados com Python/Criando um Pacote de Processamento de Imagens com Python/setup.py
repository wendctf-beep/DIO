# setup.py

from setuptools import setup, find_packages

setup(
    name='image_processing_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'convert_to_grayscale=image_processing.processing:convert_to_grayscale',
        ],
    },
    author='Wenderson Tiago Freitas',
    author_email='wendc1.wc@gmail.com',
    description='Um pacote de processamento de imagens em Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wendctf-beep/image_processing_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
