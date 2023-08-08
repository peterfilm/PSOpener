from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import sys
from pynput import keyboard
from data.design import UI
from modules import *


class PSOpener(QWidget, UI):
    '''
    Программа для создания очереди открытия файлов в фотошопе
    '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # кнопки
        self.ps = PSSelect(self)  # выбор фотошопа
        self.choose_folder = ChooseFolder(self)  # выбор папки с фотографиями
        self.shortcut = Shortcut(self)  # выбрать горячую клавишу
        # выбрать горячую клавишу на коммент
        self.shortcut_comment = Shortcut_Comment(self)
        self.photos = Photos(self)  # выбрать фотографии
        # галочка выбора все папки или только одну
        # Одна директория или еще вложенные
        self.safolders = SingleOrAllFolders(self)
        # Выбрать количество фотографий на загрузку в фотошоп
        self.count = SelectCount(self)
        # Выбираем Где публикуются комментарии к фотографиям
        self.place = LoggingPlace(self)
        # Указываем напрямую папку с фотографиями
        self.logging_folder = FolderLogging(self)
        self.chose_extensions = ChoseExtensions(
            self)  # выбор доступных расширений
        self.lw = ListViewer(self)  # главный List Viewer
        self.btns = ButtonsFile(self)  # кнопки под фоткой
        self.pshop = Photoshop(self)  # механизм открытия в фотошоп


def on_press(key):
    try:
        if key == keys[conf['SHORTCUT']]:
            window.pshop.count_open()
    except AttributeError:
        pass


if __name__ == "__main__":
    # Start the pynput listener
    app = QApplication(sys.argv)
    window = PSOpener()
    window.show()
    with keyboard.Listener(on_press=on_press) as listener:
        sys.exit(app.exec_())
