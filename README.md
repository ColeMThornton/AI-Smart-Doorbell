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

# File structure 


