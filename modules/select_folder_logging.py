from PyQt5.QtWidgets import QFileDialog, QListWidgetItem
import os
from modules.api import conf, load_key_to_api, load_api_keys


class FolderLogging:
    '''
    Выбрать где размещаем комментарии
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.lineEdit_comment.setText(conf['COMMENT_PATH'])
        self.mw.pushButton_comment.clicked.connect(self.select_folder)

    def select_folder(self):
        conf = load_api_keys()
        folder_path = QFileDialog.getExistingDirectory(
            self.mw, 'Выберите папку', conf['COMMENT_PATH'])
        if folder_path:
            load_key_to_api('COMMENT_PATH', folder_path)
            self.mw.lineEdit_comment.setText(folder_path)
