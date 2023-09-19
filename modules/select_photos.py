from modules.api import load_key_to_api, conf
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem
from PyQt5 import QtCore
from modules._selector import Selector
from modules._checker import Checker
import os


class SelectPhotos:
    '''
    Кнопка открытия нескольких фотографий
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.pushButton_choiseYourPhotos.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        file_dialog = QFileDialog(self.mw)
        file_dialog.setOption(QFileDialog.ReadOnly)
        file_dialog.setOption(QFileDialog.HideNameFilterDetails)
        file_dialog.setNameFilters(conf['ALL_FORMATS'])

        file_dialog.setFileMode(QFileDialog.ExistingFiles)  # Allow selecting multiple files

        if file_dialog.exec_():
            try:
                self.mw.listWidget.clear()
                selected_files = file_dialog.selectedFiles()
                self.mythread = Selector(files=selected_files)  # создает экземпляр класса
                self.mythread.started.connect(self.on_started)
                self.mythread.finished.connect(self.on_finished)
                self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)  # обработчик этого сигнала
                self.mythread.start()
                folder_path = os.path.dirname(os.path.abspath(selected_files[0]))
                load_key_to_api('LAST_PATH', folder_path)
                conf['LAST_PATH'] = os.path.normpath(folder_path)
                self.mw.lineEdit_choisePhotos.setText(folder_path)
            except:
                pass
            
    def on_started(self):
        self.mw.label_pathSelectedPhoto.setText('загружаю базу...')

    def on_finished(self):
        # вызывается при завершении потока
        self.mw.label_pathSelectedPhoto.setText('')

    def on_change(self, lst):
        for item in lst:
            self.mw.listWidget.addItem(item)
        Checker.checker(self.mw)
            
            
            