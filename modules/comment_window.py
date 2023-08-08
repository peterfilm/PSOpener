from PyQt5.QtWidgets import QApplication, QWidget, QDialog
import sys
from pynput import keyboard
from data.design_comment_window import UiComment
from PyQt5.QtCore import Qt, QTimer
from modules.api import conf, keys
import pygetwindow as gw


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
        self.setupUi(self)
        self.show()

        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowStaysOnTopHint)
        self.setWindowModality(Qt.ApplicationModal)  # Set modal behavior
        self.lineEdit_comment.setFocus()

        self.pushButton_ok.clicked.connect(self.close_and_activate)
        self.returnto = gw.getActiveWindow().title
        self.label_name.setText(self.returnto.split(' @')[0])

    def close_and_activate(self):
        activate_window_by_title(self.returnto)
        self.close()
