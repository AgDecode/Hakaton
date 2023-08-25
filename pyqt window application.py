import os
import sys

from PyQt5 import uic, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ import AI


class Future_Machine_Learning(QMainWindow):
    def __init__(self):
        super().__init__()
        global files
        file_path = os.path.join('files/')
        files = {'window title': 'Machine Learning application',
                 'window icon': 'icon.jpg',
                 'ui file': 'application.ui'}
        uic.loadUi(file_path + files['ui file'], self)
        self.setWindowTitle(files['window title'])
        self.setWindowIcon(QtGui.QIcon(file_path + files['window icon']))
        self.setStyleSheet("background-color: gray;")
        self.sex_input.setText('мужской - 1 или женский - 0')
        self.error_label.setHidden(True)
        self.quit_btn.clicked.connect(self.quit)
        self.calculate_btn.clicked.connect(self.calculate)

    def calculate(self):
        male = self.sex_input.text()
        rules = ((male == '0' or male == '1') and (
                self.height_input.text().isnumeric() and self.weigth_input.text().isnumeric()))
        if rules:
            sex = int(self.sex_input.text())
            height = int(self.height_input.text())
            weigth = int(self.weigth_input.text())

            res = str(AI(sex, height, weigth))
            self.thin_coeff.setText(res)
            self.thin_coeff.setFont(QFont('Times font', 24))
            self.error_label.setHidden(True)
        else:
            self.error_label.setHidden(False)

    def quit(self):
        sys.exit(application.exec_())


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Future_Machine_Learning()
    window.show()
    sys.exit(application.exec_())
