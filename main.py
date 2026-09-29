import time

from plyer import notification


def water_reminder():
    print("Water reminder started. Press Ctrl+C to stop.")

    try:
        while True:
            notification.notify(
                title="Drink Water Reminder",
                message="It's time to drink water!",
                timeout=10,
            )
            time.sleep(60 * 60)
    except KeyboardInterrupt:
        print("\nWater reminder stopped.")


if __name__ == "__main__":
    water_reminder()
