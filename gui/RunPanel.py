import sys
from PyQt5.QtWidgets import (
    QWidget, 
    QPushButton, 
    QMessageBox, 
    QHBoxLayout, 
)
from GamePrioritizer import *


class RunPanel(QWidget):
    log_updated = pyqtSignal(list)  # Custom signal to update the log

    def __init__(self, logPanel, selectorPanel, parent = None):
        super().__init__()
        self.SelectorPanel = selectorPanel
        self.logPanel = logPanel

        buttonArray = QHBoxLayout()
        btn1 = QPushButton("Run")
        btn1.clicked.connect(self.optimizeGames)
        buttonArray.setContentsMargins(0, 0, 0, 0)  

        buttonArray.addWidget(btn1)
        self.setLayout(buttonArray)
        self.setStyleSheet("border : 1px solid gray;")

    def optimizeGames(self):
        targetGame = self.SelectorPanel.selected_game
        self.logPanel.runLogData.append(run(targetGame, self.logPanel))
        print('XXX >> ')
        print(self.logPanel)
        self.log_updated.emit(self.logPanel.runLogData)  # Emit the signal with the log message
        self.show_message_box()

    def show_message_box(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Games Optimized: " + self.SelectorPanel.selected_game)
        msg.setWindowTitle("Message")
        msg.exec_()