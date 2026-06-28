from ultralytics import YOLO

from config import (
    MODEL_NAME,
    CONFIDENCE_THRESHOLD
)

# Load model only once
model = YOLO(MODEL_NAME)


def detect_objects(frame):
    """
    Returns:
    [
        {
            "name": object_name,
            "confidence": confidence,
            "box": [x1,y1,x2,y2]
        }
    ]
    """

    detections = []

    results = model(frame, verbose=False)

    for result in results:

        for box in result.boxes:

            confidence = float(box.conf[0])

            if confidence < CONFIDENCE_THRESHOLD:
                continue

            cls = int(box.cls[0])

            name = model.names[cls]
            

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            detections.append(
                {
                    "name": name,
                    "confidence": confidence,
                    "box": (x1, y1, x2, y2)
                }
            )

    return detections