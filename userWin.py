from Ui.Ui_user import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt, pyqtSignal

class userWin(Ui_Dialog, QDialog):
    Sig_user = pyqtSignal(dict)

    def __init__(self, id=None , name=None, username=None, password=None, rank_name=None, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(userWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.rank_name =rank_name

        self.pushButton_ok.clicked.connect(self.btn_ok)
        self.pushButton_cancel.clicked.connect(self.close)

        self.load()

    def load(self):
        if self.id:
            self.lineEdit_name.setText(self.name)
            self.lineEdit_username.setText(self.username)
            self.lineEdit_password.setText(self.password)
            self.comboBox_rank_name.setCurrentText(self.rank_name)

    def btn_ok(self):
        name = self.lineEdit_name.text()
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        rank_name = self.comboBox_rank_name.currentText()
        if name and username and password and rank_name:
            self.Sig_user.emit({'id':self.id,'name':name,'username':username,'password':password,'rank_name':rank_name})
        self.close()