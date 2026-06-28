import time

from config import WEAPON_OBJECTS
from logger import save_weapon


class WeaponDetector:

    def __init__(self):

        self.saved = set()

        self.first_seen = {}

    def update(self, detections, frame):

        alerts = []

        current_detected = set()

        current_time = time.time()
        person_present = False

        for obj in detections:

            name = obj["name"]
            if name == "person":
                person_present = True

            if name in WEAPON_OBJECTS:

                current_detected.add(name)

                if name not in self.first_seen:
                    self.first_seen[name] = current_time

                visible_time = (
                    current_time
                    - self.first_seen[name]
                )

                if (
                    visible_time >= 2
                    and person_present
                    and name not in self.saved
                ):

                    print(f"\n🚨 WEAPON DETECTED : {name}")

                    save_weapon(frame, name)

                    self.saved.add(name)

                    alerts.append(name)

        # Reset when weapon disappears
        for name in list(self.first_seen.keys()):
            if name not in current_detected:
                self.first_seen.pop(name)

        self.saved = self.saved.intersection(current_detected)

        return alerts