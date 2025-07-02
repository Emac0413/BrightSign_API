import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BRIGHTSIGN_IP = os.getenv("BRIGHTSIGN_IP", "192.168.0.3")

OUTPUT_FOLDER = os.path.expanduser(r"C:\Users\Terminal 1\Documents\pic_repo")
SNAPSHOT_PATH = os.path.join(OUTPUT_FOLDER, "bs_screenshot.png")
REFERENCE_IMAGE_PATH = r"C:\Users\Terminal 1\Documents\Comparator\bs_setup.jpg"