import sys
from Ui.Ui_main import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QHeaderView, QTableWidgetItem, QRadioButton
from PyQt5.QtCore import Qt
from loginWin import loginWin
from userWin import userWin
from questionsWin import questionsWin
from scantronInfoWin import scantronInfoWin
from db_class import db_class
from settings import *
from showWin import showWin
from scantronWin import scantronWin


class mainWin(Ui_Form, QWidget):
    def __init__(self, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(mainWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        headerView = self.tableWidget.horizontalHeader()
        headerView.setSectionResizeMode(QHeaderView.Stretch)

        headerView2 = self.tableWidget_2.horizontalHeader()
        headerView2.setSectionResizeMode(QHeaderView.Stretch)

        headerView3 = self.tableWidget_3.horizontalHeader()
        headerView3.setSectionResizeMode(QHeaderView.Stretch)

        headerView4 = self.tableWidget_4.horizontalHeader()
        headerView4.setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget_2.setColumnHidden(4, True)
        self.tableWidget_3.setColumnHidden(8, True)
        self.tableWidget_3.setColumnHidden(9, True)
        self.tableWidget_3.setColumnHidden(10, True)
        self.tableWidget_3.setColumnHidden(11, True)

        self.login = loginWin()
        self.login.Sig_login.connect(self.load)
        self.login.show()

        self.tableWidget.clicked.connect(self.t_check)
        self.pushButton_admin.clicked.connect(self.btn_admin)
        self.pushButton_add.clicked.connect(self.btn_add)
        self.pushButton_set.clicked.connect(self.btn_set)
        self.pushButton_del.clicked.connect(self.btn_del)

        self.tableWidget_2.clicked.connect(self.t_check2)
        self.pushButton_teacher.clicked.connect(self.btn_teacher)
        self.pushButton_add_q.clicked.connect(self.btn_teacher_add)
        self.pushButton_set_q.clicked.connect(self.btn_teacher_set)
        self.pushButton_del_q.clicked.connect(self.btn_teacher_del)
        self.pushButton_see_q.clicked.connect(self.btn_teacher_see)
        self.pushButton_search_q.clicked.connect(self.btn_teacher_search)
        self.pushButton_refresh_q.clicked.connect(self.btn_teacher)

        self.tableWidget_3.clicked.connect(self.t_check3)
        self.pushButton_add_c.clicked.connect(self.btn_teacher_add_c)
        self.pushButton_set_c.clicked.connect(self.btn_teacher_set_c)
        self.pushButton_del_c.clicked.connect(self.btn_teacher_del_c)
        self.pushButton_see_c.clicked.connect(self.btn_teacher_see_c)
        self.pushButton_search_c.clicked.connect(self.btn_teacher_search_c)
        self.pushButton_refresh_c.clicked.connect(self.btn_teacher)

        self.tableWidget_4.clicked.connect(self.t_check4)
        self.pushButton_student.clicked.connect(self.btn_student)
        self.pushButton_see_1.clicked.connect(self.btn_see_1)
        self.pushButton_see_2.clicked.connect(self.btn_see_2)
        self.pushButton_see_3.clicked.connect(self.btn_see_3)

    def t_check(self, n):
        if self.tableWidget.cellWidget(n.row(), 0).isChecked():
            self.tableWidget.cellWidget(n.row(), 0).setChecked(False)
        else:
            self.tableWidget.cellWidget(n.row(), 0).setChecked(True)

    def t_check2(self, n):
        if self.tableWidget_2.cellWidget(n.row(), 0).isChecked():
            self.tableWidget_2.cellWidget(n.row(), 0).setChecked(False)
        else:
            self.tableWidget_2.cellWidget(n.row(), 0).setChecked(True)

    def t_check3(self, n):
        if self.tableWidget_3.cellWidget(n.row(), 0).isChecked():
            self.tableWidget_3.cellWidget(n.row(), 0).setChecked(False)
        else:
            self.tableWidget_3.cellWidget(n.row(), 0).setChecked(True)

    def t_check4(self, n):
        if self.tableWidget_4.cellWidget(n.row(), 0).isChecked():
            self.tableWidget_4.cellWidget(n.row(), 0).setChecked(False)
        else:
            self.tableWidget_4.cellWidget(n.row(), 0).setChecked(True)

    def getCheckedRow(self):
        row = None
        rowCount = self.tableWidget.rowCount()
        for r in range(rowCount):
            if self.tableWidget.cellWidget(r, 0).isChecked():
                row = r
                break
        return row

    def getCheckedRow2(self):
        row = None
        rowCount = self.tableWidget_2.rowCount()
        for r in range(rowCount):
            if self.tableWidget_2.cellWidget(r, 0).isChecked():
                row = r
                break
        return row

    def getCheckedRow3(self):
        row = None
        rowCount = self.tableWidget_3.rowCount()
        for r in range(rowCount):
            if self.tableWidget_3.cellWidget(r, 0).isChecked():
                row = r
                break
        return row

    def getCheckedRow4(self):
        row = None
        rowCount = self.tableWidget_4.rowCount()
        for r in range(rowCount):
            if self.tableWidget_4.cellWidget(r, 0).isChecked():
                row = r
                break
        return row

    def load(self, userList):
        self.show()
        self.userid = userList[0]
        self.label_rank.setText(userList[5])
        self.label_name.setText(userList[1])
        if userList[4] == 0:
            self.pushButton_admin.setDisabled(False)
        elif userList[4] == 1:
            self.pushButton_teacher.setDisabled(False)
        elif userList[4] == 2:
            self.pushButton_student.setDisabled(False)

    def btn_admin(self):
        self.stackedWidget.setCurrentIndex(1)
        db = db_class()
        db.open()
        datas = db.select_all(user_table)
        self.load_table(datas)

    def btn_add(self):
        self.userWin = userWin()
        self.userWin.Sig_user.connect(self.userSlot)
        self.userWin.show()

    def btn_set(self):
        row = self.getCheckedRow()
        if row != None:
            id = self.tableWidget.item(row, 1).text()
            name = self.tableWidget.item(row, 2).text()
            username = self.tableWidget.item(row, 3).text()
            password = self.tableWidget.item(row, 4).text()
            rank_name = self.tableWidget.item(row, 5).text()
            self.userWin = userWin(id=id, name=name, username=username, password=password, rank_name=rank_name)
            self.userWin.Sig_user.connect(self.userSlot)
            self.userWin.show()

    def btn_del(self):
        row = self.getCheckedRow()
        if row != None:
            id = self.tableWidget.item(row, 1).text()
            db = db_class()
            db.open()
            db.delete_many(user_table, [{'id': id}])
            db.close()
            self.btn_admin()

    def load_table(self, items):
        '''
        数据写入表
        :param items:数据集合
        :return:
        '''
        try:
            self.tableWidget.setRowCount(0)
            for n, item in enumerate(items):
                self.tableWidget.setRowCount(n + 1)
                radio = QRadioButton()
                self.tableWidget.setCellWidget(n, 0, radio)
                self.tableWidget.setItem(n, 1, QTableWidgetItem(str(item[0])))
                self.tableWidget.setItem(n, 2, QTableWidgetItem(str(item[1])))
                self.tableWidget.setItem(n, 3, QTableWidgetItem(str(item[2])))
                self.tableWidget.setItem(n, 4, QTableWidgetItem(str(item[3])))
                self.tableWidget.setItem(n, 5, QTableWidgetItem(str(item[5])))
        except Exception as e:
            print(e)

    def load_table_q(self, items):
        '''
        数据写入表
        :param items:数据集合
        :return:
        '''
        try:
            self.tableWidget_2.setRowCount(0)
            for n, item in enumerate(items):
                self.tableWidget_2.setRowCount(n + 1)
                radio = QRadioButton()
                self.tableWidget_2.setCellWidget(n, 0, radio)
                self.tableWidget_2.setItem(n, 1, QTableWidgetItem(str(item[0])))
                self.tableWidget_2.setItem(n, 2, QTableWidgetItem(str(item[1])))
                self.tableWidget_2.setItem(n, 3, QTableWidgetItem(str(item[3])))
                self.tableWidget_2.setItem(n, 4, QTableWidgetItem(str(item[2])))
        except Exception as e:
            print(e)

    def load_table_c(self, items):
        '''
        数据写入表
        :param items:数据集合
        :return:
        '''
        try:
            self.tableWidget_3.setRowCount(0)
            for n, item in enumerate(items):
                self.tableWidget_3.setRowCount(n + 1)
                radio = QRadioButton()
                self.tableWidget_3.setCellWidget(n, 0, radio)
                self.tableWidget_3.setItem(n, 1, QTableWidgetItem(str(item[0])))
                self.tableWidget_3.setItem(n, 2, QTableWidgetItem(str(item[9])))
                self.tableWidget_3.setItem(n, 3, QTableWidgetItem(str(item[8])))
                self.tableWidget_3.setItem(n, 4, QTableWidgetItem(str(item[4])))
                self.tableWidget_3.setItem(n, 5, QTableWidgetItem(str(item[5])))
                self.tableWidget_3.setItem(n, 6, QTableWidgetItem(str(item[6])))
                self.tableWidget_3.setItem(n, 7, QTableWidgetItem(str(item[7])))
                self.tableWidget_3.setItem(n, 8, QTableWidgetItem(str(item[1])))
                self.tableWidget_3.setItem(n, 9, QTableWidgetItem(str(item[2])))
                self.tableWidget_3.setItem(n, 10, QTableWidgetItem(str(item[3])))
                self.tableWidget_3.setItem(n, 11, QTableWidgetItem(str(item[10])))
        except Exception as e:
            print(e)

    def load_table_s(self, items):
        '''
        数据写入表
        :param items:数据集合
        :return:
        '''
        try:
            self.tableWidget_4.setRowCount(0)
            for n, item in enumerate(items):
                self.tableWidget_4.setRowCount(n + 1)
                radio = QRadioButton()
                self.tableWidget_4.setCellWidget(n, 0, radio)
                self.tableWidget_4.setItem(n, 1, QTableWidgetItem(str(item[0])))
                self.tableWidget_4.setItem(n, 2, QTableWidgetItem(str(item[1])))
                self.tableWidget_4.setItem(n, 3, QTableWidgetItem(str(item[2])))
                self.tableWidget_4.setItem(n, 4, QTableWidgetItem(str(item[3])))
                self.tableWidget_4.setItem(n, 5, QTableWidgetItem(str(item[4])))
                self.tableWidget_4.setItem(n, 6, QTableWidgetItem(str(item[5])))
        except Exception as e:
            print(e)

    def userSlot(self, userObj):
        db = db_class()
        db.open()
        userObj['rank_id'] = '0' if userObj['rank_name'] == '管理员' else '1' if userObj['rank_name'] == '教师' else '2'
        if userObj['id']:
            id = userObj.pop('id')
            db.update_many(user_table, [userObj], [{'id': id}])
        else:
            userObj.pop('id')
            db.insert_many(user_table, [userObj])
        db.close()
        self.btn_admin()

    def btn_teacher(self):
        self.stackedWidget.setCurrentIndex(2)
        db = db_class()
        db.open()
        datas = db.select_all(questions)
        datas1 = db.select_scantron()
        db.close()
        self.load_table_q(datas)
        self.load_table_c(datas1)

    def btn_teacher_add(self):
        self.questionsWin = questionsWin()
        self.questionsWin.Sig_questions.connect(self.questionsSlot)
        self.questionsWin.show()

    def questionsSlot(self, questionsObj):
        db = db_class()
        db.open()
        if questionsObj['id']:
            id = questionsObj.pop('id')
            db.update_many(questions, [questionsObj], [{'id': id}])
        else:
            questionsObj.pop('id')
            db.insert_many(questions, [questionsObj])
        db.close()
        self.btn_teacher()

    def btn_teacher_set(self):
        row = self.getCheckedRow2()
        if row != None:
            id = self.tableWidget_2.item(row, 1).text()
            title = self.tableWidget_2.item(row, 2).text()
            answer = self.tableWidget_2.item(row, 3).text()
            paper = self.tableWidget_2.item(row, 4).text()
            self.questionsWin = questionsWin(id=id, title=title, answer=answer, paper=paper)
            self.questionsWin.Sig_questions.connect(self.questionsSlot)
            self.questionsWin.show()

    def btn_teacher_del(self):
        row = self.getCheckedRow2()
        if row != None:
            id = self.tableWidget_2.item(row, 1).text()
            db = db_class()
            db.open()
            db.delete_many(questions, [{'id': id}])
            db.close()
            self.btn_teacher()

    def btn_teacher_see(self):
        row = self.getCheckedRow2()
        if row != None:
            try:
                imgData = self.tableWidget_2.item(row, 4).text()
                self.showWin = showWin(imgData)
                self.showWin.show()
            except Exception as e:
                print(e)

    def btn_teacher_search(self):
        text = self.lineEdit_q.text().strip()
        if text:
            db = db_class()
            db.open()
            result = db.select_condition(questions, 'title like "%' + text + '%"')
            db.close()
            if result:
                self.load_table_q(result)

    def btn_teacher_add_c(self):
        self.scantronWin = scantronWin()
        self.scantronWin.Sig_scantron.connect(self.scantronWinSlot)
        self.scantronWin.show()

    def btn_teacher_set_c(self):
        row = self.getCheckedRow3()
        if row != None:
            id = self.tableWidget_3.item(row, 1).text()
            student_name = self.tableWidget_3.item(row, 2).text()
            question_title = self.tableWidget_3.item(row, 3).text()
            reply = self.tableWidget_3.item(row, 4).text()
            correct = self.tableWidget_3.item(row, 5).text()
            score = self.tableWidget_3.item(row, 6).text()
            sumscore = self.tableWidget_3.item(row, 7).text()
            student_id = self.tableWidget_3.item(row, 8).text()
            question_id = self.tableWidget_3.item(row, 9).text()
            paper = self.tableWidget_3.item(row, 10).text()
            answer = self.tableWidget_3.item(row, 11).text()
            self.scantronWin = scantronWin(id=id, student_name=student_name, question_title=question_title, reply=reply,
                                           correct=correct, score=score, sumscore=sumscore, student_id=student_id,
                                           question_id=question_id, paper=paper, answer=answer)
            self.scantronWin.Sig_scantron.connect(self.scantronWinSlot)
            self.scantronWin.show()

    def btn_teacher_del_c(self):
        row = self.getCheckedRow3()
        if row != None:
            id = self.tableWidget_3.item(row, 1).text()
            db = db_class()
            db.open()
            db.delete_many(scantron, [{'id': id}])
            db.close()
            self.btn_teacher()

    def btn_teacher_see_c(self):
        row = self.getCheckedRow3()
        if row != None:
            try:
                imgData = self.tableWidget_3.item(row, 10).text()
                self.showWin = showWin(imgData)
                self.showWin.show()
            except Exception as e:
                print(e)

    def btn_teacher_search_c(self):
        text = self.lineEdit_c.text().strip()
        if text:
            db = db_class()
            db.open()
            result = db.select_scantron_like(text)
            db.close()
            if result:
                self.load_table_c(result)

    def scantronWinSlot(self, Obj):
        db = db_class()
        db.open()
        if Obj['id']:
            id = Obj.pop('id')
            db.update_many(scantron, [Obj], [{'id': id}])
        else:
            Obj.pop('id')
            db.insert_many(scantron, [Obj])
        db.close()
        self.btn_teacher()

    def btn_student(self):
        self.stackedWidget.setCurrentIndex(3)
        db = db_class()
        db.open()
        datas = db.select_student_condition(self.userid)
        db.close()
        self.load_table_s(datas)

    def btn_see_1(self):
        row = self.getCheckedRow4()
        if row != None:
            try:
                id = self.tableWidget_4.item(row,1).text()
                db =db_class()
                db.open()
                imgData = db.select_question_condition(id)
                db.close()
                self.showWin = showWin(imgData[0][0])
                self.showWin.show()
            except Exception as e:
                print(e)

    def btn_see_2(self):
        row = self.getCheckedRow4()
        if row != None:
            try:
                id = self.tableWidget_4.item(row,1).text()
                db =db_class()
                db.open()
                imgData = db.select_scantron_condition(id)
                db.close()
                self.showWin = showWin(imgData[0][0])
                self.showWin.show()
            except Exception as e:
                print(e)

    def btn_see_3(self):
        row = self.getCheckedRow4()
        if row != None:
            try:
                id = self.tableWidget_4.item(row,1).text()
                self.scantronInfoWin = scantronInfoWin(id)
                self.scantronInfoWin.show()
            except Exception as e:
                print(e)

    def close(self):
        sys.exit(0)

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainWin()
    # win.show()
    sys.exit(app.exec_())
