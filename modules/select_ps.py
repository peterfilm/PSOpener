from PyQt5.QtWidgets import QFileDialog, QMessageBox
from modules.api import conf, load_key_to_api
from modules._no_photoshop import PhotoshopChecker
import os


class PSSelect:
    '''
    Кнопка выбора фотошопа.
    Нужно предоставить полный путь до установленного фотошопа в системе
    '''

    def __init__(self, main_window):
        self.mw = main_window

        PhotoshopChecker.set_photoshop(self.mw)
        if not conf['PS_PATH']:
            QMessageBox.information(
                self.mw, 'Укажите путь к Photoshop', 'Укажите правильный путь к Photoshop.exe')

        self.mw.toolButton_psPath.clicked.connect(self.select_ps)
        self.mw.lineEdit_psPath.setText(conf['PS_PATH'])
        self.mw.lineEdit_psPath.editingFinished.connect(self.writepath)

    def check_link(self, link):
        if link and conf['PHOTOSHOP_NAME'] == os.path.basename(link):
            self.mw.lineEdit_psPath.setText(link)
            load_key_to_api('PS_PATH', link)
            conf['PS_PATH'] = os.path.normpath(link)
            PhotoshopChecker.set_photoshop(self.mw)
        else:
            load_key_to_api('PS_PATH', '')
            conf['PS_PATH'] = ''
            self.mw.lineEdit_psPath.setText('')
            PhotoshopChecker.set_photoshop(self.mw)

    def writepath(self):
        self.check_link(self.mw.lineEdit_psPath.text())
        PhotoshopChecker.set_photoshop(self.mw)

    def select_ps(self):
        folder_path = QFileDialog.getOpenFileName(
            self.mw, 'Установите путь к Photoshop', conf['PS_PATH'], 'Photoshop.exe *.exe')
        if folder_path:
            self.check_link(folder_path[0])
        if not self.mw.lineEdit_psPath.text():
            QMessageBox.information(
                self.mw, 'Укажите путь к Photoshop', 'Укажите правильный путь к Photoshop.exe')
