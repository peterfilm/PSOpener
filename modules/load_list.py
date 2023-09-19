from modules.api import load_key_to_api, conf
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem
from PyQt5 import QtCore
from modules._selector import Selector
from modules._checker import Checker
import os

class LoadList:
    '''
    Загрузка готового списка файлов
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.pushButton_loadList.clicked.connect(self.button_clicked)
        
        
    def button_clicked(self):
        file_path = QFileDialog.getOpenFileName(self.mw, 'Загрузить список фотографий', '', 'Текстовой документ *.txt') # один формат
        if file_path[0]:
            try:
                self.mw.listWidget.clear()
                with open(file_path[0], 'r') as f:
                    files = [i.rstrip() for i in f.readlines()]
                    self.mythread = Selector(files=files)  # создает экземпляр класса
                    self.mythread.started.connect(self.on_started)
                    self.mythread.finished.connect(self.on_finished)
                    self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)  # обработчик этого сигнала
                    self.mythread.start()
            except:
                pass
                
    def on_started(self):
        self.mw.label_pathSelectedPhoto.setText('загружаю базу...')

    def on_finished(self):
        # вызывается при завершении потока
        self.mw.label_pathSelectedPhoto.setText('')
        if self.mw.listWidget.count() > 0:
            folder_path = os.path.dirname(os.path.abspath(self.mw.listWidget.item(0).value))
            load_key_to_api('LAST_PATH', folder_path)
            conf['LAST_PATH'] = os.path.normpath(folder_path)
            self.mw.lineEdit_choisePhotos.setText(folder_path)

    def on_change(self, lst):
        for item in lst:
            self.mw.listWidget.addItem(item)
        Checker.checker(self.mw)