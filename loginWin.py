import sys
from Ui.Ui_login import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox
from db_class import db_class
from settings import user_table
from PyQt5.QtCore import Qt, pyqtSignal

class loginWin(Ui_Dialog, QDialog):
    Sig_login = pyqtSignal(list)

    def __init__(self, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(loginWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_close.clicked.connect(self.quit)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    def login(self):
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()
        if username and password:
            db = db_class()
            db.open()
            result = db.select_condition(user_table, 'username="' + username + '" and password="' + password+'"')
            db.close()
            if result:
                self.Sig_login.emit(list(result[0]))
                self.close()
            else:
                QMessageBox.about(self,'提示','账号或密码错误！')

    def quit(self):
        sys.exit(0)
