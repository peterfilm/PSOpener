from modules.api import load_key_to_api, conf


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
        c = int(self.mw.comboBox_howMuch.currentText())
        load_key_to_api('COUNT', c)
        conf['COUNT'] = c
