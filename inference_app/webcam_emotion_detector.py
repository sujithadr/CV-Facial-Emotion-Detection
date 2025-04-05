from ultralytics import YOLO
import cv2
import os

# Define the path to the model in the 'models' directory
model_path = os.path.join("models", "best.pt")

# Load the trained model
model = YOLO(model_path)

# Start webcam and run prediction
results = model.predict(source=0, show=True)
