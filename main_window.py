import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton

class CustomMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Main Window: Savings app")
        self.setGeometry(100,50,1080,800)

        # Central Widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        # Custom Widgets
        self.label = QLabel("Hello, Custom QMainWindow!", self)
        self.button = QPushButton("Click me!", self)
        self.button.clicked.connect(self.on_button_clicked)

        # Adding Widgets to Layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

    
    def on_button_clicked(self):
        self.layout.addWidget(QLabel("New Label"))
        print("Button Clicked!")