# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        Form.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(180, 0))
        self.widget.setMaximumSize(QtCore.QSize(180, 16777215))
        self.widget.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_3.setObjectName("widget_3")
        self.label_name = QtWidgets.QLabel(self.widget_3)
        self.label_name.setGeometry(QtCore.QRect(80, 70, 50, 16))
        self.label_name.setMinimumSize(QtCore.QSize(0, 0))
        self.label_name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_name.setObjectName("label_name")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_rank = QtWidgets.QLabel(self.widget_3)
        self.label_rank.setGeometry(QtCore.QRect(20, 70, 50, 16))
        self.label_rank.setMinimumSize(QtCore.QSize(50, 0))
        self.label_rank.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_rank.setObjectName("label_rank")
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_2.setStyleSheet("QPushButton{background-color: rgb(0, 170, 255);border-style:none;border-radius: 10px;}\n"
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
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(-1, 100, -1, -1)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_admin = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_admin.setEnabled(False)
        self.pushButton_admin.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_admin.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_admin.setAutoFillBackground(False)
        self.pushButton_admin.setStyleSheet("")
        self.pushButton_admin.setCheckable(False)
        self.pushButton_admin.setObjectName("pushButton_admin")
        self.verticalLayout.addWidget(self.pushButton_admin)
        self.pushButton_teacher = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_teacher.setEnabled(False)
        self.pushButton_teacher.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_teacher.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_teacher.setObjectName("pushButton_teacher")
        self.verticalLayout.addWidget(self.pushButton_teacher)
        self.pushButton_student = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_student.setEnabled(False)
        self.pushButton_student.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_student.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_student.setObjectName("pushButton_student")
        self.verticalLayout.addWidget(self.pushButton_student)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setStyleSheet("QStackedWidget{background-color: rgb(255, 255, 255);}\n"
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
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("\n"
"border-image: url(:/newPrefix/img/mainBG.jpg);")
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QtWidgets.QWidget(self.page_2)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_add = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_add.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_add.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_2.addWidget(self.pushButton_add)
        self.pushButton_set = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_set.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_set.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_set.setObjectName("pushButton_set")
        self.horizontalLayout_2.addWidget(self.pushButton_set)
        self.pushButton_del = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_del.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_del.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_del.setObjectName("pushButton_del")
        self.horizontalLayout_2.addWidget(self.pushButton_del)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.page_3)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_5 = QtWidgets.QWidget(self.groupBox)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_add_q = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_add_q.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_add_q.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_add_q.setObjectName("pushButton_add_q")
        self.horizontalLayout_3.addWidget(self.pushButton_add_q)
        self.pushButton_set_q = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_set_q.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_set_q.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_set_q.setObjectName("pushButton_set_q")
        self.horizontalLayout_3.addWidget(self.pushButton_set_q)
        self.pushButton_del_q = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_del_q.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_del_q.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_del_q.setObjectName("pushButton_del_q")
        self.horizontalLayout_3.addWidget(self.pushButton_del_q)
        self.pushButton_see_q = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_see_q.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_see_q.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_see_q.setObjectName("pushButton_see_q")
        self.horizontalLayout_3.addWidget(self.pushButton_see_q)
        self.pushButton_search_q = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_search_q.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_search_q.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_search_q.setObjectName("pushButton_search_q")
        self.horizontalLayout_3.addWidget(self.pushButton_search_q)
        self.lineEdit_q = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_q.setObjectName("lineEdit_q")
        self.horizontalLayout_3.addWidget(self.lineEdit_q)
        self.pushButton_refresh_q = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_refresh_q.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButton_refresh_q.setMaximumSize(QtCore.QSize(60, 25))
        self.pushButton_refresh_q.setObjectName("pushButton_refresh_q")
        self.horizontalLayout_3.addWidget(self.pushButton_refresh_q)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_5.addWidget(self.widget_5)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.tableWidget_2)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_6 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_add_c = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_add_c.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_add_c.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_add_c.setObjectName("pushButton_add_c")
        self.horizontalLayout_4.addWidget(self.pushButton_add_c)
        self.pushButton_set_c = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_set_c.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_set_c.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_set_c.setObjectName("pushButton_set_c")
        self.horizontalLayout_4.addWidget(self.pushButton_set_c)
        self.pushButton_del_c = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_del_c.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_del_c.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_del_c.setObjectName("pushButton_del_c")
        self.horizontalLayout_4.addWidget(self.pushButton_del_c)
        self.pushButton_see_c = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_see_c.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_see_c.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_see_c.setObjectName("pushButton_see_c")
        self.horizontalLayout_4.addWidget(self.pushButton_see_c)
        self.pushButton_search_c = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_search_c.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_search_c.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_search_c.setObjectName("pushButton_search_c")
        self.horizontalLayout_4.addWidget(self.pushButton_search_c)
        self.lineEdit_c = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_c.setObjectName("lineEdit_c")
        self.horizontalLayout_4.addWidget(self.lineEdit_c)
        self.pushButton_refresh_c = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_refresh_c.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButton_refresh_c.setMaximumSize(QtCore.QSize(60, 25))
        self.pushButton_refresh_c.setObjectName("pushButton_refresh_c")
        self.horizontalLayout_4.addWidget(self.pushButton_refresh_c)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_6.addWidget(self.widget_6)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(12)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(11, item)
        self.tableWidget_3.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_6.addWidget(self.tableWidget_3)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_7 = QtWidgets.QWidget(self.page_4)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_see_1 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_see_1.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_see_1.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_see_1.setObjectName("pushButton_see_1")
        self.horizontalLayout_5.addWidget(self.pushButton_see_1)
        self.pushButton_see_2 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_see_2.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_see_2.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_see_2.setObjectName("pushButton_see_2")
        self.horizontalLayout_5.addWidget(self.pushButton_see_2)
        self.pushButton_see_3 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_see_3.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_see_3.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_see_3.setObjectName("pushButton_see_3")
        self.horizontalLayout_5.addWidget(self.pushButton_see_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_8.addWidget(self.widget_7)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget_4.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(7)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        self.tableWidget_4.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_4.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_8.addWidget(self.tableWidget_4)
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "试卷管理系统"))
        self.label_name.setText(_translate("Form", "管理员"))
        self.label_3.setText(_translate("Form", "欢迎使用试卷管理系统"))
        self.label_rank.setText(_translate("Form", "管理员"))
        self.pushButton_admin.setText(_translate("Form", "管理员模块"))
        self.pushButton_teacher.setText(_translate("Form", "教师模块"))
        self.pushButton_student.setText(_translate("Form", "学生模块"))
        self.pushButton_add.setText(_translate("Form", "添加用户"))
        self.pushButton_set.setText(_translate("Form", "修改用户"))
        self.pushButton_del.setText(_translate("Form", "删除用户"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "选择"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "账号"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "密码"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "身份"))
        self.groupBox.setTitle(_translate("Form", "试卷管理"))
        self.pushButton_add_q.setText(_translate("Form", "添加试卷"))
        self.pushButton_set_q.setText(_translate("Form", "修改试卷"))
        self.pushButton_del_q.setText(_translate("Form", "删除试卷"))
        self.pushButton_see_q.setText(_translate("Form", "查看试卷"))
        self.pushButton_search_q.setText(_translate("Form", "搜索试卷"))
        self.lineEdit_q.setPlaceholderText(_translate("Form", "试卷名称"))
        self.pushButton_refresh_q.setText(_translate("Form", "刷新"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "选择"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "试卷名称"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "答案"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "paper"))
        self.groupBox_2.setTitle(_translate("Form", "答题卡管理"))
        self.pushButton_add_c.setText(_translate("Form", "添加答题卡"))
        self.pushButton_set_c.setText(_translate("Form", "修改答题卡"))
        self.pushButton_del_c.setText(_translate("Form", "删除答题卡"))
        self.pushButton_see_c.setText(_translate("Form", "查看答题卡"))
        self.pushButton_search_c.setText(_translate("Form", "搜索答题卡"))
        self.lineEdit_c.setPlaceholderText(_translate("Form", "学生姓名"))
        self.pushButton_refresh_c.setText(_translate("Form", "刷新"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "选择"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Form", "学生姓名"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Form", "试卷名称"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("Form", "回答"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("Form", "批改"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("Form", "得分"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("Form", "总分"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("Form", "sid"))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("Form", "qid"))
        item = self.tableWidget_3.horizontalHeaderItem(10)
        item.setText(_translate("Form", "paper"))
        item = self.tableWidget_3.horizontalHeaderItem(11)
        item.setText(_translate("Form", "answer"))
        self.pushButton_see_1.setText(_translate("Form", "查看试卷"))
        self.pushButton_see_2.setText(_translate("Form", "查看答题卡"))
        self.pushButton_see_3.setText(_translate("Form", "查看批改"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Form", "选择"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("Form", "试卷名称"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("Form", "回答"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("Form", "批改"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("Form", "得分"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("Form", "总分"))
import image_rc
