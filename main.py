# -*- coding: utf-8 -*-
# @Author: YokDen
# @Time: 2022/9/13
# @Email: dyk_693@qq.com

import sys
import standard
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = standard.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
