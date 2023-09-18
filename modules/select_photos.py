from modules.api import load_key_to_api, conf
from PyQt5.QtWidgets import QFileDialog


class SelectPhotos:
    '''
    Кнопка открытия нескольких фотографий
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.pushButton_choiseYourPhotos.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        file_dialog = QFileDialog(self.mw)
        file_dialog.setOption(QFileDialog.ReadOnly)
        file_dialog.setOption(QFileDialog.HideNameFilterDetails)
        file_dialog.setNameFilters([
            "All Files (*.cr2 *.ari *.dpx *.arw *.srf *.sr2 *.bay *.crw *.cr2 *.cr3 *.dng *.dcr *.kdc *.erf *.3fr *.mef *.mrw *.nef *.nrw *.orf *.ptx *.pef *.raf *.raw *.rwl *.dng *.raw *.rw2 *.r3d *.srw *.x3f *.jpeg *.jpg *.jpe *.png *.bmp *.psd *.pdd *.psdt *.tiff *.tif)",
            "RAWs (*.cr2 *.ari *.dpx *.arw *.srf *.sr2 *.bay *.crw *.cr2 *.cr3 *.dng *.dcr *.kdc *.erf *.3fr *.mef *.mrw *.nef *.nrw *.orf *.ptx *.pef *.raf *.raw *.rwl *.dng *.raw *.rw2 *.r3d *.srw *.x3f)",
            "JPEGs (*.jpg *.jpeg)",
            "Photoshop (*.psd *.pdd *.psdt)",
            "TIFF (*.tiff *.tif)",
            "BMP (*.bmp)"
        ])

        file_dialog.setFileMode(QFileDialog.ExistingFiles)  # Allow selecting multiple files

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            print("Selected files:", selected_files)