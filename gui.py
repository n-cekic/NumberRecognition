from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton
from PyQt5.QtCore import Qt
import sys


class GUI:
    def display_message(self):
        self.hw_label.setText("AAAAAAAAAAAAA")

    def __init__(self):
        self.app = QApplication([])

        self.window = QWidget(flags=Qt.WindowFlags())
        self.window.setWindowTitle("Number Recognition")
        self.window.setGeometry(100, 100, 400, 400)

        self.hw_label = QLabel("<h1>Hello, World!</h1>")
        self.hw_label.setParent(self.window)
        self.hw_label.move(15, 60)

        self.print_message_btn = QPushButton("Display Message")
        self.print_message_btn.setParent(self.window)
        self.print_message_btn.clicked.connect(self.display_message)

    def show(self):
        self.window.show()
        sys.exit(self.app.exec())


gui = GUI()
gui.show()
