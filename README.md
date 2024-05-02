# Patient-data-processing
This repository provides tools to streamline the preparation of healthcare imaging datasets for ML applications. It includes routines for pre-processing tasks and facilitates patient-level data splitting for model training and evaluation.
This repository contains Python routines for preprocessing patient imaging data for machine learning applications.

## Project Structure
* `data_preprocessing.py` - A data preprocessing function that inputs a folder with patient data organized in sub-flders to generate a patient-level test-train split of data
* `imagesieviewer.py` - An Py Qt window to view the pixels identity of an image , helps in identifying the crop points for image post-processing
* ... (other files as I develop the project)

## Usage
All the requirements have been put in the requirements.txt file
```bash
pip install -r requirements.txt
```
