import sys
from PyQt5.QtWidgets import (
    QWidget, 
    QVBoxLayout,
    QHBoxLayout,
    QLabel
)

class RunLog (QWidget):
    def __init__(self, logList, parent = None):
        super().__init__()
        self.logList = logList

        panelStack = QVBoxLayout()
        panelStack.addWidget(QLabel('Run Log', self))
        if len(self.logList) > 0:
            for item in self.logList:
                print("Current Log List_________________")
                print(item)
                panelStack.addWidget(LineItem(item))
        panelStack.setContentsMargins(0, 0, 0, 0)
        self.setLayout(panelStack)
        self.setStyleSheet("border : 1px solid blue;")


class LineItem (QWidget):
    def __init__(self, runData, parent = None):
        super().__init__()
        
        itemLayout = QHBoxLayout()
        itemLayout.addWidget(QLabel(runData["game"], self))
        itemLayout.addWidget(QLabel(runData["timestamp"], self))
        itemLayout.addWidget(QLabel(runData["run time"], self))

        itemLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(itemLayout)
        self.setStyleSheet("border : 1px solid gray;")






