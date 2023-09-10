from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QScrollArea, QFrame, QSizePolicy, QWidget

from .CustomerGameList import CustomerGameList
from ..generic.CustomImageLabel import CustomImageLabel
from papasGuideria.data.Customer import Customer
from ..generic.CustomerNameHeader import CustomerNameHeader


class CustomerOverviewScreen(QWidget):
    """Screen showing an overview of a customer."""

    def __init__(self, customer: Customer, parent=None):
        super().__init__(parent)

        # Main layout
        layout = QGridLayout(self)

        # Customer portrait
        portrait_label = CustomImageLabel(customer.main_portrait)
        portrait_label.resize_image(150, 240)
        layout.addWidget(portrait_label, 0, 0, -1, 1, Qt.AlignTop)

        # Customer header
        customer_header = CustomerNameHeader(customer)
        layout.addWidget(customer_header, 0, 1, 1, -1, Qt.AlignTop)

        # Game list scroll area
        game_scroll_area = QScrollArea()
        game_scroll_area.setWidgetResizable(True)
        game_scroll_area.setFrameShape(QFrame.NoFrame)
        layout.addWidget(game_scroll_area, 1, 1, -1, -1)

        # Game list widget
        game_list = CustomerGameList(customer)
        game_list.setStyleSheet(
            "margin: 0px 10px 0px 10px;"
        )
        game_scroll_area.setWidget(game_list)
        game_scroll_area.setFixedWidth(game_list.sizeHint().width() + 25)
