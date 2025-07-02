import image_interpreter.snapshot
print("Snapshot module loaded from:", image_interpreter.snapshot.__file__)
print("Contents of snapshot module:", dir(image_interpreter.snapshot))
import os
from image_interpreter.config import (
    OPENAI_API_KEY, BRIGHTSIGN_IP, SNAPSHOT_PATH, REFERENCE_IMAGE_PATH, OUTPUT_FOLDER
)

from image_interpreter.snapshot import get_brightsign_snapshot
from image_interpreter.analyzer import analyze_images

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    if not OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY not found in .env file")
        exit(1)

    snapshot_file = get_brightsign_snapshot(BRIGHTSIGN_IP, SNAPSHOT_PATH)
    if not snapshot_file:
        print("Failed to capture snapshot. Exiting.")
        return

    analyze_images(snapshot_file, REFERENCE_IMAGE_PATH)

if __name__ == "__main__":
    main()
