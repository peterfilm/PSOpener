from modules import conf
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from modules.api import load_api_keys, load_key_to_api
import os
import subprocess
from modules._checker import Checker


class ButtonsFile:
    '''
    Кнопки для работы с фотографией
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.pushButton_oneOpen.clicked.connect(self.open_in_viewer)
        self.mw.pushButton_oneDelete.clicked.connect(self.remove_from_list)
        self.mw.pushButton_oneOpenFolder.clicked.connect(self.open_folder)

    # Открыть фото в просмотрщике
    def open_in_viewer(self):
        file_path = self.mw.listWidget.currentItem().value
        url = QUrl.fromLocalFile(file_path)
        QDesktopServices.openUrl(url)

    # Открыть фото в папке
    def open_folder(self):
        file_path = self.mw.listWidget.currentItem().value  # путь к файлу
        folder_path = os.path.dirname(file_path)  # Путь к папке

        # Если файл есть - открывается в эксплорере
        try:
            if os.name == "nt":  # Windows
                subprocess.Popen(
                    ["explorer", "/select,", os.path.normpath(file_path)])
            elif os.name == "posix":  # macOS or Linux
                subprocess.Popen(["xdg-open", os.path.normpath(folder_path)])
            else:
                print("Не поддерживается система")
        except Exception as e:
            print("Ошибка открытия папки:", e)

    # Убрать фото из списка
    def remove_from_list(self):
        row = self.mw.listWidget.currentRow()
        item = self.mw.listWidget.item(row)
        if item is None:
            return
        self.mw.listWidget.takeItem(row)
        Checker.checker(self.mw)
