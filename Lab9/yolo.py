from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load an official model

# Predict with the model, focusing on a specific class (e.g., class 0 for 'person')
results = model(source="vid.mp4", show=True, conf=0.4, save=True, classes=[0])  # predict on an image