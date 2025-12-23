import os
import shutil

DOWNLOADS_DIR = os.path.join(os.path.expanduser("~"), "Downloads")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Executables": [".exe", ".msi"],
}

def get_folder_name(extension):
    for folder, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return folder
    return "Others"

def organize_downloads():
    for filename in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        folder_name = get_folder_name(ext)

        target_folder = os.path.join(DOWNLOADS_DIR, folder_name)
        os.makedirs(target_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(target_folder, filename))
        print(f"Moved: {filename} → {folder_name}/")

if __name__ == "__main__":
    organize_downloads()
    print("✅ Download folder organized!")
