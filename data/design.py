from PyQt5 import QtCore, QtGui, QtWidgets
from modules._clicable_label import ClickableLabel
from modules.api import conf


class UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(984, 730)
        Form.setMinimumSize(QtCore.QSize(984, 730))
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_choisePhotos = QtWidgets.QLineEdit(Form)
        self.lineEdit_choisePhotos.setEnabled(True)
        self.lineEdit_choisePhotos.setMinimumSize(QtCore.QSize(0, 33))
        self.lineEdit_choisePhotos.setObjectName("lineEdit_choisePhotos")
        self.horizontalLayout_2.addWidget(self.lineEdit_choisePhotos)
        self.pushButton_choisePhotos = QtWidgets.QPushButton(Form)
        self.pushButton_choisePhotos.setMinimumSize(QtCore.QSize(150, 33))
        self.pushButton_choisePhotos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_choisePhotos.setObjectName("pushButton_choisePhotos")
        self.horizontalLayout_2.addWidget(self.pushButton_choisePhotos)
        self.pushButton_choiseYourPhotos = QtWidgets.QPushButton(Form)
        self.pushButton_choiseYourPhotos.setMinimumSize(QtCore.QSize(150, 33))
        self.pushButton_choiseYourPhotos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_choiseYourPhotos.setObjectName("pushButton_choiseYourPhotos")
        self.horizontalLayout_2.addWidget(self.pushButton_choiseYourPhotos)
        self.pushButton_choiseYourPhotos_2 = QtWidgets.QPushButton(Form)
        self.pushButton_choiseYourPhotos_2.setMinimumSize(QtCore.QSize(150, 33))
        self.pushButton_choiseYourPhotos_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_choiseYourPhotos_2.setObjectName("pushButton_choiseYourPhotos_2")
        self.horizontalLayout_2.addWidget(self.pushButton_choiseYourPhotos_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_countPhotos = QtWidgets.QLabel(Form)
        self.label_countPhotos.setMinimumSize(QtCore.QSize(300, 0))
        self.label_countPhotos.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_countPhotos.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_countPhotos.setStyleSheet("color: #565656")
        self.label_countPhotos.setText("")
        self.label_countPhotos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_countPhotos.setObjectName("label_countPhotos")
        self.horizontalLayout_9.addWidget(self.label_countPhotos)
        self.label_pathSelectedPhoto = ClickableLabel(Form)
        self.label_pathSelectedPhoto.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_pathSelectedPhoto.setStyleSheet("color: #565656")
        self.label_pathSelectedPhoto.setText("")
        self.label_pathSelectedPhoto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_pathSelectedPhoto.setObjectName("label_pathSelectedPhoto")
        self.horizontalLayout_9.addWidget(self.label_pathSelectedPhoto)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_psPath = QtWidgets.QLineEdit(Form)
        self.lineEdit_psPath.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_psPath.setFont(font)
        self.lineEdit_psPath.setObjectName("lineEdit_psPath")
        self.horizontalLayout_7.addWidget(self.lineEdit_psPath)
        self.toolButton_psPath = QtWidgets.QToolButton(Form)
        self.toolButton_psPath.setMinimumSize(QtCore.QSize(33, 34))
        self.toolButton_psPath.setObjectName("toolButton_psPath")
        self.horizontalLayout_7.addWidget(self.toolButton_psPath)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox_howMuch = QtWidgets.QComboBox(Form)
        self.comboBox_howMuch.setMinimumSize(QtCore.QSize(0, 33))
        self.comboBox_howMuch.setObjectName("comboBox_howMuch")
        self.comboBox_howMuch.addItem("")
        self.comboBox_howMuch.addItem("")
        self.comboBox_howMuch.addItem("")
        self.comboBox_howMuch.addItem("")
        self.comboBox_howMuch.addItem("")
        self.comboBox_howMuch.addItem("")
        self.comboBox_howMuch.addItem("")
        self.comboBox_howMuch.addItem("")
        self.comboBox_howMuch.addItem("")
        self.comboBox_howMuch.addItem("")
        self.comboBox_howMuch.addItem("")
        self.comboBox_howMuch.addItem("")
        self.verticalLayout.addWidget(self.comboBox_howMuch)
        self.checkBox_allFolders = QtWidgets.QCheckBox(Form)
        self.checkBox_allFolders.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_allFolders.setFont(font)
        self.checkBox_allFolders.setInputMethodHints(QtCore.Qt.ImhNoEditMenu)
        self.checkBox_allFolders.setObjectName("checkBox_allFolders")
        self.verticalLayout.addWidget(self.checkBox_allFolders)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBox_shortcut = QtWidgets.QComboBox(Form)
        self.comboBox_shortcut.setMinimumSize(QtCore.QSize(0, 33))
        self.comboBox_shortcut.setObjectName("comboBox_shortcut")
        self.comboBox_shortcut.addItem("")
        self.comboBox_shortcut.addItem("")
        self.comboBox_shortcut.addItem("")
        self.comboBox_shortcut.addItem("")
        self.comboBox_shortcut.addItem("")
        self.comboBox_shortcut.addItem("")
        self.comboBox_shortcut.addItem("")
        self.comboBox_shortcut.addItem("")
        self.comboBox_shortcut.addItem("")
        self.comboBox_shortcut.addItem("")
        self.comboBox_shortcut.addItem("")
        self.comboBox_shortcut.addItem("")
        self.verticalLayout.addWidget(self.comboBox_shortcut)
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.comboBox_shortcut_comment = QtWidgets.QComboBox(Form)
        self.comboBox_shortcut_comment.setMinimumSize(QtCore.QSize(0, 33))
        self.comboBox_shortcut_comment.setObjectName("comboBox_shortcut_comment")
        self.comboBox_shortcut_comment.addItem("")
        self.comboBox_shortcut_comment.addItem("")
        self.comboBox_shortcut_comment.addItem("")
        self.comboBox_shortcut_comment.addItem("")
        self.comboBox_shortcut_comment.addItem("")
        self.comboBox_shortcut_comment.addItem("")
        self.comboBox_shortcut_comment.addItem("")
        self.comboBox_shortcut_comment.addItem("")
        self.comboBox_shortcut_comment.addItem("")
        self.comboBox_shortcut_comment.addItem("")
        self.comboBox_shortcut_comment.addItem("")
        self.comboBox_shortcut_comment.addItem("")
        self.verticalLayout.addWidget(self.comboBox_shortcut_comment)
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_commentSameFolder = QtWidgets.QRadioButton(Form)
        self.radioButton_commentSameFolder.setChecked(True)
        self.radioButton_commentSameFolder.setObjectName("radioButton_commentSameFolder")
        self.horizontalLayout.addWidget(self.radioButton_commentSameFolder)
        self.radioButton_commentChoise = QtWidgets.QRadioButton(Form)
        self.radioButton_commentChoise.setObjectName("radioButton_commentChoise")
        self.horizontalLayout.addWidget(self.radioButton_commentChoise)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lineEdit_comment = QtWidgets.QLineEdit(Form)
        self.lineEdit_comment.setEnabled(False)
        self.lineEdit_comment.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_comment.setFont(font)
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.verticalLayout.addWidget(self.lineEdit_comment)
        self.pushButton_comment = QtWidgets.QPushButton(Form)
        self.pushButton_comment.setEnabled(False)
        self.pushButton_comment.setMinimumSize(QtCore.QSize(0, 33))
        self.pushButton_comment.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_comment.setObjectName("pushButton_comment")
        self.verticalLayout.addWidget(self.pushButton_comment)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_formats = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_formats.setFont(font)
        self.label_formats.setObjectName("label_formats")
        self.verticalLayout_5.addWidget(self.label_formats)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_raw = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_raw.setFont(font)
        self.checkBox_raw.setObjectName("checkBox_raw")
        self.horizontalLayout_6.addWidget(self.checkBox_raw)
        self.checkBox_jpg = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_jpg.setFont(font)
        self.checkBox_jpg.setObjectName("checkBox_jpg")
        self.horizontalLayout_6.addWidget(self.checkBox_jpg)
        self.checkBox_psd = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_psd.setFont(font)
        self.checkBox_psd.setObjectName("checkBox_psd")
        self.horizontalLayout_6.addWidget(self.checkBox_psd)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_png = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_png.setFont(font)
        self.checkBox_png.setObjectName("checkBox_png")
        self.horizontalLayout_8.addWidget(self.checkBox_png)
        self.checkBox_tiff = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_tiff.setFont(font)
        self.checkBox_tiff.setObjectName("checkBox_tiff")
        self.horizontalLayout_8.addWidget(self.checkBox_tiff)
        self.checkBox_bmp = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_bmp.setFont(font)
        self.checkBox_bmp.setObjectName("checkBox_bmp")
        self.horizontalLayout_8.addWidget(self.checkBox_bmp)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setEnabled(True)
        self.listWidget.setMinimumSize(QtCore.QSize(311, 0))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.pushButton_allOpen = QtWidgets.QPushButton(Form)
        self.pushButton_allOpen.setMinimumSize(QtCore.QSize(0, 41))
        self.pushButton_allOpen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_allOpen.setObjectName("pushButton_allOpen")
        self.verticalLayout_2.addWidget(self.pushButton_allOpen)
        self.pushButton_saveList = QtWidgets.QPushButton(Form)
        self.pushButton_saveList.setMinimumSize(QtCore.QSize(150, 41))
        self.pushButton_saveList.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_saveList.setObjectName("pushButton_saveList")
        self.verticalLayout_2.addWidget(self.pushButton_saveList)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_photos = QtWidgets.QLabel(Form)
        self.label_photos.setMinimumSize(QtCore.QSize(0, 350))
        self.label_photos.setText("")
        self.label_photos.setObjectName("label_photos")
        self.verticalLayout_3.addWidget(self.label_photos, 0, QtCore.Qt.AlignVCenter)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.pushButton_oneOpenPs = QtWidgets.QPushButton(Form)
        self.pushButton_oneOpenPs.setMinimumSize(QtCore.QSize(0, 41))
        self.pushButton_oneOpenPs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_oneOpenPs.setObjectName("pushButton_oneOpenPs")
        self.verticalLayout_3.addWidget(self.pushButton_oneOpenPs)
        self.pushButton_oneOpenFolder = QtWidgets.QPushButton(Form)
        self.pushButton_oneOpenFolder.setMinimumSize(QtCore.QSize(0, 41))
        self.pushButton_oneOpenFolder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_oneOpenFolder.setObjectName("pushButton_oneOpenFolder")
        self.verticalLayout_3.addWidget(self.pushButton_oneOpenFolder)
        self.pushButton_oneOpen = QtWidgets.QPushButton(Form)
        self.pushButton_oneOpen.setMinimumSize(QtCore.QSize(0, 41))
        self.pushButton_oneOpen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_oneOpen.setObjectName("pushButton_oneOpen")
        self.verticalLayout_3.addWidget(self.pushButton_oneOpen)
        self.pushButton_oneDelete = QtWidgets.QPushButton(Form)
        self.pushButton_oneDelete.setMinimumSize(QtCore.QSize(0, 41))
        self.pushButton_oneDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_oneDelete.setObjectName("pushButton_oneDelete")
        self.verticalLayout_3.addWidget(self.pushButton_oneDelete)
        self.pushButton_oneComment = QtWidgets.QPushButton(Form)
        self.pushButton_oneComment.setMinimumSize(QtCore.QSize(0, 41))
        self.pushButton_oneComment.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_oneComment.setObjectName("pushButton_oneComment")
        self.verticalLayout_3.addWidget(self.pushButton_oneComment)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.pushButton_about = QtWidgets.QPushButton(Form)
        self.pushButton_about.setMinimumSize(QtCore.QSize(23, 23))
        self.pushButton_about.setMaximumSize(QtCore.QSize(23, 23))
        self.pushButton_about.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_about.setObjectName("pushButton_about")
        self.horizontalLayout_5.addWidget(self.pushButton_about)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PS Opener v.1.01"))
        self.lineEdit_choisePhotos.setPlaceholderText(_translate("Form", "Выберите папку с фотографиями"))
        self.pushButton_choisePhotos.setToolTip(_translate("Form", "<html><head/><body><p>Горячие клавиши:<br/>Ctrl + O</p></body></html>"))
        self.pushButton_choisePhotos.setText(_translate("Form", "Выбрать папку"))
        self.pushButton_choisePhotos.setShortcut(_translate("Form", "Ctrl+O"))
        self.pushButton_choiseYourPhotos.setToolTip(_translate("Form", "<html><head/><body><p>Горячие клавиши:<br/>Ctrl + SHIFT + O</p></body></html>"))
        self.pushButton_choiseYourPhotos.setText(_translate("Form", "Выбрать фотографии"))
        self.pushButton_choiseYourPhotos.setShortcut(_translate("Form", "Ctrl+Shift+O"))
        self.pushButton_choiseYourPhotos_2.setToolTip(_translate("Form", "<html><head/><body><p>Горячие клавиши:<br/>Ctrl + L</p></body></html>"))
        self.pushButton_choiseYourPhotos_2.setText(_translate("Form", "Загрузить список"))
        self.pushButton_choiseYourPhotos_2.setShortcut(_translate("Form", "Ctrl+L"))
        self.label_5.setText(_translate("Form", "Полный путь до Photoshop.exe:"))
        self.lineEdit_psPath.setPlaceholderText(_translate("Form", "Укажите путь"))
        self.toolButton_psPath.setText(_translate("Form", "..."))
        self.label_3.setText(_translate("Form", "Сколько фотографий открывать?"))
        self.comboBox_howMuch.setItemText(0, _translate("Form", "1"))
        self.comboBox_howMuch.setItemText(1, _translate("Form", "2"))
        self.comboBox_howMuch.setItemText(2, _translate("Form", "3"))
        self.comboBox_howMuch.setItemText(3, _translate("Form", "4"))
        self.comboBox_howMuch.setItemText(4, _translate("Form", "5"))
        self.comboBox_howMuch.setItemText(5, _translate("Form", "6"))
        self.comboBox_howMuch.setItemText(6, _translate("Form", "7"))
        self.comboBox_howMuch.setItemText(7, _translate("Form", "8"))
        self.comboBox_howMuch.setItemText(8, _translate("Form", "9"))
        self.comboBox_howMuch.setItemText(9, _translate("Form", "10"))
        self.comboBox_howMuch.setItemText(10, _translate("Form", "15"))
        self.comboBox_howMuch.setItemText(11, _translate("Form", "20"))
        self.checkBox_allFolders.setText(_translate("Form", "Включая все папки внутри директории"))
        self.label_4.setText(_translate("Form", "Выберите горячую клавишу"))
        self.comboBox_shortcut.setCurrentText(_translate("Form", "F1"))
        self.comboBox_shortcut.setItemText(0, _translate("Form", "F1"))
        self.comboBox_shortcut.setItemText(1, _translate("Form", "F2"))
        self.comboBox_shortcut.setItemText(2, _translate("Form", "F3"))
        self.comboBox_shortcut.setItemText(3, _translate("Form", "F4"))
        self.comboBox_shortcut.setItemText(4, _translate("Form", "F5"))
        self.comboBox_shortcut.setItemText(5, _translate("Form", "F6"))
        self.comboBox_shortcut.setItemText(6, _translate("Form", "F7"))
        self.comboBox_shortcut.setItemText(7, _translate("Form", "F8"))
        self.comboBox_shortcut.setItemText(8, _translate("Form", "F9"))
        self.comboBox_shortcut.setItemText(9, _translate("Form", "F10"))
        self.comboBox_shortcut.setItemText(10, _translate("Form", "F11"))
        self.comboBox_shortcut.setItemText(11, _translate("Form", "F12"))
        self.label_7.setText(_translate("Form", "Выберите горячую клавишу для комментариев"))
        self.comboBox_shortcut_comment.setCurrentText(_translate("Form", "F1"))
        self.comboBox_shortcut_comment.setItemText(0, _translate("Form", "F1"))
        self.comboBox_shortcut_comment.setItemText(1, _translate("Form", "F2"))
        self.comboBox_shortcut_comment.setItemText(2, _translate("Form", "F3"))
        self.comboBox_shortcut_comment.setItemText(3, _translate("Form", "F4"))
        self.comboBox_shortcut_comment.setItemText(4, _translate("Form", "F5"))
        self.comboBox_shortcut_comment.setItemText(5, _translate("Form", "F6"))
        self.comboBox_shortcut_comment.setItemText(6, _translate("Form", "F7"))
        self.comboBox_shortcut_comment.setItemText(7, _translate("Form", "F8"))
        self.comboBox_shortcut_comment.setItemText(8, _translate("Form", "F9"))
        self.comboBox_shortcut_comment.setItemText(9, _translate("Form", "F10"))
        self.comboBox_shortcut_comment.setItemText(10, _translate("Form", "F11"))
        self.comboBox_shortcut_comment.setItemText(11, _translate("Form", "F12"))
        self.label_6.setText(_translate("Form", "Где размещать комментарии?"))
        self.radioButton_commentSameFolder.setText(_translate("Form", "В папке с фото"))
        self.radioButton_commentChoise.setText(_translate("Form", "Выбрать"))
        self.lineEdit_comment.setPlaceholderText(_translate("Form", "Укажите путь"))
        self.pushButton_comment.setText(_translate("Form", "Выбрать"))
        self.label_formats.setText(_translate("Form", "Форматы:"))
        self.checkBox_raw.setText(_translate("Form", "RAWs"))
        self.checkBox_jpg.setText(_translate("Form", "*.jpg"))
        self.checkBox_psd.setText(_translate("Form", "*.psd"))
        self.checkBox_png.setText(_translate("Form", "*.png"))
        self.checkBox_tiff.setText(_translate("Form", "*.tiff"))
        self.checkBox_bmp.setText(_translate("Form", "*.bmp"))
        self.pushButton_allOpen.setToolTip(_translate("Form", "<html><head/><body><p>Горячая клавиша: F12</p></body></html>"))
        self.pushButton_allOpen.setText(_translate("Form", "Открыть в Photoshop"))
        self.pushButton_allOpen.setShortcut(_translate("Form", "Ctrl+X"))
        self.pushButton_saveList.setToolTip(_translate("Form", "<html><head/><body><p>Горячие клавиши:<br/>Ctrl + S</p></body></html>"))
        self.pushButton_saveList.setText(_translate("Form", "Сохранить список"))
        self.pushButton_saveList.setShortcut(_translate("Form", "Ctrl+S"))
        self.label.setText(_translate("Form", "Выбранную фотографию:"))
        self.pushButton_oneOpenPs.setToolTip(_translate("Form", "<html><head/><body><p>Горячие клавиши:<br/>Ctrl + P</p></body></html>"))
        self.pushButton_oneOpenPs.setText(_translate("Form", "Открыть в Photoshop"))
        self.pushButton_oneOpenPs.setShortcut(_translate("Form", "Ctrl+P"))
        self.pushButton_oneOpenFolder.setToolTip(_translate("Form", "<html><head/><body><p>Горячая клавиша: Ctrl + F</p></body></html>"))
        self.pushButton_oneOpenFolder.setText(_translate("Form", "Открыть Папку"))
        self.pushButton_oneOpenFolder.setShortcut(_translate("Form", "Ctrl+F"))
        self.pushButton_oneOpen.setToolTip(_translate("Form", "<html><head/><body><p>Горячая клавиша: Ctrl + I</p></body></html>"))
        self.pushButton_oneOpen.setText(_translate("Form", "Открыть"))
        self.pushButton_oneOpen.setShortcut(_translate("Form", "Ctrl+I"))
        self.pushButton_oneDelete.setToolTip(_translate("Form", "<html><head/><body><p>Горячая клавиша: -</p></body></html>"))
        self.pushButton_oneDelete.setText(_translate("Form", "Убрать"))
        self.pushButton_oneDelete.setShortcut(_translate("Form", "-"))
        self.pushButton_oneComment.setToolTip(_translate("Form", "<html><head/><body><p>Горячая клавиша: /</p></body></html>"))
        self.pushButton_oneComment.setText(_translate("Form", "Комментарий"))
        self.pushButton_oneComment.setShortcut(_translate("Form", "/"))
        self.pushButton_about.setText(_translate("Form", "?"))
