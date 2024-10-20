from setuptools import setup, find_packages

setup(
    name='image_processing_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'image-processing=image_processing:main',
        ],
    },
    author='Seu Nome',
    author_email='seu.email@example.com',
    description='Um pacote de processamento de imagens',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seuusuario/image-processing-package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
