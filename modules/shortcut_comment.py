from modules.api import load_api_keys, load_key_to_api, conf
from PyQt5 import QtCore


class Shortcut_Comment:
    '''
    Кнопка выбора горячей клавиши на комментарии
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.comboBox_shortcut_comment.setCurrentText(
            conf['SHORTCUT_COMMENT'])
        self.last_index = self.mw.comboBox_shortcut.findText(
            conf['SHORTCUT_COMMENT'])
        self.mw.comboBox_shortcut.model().item(self.last_index).setEnabled(False)
        self.mw.comboBox_shortcut_comment.currentTextChanged.connect(
            self.choose_shortcut_comment)

    def choose_shortcut_comment(self):
        self.mw.comboBox_shortcut.model().item(self.last_index).setEnabled(True)
        load_key_to_api('SHORTCUT_COMMENT',
                        self.mw.comboBox_shortcut_comment.currentText())
        self.last_index = self.mw.comboBox_shortcut_comment.findText(
            self.mw.comboBox_shortcut_comment.currentText())
        self.mw.comboBox_shortcut.model().item(self.last_index).setEnabled(False)
