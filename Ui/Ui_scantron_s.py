# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_scantron_s.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(378, 488)
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
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QtWidgets.QPushButton(self.widget)
        self.pushButton_save.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_save.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "选择"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "学生姓名"))
        self.pushButton_save.setText(_translate("Dialog", "确定"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
