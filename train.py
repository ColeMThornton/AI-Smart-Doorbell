# The purpose of this file is to generate a necessary YAML file from a custom data zip file and train a YOLO11n model using the data zip file.
# The data.zip file should contain folders labeled "images" and "labels". This file can be generated using various tools like Label-Studio for free.

import zipfile
import yaml
import os
from ultralytics import YOLO

def create_yaml(file_path_classes, file_path_data):
    
    # Check if the classes.txt file exists
    if not os.path.exists(file_path_classes):
        print(f"Unable to find classes.txt file. Please create a classes.txt file and move it to {file_path_classes}")\
    
    # open and read classes.txt file
    with open(file_path_classes, 'r') as f:
        classes = []
        for line in f.readlines():
            if len(line.strip()) == 0: continue
            classes.append(line.strip())
    class_quantity = len(classes)

    # data dictionary
    data = {'path': r'C:\Users\Cole\OneDrive\Desktop\yolo\data_split', 
            'train': 'train/images', 
            'val':"validation/images",
            'nc': class_quantity,
            'names': classes}
    
    # Create YAML file
    with open(file_path_data, "w") as f:
        yaml.dump(data, f, sort_keys = False)
    print("YAML file created.")
    return


def main():
    # Define file paths
    file_path_classes_txt = r'C:\Users\Cole\OneDrive\Desktop\yolo\data\classes.txt' # rename this str to the file path where your data.zip is. This should be the pre-split data set.
    file_path_data_yaml = r"C:\Users\Cole\OneDrive\Desktop\yolo\data.yaml"

    # Create YAML
    create_yaml(file_path_classes_txt, file_path_data_yaml)
    print("YAML file created!")

    # Load and train the yolo11n model
    model = YOLO('yolo11n.pt')
    print("Model Loaded. Begin training...")
    results = model.train(data = r"C:\Users\Cole\OneDrive\Desktop\yolo\data.yaml", epochs = 60 , imgsz = 640, batch = 16, device = 0, workers = 0)
    print("Training complete. Begin validation step. Loading best model for final validation.")
    best_model = YOLO(r"runs\detect\train\weights\best.pt")
    metrics = best_model.val()
    print(f"Final overall accuracy (mAP50-95): {metrics.box.map:.4f}")

    
if __name__ == "__main__":
    main()