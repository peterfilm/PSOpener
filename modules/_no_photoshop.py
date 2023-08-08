from PyQt5.QtGui import QCursor, QPixmap
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QMessageBox
from modules.api import load_api_keys


class PhotoshopChecker:
    ISPHOTOSHOP = 0
    '''
    Скрипт проверяет есть ли ссылка на фотошоп, иначе блокирует все кнопки.
    В случае ошибки связанной с тем, что фотошоп не найдет - снова заблокирует все кнопки
    '''

    def disabler(self, value):
        self.comboBox_howMuch.setEnabled(value)
        self.checkBox_allFolders.setEnabled(value)
        self.comboBox_shortcut.setEnabled(value)
        self.comboBox_shortcut_comment.setEnabled(value)
        self.radioButton_commentSameFolder.setEnabled(value)
        self.radioButton_commentChoise.setEnabled(value)
        self.lineEdit_choisePhotos.setEnabled(value)
        self.pushButton_choisePhotos.setEnabled(value)

        if self.listWidget.count() != 0:
            self.pushButton_allOpen.setEnabled(value)
            self.pushButton_oneOpen.setEnabled(value)
            self.pushButton_oneDelete.setEnabled(value)
            self.pushButton_oneComment.setEnabled(value)
            self.pushButton_oneOpenPs.setEnabled(value)
            self.pushButton_oneOpenFolder.setEnabled(value)

        self.checkBox_raw.setEnabled(value)
        self.checkBox_jpg.setEnabled(value)
        self.checkBox_psd.setEnabled(value)
        self.checkBox_png.setEnabled(value)
        self.checkBox_tiff.setEnabled(value)
        self.checkBox_bmp.setEnabled(value)
        self.listWidget.setEnabled(value)

    def set_photoshop(self):
        PhotoshopChecker.ISPHOTOSHOP = PhotoshopChecker.check_photoshop(
            self)
        PhotoshopChecker.disabler(self, PhotoshopChecker.ISPHOTOSHOP)

    def check_photoshop(self):
        conf = load_api_keys()
        if conf['PS_PATH']:
            return True
        else:
            return False
