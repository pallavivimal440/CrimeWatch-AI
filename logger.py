import os
import cv2
import time
from datetime import datetime

from config import (
    THEFT_FOLDER,
    WEAPON_FOLDER,
    LOG_FILE
)

# Create folders automatically
os.makedirs(THEFT_FOLDER, exist_ok=True)
os.makedirs(WEAPON_FOLDER, exist_ok=True)
os.makedirs("logs", exist_ok=True)


def save_theft(frame, object_name):

    timestamp = time.strftime("%Y%m%d_%H%M%S")

    filename = (
        f"{THEFT_FOLDER}/"
        f"{object_name.replace(' ','_')}_{timestamp}.jpg"
    )

    cv2.imwrite(filename, frame)

    with open(LOG_FILE, "a") as log:

        log.write(
            f"[{datetime.now()}] "
            f"THEFT | {object_name} | "
            f"{filename}\n"
        )

    print(f"📸 Theft Evidence Saved : {filename}")

    return filename


def save_weapon(frame, weapon_name):

    timestamp = time.strftime("%Y%m%d_%H%M%S")

    filename = (
        f"{WEAPON_FOLDER}/"
        f"{weapon_name.replace(' ','_')}_{timestamp}.jpg"
    )

    cv2.imwrite(filename, frame)

    with open(LOG_FILE, "a") as log:

        log.write(
            f"[{datetime.now()}] "
            f"WEAPON | {weapon_name} | "
            f"{filename}\n"
        )

    print(f"🔪 Weapon Evidence Saved : {filename}")

    return filename