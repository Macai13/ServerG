# Form implementation generated from reading ui file 'design\OwnerDialog_UI.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(481, 130)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("design\\../assets/config_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.okBtn = QtWidgets.QPushButton(parent=Dialog)
        self.okBtn.setGeometry(QtCore.QRect(260, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName("okBtn")
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(370, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 411, 21))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QPlainTextEdit(parent=Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 451, 31))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configurações"))
        self.okBtn.setText(_translate("Dialog", "Ok"))
        self.cancelBtn.setText(_translate("Dialog", "Cancelar"))
        self.label.setText(_translate("Dialog", "Quem vai ser o dono agora?"))
