# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(403, 242)
        Dialog.setAcceptDrops(False)
        Dialog.setStyleSheet("QDialog{background-color: rgb(255, 255, 255);}\n"
"#widget{border-image: url(:/newPrefix/img/login.png);}\n"
"QPushButton{background-color: #b3dbff;border-style:none;border-radius: 10px;}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed {  \n"
"    /* 改变背景色 */  \n"
"    background-color:rgb(180, 180, 180);  \n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */  \n"
"    padding-left:1px;  \n"
"    padding-top:1px;  \n"
"}")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(0, 100))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setAcceptDrops(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(-1, 20, -1, 10)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMinimumSize(QtCore.QSize(60, 0))
        self.label_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_username.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_login = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_login.setMinimumSize(QtCore.QSize(80, 20))
        self.pushButton_login.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.pushButton_login)
        self.pushButton_close = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_close.setMinimumSize(QtCore.QSize(80, 20))
        self.pushButton_close.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout.addWidget(self.widget_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "试卷管理系统"))
        self.label_3.setText(_translate("Dialog", "密  码："))
        self.lineEdit_username.setText(_translate("Dialog", "xiaoming"))
        self.label_2.setText(_translate("Dialog", "用户名："))
        self.lineEdit_password.setText(_translate("Dialog", "123456"))
        self.pushButton_login.setText(_translate("Dialog", "登 录"))
        self.pushButton_close.setText(_translate("Dialog", "关 闭"))
import image_rc
