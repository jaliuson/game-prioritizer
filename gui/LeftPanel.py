import sys
from PyQt5.QtWidgets import (
    QWidget, 
    QVBoxLayout,
)

from gui.GameSelector import SelectPanel
from gui.RunPanel import RunPanel

class LeftPanel(QWidget):
    def __init__ (self, logPanel, parent = None):
        super().__init__()
        self.logPanel = logPanel
        selector = SelectPanel()
        
        panelStack = QVBoxLayout()
        panelStack.addWidget(selector)
        panelStack.addWidget(RunPanel(self.logPanel, selector))
        panelStack.setContentsMargins(0, 0, 0, 0)

        self.setLayout(panelStack)
        self.setStyleSheet("border : 1px solid blue;")
