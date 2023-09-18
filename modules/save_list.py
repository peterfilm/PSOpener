from modules.api import load_key_to_api, conf
from PyQt5.QtWidgets import QFileDialog
import os
from datetime import datetime


class SaveList:
    '''
    Кнопка сохранения txt файла со списком фоток
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.pushButton_saveList.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        try:
            date_now = datetime.now().strftime('psopen_%Y%m%d_%H_%M')
            file_path = QFileDialog.getSaveFileName(self.mw, 'Сохранить список файлов', date_now, 'Document *.txt')
            items = '\n'.join([os.path.normpath(self.mw.listWidget.item(i).value) for i in range(self.mw.listWidget.count())])
            with open(file_path[0], 'w') as file:
                file.write(items)
        except:
            pass
        
        
