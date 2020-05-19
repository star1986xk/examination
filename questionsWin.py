from Ui.Ui_questions import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QFileDialog, QHeaderView,QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal
import base64


class questionsWin(Ui_Dialog, QDialog):
    Sig_questions = pyqtSignal(dict)

    def __init__(self, id=None, title=None, paper=None, answer=None, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(questionsWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        headerView = self.tableWidget.horizontalHeader()
        headerView.setSectionResizeMode(QHeaderView.Stretch)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        self.pushButton_upload.clicked.connect(self.upload)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_add.clicked.connect(self.add_T)
        self.pushButton_del.clicked.connect(self.del_T)

        self.id = id
        self.title = title
        self.paper = paper
        self.answer = answer

        self.load()

    def load(self):
        if self.id:
            self.lineEdit_title.setText(self.title)
            self.tableWidget.setRowCount(len(eval(self.answer)))
            for n,li in enumerate(eval(self.answer)):
                self.tableWidget.setItem(n,0,QTableWidgetItem(li[0]))
                self.tableWidget.setItem(n,1,QTableWidgetItem(li[1]))
                self.tableWidget.setItem(n,2,QTableWidgetItem(li[2]))

    def upload(self):
        '''
        导入图片路径
        :return:
        '''
        filename, _ = QFileDialog.getOpenFileName(self, '选取文件', './', '图片文件 (*.jpg; *.png)')
        if filename:
            self.lineEdit_upload.setText(filename)

    def add_T(self):
        try:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rowCount + 1)
        except Exception as e:
            print(e)

    def del_T(self):
        row = self.tableWidget.currentRow()
        if row !=None:
            self.tableWidget.removeRow(row)

    def save(self):
        path = self.lineEdit_upload.text()
        title = self.lineEdit_title.text()
        if title and (path or self.paper):
            if path:
                paper = self.ImgToBase64(path)
            else:
                paper = self.paper
            rowCount = self.tableWidget.rowCount()
            items = []
            for r in range(rowCount):
                a = self.tableWidget.item(r,0).text()
                b = self.tableWidget.item(r,1).text()
                c = self.tableWidget.item(r,2).text()
                items.append([a,b,c])
            self.Sig_questions.emit({'id':self.id,'title':title,'paper':paper,'answer ':str(items)})
            self.close()

    def ImgToBase64(self,path):
        with open(path, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            s = base64_data.decode()
        return s