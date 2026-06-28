import cv2

from detector import detect_objects
from theft_detector import TheftDetector
from weapon_detector import WeaponDetector
from utils import draw_box, draw_text, draw_alert

# -----------------------------
# Initialize
# -----------------------------
camera = cv2.VideoCapture(0)

theft_detector = TheftDetector()
weapon_detector = WeaponDetector()

while True:

    ret, frame = camera.read()

    if not ret:
        break

    # -----------------------------
    # Detect Objects
    # -----------------------------
    detections = detect_objects(frame)

    # -----------------------------
    # Theft Detection
    # -----------------------------
    theft_alerts = theft_detector.update(
        detections,
        frame
    )

    # -----------------------------
    # Weapon Detection
    # -----------------------------
    weapon_alerts = weapon_detector.update(
        detections,
        frame
    )

    # -----------------------------
    # Draw Bounding Boxes
    # -----------------------------
    for obj in detections:

        name = obj["name"]
        confidence = obj["confidence"]
        box = obj["box"]

        draw_box(frame, box)

        draw_text(
            frame,
            f"{name} {confidence:.2f}",
            box[0],
            box[1] - 10
        )

    # -----------------------------
    # Theft Alert
    # -----------------------------
    for obj in theft_alerts:

        draw_alert(
            frame,
            "THEFT DETECTED",
            obj
        )

    # -----------------------------
    # Weapon Alert
    # -----------------------------
    for obj in weapon_alerts:

        draw_alert(
            frame,
            "WEAPON DETECTED",
            obj
        )

    # -----------------------------
    # Window
    # -----------------------------
    cv2.imshow(
        "CrimeWatch AI",
        frame
    )

    # Exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()

cv2.destroyAllWindows()