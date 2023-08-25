import sys

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

from .resources.ResourceManager import ResourceManager
from .ui.MainWindow import MainWindow
from .ui.customerlist.CustomerListScreen import CustomerListScreen


def run():
    # Run the app
    app = QApplication(sys.argv)

    ResourceManager.resources_setup()

    window = MainWindow()
    window.show_new_screen(CustomerListScreen())

    window.show()
    sys.exit(app.exec())
