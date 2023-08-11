from PyQt5.QtGui import QCursor, QPixmap
from PyQt5.QtCore import Qt, QCoreApplication
import os


class Checker:
    DISABLER = 0
    '''
    Проверяем пустой ли список
    '''

    def disabler(self, value):
        self.pushButton_allOpen.setDisabled(value)
        self.pushButton_oneOpen.setDisabled(value)
        self.pushButton_oneDelete.setDisabled(value)
        self.pushButton_oneComment.setDisabled(value)
        self.pushButton_oneOpenPs.setDisabled(value)
        self.pushButton_oneOpenFolder.setDisabled(value)

    def checker(self):
        _translate = QCoreApplication.translate
        if self.listWidget.count():
            Checker.DISABLER = 0
            self.label_pathSelectedPhoto.setCursor(
                QCursor(Qt.PointingHandCursor))
            self.label_pathSelectedPhoto.setToolTip(_translate(
                "Form", "<html><head/><body><p>Копировать путь к файлу</p></body></html>"))
        elif self.listWidget.count() == 0 or self.lineEdit_psPath.text() == '':
            Checker.DISABLER = 1
            pixmap = QPixmap(os.path.join("img", "willbephoto.jpg"))
            self.label_photos.setPixmap(pixmap)
            self.label_pathSelectedPhoto.setCursor(
                QCursor(Qt.ArrowCursor))
            self.label_pathSelectedPhoto.setToolTip('')
            self.label_pathSelectedPhoto.setText('')
        Checker.disabler(self, Checker.DISABLER)
