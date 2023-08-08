from modules.api import load_api_keys, load_key_to_api, conf
from functools import partial


class ChoseExtensions:
    '''
    Чекбоксы разрешенных разрешений
    '''

    def __init__(self, main_window):
        self.mw = main_window
        # устанавливаем значения
        if '.jpg' in conf['SELECTED_EXTENSIONS']:
            self.mw.checkBox_jpg.setChecked(True)
        if '.cr2' in conf['SELECTED_EXTENSIONS']:
            self.mw.checkBox_raw.setChecked(True)
        if '.png' in conf['SELECTED_EXTENSIONS']:
            self.mw.checkBox_png.setChecked(True)
        if '.tiff' in conf['SELECTED_EXTENSIONS']:
            self.mw.checkBox_tiff.setChecked(True)
        if '.psd' in conf['SELECTED_EXTENSIONS']:
            self.mw.checkBox_psd.setChecked(True)
        if '.bmp' in conf['SELECTED_EXTENSIONS']:
            self.mw.checkBox_bmp.setChecked(True)

        # отслеживаем состояния
        self.mw.checkBox_raw.stateChanged.connect(
            partial(self.check_raws, 'RAWS', self.mw.checkBox_raw))
        self.mw.checkBox_jpg.stateChanged.connect(
            partial(self.check_raws, 'JPEG', self.mw.checkBox_jpg))
        self.mw.checkBox_psd.stateChanged.connect(
            partial(self.check_raws, 'PSD', self.mw.checkBox_psd))
        self.mw.checkBox_png.stateChanged.connect(
            partial(self.check_raws, 'PNG', self.mw.checkBox_png))
        self.mw.checkBox_tiff.stateChanged.connect(
            partial(self.check_raws, 'TIFF', self.mw.checkBox_tiff))
        self.mw.checkBox_bmp.stateChanged.connect(
            partial(self.check_raws, 'BMP', self.mw.checkBox_bmp))

    def check_raws(self, value, button):
        conf = load_api_keys()
        if button.isChecked():
            conf['SELECTED_EXTENSIONS'].extend(conf[value])
            load_key_to_api('SELECTED_EXTENSIONS',
                            conf['SELECTED_EXTENSIONS'])
        else:
            for i in conf[value]:
                conf['SELECTED_EXTENSIONS'].remove(i)
            load_key_to_api('SELECTED_EXTENSIONS',
                            conf['SELECTED_EXTENSIONS'])
