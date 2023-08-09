from PyQt5.QtWidgets import QMainWindow, QStackedWidget


class MainWindow(QMainWindow):
    """The main ui window."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Papa's Guideria")
        self.create_ui()

    def create_ui(self) -> None:
        """Set up the ui of the widget."""
        # Overall style
        self.setStyleSheet(
            "background-color: white;")

        # Widgets
        main_widget = QStackedWidget()
        self.setCentralWidget(main_widget)
