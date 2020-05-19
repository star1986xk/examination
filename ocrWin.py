from Ui.Ui_ocr import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt, pyqtSignal


class ocrWin(Ui_Dialog, QDialog):
    Sig_ocr = pyqtSignal(str)

    def __init__(self, text=None, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(ocrWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        if text:
            self.textEdit.setText(text)

        self.pushButton_add.clicked.connect(self.btn_add)
        self.pushButton_close.clicked.connect(self.close)

    def btn_add(self):
        text = self.textEdit.toPlainText()
        if text:
            self.Sig_ocr.emit(text)
            self.close()