import sys
from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow


if __name__ == "__main__":
    # Setup app
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()
    sys.exit(app.exec())
