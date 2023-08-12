from PyQt5.QtWidgets import QWidget


class AbstractCustomWidget(QWidget):
    """A custom complex widget. Override create_ui for usage."""

    def __init__(self, parent=None, *args):
        super().__init__(parent)
        self.create_ui(*args)

    def create_ui(self, *args):
        """Creates the ui of the widget. To be overridden."""
        pass
