from PyQt5.QtWidgets import QLabel, QGridLayout

from papasGuideria.resources.ResourceManager import ResourceManager


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
                text_colour = ResourceManager.get_colour("jojo_blue")
            case "Closer" | "Ex-Closer":
                text_colour = ResourceManager.get_colour("closer_red")
            case "Local":
                text_colour = ResourceManager.get_colour("local")
            case _:
                text_colour = ResourceManager.get_colour("text_light_grey")
        self._text_style = f"color: '{text_colour}';"

        # Title label
        self.setText(customer_title)
        self.setStyleSheet(
            self._text_style
        )

    def setStyleSheet(self, p_str):
        style_string = self._text_style + p_str
        super().setStyleSheet(style_string)

