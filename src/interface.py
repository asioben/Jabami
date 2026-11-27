from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jabami")
        self.setStyleSheet("background-color: magenta;")
        self.setGeometry(500, 500, 400, 300)
        self.show()

App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())
