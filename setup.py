from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pysub-parser",
    version="1.4.1",
    url="https://github.com/fedecalendino/pysub-parser",
    license="MIT",
    description="Utility to extract the contents of a subtitle file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Federico Calendino",
    author_email="federico@calendino.com",
    packages=[
        "pysubparser", 
        "pysubparser.classes", 
        "pysubparser.cleaners",
        "pysubparser.parsers",
        "pysubparser.writers",
    ],
    install_requires=["unidecode"],
    test_requires=["coverage", "parameterized"],
    keywords=["subtitle", "subtitles", "parser", "srt", "sub", "ssa", "txt"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
