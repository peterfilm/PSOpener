import os
import sys
import pygetwindow as gw
import psutil
import keyboard
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QEvent, Qt
from modules.api import conf


def is_photoshop_active(photoshop_exe):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == os.path.basename(photoshop_exe):
            return True
    return False


def get_active_photo_name(photoshop_exe):
    try:
        if is_photoshop_active(photoshop_exe):
            active_window = gw.getActiveWindow()
            title = active_window.title
            # Extract only the filename from the complete string
            return title
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None


class PSName:
    def __init__(self, main_window):
        self.mw = main_window

    def get_active_photo_name(self, event):
        photoshop_exe = conf['PS_PATH']
        active_photo_name = get_active_photo_name(photoshop_exe)

        if active_photo_name:
            print("Name of the active photo in Photoshop:", active_photo_name)
        else:
            print(
                "Photoshop is not active or the active photo name could not be retrieved.")

    # def event(self, event):
    #     # Override event function to keep the window running in the background
    #     if event.type() == QEvent.WindowStateChange and self.isMinimized():
    #         self.hide()  # Hide the window when it's minimized
    #         event.ignore()  # Ignore the event to prevent closing the application
    #         return True
    #     return super().event(event)
