import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QTextEdit, 
    QPushButton, 
    QMessageBox, 
    QHBoxLayout, 
    QVBoxLayout
)

from gui.RunLog import RunLog

class RightPanel(QWidget):
    def __init__ (self, parent = None):
        super().__init__()
        testLogList = [
            {
                "game": 'Valorant',
                "run time": "123",
                "timestamp": "456"
            },
            {
                "game": 'LoL',
                "run time": "789",
                "timestamp": "000"  
            },
            {
                "game": 'Valorant',
                "run time": "246",
                "timestamp": "135"
            }
        ]
        self.runLogData = []

        super().__init__()

        panelStack = QVBoxLayout()
        panelStack.addWidget(RunLog(self.runLogData))
        panelStack.setContentsMargins(0, 0, 0, 0)

        self.setLayout(panelStack)
        self.setStyleSheet("border : 1px solid gray;")

class RightPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.log_widget = QTextEdit()
        self.log_widget.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.log_widget)
        self.setLayout(layout)

    def update_log(self, log_messages):
        # Append log messages from a list of dictionaries to the QTextEdit
        for message in log_messages:
            timestamp = message.get("timestamp", "")
            duration = message.get("duration", "")
            message_text = message.get("message", "")
            log_entry = f"Timestamp: {timestamp}, Duration: {duration}, Message: {message_text}\n"
            current_text = self.log_widget.toPlainText()
            new_text = current_text + log_entry
            self.log_widget.setPlainText(new_text)