from modules import conf
from modules.api import load_api_keys, load_key_to_api


class SelectCount:
    '''
    Кнопка выбора поличества фотока на загрузку
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.comboBox_howMuch.setCurrentText(str(conf['COUNT']))
        self.mw.comboBox_howMuch.currentTextChanged.connect(
            self.choose_shortcut)

    def choose_shortcut(self):
        load_key_to_api('COUNT', int(
            self.mw.comboBox_howMuch.currentText()))
