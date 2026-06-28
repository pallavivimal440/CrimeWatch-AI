import cv2


def draw_text(frame, text, x, y, color=(0, 255, 0), scale=0.7):

    cv2.putText(
        frame,
        text,
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        scale,
        color,
        2
    )


def draw_box(frame, box, color=(0, 255, 0)):

    x1, y1, x2, y2 = box

    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        color,
        2
    )


def draw_alert(frame, title, obj):

    # Background
    cv2.rectangle(
        frame,
        (10, 10),
        (500, 120),
        (0, 0, 255),
        -1
    )

    # Border
    cv2.rectangle(
        frame,
        (10, 10),
        (500, 120),
        (255, 255, 255),
        2
    )

    # Heading
    cv2.putText(
        frame,
        "CRIMEWATCH AI ALERT",
        (25, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    # Alert Type
    cv2.putText(
        frame,
        title,
        (25, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        (0, 255, 255),
        2
    )

    # Object Name
    cv2.putText(
        frame,
        obj.upper(),
        (25, 105),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )