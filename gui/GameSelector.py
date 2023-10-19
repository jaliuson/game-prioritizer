import sys
from PyQt5.QtCore import Qt, pyqtSignal
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
            radio_button.clicked.connect(self.on_radio_button_clicked)
            self.radio_buttons.append(radio_button)
            gameSelector.addWidget(radio_button)

        gameSelector.setContentsMargins(0, 0, 0, 0)

        self.setLayout(gameSelector)
        self.setStyleSheet("border : 1px solid gray;")
    
    def on_radio_button_clicked(self):
        sender = self.sender()  # Get the radio button that was clicked
        if sender.isChecked():
            self.selected_game = sender.text()
            updated_string = self.selected_game
            self.string_updated.emit(updated_string)  # Emit the signal when the string changes