from modules.api import conf, load_key_to_api, load_api_keys


class SingleOrAllFolders:
    '''
    Галочка, дающая возможность видеть все файлы сквозь все папки внутри директории
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.checkBox_allFolders.setChecked(conf['THROUGH_FOLDERS'])
        self.mw.checkBox_allFolders.toggled.connect(self.toggle)

    def toggle(self):
        conf = load_api_keys()
        through_folders = 0 if conf['THROUGH_FOLDERS'] == 1 else 1
        load_key_to_api('THROUGH_FOLDERS', through_folders)
