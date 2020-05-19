# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_user.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(223, 275)
        Dialog.setStyleSheet("QDialog{background-color: rgb(220, 220, 220);}\n"
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
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout_2.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout_2.addWidget(self.lineEdit_username, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout_2.addWidget(self.lineEdit_password, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox_rank_name = QtWidgets.QComboBox(self.widget)
        self.comboBox_rank_name.setObjectName("comboBox_rank_name")
        self.comboBox_rank_name.addItem("")
        self.comboBox_rank_name.addItem("")
        self.comboBox_rank_name.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_rank_name, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_ok = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_ok.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButton_ok.setMaximumSize(QtCore.QSize(60, 25))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(60, 25))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "姓  名："))
        self.label_2.setText(_translate("Dialog", "账  号："))
        self.label_3.setText(_translate("Dialog", "密  码："))
        self.label_4.setText(_translate("Dialog", "身  份："))
        self.comboBox_rank_name.setItemText(0, _translate("Dialog", "管理员"))
        self.comboBox_rank_name.setItemText(1, _translate("Dialog", "教师"))
        self.comboBox_rank_name.setItemText(2, _translate("Dialog", "学生"))
        self.pushButton_ok.setText(_translate("Dialog", "确定"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
