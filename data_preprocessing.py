import os
import random
import shutil
import numpy as np

def data_preprocessing(data_root,percentage=0.15):
    # Percentage is preset to 15% for test set
    """
    Processes patient data within the specified root directory.

    Args:
        data_root (str): The root directory containing patient data folders.

    Returns:
        tuple: (trainval_data, test_data)
            - trainval_data (list): List of (image_path, mask_path) tuples for training/validation.
            - test_data (list): List of (image_path, mask_path) tuples for testing.
    """

    patient_folders = [f for f in os.listdir(data_root) if os.path.isdir(os.path.join(data_root, f))]
    #Descibing the patient data and converting to a list
    # print(f"Number of patients: {len(patient_folders)}")
    patient_summary = []  # Create the summary list
    trainval_data = []
    test_data = []

    for patient_folder in patient_folders:
        patient_path = os.path.join(data_root, patient_folder)

        images = [f for f in os.listdir(patient_path) if f.endswith('.jpg') or f.endswith('.png') and not f.endswith('_mask.png')]
        masks = [f for f in os.listdir(patient_path) if f.endswith('_mask.jpg') or f.endswith('_mask.png')]  # Assuming .mask extension

        # print(f"Patient: {patient_folder}, Images: {len(images)}, Masks: {len(masks)}")
        patient_summary.append({
                "Patient ID": patient_folder,
                "No. of Images": len(images),
                "No. of Labels/Masks": len(masks)
            })
        
    patient_summary.sort(key = lambda x: x["No. of Labels/Masks"], reverse=False)
    # print(patient_summary)
    # sum_masks = np.sum(patient_summary[:]["No. of Labels/Masks"])
    # sum_images = np.sum(patient_summary[:]["No. of Images"])
    sum_no_of_patients = len(patient_summary)
    _percent_patients = int(sum_no_of_patients * percentage)
    if _percent_patients == 0:  _percent_patients = 1    # Ensure at least one patient is in the test set
    test_patient = [patient["Patient ID"] for patient in patient_summary[0:_percent_patients]]
    # print(f"15% of patients: {_percent_patients}")
    # test_patient = [patient["Patient ID"] for patient in patient_summary[0:_percent_patients]]
    # print(f"Test patients: {test_patient}")
    # print(f"Total number of patients: {sum_no_of_patients}")
    # print(f"15% of patients: {_percent_patients}")

    # Split data into trainval and test sets
    for patient_folder in patient_folders:
        patient_path = os.path.join(data_root, patient_folder)
        print()
        images = [f for f in os.listdir(patient_path) if f.endswith('.jpg') or f.endswith('.png') and not f.endswith('_mask.png')]
        masks = [f for f in os.listdir(patient_path) if f.endswith('_mask.jpg') or f.endswith('_mask.png')]  # Assuming .mask extension
        files_without_masks = 0
        for image in images:
            image_path = os.path.join(patient_path, image)
            mask_name = os.path.splitext(image)[0] + '_mask.png'  # Infer mask name
            mask_path = os.path.join(patient_path, mask_name)

            if os.path.exists(mask_path):
                if patient_folder in test_patient:  # ~15% for test set
                    test_data.append((image_path.split(".")[0].split("/")[-2:]))
                else:
                    trainval_data.append((image_path.split(".")[0].split("/")[-2:]))    
            else:
                files_without_masks += 1 

        # print(f"Files without masks in {patient_folder}: {files_without_masks}")
    with open(data_root+"trainval.txt", "w") as f:  # Save trainval data to a file
        for image_path in trainval_data:
            image_path_joined = "/".join(image_path)
            f.write(f"{image_path_joined}\n")

    with open(data_root+"test.txt", "w") as f:  # Save test data to a file
        for image_path in test_data:
            image_path_joined = "/".join(image_path)
            f.write(f"{image_path_joined}\n")
    
    print("trainval.txt with {} datapoints and test.txt with {} datapoints created successfully!".format(len(trainval_data), len(test_data)))                 
    return patient_summary,trainval_data, test_data # Return the summary and data splits

# if __name__ == "__main__":

data_root = "/home/ark/Documents/Ultrasound Guided Needle Project/needle segmentation_true/"  # Replace with the actual path to your data
patient_summary,trainval_data, test_data = data_preprocessing(data_root,0.15)



