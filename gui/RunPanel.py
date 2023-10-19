import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QLabel, 
    QPushButton, 
    QMessageBox, 
    QHBoxLayout, 
    QVBoxLayout,
    QRadioButton
)
from GamePrioritizer import *


class RunPanel(QWidget):
    def __init__(self, selectorPanel, parent = None):
        super().__init__()
        self.SelectorPanel = selectorPanel

        buttonArray = QHBoxLayout()
        btn1 = QPushButton("Run")
        btn1.clicked.connect(self.optimizeGames)
        buttonArray.setContentsMargins(0, 0, 0, 0)  

        buttonArray.addWidget(btn1)
        self.setLayout(buttonArray)
        self.setStyleSheet("border : 1px solid gray;")

    def optimizeGames(self):
        targetGame = self.SelectorPanel.selected_game
        run(targetGame)
        self.show_message_box()

    def show_message_box(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Games Optimized: " + self.SelectorPanel.selected_game)
        msg.setWindowTitle("Message")
        msg.exec_()