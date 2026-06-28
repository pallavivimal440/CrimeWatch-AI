# ===============================
# CrimeWatch AI Configuration
# ===============================

MODEL_NAME = "yolov8n.pt"

# Objects monitored for theft
VALUABLE_OBJECTS = [
    "cell phone",
    "laptop",
    "backpack",
    "handbag",
    "remote"
]

# Weapon classes from COCO dataset
WEAPON_OBJECTS = [
    "knife",
    "scissors",
    "baseball bat"
]

# Detection confidence
CONFIDENCE_THRESHOLD = 0.50

# Seconds before theft alert
MISSING_THRESHOLD = 5

# Evidence folders
THEFT_FOLDER = "evidence/theft"
WEAPON_FOLDER = "evidence/weapons"

# Log file
LOG_FILE = "logs/crime_log.txt"