from PyQt5.QtWidgets import QFileDialog, QListWidgetItem
import os
from PyQt5 import QtCore
from modules.api import conf, load_key_to_api
import re
from modules._checker import Checker


def natural_sort_key(s):
    '''
    Натуральный порядок чисел
    '''
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


def get_files_by_extension(folder_path, extensions):
    '''
    Выбираем только файлы нужных форматов
    '''
    absolute_paths = []
    for file in os.listdir(folder_path):
        for extension in extensions:
            if file.lower().endswith(extension):
                absolute_paths.append(
                    '/'.join([folder_path, file]).replace('//', '/'))
                break
    return sorted(absolute_paths, key=natural_sort_key)


def get_files_all_folders(folder_path, extensions):
    '''
    Выбираем только файлы нужных форматов со всех папок
    '''
    absolute_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            for extension in extensions:
                if file.lower().endswith(extension):
                    absolute_paths.append(
                        '/'.join([root, file]).replace('\\', '/').replace('//', '/'))
                    break
    return sorted(absolute_paths, key=natural_sort_key)


class Selector(QtCore.QThread):
    '''
    Поток на создание списка из QListWidgetItem путей фотографий
    '''
    mysignal = QtCore.pyqtSignal(list)

    def __init__(self, link, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.link = link
        self.lst = []

    def change_folder(self, folder_path):
        try:
            if conf['THROUGH_FOLDERS'] == 0:
                files_with_extension = get_files_by_extension(
                    folder_path, conf['SELECTED_EXTENSIONS'])
            elif conf['THROUGH_FOLDERS'] == 1:
                files_with_extension = get_files_all_folders(
                    folder_path, conf['SELECTED_EXTENSIONS'])
            for file in files_with_extension:
                if file is not None:
                    file_name = file.split('/')[-1]
                    item = QListWidgetItem(file_name)
                    item.value = file
                self.lst.append(item)
        except Exception as e:
            print(e)

    def run(self):  # обязательный для потоков метод
        self.change_folder(self.link)
        self.mysignal.emit(self.lst)


class ChooseFolder:
    '''
    Выбрать фотографии нужных форматов и загрузить их в ListWidget.
    '''

    def __init__(self, main_window):
        self.mw = main_window
        load_key_to_api('LAST_PATH', '')
        conf['LAST_PATH'] = ''
        Checker.DISABLER = 0
        Checker.checker(self.mw)

        self.mw.pushButton_choisePhotos.clicked.connect(self.select_folder)
        self.mw.lineEdit_choisePhotos.returnPressed.connect(
            self.pressedReturn)

    def pressedReturn(self):
        folder_path = self.mw.lineEdit_choisePhotos.text()
        self.mw.listWidget.clear()
        self.mythread = Selector(link=folder_path)
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(
            self.on_change, QtCore.Qt.QueuedConnection)  # обработчик этого сигнала
        self.mw.lineEdit_choisePhotos.setText(folder_path)
        self.mythread.start()
        load_key_to_api('LAST_PATH', folder_path)
        conf['LAST_PATH'] = folder_path
        Checker.checker(self.mw)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(
            self.mw, 'Выберите папку', conf['LAST_PATH'])
        if folder_path:
            self.mw.listWidget.clear()
            self.mythread = Selector(link=folder_path)
            self.mythread.started.connect(self.on_started)
            self.mythread.finished.connect(self.on_finished)
            self.mythread.mysignal.connect(
                self.on_change, QtCore.Qt.QueuedConnection)  # обработчик этого сигнала
            self.mw.lineEdit_choisePhotos.setText(folder_path)
            self.mythread.start()
            load_key_to_api('LAST_PATH', folder_path)
            conf['LAST_PATH'] = folder_path

    def on_started(self):
        self.mw.label_pathSelectedPhoto.setText('загружаю базу...')

    def on_finished(self):
        # вызывается при завершении потока
        self.mw.label_pathSelectedPhoto.setText('')

    def on_change(self, lst):
        for item in lst:
            self.mw.listWidget.addItem(item)
        Checker.checker(self.mw)
