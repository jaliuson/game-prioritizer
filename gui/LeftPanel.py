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

from gui.GameSelector import SelectPanel
from gui.RunPanel import RunPanel

class LeftPanel(QWidget):
    def __init__ (self, parent = None):
        super().__init__()
        selector = SelectPanel()
        panelStack = QVBoxLayout()
        panelStack.addWidget(selector)
        print(selector.selected_game)
        panelStack.addWidget(RunPanel(selector))
        panelStack.setContentsMargins(0, 0, 0, 0)
        self.setLayout(panelStack)
        self.setStyleSheet("border : 1px solid blue;")
