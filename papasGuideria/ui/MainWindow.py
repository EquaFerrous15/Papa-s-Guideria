from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from .generic.AbstractScreen import AbstractScreen


class MainWindow(QMainWindow):
    """The main ui window."""

    def __init__(self):
        super().__init__()

        self.main_widget: QStackedWidget | None = None

        self.setWindowTitle("Papa's Guideria")
        self.create_ui()

    def create_ui(self) -> None:
        """Set up the ui of the widget."""
        # Overall style
        self.setStyleSheet(
            "background-color: white;")

        # Widgets
        self.main_widget = QStackedWidget()
        self.setCentralWidget(self.main_widget)

    def show_new_screen(self, new_screen: AbstractScreen) -> None:
        """Shows the new screen over any previous screens."""
        self.main_widget.insertWidget(0, new_screen)
        self.update_window()

    def update_window(self) -> None:
        """Updates the window based on current screen."""
        self.main_widget.setCurrentIndex(0)
        size_hint = self.main_widget.currentWidget().sizeHint()
        if size_hint.isValid():
            self.main_widget.setFixedSize(size_hint)


