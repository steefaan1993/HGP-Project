from PyQt5.QtWidgets import QDockWidget, QLabel
from PyQt5.QtGui import QIcon
from board import Board
import sys

class ScoreBoard(QDockWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''initiates ScoreBoard UI'''
        self.lab = QLabel("Player 1")
        self.resize(200, 200)
        self.center()
        self.setWindowTitle('ScoreBoard')
        self.
        self.show()

    def center(self):
        '''centers the window on the screen'''

