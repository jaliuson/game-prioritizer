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


class RunPanel(QWidget):
    def __init__(self, selectorPanel, parent = None):
        super().__init__()
        self.SelectorPanel = selectorPanel

        buttonArray = QHBoxLayout()
        btn1 = QPushButton("Run")
        btn1.clicked.connect(self.show_message_box)
        buttonArray.setContentsMargins(0, 0, 0, 0)  

        buttonArray.addWidget(btn1)
        self.setLayout(buttonArray)
        self.setStyleSheet("border : 1px solid gray;")

    def optimizeGames(self):
        print('run here')

    def show_message_box(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Games Optimized: " + self.SelectorPanel.selected_game)
        msg.setWindowTitle("Message")
        msg.exec_()