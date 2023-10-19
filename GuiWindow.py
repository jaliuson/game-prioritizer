import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QLabel, 
    QHBoxLayout, 
    QVBoxLayout
)
from gui.LeftPanel import LeftPanel
#from gui.RightPanel import RightPanel

class GamePrioritizerWindow(QWidget):
   def __init__(self, parent = None):
      super().__init__()
      self.setWindowTitle("Game Prioritizer")

      app = QVBoxLayout()
      app.addWidget(Header())
      app.addWidget(Body())
      app.setContentsMargins(0,0,0,0)
      self.setLayout(app) 
   
class Header(QWidget):
   def __init__(self, parent = None):
      super().__init__()

      title = QLabel("Game Prioritizer")
      title.setStyleSheet("background-color: #021a40; color: white; font-size: 32px; padding: 10px;")      
      label = QHBoxLayout()
      label.addWidget(title)
      label.setContentsMargins(0, 0, 0, 0)  
      self.setLayout(label)
      self.setStyleSheet("border : 1px solid gray;")
      
      self.setFixedHeight(75)

class Body(QWidget):    
   def __init__(self, parent = None):
      super().__init__()
      panels = QHBoxLayout()
      panels.addWidget(LeftPanel(self))
      panels.addWidget(QLabel("right"))
      panels.setContentsMargins(0, 0, 0, 0)  
      self.setLayout(panels)
      self.setStyleSheet("border : 1px solid blue;")
      
def main():
   app = QApplication(sys.argv)
   window = GamePrioritizerWindow()
   window.setMinimumSize(600, 400)
   window.resize(600, 400)
   window.setContentsMargins(0,0,0,0)
   window.setAttribute(QtCore.Qt.WA_StyledBackground, True)
   window.setStyleSheet('background-color: #acc9fc')
   window.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()