import psutil
import os


def is_photoshop_active(photoshop_exe):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == os.path.basename(photoshop_exe):
            return True
    return False
