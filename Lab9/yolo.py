import os
from ultralytics import YOLO

# Set the environment variable to avoid OpenMP runtime error
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Load a model
model = YOLO("yolo11n.pt")  # load an official model

# Predict with the model
# results = model(source="vid.mp4", show=True, conf=0.4, save=True)  # video
# results = model(source="vid.mp4", show=True, conf=0.4, save=True, classes=[0])  # specific class

results = model.track(source="vid.mp4", show=True, conf=0.4, save=True, classes=[2])

# Count unique object detections
unique_objects = set()
for result in results:
    for obj in result.boxes:
        unique_objects.add(obj.id)

print(f"Number of unique objects detected: {len(unique_objects)}")