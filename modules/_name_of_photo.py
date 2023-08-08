import os
import pygetwindow as gw
import psutil
import keyboard
from PyQt5.QtCore import QEvent
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
            filename = title.split(" @")[0].strip()
            return filename
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None


class NameOfPhoto():
    def __init__(self, main_window):
        super().__init__()
        # Hook F11 key press event
        self.mw = main_window
        keyboard.on_press_key("F11", self.get_active_photo_name)

    def get_active_photo_name(self, event):
        photoshop_exe = conf['PS_PATH']
        active_photo_name = get_active_photo_name(photoshop_exe)

        if active_photo_name:
            return active_photo_name
        else:
            return None

    def event(self, event):
        # Override event function to keep the window running in the background
        if event.type() == QEvent.WindowStateChange and self.isMinimized():
            self.hide()  # Hide the window when it's minimized
            event.ignore()  # Ignore the event to prevent closing the application
            return True
        return super().event(event)
