import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QWidget, 
    QLabel, 
    QVBoxLayout,
    QRadioButton
)
from data.GamesList import GAME_OPTIONS

class SelectPanel(QWidget):
    string_updated = pyqtSignal(str)  # Define a signal

    def __init__(self, parent = None):
        super().__init__()
        games = GAME_OPTIONS
        self.selected_game = None
        self.radio_buttons = []
        
        gameSelector = QVBoxLayout()
        gameSelector.addWidget(QLabel("Select game to optimize"))
        for g in games:
            radio_button = QRadioButton(g)
            radio_button.clicked.connect(self.onRadioBtnClick)
            self.radio_buttons.append(radio_button)
            gameSelector.addWidget(radio_button)

        gameSelector.setContentsMargins(0, 0, 0, 0)

        self.setLayout(gameSelector)
        self.setStyleSheet("border : 1px solid gray;")
    
    def onRadioBtnClick(self):
        sender = self.sender()  # Get the radio button that was clicked
        if sender.isChecked():
            self.selected_game = sender.text()
            self.string_updated.emit(self.selected_game)  # Emit the signal when the string changes