# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ocr.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(337, 419)
        Dialog.setStyleSheet("QStackedWidget{background-color: rgb(255, 255, 255);}\n"
"QPushButton{background-color: rgb(0, 170, 255);border-style:none;border-radius: 10px;}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed {  \n"
"    /* 改变背景色 */  \n"
"    background-color:rgb(180, 180, 180);  \n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */  \n"
"    padding-left:1px;  \n"
"    padding-top:1px;  \n"
"}\n"
"\n"
"QLineEdit{border: 1px solid rgb(0, 170, 255);}\n"
"QLineEdit{border-radius:5px;}\n"
"QLineEdit:focus{border: 2px solid rgb(100, 170, 255);}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_add = QtWidgets.QPushButton(self.widget)
        self.pushButton_add.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_add.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.pushButton_close = QtWidgets.QPushButton(self.widget)
        self.pushButton_close.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_close.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "调整识别后的字符点击载入"))
        self.pushButton_add.setText(_translate("Dialog", "载入"))
        self.pushButton_close.setText(_translate("Dialog", "关闭"))
