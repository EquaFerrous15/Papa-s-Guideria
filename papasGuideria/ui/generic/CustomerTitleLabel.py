from PyQt5.QtWidgets import QLabel, QGridLayout

from .AbstractCustomWidget import AbstractCustomWidget


class CustomerTitleLabel(QLabel):
    """A label to display a customer's title with special formatting depending on the title."""

    def __init__(self, customer_title: str, parent=None):
        super().__init__(parent)

        if customer_title is None:
            customer_title = "Normal Customer"
        customer_title = customer_title.title()

        # Choose text colour
        match customer_title:
            case "Food Critic":
                text_colour = "#0167CD"
            case "Closer" | "Ex-Closer":
                text_colour = "#CD0101"
            case "Local":
                text_colour = "#FEC418"
            case _:
                text_colour = "#CBCBCB"
        self._text_style = f"color: '{text_colour}';"

        # Title label
        self.setText(customer_title)
        self.setStyleSheet(
            self._text_style
        )

    def setStyleSheet(self, p_str):
        style_string = self._text_style + p_str
        super().setStyleSheet(style_string)

