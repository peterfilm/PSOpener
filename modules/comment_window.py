from PyQt5.QtWidgets import QDialog, QMessageBox
from data.design_comment_window import UiComment
from PyQt5.QtCore import Qt
from modules.api import conf
import pygetwindow as gw
from modules._write_logs import write_log


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
            write_log(self.label_name.text(), self.lineEdit_comment.text())
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Ошибка', 'Введите комментарий к фотографии')

    def simple_close(self):
        if self.returnto != 'PS Opener':
            activate_window_by_title(self.returnto)
        self.close()
