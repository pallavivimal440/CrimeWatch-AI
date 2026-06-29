import time

from config import WEAPON_OBJECTS
from logger import save_weapon


class WeaponDetector:

    def __init__(self):

        self.saved = set()

        self.current_alert = None
        self.alert_time = 0
        self.alert_duration = 8

    def update(self, detections, frame):

        current_time = time.time()

        person_present = False

        weapon_found = None

        # -------------------------
        # Check detections
        # -------------------------
        for obj in detections:

            name = obj["name"]

            if name == "person":
                person_present = True

            if name in WEAPON_OBJECTS:
                weapon_found = name

        # -------------------------
        # Weapon Alert
        # -------------------------
        if (
            person_present
            and weapon_found is not None
            and weapon_found not in self.saved
        ):

            print("\n====================================")
            print("🚨 WEAPON DETECTED")
            print(f"Weapon : {weapon_found.upper()}")
            print("Saving Evidence...")
            print("====================================")

            save_weapon(frame, weapon_found)

            self.saved.add(weapon_found)

            self.current_alert = weapon_found
            self.alert_time = current_time

        # -------------------------
        # Reset when weapon disappears
        # -------------------------
        if weapon_found is None:

            self.saved.clear()

        # -------------------------
        # Keep alert for 8 sec
        # -------------------------
        if (
            self.current_alert is not None
            and current_time - self.alert_time <= self.alert_duration
        ):
            return [self.current_alert]

        return []