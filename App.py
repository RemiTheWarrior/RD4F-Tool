from PyQt5.QtWidgets import (QWidget,
                             QVBoxLayout, 
                             QTabWidget,
                             QDesktopWidget,
                             QMainWindow,
                             QAction,
                             QMenuBar,
                             QDialog,
                             QMessageBox
                            )
from PyQt5.QtGui import QIcon, QColor, QPalette, QBrush
import matplotlib.pyplot as plt
from FirstTab import FirstTab
from SecondTab import SecondTab
from ThirdTab import ThirdTab
import os
from PyQt5.QtCore import Qt
from HelpWindow import HelpWindow
from MainWidget import MainWidget
from AboutWindow import AboutWindow


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'RDRP Database Tools'
        self.left = 10
        self.top = 10
        self.width = 1600  # 640
        self.height = 640
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + "ressources" +  os.path.sep + "logo.png"))
        # menu part
        bar = self.menuBar()
        helpAction = QAction('Show help', self)
        helpAction.setShortcut('Ctrl+H')
        # helpAction.setStatusTip('Open Directory')
        helpAction.triggered.connect(self.openHelp)
        aboutAction = QAction("Show about", self)
        aboutAction.setShortcut("Ctrl+A")
        aboutAction.triggered.connect(self.openAbout)
        helpMenu = bar.addMenu('Help')
        helpMenu.addAction(helpAction)
        aboutMenu = bar.addMenu('About')
        aboutMenu.addAction(aboutAction)
        self.setCentralWidget(MainWidget())
        self.center()
        #set background color
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(0, 113, 134))
        self.setPalette(p)
        self.show()

    def center(self):
        # see answer of BPL on https://stackoverflow.com/questions/39046059/pyqt-location-of-the-window
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        widget = self.geometry()
        maxX = ag.width() - widget.width()
        maxY = 2 * ag.height() - sg.height() - widget.height()
        self.move(maxX/2, maxY/2)

    def openHelp(self):
        dialog = HelpWindow(self)
        dialog.show()
    
    def openAbout(self):
        dialog = AboutWindow(self)
        dialog.show()
