import os
import time
import shutil
import requests
from datetime import datetime

# === CONFIGURATION ===
SOURCE_FOLDER = "C:/Users/YourName/Downloads"
DESTINATION_FOLDER = "C:/Users/YourName/Documents/Organized"
FILE_TYPES = {
    "Images": [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"],
}

# === AUTOMATION TASK ===
def organize_files():
    print(f"📁 Organizing files from {SOURCE_FOLDER}...")
    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    target_folder = os.path.join(DESTINATION_FOLDER, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"✅ Moved: {filename} → {folder}")
                    break

# === OPTIONAL: Scheduled Execution ===
def run_every(interval_seconds=3600):
    while True:
        organize_files()
        print(f"⏳ Waiting {interval_seconds} seconds...\n")
        time.sleep(interval_seconds)

# === MAIN ===
if __name__ == "__main__":
    organize_files()
    # Uncomment below to run on a schedule
    # run_every(3600)  # every hour