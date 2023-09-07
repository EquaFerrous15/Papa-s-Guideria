from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QGridLayout, QSizePolicy, QLabel, QHBoxLayout

from .CustomerTitleLabel import CustomerTitleLabel
from ...resources.ResourceManager import ResourceManager


class CustomerNameHeader(QFrame):
    """A header bar displaying a customer's name and title."""

    def __init__(self, customer_name: str, customer_title: str, parent=None):
        super().__init__(parent)

        bg_colour = ResourceManager.get_colour("bg_dark_grey")
        name_colour = ResourceManager.get_colour("text_dark_grey")
        name_font = ResourceManager.get_font("names")
        title_font = ResourceManager.get_font("body")

        # Main frame
        self.setObjectName("MainFrame")
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        self.setStyleSheet(
            f"*{{background-color: '{bg_colour}';}}"
            f"QFrame#{self.objectName()}" +
            "{border-radius: 30px;" +
            "min-width: 400px;}"
        )

        # Frame layout
        frame_layout = QHBoxLayout(self)

        # Name label
        name_label = QLabel(customer_name)
        name_label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        name_label.setStyleSheet(
            "margin: 0px 50px 0px 10px;" +
            f"color: '{name_colour}';" +
            f"font: 40px '{name_font}';"
        )
        frame_layout.addWidget(name_label)

        # Title label
        title_label = CustomerTitleLabel(customer_title)
        title_label.setStyleSheet(
            "margin: 0px 10px 0px 0px;" +
            f"font: 30px '{title_font}';"
        )
        frame_layout.addWidget(title_label)
