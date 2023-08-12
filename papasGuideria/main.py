import sys
from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow
from ui.customerlist.CustomerListScreen import CustomerListScreen


if __name__ == "__main__":
    # Setup app
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show_new_screen(CustomerListScreen())

    window.show()
    sys.exit(app.exec())
