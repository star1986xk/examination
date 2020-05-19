# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_scantronInfo.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(677, 429)
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
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(80, 25))
        self.label_6.setMaximumSize(QtCore.QSize(80, 25))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_1 = QtWidgets.QLabel(self.widget)
        self.label_1.setMinimumSize(QtCore.QSize(80, 25))
        self.label_1.setMaximumSize(QtCore.QSize(80, 25))
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.horizontalLayout.addWidget(self.label_1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_close = QtWidgets.QPushButton(self.widget)
        self.pushButton_close.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButton_close.setMaximumSize(QtCore.QSize(60, 25))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout.addWidget(self.widget)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "总分："))
        self.pushButton_close.setText(_translate("Dialog", "关闭"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "题号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "答案"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "分数"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "回答"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "批改"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "得分"))
