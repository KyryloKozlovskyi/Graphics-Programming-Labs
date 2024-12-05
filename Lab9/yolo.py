from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load an official model

# Predict with the model
results = model(source="vid.mp4", show=True, conf=0.4, save=True)  # predict on an image