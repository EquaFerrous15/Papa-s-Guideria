from PyQt5.QtWidgets import QWidget


class AbstractCustomWidget(QWidget):
    """A custom complex widget."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.create_ui()

    def create_ui(self):
        """Creates the ui of the widget. To be overridden."""
        pass
