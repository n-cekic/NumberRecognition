from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import sys


class GUI:
    def set_message(self):
        path = self.text_field.text()
        print(path)
        self.load_image(path)

    def load_image(self, path_to_image):
        pixmap = QPixmap(path_to_image)
        self.hw_label.setPixmap(pixmap)

    def __init__(self):
        # test_image_path = r"C:\Users\nceki\Desktop\стипендија\IMG_20221217_180054 AA.jpg"

        self.app = QApplication([])

        self.window = QWidget(flags=Qt.WindowFlags())
        self.window.setWindowTitle("Number Recognition")
        self.window.setGeometry(100, 100, 400, 400)

        self.hw_label = QLabel("<h1>Hello, World!</h1>")
        self.hw_label.setParent(self.window)
        self.hw_label.move(15, 60)
        self.hw_label.setFixedSize(200, 200)
        self.hw_label.setAlignment(Qt.AlignCenter)
        self.hw_label.setScaledContents(True)

        self.image_label = QLabel()

        self.display_image_btn = QPushButton("Display Message")
        self.display_image_btn.setParent(self.window)
        self.display_image_btn.setGeometry(220, 10, 90, 25)
        self.display_image_btn.setStyleSheet("text_align: center")
        self.display_image_btn.clicked.connect(self.set_message)

        self.text_field = QLineEdit()
        self.text_field.setParent(self.window)
        self.text_field.setGeometry(10, 10, 200, 25)

    def show(self):
        self.window.show()
        sys.exit(self.app.exec())
