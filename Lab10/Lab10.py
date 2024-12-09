import cv2
import os
from collections import Counter, defaultdict

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

# Initialize a dictionary to store previous bounding boxes
previous_bboxes = defaultdict(list)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLO11 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True, classes=[2])

        # Extract class IDs and bounding boxes of tracked detections
        class_ids = results[0].boxes.cls.tolist()
        bboxes = results[0].boxes.xyxy.tolist()  # Bounding boxes in [x1, y1, x2, y2] format
        tracked_detections.update(class_ids)

        # Determine the movement direction of each object
        for class_id, bbox in zip(class_ids, bboxes):
            direction = ""
            if class_id in previous_bboxes:
                prev_bbox = previous_bboxes[class_id]
                if bbox[1] < prev_bbox[1]:  # Compare y1 coordinates
                    direction += ", Up"
                else:
                    direction += ", Down"
                print(f"#{class_id} is moving {direction}")
            previous_bboxes[class_id] = bbox

            # Display the direction on the frame
            cv2.putText(frame, direction, (int(bbox[0]), int(bbox[1]) - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

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