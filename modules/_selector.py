from PyQt5 import QtCore
from PyQt5.QtWidgets import QListWidgetItem
import os


class Selector(QtCore.QThread):
    '''
    Многопоточное добавление файлов в список программы
    '''
    mysignal = QtCore.pyqtSignal(list)
    
    def __init__(self, files, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.files = files
        self.lst = []
        
    def add_to_lst(self):
        try:
            for file in self.files:
                if os.path.exists(file):
                    file_name = os.path.basename(file)
                    item = QListWidgetItem(file_name)
                    item.value = os.path.normpath(file)
                    self.lst.append(item)
        except Exception as e:
            print(e)
    
    def run(self):
        self.add_to_lst()
        self.mysignal.emit(self.lst)