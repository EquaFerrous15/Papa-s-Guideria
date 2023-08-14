from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QGridLayout, QSizePolicy, QLabel, QHBoxLayout

from .AbstractCustomWidget import AbstractCustomWidget
from .CustomerTitleLabel import CustomerTitleLabel


class CustomerNameHeader(AbstractCustomWidget):
    """A header bar displaying a customer's name and title."""

    def __init__(self, name: str, title: str, parent=None):
        super().__init__(parent, name, title)

    def create_ui(self, customer_name: str, customer_title: str):
        # Layout
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Main frame
        frame = QFrame()
        frame.setObjectName("MainFrame")
        frame.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        frame.setStyleSheet(
            "*{background-color: '#dedede';}"
            f"QFrame#{frame.objectName()}" +
            "{border-radius: 30px;" +
            "margin: 0px 0px 0px 5px;" +
            "min-width: 400px;}"
        )
        layout.addWidget(frame)

        # Frame layout
        frame_layout = QHBoxLayout(frame)

        # Name label
        name_label = QLabel(customer_name)
        name_label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        name_label.setStyleSheet(
            "padding: 5px 50px 5px 10px;" +
            "color: '#505050';" +
            "font: 36px;"
        )
        frame_layout.addWidget(name_label)

        # Title label
        title_label = CustomerTitleLabel(customer_title)
        title_label.setStyleSheet(
            "padding: 0px 10px 0px 0px;" +
            "font: 30px;"
        )
        frame_layout.addWidget(title_label)
