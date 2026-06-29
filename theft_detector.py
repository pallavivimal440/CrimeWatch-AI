import time

from config import (
    VALUABLE_OBJECTS,
    MISSING_THRESHOLD
)

from logger import save_theft


class TheftDetector:

    def __init__(self):

        self.last_seen = {}
        self.first_seen = {}
        self.alerted = set()

        # Keep alert visible
        self.current_alert = None
        self.alert_time = 0
        self.alert_duration = 8  # seconds

    def update(self, detections, frame):

        current_time = time.time()

        person_present = False

        # -------------------------
        # Update detected objects
        # -------------------------
        for obj in detections:

            name = obj["name"]

            if name == "person":
                person_present = True

            if name in VALUABLE_OBJECTS:

                if name not in self.first_seen:
                    self.first_seen[name] = current_time

                self.last_seen[name] = current_time

                # Object recovered
                if name in self.alerted:

                    print(f"✅ OBJECT RECOVERED : {name}")

                    self.alerted.remove(name)

                    if self.current_alert == name:
                        self.current_alert = None

        # -------------------------
        # Missing Check
        # -------------------------
        for name in VALUABLE_OBJECTS:

            if name not in self.last_seen:
                continue

            if name not in self.first_seen:
                continue

            missing_time = current_time - self.last_seen[name]

            visible_time = (
                self.last_seen[name]
                - self.first_seen[name]
            )

            if (
                visible_time >= 3
                and missing_time > MISSING_THRESHOLD
                and name not in self.alerted
                and person_present
            ):

                print("\n" + "=" * 45)
                print("🚨 THEFT DETECTED")
                print(f"Missing Object : {name.upper()}")
                print("Evidence Saved")
                print("=" * 45)

                save_theft(frame, name)

                self.alerted.add(name)

                self.current_alert = name
                self.alert_time = current_time

        # -------------------------
        # Keep alert on screen
        # -------------------------
        if (
            self.current_alert is not None
            and current_time - self.alert_time <= self.alert_duration
        ):
            return [self.current_alert]

        return []