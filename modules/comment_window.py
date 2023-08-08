from PyQt5.QtWidgets import QApplication, QWidget, QDialog
import sys
from pynput import keyboard
from data.design_comment_window import UiComment
from PyQt5.QtCore import Qt
from modules.api import conf, keys


class CommentWindow(QDialog, UiComment):
    '''
    Окошко для комментария
    '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


def on_press(key):
    try:
        if key == keys[conf['SHORTCUT']]:
            window.pshop.count_open()
    except AttributeError:
        pass


if __name__ == "__main__":
    # Start the pynput listener
    app = QApplication(sys.argv)
    window = CommentWindow()
    window.show()
    with keyboard.Listener(on_press=on_press) as listener:
        sys.exit(app.exec_())
