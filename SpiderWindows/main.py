# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from text import *

if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    ui = Ui_windows()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
