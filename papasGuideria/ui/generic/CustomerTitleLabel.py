from PyQt5.QtWidgets import QLabel, QGridLayout

from .AbstractCustomWidget import AbstractCustomWidget


class CustomerTitleLabel(AbstractCustomWidget):
    """A label to display a customer's title with special formatting depending on the title."""

    def __init__(self, customer_title: str, parent=None):
        super().__init__(parent, customer_title)

    def create_ui(self, customer_title: str):
        if customer_title is None:
            customer_title = "Normal Customer"
        customer_title = customer_title.title()

        # Choose text colour
        text_colour = "color: "
        match customer_title:
            case "Food Critic":
                text_colour += "'#0167CD';"
            case "Closer" | "Ex-Closer":
                text_colour += "'#CD0101';"
            case "Local":
                text_colour += "'#FEC418';"
            case _:
                text_colour += "'#CBCBCB';"

        # Main layout
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Title label
        title_label = QLabel(customer_title)
        title_label.setStyleSheet(
            "font: 30px;" +
            text_colour
        )
        layout.addWidget(title_label, 0, 0)
