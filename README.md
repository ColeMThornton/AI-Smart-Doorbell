# AI-Smart-Doorbell


This repository contains code to serve as the basis for a smart doorbell prototype capable of AI powered object detection. The code is designed to run on a Raspberry Pi 4B, however, can be adapted to run on other hardware constrained devices.

## Code
main.py - The purpose of this code is to initialize system parameters, load the pretrained or trained YOLO11n model, create the live doorbell camera feed, pass each frame to the model, and annotate the frame with bounding boxes detailing the class identifier and confidence. 

train.py - The purpose of this code is to create a YOLO configuration file, import training and testing data sets, run YOLO11n training, and evaluate the 

## Hardware

Compute: Raspberry Pi 4B
Camera: 
