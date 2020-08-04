import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="tensorflow-technical-indicators",
    version="0.1.0",
    author="Theodoros Ntakouris",
    author_email="zarkopafilis@gmail.com",
    description="Technical Indicators as TensorFlow Graph Functions",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ntakouris/tensorflow-technical-indicators",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
