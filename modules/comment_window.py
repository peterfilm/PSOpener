from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QMessageBox
import sys
from pynput import keyboard
from data.design_comment_window import UiComment
from PyQt5.QtCore import Qt, QTimer
from modules.api import conf, keys
import pygetwindow as gw
from modules._isphotoshop import is_photoshop_active


def activate_window_by_title(window_title):
    window = gw.getWindowsWithTitle(window_title)
    if window:
        # Activate the first window with the given title
        window[0].activate()
        return True
    return False


class CommentWindow(QDialog, UiComment):
    '''
    Окошко для комментария
    '''

    def __init__(self, parent=None):
        super().__init__(parent)
        self.mw = parent
        self.setupUi(self)
        self.show()
        print(gw.getAllTitles())
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowStaysOnTopHint)
        self.setWindowModality(Qt.ApplicationModal)  # Set modal behavior
        self.pushButton_ok.clicked.connect(self.close_and_activate)
        self.returnto = gw.getActiveWindow().title
        self.pushButton_cancel.clicked.connect(self.simple_close)
        self.lineEdit_comment.setFocus()

        if self.returnto == conf['PROGRAM_NAME']:
            self.label_name.setText(self.mw.listWidget.currentItem().value)
        else:
            self.label_name.setText(self.returnto.split(' @')[0])

    def close_and_activate(self):
        if self.lineEdit_comment.text():
            if self.returnto != conf['PROGRAM_NAME']:
                activate_window_by_title(self.returnto)
            print('accept')
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Ошибка', 'Введите комментарий к фотографии')

    def simple_close(self):
        if self.returnto != 'PS Opener':
            activate_window_by_title(self.returnto)
        print('close')
        self.close()
