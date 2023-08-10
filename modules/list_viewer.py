from modules.api import conf
from PyQt5.QtGui import QPixmap, QImageReader, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
import rawpy


class ListViewer:
    '''
    Главный List Widget
    '''
    PIXMAP_FORMATS = ['bmp', 'gif', 'jpg', 'jpeg',
                      'png', 'pbm', 'pgm', 'ppm', 'xbm', 'xpm']

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.listWidget.itemClicked.connect(self.clicked)
        self.mw.listWidget.currentItemChanged.connect(self.clicked)

    def change_photo(self, item):

        image_reader = QImageReader(item)
        # Automatically transform based on Exif orientation
        image_reader.setAutoTransform(True)

        image = image_reader.read()

        pixmap = QPixmap.fromImage(image)
        pixmap = pixmap.scaled(312, 350, aspectRatioMode=Qt.KeepAspectRatio)
        self.mw.label_photos.setPixmap(pixmap)
        self.mw.label_photos.setAlignment(Qt.AlignCenter)

    def open_raw(self, item):
        try:
            with rawpy.imread(item) as raw:
                rgb = raw.postprocess(use_camera_wb=True,
                                      output_bps=8, half_size=True)

            # Convert the raw image data to QImage
            height, width, channel = rgb.shape
            q_image = QImage(rgb, width, height,
                             width * 3, QImage.Format_RGB888)

            desired_height = 350
            q_image = q_image.scaledToHeight(desired_height)

            pixmap = QPixmap.fromImage(q_image)
            pixmap = pixmap.scaled(
                312, 350, aspectRatioMode=Qt.KeepAspectRatio)
            self.mw.label_photos.setPixmap(pixmap)
            self.mw.label_photos.setAlignment(Qt.AlignCenter)
        except:
            self.change_photo('img/nophoto.jpg')

    def clicked(self, item):
        if item:
            self.mw.label_pathSelectedPhoto.setText(item.value)
            self.mw.label_pathSelectedPhoto.clicked.connect(self.buffer)
            frmt = item.value.split('.')[-1].lower()
            if frmt in self.PIXMAP_FORMATS:
                try:
                    pass
                    self.change_photo(item.value)
                except:
                    self.change_photo('img/nophoto.jpg')
            elif '.' + frmt in conf['RAWS']:
                self.open_raw(item.value)
            else:
                self.change_photo('img/nophoto.jpg')

    def buffer(self):
        # копировать текст в буффер обмена
        a = self.mw.label_pathSelectedPhoto.text()
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(a, mode=cb.Clipboard)
