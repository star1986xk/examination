# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_scantron.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 789)
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
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_q = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_q.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButton_q.setMaximumSize(QtCore.QSize(60, 25))
        self.pushButton_q.setObjectName("pushButton_q")
        self.horizontalLayout_3.addWidget(self.pushButton_q)
        self.pushButton_s = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_s.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButton_s.setMaximumSize(QtCore.QSize(60, 25))
        self.pushButton_s.setObjectName("pushButton_s")
        self.horizontalLayout_3.addWidget(self.pushButton_s)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(Dialog)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setMinimumSize(QtCore.QSize(100, 25))
        self.label_4.setMaximumSize(QtCore.QSize(100, 25))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setMinimumSize(QtCore.QSize(100, 25))
        self.label_2.setMaximumSize(QtCore.QSize(100, 25))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setMinimumSize(QtCore.QSize(80, 25))
        self.label_5.setMaximumSize(QtCore.QSize(80, 25))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setMinimumSize(QtCore.QSize(80, 25))
        self.label_3.setMaximumSize(QtCore.QSize(80, 25))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.widget_5)
        self.label_6.setMinimumSize(QtCore.QSize(80, 25))
        self.label_6.setMaximumSize(QtCore.QSize(80, 25))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setMinimumSize(QtCore.QSize(80, 25))
        self.label_7.setMaximumSize(QtCore.QSize(80, 25))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.verticalLayout_2.addWidget(self.widget_5)
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
        self.pushButton_ocr = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_ocr.setMinimumSize(QtCore.QSize(60, 20))
        self.pushButton_ocr.setMaximumSize(QtCore.QSize(60, 25))
        self.pushButton_ocr.setObjectName("pushButton_ocr")
        self.horizontalLayout_2.addWidget(self.pushButton_ocr)
        self.pushButton_score = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_score.setMinimumSize(QtCore.QSize(60, 20))
        self.pushButton_score.setMaximumSize(QtCore.QSize(60, 25))
        self.pushButton_score.setObjectName("pushButton_score")
        self.horizontalLayout_2.addWidget(self.pushButton_score)
        self.verticalLayout.addWidget(self.widget_3)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
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
        self.pushButton_upload.setText(_translate("Dialog", "上传答题卡"))
        self.pushButton_q.setText(_translate("Dialog", "选择试卷"))
        self.pushButton_s.setText(_translate("Dialog", "选择学生"))
        self.label_4.setText(_translate("Dialog", "试卷："))
        self.label_5.setText(_translate("Dialog", "学生："))
        self.label_6.setText(_translate("Dialog", "总分："))
        self.groupBox.setTitle(_translate("Dialog", "批卷"))
        self.pushButton_ocr.setText(_translate("Dialog", "自动识别"))
        self.pushButton_score.setText(_translate("Dialog", "自动算分"))
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
        self.pushButton_save.setText(_translate("Dialog", "保存"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
