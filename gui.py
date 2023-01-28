from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from Image import ImagePreprocessing as IP
import predict

from PIL.ImageQt import ImageQt

import sys


class GUI:
    def set_message(self):
        path = self.text_field.text()
        print(path)
        self.load_image(path)

    def load_image(self):
        self.image_path = self.text_field.text()
        pixmap = QPixmap(self.image_path)
        self.image_label.setPixmap(pixmap)

    def process_image(self):
        if self.image_path is None or self.image_path == "":
            return
        image = IP()
        image.open(self.image_path)
        image.to_gray()
        image.locate_content()
        image.pixelate()
        qimg = ImageQt(image.image)
        piximg = QPixmap.fromImage(qimg)
        self.image_label.setPixmap(piximg)

    def predict(self):
        # call predicting function from ML lib
        prediction = predict.predict(self.image_path)
        self.output_label.setText(f"<h1>{prediction}</h1>")

    def __init__(self):
        self.image_path = None

        self.app = QApplication([])

        self.window = QWidget(flags=Qt.WindowFlags())
        self.window.setWindowTitle("Number Recognition")
        self.window.setGeometry(100, 100, 400, 330)

        self.text_field = QLineEdit()
        self.text_field.setGeometry(10, 10, 380, 25)
        self.text_field.setParent(self.window)

        self.display_image_btn = QPushButton("Load Image")
        self.display_image_btn.setParent(self.window)
        self.display_image_btn.setGeometry(300, 45, 90, 25)
        self.display_image_btn.setStyleSheet("text_align: center")
        self.display_image_btn.clicked.connect(self.load_image)

        self.process_image_btn = QPushButton("Process Image")
        self.process_image_btn.setParent(self.window)
        self.process_image_btn.setGeometry(300, 80, 90, 25)
        self.process_image_btn.setStyleSheet("text_align: center")
        self.process_image_btn.clicked.connect(self.process_image)

        self.process_image_btn = QPushButton("Predict")
        self.process_image_btn.setParent(self.window)
        self.process_image_btn.setGeometry(300, 115, 90, 25)
        self.process_image_btn.setStyleSheet("text_align: center")
        self.process_image_btn.clicked.connect(self.predict)

        self.image_label = QLabel("<h1>Hello, World!</h1>")
        self.image_label.setParent(self.window)
        self.image_label.move(10, 40)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(280, 280)
        self.image_label.setScaledContents(True)
        self.image_label.setStyleSheet("border: 1px solid black;")

        self.output_label = QLabel("t")
        self.output_label.setParent(self.window)
        self.output_label.move(300, 150)
        self.output_label.setFixedSize(90, 90)
        self.output_label.setAlignment(Qt.AlignCenter)
        self.output_label.setScaledContents(True)
        self.output_label.setStyleSheet("border: 1px solid black;")

    def show(self):
        self.window.show()
        sys.exit(self.app.exec())
