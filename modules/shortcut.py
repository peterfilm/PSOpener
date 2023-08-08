from modules.api import load_key_to_api, conf
from PyQt5 import QtCore


class Shortcut:
    '''
    Кнопка выбора горячей клавиши на загрузку фото в фотошоп
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.comboBox_shortcut.setCurrentText(conf['SHORTCUT'])
        self.get_f_key()
        self.last_index = self.mw.comboBox_shortcut.findText(conf['SHORTCUT'])
        self.mw.comboBox_shortcut_comment.model().item(self.last_index).setEnabled(False)
        self.mw.comboBox_shortcut.currentTextChanged.connect(
            self.choose_shortcut)

    def get_f_key(self):
        # горячая F-клавиша
        _translate = QtCore.QCoreApplication.translate
        self.mw.pushButton_allOpen.setToolTip(_translate(
            "Form", f"<html><head/><body><p>Горячая клавиша: {conf['SHORTCUT']}</p></body></html>"))

    def choose_shortcut(self):
        self.mw.comboBox_shortcut_comment.model().item(self.last_index).setEnabled(True)
        load_key_to_api('SHORTCUT', self.mw.comboBox_shortcut.currentText())
        conf['SHORTCUT'] = self.mw.comboBox_shortcut.currentText()
        self.last_index = self.mw.comboBox_shortcut.findText(
            self.mw.comboBox_shortcut.currentText())
        self.mw.comboBox_shortcut_comment.model().item(self.last_index).setEnabled(False)
        self.get_f_key()
