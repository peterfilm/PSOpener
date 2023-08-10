from PyQt5 import QtCore, QtGui, QtWidgets
from modules._text_selectable_label import TextSelectableLabel


class UiComment(object):
    def setupUi(self, CommentOfUser):
        CommentOfUser.setObjectName("CommentOfUser")
        CommentOfUser.resize(768, 100)
        CommentOfUser.setMinimumSize(QtCore.QSize(768, 100))
        CommentOfUser.setMaximumSize(QtCore.QSize(768, 100))
        self.layoutWidget = QtWidgets.QWidget(CommentOfUser)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 714, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_comment = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_comment.setMinimumSize(QtCore.QSize(550, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_comment.setFont(font)
        self.lineEdit_comment.setText("")
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.horizontalLayout.addWidget(self.lineEdit_comment)
        self.pushButton_ok = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ok.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.label = QtWidgets.QLabel(CommentOfUser)
        self.label.setGeometry(QtCore.QRect(290, 70, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_name = TextSelectableLabel(CommentOfUser)
        self.label_name.setGeometry(QtCore.QRect(30, 10, 711, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("color: #787878")
        self.label_name.setText("")
        self.label_name.setObjectName("label_name")

        self.retranslateUi(CommentOfUser)
        QtCore.QMetaObject.connectSlotsByName(CommentOfUser)

    def retranslateUi(self, CommentOfUser):
        _translate = QtCore.QCoreApplication.translate
        CommentOfUser.setWindowTitle(_translate(
            "CommentOfUser", "Добавить комментарий к фотографии"))
        self.pushButton_ok.setText(_translate("CommentOfUser", "Отправить"))
        self.pushButton_cancel.setText(_translate("CommentOfUser", "Отменить"))
        self.label.setText(_translate(
            "CommentOfUser", "Напишите комментарий к фотографии"))
