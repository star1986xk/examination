from Ui.Ui_scantron_q import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QRadioButton
from PyQt5.QtCore import Qt, pyqtSignal
from db_class import db_class
from settings import questions


class scantron_qWin(Ui_Dialog, QDialog):
    Sig_questions = pyqtSignal(str,str,str)

    def __init__(self, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(scantron_qWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        headerView = self.tableWidget.horizontalHeader()
        headerView.setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setColumnHidden(3, True)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        self.tableWidget.clicked.connect(self.t_check)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_cancel.clicked.connect(self.close)

        self.load()

    def t_check(self, n):
        if self.tableWidget.cellWidget(n.row(), 0).isChecked():
            self.tableWidget.cellWidget(n.row(), 0).setChecked(False)
        else:
            self.tableWidget.cellWidget(n.row(), 0).setChecked(True)

    def load(self):
        db = db_class()
        db.open()
        datas = db.select_all(questions)
        self.load_table_q(datas)
        db.close()

    def load_table_q(self, items):
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
                self.tableWidget.setItem(n, 3, QTableWidgetItem(str(item[3])))
        except Exception as e:
            print(e)

    def save(self):
        row = self.tableWidget.currentRow()
        if row !=None:
            id = self.tableWidget.item(row,1).text()
            title = self.tableWidget.item(row,2).text()
            answer = self.tableWidget.item(row,3).text()
            self.Sig_questions.emit(id,title,answer)
            self.close()