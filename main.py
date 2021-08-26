#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
guaDictateTool

An dictate tool for LTH.

Author: Yiqin Xiong
Create: August 2021
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMainWindow
from guaWindow import Ui_MainWindow


class MWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.jfif'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MWindow()
    m.show()
    sys.exit(app.exec_())
