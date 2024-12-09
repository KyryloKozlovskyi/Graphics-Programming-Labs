import cv2
import os
from collections import Counter

from ultralytics import YOLO

# Set the environment variable to avoid OpenMP runtime error
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Load the YOLO11 model
model = YOLO("yolo11n.pt")

# Open the video file
video_path = "vid.mp4"
cap = cv2.VideoCapture(video_path)

# Initialize a counter for tracked detections
tracked_detections = Counter()

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLO11 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True, classes=[2])

        # Extract class IDs of tracked detections
        class_ids = results[0].boxes.cls.tolist()
        tracked_detections.update(class_ids)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.namedWindow("YOLOv11 Tracking", cv2.WINDOW_KEEPRATIO)
        cv2.imshow("YOLOv11 Tracking", annotated_frame)
        cv2.resizeWindow("YOLO11 Tracking", 1240, 700)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

# Print the number of different tracked detections of each class
print("Tracked detections per class:")
for class_id, count in tracked_detections.items():
    print(f"Class {class_id}: {count}")