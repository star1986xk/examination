from Ui.Ui_scantron import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QFileDialog, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal
from scantron_qWin import scantron_qWin
from scantron_sWin import scantron_sWin
from db_class import db_class
from ocrWin import ocrWin
import split_class
import base64


class scantronWin(Ui_Dialog, QDialog):
    Sig_scantron = pyqtSignal(dict)

    def __init__(self, id=None, student_name=None, question_title=None, paper=None, reply=None, correct=None,
                 score=None, sumscore=None, student_id=None, question_id=None, answer=None, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(scantronWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        headerView = self.tableWidget.horizontalHeader()
        headerView.setSectionResizeMode(QHeaderView.Stretch)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        self.id = id
        self.student_id = student_id
        self.student_name = student_name
        self.question_id = question_id
        self.question_title = question_title
        self.paper = paper
        self.reply = reply
        self.correct = correct
        self.score = score
        self.sumscore = sumscore
        self.answer = answer
        self.load()

        self.pushButton_upload.clicked.connect(self.upload)
        self.pushButton_q.clicked.connect(self.btn_q)
        self.pushButton_s.clicked.connect(self.btn_s)
        self.pushButton_ocr.clicked.connect(self.btn_ocr)
        self.pushButton_score.clicked.connect(self.btn_score)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_cancel.clicked.connect(self.close)

    def load(self):
        if self.id:
            self.label_2.setText(self.question_title)
            self.label_3.setText(self.student_name)
            self.label_7.setText(self.sumscore)
            self.tableWidget.setRowCount(len(eval(self.answer)))
            for n, (a, r, c, s) in enumerate(
                    zip(eval(self.answer), eval(self.reply), eval(self.correct), eval(self.score))):
                self.tableWidget.setItem(n, 0, QTableWidgetItem(a[0]))
                self.tableWidget.setItem(n, 1, QTableWidgetItem(a[1]))
                self.tableWidget.setItem(n, 2, QTableWidgetItem(a[2]))
                self.tableWidget.setItem(n, 3, QTableWidgetItem(r))
                self.tableWidget.setItem(n, 4, QTableWidgetItem(c))
                self.tableWidget.setItem(n, 5, QTableWidgetItem(s))

    def upload(self):
        '''
        导入图片路径
        :return:
        '''
        filename, _ = QFileDialog.getOpenFileName(self, '选取文件', './', '图片文件 (*.jpg; *.png)')
        if filename:
            self.lineEdit_upload.setText(filename)

    def btn_q(self):
        self.scantron_qWin = scantron_qWin()
        self.scantron_qWin.Sig_questions.connect(self.set_q)
        self.scantron_qWin.show()

    def btn_s(self):
        self.scantron_sWin = scantron_sWin()
        self.scantron_sWin.Sig_student.connect(self.set_s)
        self.scantron_sWin.show()

    def set_q(self, id, title, answer):
        self.question_id = id
        self.question_title = title
        self.label_2.setText(title)
        self.load_T(answer)

    def set_s(self, id, name):
        self.student_id = id
        self.student_name = name
        self.label_3.setText(name)

    def load_T(self, answer):
        self.tableWidget.setRowCount(len(eval(answer)))
        for n, li in enumerate(eval(answer)):
            self.tableWidget.setItem(n, 0, QTableWidgetItem(li[0]))
            self.tableWidget.setItem(n, 1, QTableWidgetItem(li[1]))
            self.tableWidget.setItem(n, 2, QTableWidgetItem(li[2]))

    def btn_ocr(self):
        path = self.lineEdit_upload.text()
        if path or self.paper:
            if path:
                paper = self.ImgToBase64(path)
            else:
                paper = self.paper
            text = split_class.split_img(paper)
            self.ocrWin = ocrWin(text)
            self.ocrWin.Sig_ocr.connect(self.addocr)
            self.ocrWin.show()

    def addocr(self, text):
        text_list = text.split('\n')
        rowCount = self.tableWidget.rowCount()
        for r in range(rowCount):
            if r < len(text_list):
                self.tableWidget.setItem(r, 3, QTableWidgetItem(text_list[r]))

    def btn_score(self):
        rowCount = self.tableWidget.rowCount()
        scorelist = 0
        for i in range(rowCount):
            answer = self.tableWidget.item(i, 1).text()
            score = self.tableWidget.item(i, 2).text()
            reply = self.tableWidget.item(i, 3).text()
            correct = '对' if answer == reply else '错'
            self.tableWidget.setItem(i, 4, QTableWidgetItem(correct))
            if correct == '对':
                scorelist += int(score)
                self.tableWidget.setItem(i, 5, QTableWidgetItem(score))
            else:
                self.tableWidget.setItem(i, 5, QTableWidgetItem('0'))
        self.label_7.setText(str(scorelist))

    def save(self):
        path = self.lineEdit_upload.text()
        sumscore = self.label_7.text()
        if path or self.paper:
            if path:
                paper = self.ImgToBase64(path)
            else:
                paper = self.paper
            rowCount = self.tableWidget.rowCount()
            replyList = []
            correctList = []
            scoreList = []
            for r in range(rowCount):
                replyList.append(self.tableWidget.item(r, 3).text())
                correctList.append(self.tableWidget.item(r, 4).text())
                scoreList.append(self.tableWidget.item(r, 5).text())
            self.Sig_scantron.emit(
                {'id': self.id, 'student_id': self.student_id, 'question_id': self.question_id, 'paper ': paper,
                 'reply': str(replyList), 'correct': str(correctList), 'score': str(scoreList), 'sumscore': sumscore})
            self.close()

    def ImgToBase64(self, path):
        with open(path, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            s = base64_data.decode()
        return s
