# AI-Smart-Doorbell


This repository contains code to serve as the basis for a smart doorbell prototype capable of AI powered package detection. The code is designed to run on a Raspberry Pi 4B, however, can be adapted to run on other hardware constrained devices.

## Code
main.py - Initializes system variables, loads the YOLO11n model, and processes the live camera feed to output real-time bounding box annotations (class and confidence). 

train.py - Configures, trains, and evaluates the YOLO11n model. Data must be pre-labeled and split prior to execution. This training file is intended to be ran on a capable computer, not the Raspberry Pi 4B. After training and evaluation, the model can be transferred to the Pi for real-time inference. 

## Hardware
Compute: Raspberry Pi 4B

Camera: Arducam IMX708 (or Pi 3 camera equivalent)

## Model

The model used is YOLO11n and the expected format is NCNN. NCNN is used to improve performance. Running the standard model format will result in unusable framerates on the Pi 4B. 

# Setup

## Training and Evaluation
1. Generate labeled training and testing data sets. Split the data into seperate folders labeled train and validation, as shown in the file structure example below.
2. In train.py, edit lines 24 thru 26 with the correct file path information. This portion of code generates a YAML file necessary to use the YOLO training libraries.
3. In train.py, edit line 39 with the file path to the classes.txt file. Update lines 40 and 49 with the correct file path to the data.yaml file.
4. If file paths are incorrect an error message should display. Otherwise, the YOLO11n model will begin training. Training parameters can be modified on line 49.
5. After training is complete, train.py will automatically retrieve the run with the best weights and begin validation. Metrics are printed displaying accuracy. 

Example File Structure:
train_split/
├── train/
│   ├── images/
│   └── labels/
└── validation/
    ├── images/
    └── labels/

## Main
1. Load the pretrained or trained model


