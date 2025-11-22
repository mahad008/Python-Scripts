import os
import shutil
from pathlib import Path

def organize_file(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print("The provided folder does not exist.")
        return

    file_types = {
        "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".html", ".css"],
        "BLENDER":[".blend"],
        "STLS":[".stl"],
        "USDZ":[".usdz"],
        "FBX":[".fbx"],
        "Others": []
    }

    for file in folder.iterdir():
        if file.is_file():
            file_ext = file.suffix.lower()
            moved = False
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    target_folder = folder / category
                    target_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(target_folder / file.name))
                    moved = True
                    break
            if not moved:
                target_folder = folder / "Others"
                target_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(target_folder / file.name))

    print("File organization complete!")

# CALL the function with your folder path here:
organize_file(r"C:/Users/Mahad/Downloads")
