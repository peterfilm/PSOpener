from api import conf
import subprocess


def open_photos_in_photoshop(file_paths):
    try:
        # Replace "Photoshop.exe" with the actual path to Photoshop executable on your system
        photoshop_exe = conf['PS_PATH']

        # Loop through the list of file paths and open each photo in Photoshop
        for file_path in file_paths:
            command = [photoshop_exe, file_path]
            subprocess.Popen(command)

    except Exception as e:
        print(f"Error: {e}")
