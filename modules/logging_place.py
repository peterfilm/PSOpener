from modules import conf
from modules.api import load_api_keys, load_key_to_api


class LoggingPlace:
    '''
    Выбрать где размещать комментарии к фотографиям.
    '''

    def __init__(self, main_window):
        self.mw = main_window
        if not conf['LOGGING_PLACE']:
            self.mw.radioButton_commentSameFolder.setChecked(True)
            self.mw.lineEdit_comment.setEnabled(False)
            self.mw.pushButton_comment.setEnabled(False)
        else:
            self.mw.radioButton_commentChoise.setChecked(True)
            self.mw.lineEdit_comment.setEnabled(True)
            self.mw.pushButton_comment.setEnabled(True)
        self.mw.radioButton_commentSameFolder.toggled.connect(
            self.radio_selected)

    def radio_selected(self):
        conf = load_api_keys()
        radio_btn = self.mw.sender()
        if radio_btn.isChecked():
            load_key_to_api('LOGGING_PLACE', 0)
            self.mw.lineEdit_comment.setEnabled(False)
            self.mw.pushButton_comment.setEnabled(False)
            load_key_to_api('COMMENT_PATH', conf['LAST_PATH'])
        else:
            load_key_to_api('LOGGING_PLACE', 1)
            self.mw.lineEdit_comment.setEnabled(True)
            self.mw.pushButton_comment.setEnabled(True)
