import subprocess
from modules.api import load_api_keys
from modules._no_photoshop import PhotoshopChecker
import time


def open_photos_in_photoshop(file_paths, ps_path):
    try:
        # Loop through the list of file paths and open each photo in Photoshop
        for file_path in file_paths:
            command = [ps_path, file_path]
            subprocess.Popen(command)
    except Exception as e:
        print(f"Error: {e}")


class Photoshop:
    '''
    Механизм открытия файлов в фотошопе
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.pushButton_oneOpenPs.clicked.connect(self.one_open)
        self.mw.pushButton_allOpen.clicked.connect(self.count_open)

    def one_open(self):
        ps_path = load_api_keys()['PS_PATH']
        file_path = self.mw.listWidget.currentItem().value
        open_photos_in_photoshop([file_path], ps_path)

    def count_open(self):
        ps_path = load_api_keys()['PS_PATH']
        if ps_path:
            try:
                conf = load_api_keys()
                count = conf['COUNT']
                items_to_remove = []
                for i in range(count):
                    if not getattr(self, 'listWidget', False):
                        item = self.mw.listWidget.takeItem(0)
                    if not getattr(self, 'mw', False):
                        item = self.listWidget.takeItem(0)
                    if item:
                        items_to_remove.append(item.value)
                open_photos_in_photoshop(items_to_remove, ps_path)
            except Exception as e:
                print(f'Error {e}')
