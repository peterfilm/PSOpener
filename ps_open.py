from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer, QEvent
import sys
from pynput import keyboard
from data.design import UI
from data.design_comment_window import UiComment
from modules import *
import pygetwindow as gw


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

        # окошко для комментария
        self.pushButton_oneComment.clicked.connect(self.open_modal_comment)

    def open_modal_comment(self):
        # модальное окно для комментария
        if is_photoshop_active:
            if self.listWidget.currentItem() or gw.getActiveWindow().title != conf['PROGRAM_NAME']:
                modal = CommentWindow(self)
                modal.show()
            else:
                QMessageBox.information(
                    self, 'Нет фото', 'Выберите фото для комментирования')


class ListenerThread(QThread):
    shortcut_pressed = pyqtSignal(str)

    def __init__(self, shortcut):
        super().__init__()
        self.shortcut = shortcut

    def run(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        try:
            if key == keys[self.shortcut]:
                self.shortcut_pressed.emit(self.shortcut)
        except AttributeError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PSOpener()
    window.show()

    shortcut_thread = ListenerThread(conf['SHORTCUT'])
    comment_shortcut_thread = ListenerThread(conf['SHORTCUT_COMMENT'])

    shortcut_thread.shortcut_pressed.connect(window.pshop.count_open)
    comment_shortcut_thread.shortcut_pressed.connect(window.open_modal_comment)

    shortcut_thread.start()
    comment_shortcut_thread.start()

    sys.exit(app.exec_())
