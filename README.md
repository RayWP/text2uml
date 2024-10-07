# Text2UML: a Preprocessing Pipeline for NLP Applications focused on turning Requirements Texts into UML

This repository holds the datasets and code of which the results are published in the paper "Preprocessing Requirements Documents for Automatic UML Modelling" by Martijn Schouten, Guus Ramackers and Suzan Verberne for the 27th International Conference on Natural Language & Information Systems. 

## Datasets

Next to the code for the preprocessing class that can be found in the `run_pipeline.py` file, this repository holds datasets that can be used for future research:

1. We manually labelled requirements texts of the [PURE dataset by Ferrari et al. (2017)](https://zenodo.org/record/1414117#.YmBpYdNBw-Q) with whether word(groups) are attributes or classes. This [new dataset](https://github.com/MeMartijn/text2uml/blob/main/data/train-full.tsv) contains almost 80.000 rows for training algorithms to distinguish classes and attributes in running texts. 
2. We also manually labelled a [new validation dataset](https://github.com/MeMartijn/text2uml/blob/main/data/validation-full.tsv) that include more focused, smaller texts for generating and validating UML models. The source of these texts are training materials of a big U.S.-based software company. 
3. [Our version of the Lindholmen dataset](https://github.com/MeMartijn/text2uml/blob/main/data/lindholmen/uml_extracted_metadata_annotated.json) contains a cleaned and preprocessed overview of all classes and attributes of the [Lindholmen dataset by Chaudron et al. (2017)](https://research.tue.nl/nl/datasets/lindholmen-dataset-of-uml-models).
4. To combat the development focus of the Lindholmen dataset, this repository contains a similar [dataset](https://github.com/MeMartijn/text2uml/blob/main/data/genmymodel/genmymodel_uml_extracted_metadata_final.json) of files with their (cleaned and normalised) classes and attributes that we extracted from the [MAR search engine by Lopez et al. (2020)](https://dl.acm.org/doi/10.1145/3365438.3410947). 

# Runing guide, extended by: github.com/rwp1byte

## installing python
1. Download and install python from [python.org](https://www.python.org/downloads/)
2. Add python to your PATH
3. Open a terminal and run `python --version` to check if python is installed correctly
4. run `pip --version` to check if pip is installed correctly

## installing poetry and creating a virtual environment
1. run `pip install poetry` to install poetry
2. run `poetry install`  to create a virtual environment and install the dependencies
3. run `poetry shell` to activate the virtual environment

## install en_core_web_sm (run after run poetry shell)
1. run `python -m spacy download en_core_web_sm` to install the english language model for spacy :D
