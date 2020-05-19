from Ui.Ui_scantronInfo import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal
from db_class import db_class


class scantronInfoWin(Ui_Dialog, QDialog):
    Sig_scantron = pyqtSignal(dict)

    def __init__(self, id=None, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(scantronInfoWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        headerView = self.tableWidget.horizontalHeader()
        headerView.setSectionResizeMode(QHeaderView.Stretch)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        db = db_class()
        db.open()
        result = db.select_scantronInfo_condition(id)
        db.close()
        self.label_1.setText(str(result[0][4]))

        self.tableWidget.setRowCount(len(eval(result[0][0])))
        for n, (a, r, c, s) in enumerate(
                zip(eval(result[0][0]), eval(result[0][1]), eval(result[0][2]), eval(result[0][3]))):
            self.tableWidget.setItem(n, 0, QTableWidgetItem(a[0]))
            self.tableWidget.setItem(n, 1, QTableWidgetItem(a[1]))
            self.tableWidget.setItem(n, 2, QTableWidgetItem(a[2]))
            self.tableWidget.setItem(n, 3, QTableWidgetItem(r))
            self.tableWidget.setItem(n, 4, QTableWidgetItem(c))
            self.tableWidget.setItem(n, 5, QTableWidgetItem(s))

        self.pushButton_close.clicked.connect(self.close)