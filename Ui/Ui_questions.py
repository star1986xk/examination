# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_questions.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(490, 698)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_upload = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_upload.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_upload.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.gridLayout.addWidget(self.pushButton_upload, 0, 0, 1, 1)
        self.lineEdit_upload = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_upload.setReadOnly(True)
        self.lineEdit_upload.setObjectName("lineEdit_upload")
        self.gridLayout.addWidget(self.lineEdit_upload, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMinimumSize(QtCore.QSize(50, 25))
        self.label.setMaximumSize(QtCore.QSize(50, 25))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_title = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.gridLayout.addWidget(self.lineEdit_title, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.groupBox)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(15, 9, 15, 9)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_add = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_add.setMinimumSize(QtCore.QSize(60, 20))
        self.pushButton_add.setMaximumSize(QtCore.QSize(60, 25))
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_2.addWidget(self.pushButton_add)
        self.pushButton_del = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_del.setMinimumSize(QtCore.QSize(60, 20))
        self.pushButton_del.setMaximumSize(QtCore.QSize(60, 25))
        self.pushButton_del.setObjectName("pushButton_del")
        self.horizontalLayout_2.addWidget(self.pushButton_del)
        self.verticalLayout.addWidget(self.widget_3)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
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
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addWidget(self.groupBox)
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
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_upload.setText(_translate("Dialog", "上传试卷"))
        self.label.setText(_translate("Dialog", "试卷名称"))
        self.groupBox.setTitle(_translate("Dialog", "答案编辑"))
        self.pushButton_add.setText(_translate("Dialog", "加"))
        self.pushButton_del.setText(_translate("Dialog", "减"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "题号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "答案"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "分值"))
        self.pushButton_save.setText(_translate("Dialog", "保存"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
