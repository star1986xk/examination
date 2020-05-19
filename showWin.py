import base64
import sys
from Ui.Ui_show import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog
import cv2
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class showWin(Ui_Dialog, QDialog):

    def __init__(self,imgData=None, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(showWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        nparr = np.fromstring(base64.b64decode(imgData), np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        self.figure = plt.figure(figsize=(10,20))
        self.canvas = FigureCanvas(self.figure)

        ax = self.figure.add_subplot(111)
        ax.imshow(img_np)
        ax.set_xticks([])
        ax.set_yticks([])
        self.canvas.draw()
        self.horizontalLayout_2.addWidget(self.canvas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = showWin()
    win.show()
    sys.exit(app.exec_())
