from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os


class Photos:
    '''
    Миниатюки фотографий
    '''

    def __init__(self, main_window):
        self.mw = main_window
        pixmap = QPixmap(os.path.join("img", "willbephoto.jpg"))
        pixmap = pixmap.scaled(
            312, 350, aspectRatioMode=Qt.KeepAspectRatio)
        self.mw.label_photos.setPixmap(pixmap)
        self.mw.label_photos.setAlignment(Qt.AlignCenter)
