from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QSizePolicy

from .CustomerInfoWidget import CustomerInfoWidget
from ..generic.AbstractScreen import AbstractScreen
from ..generic.CustomImageLabel import CustomImageLabel
from ..generic.CustomerNameHeader import CustomerNameHeader
from ...data.Customer import Customer
from ...data.Game import Game


class CustomerInfoScreen(AbstractScreen):
    """A screen showing info about the customer from a particular game."""

    def __init__(self, customer: Customer, game: Game, parent=None):
        super().__init__(parent, customer, game)

    def create_ui(self, customer: Customer, game: Game):
        # Main layout
        layout = QGridLayout(self)

        # Customer game portrait
        game_portrait = CustomImageLabel(customer.game_info[game.name]["Portrait"])
        game_portrait.resize_by_scale_factor(3)
        layout.addWidget(game_portrait, 0, 0)

        # Customer header
        customer_header = CustomerNameHeader(customer.name, customer.game_info[game.name]["Title"])
        layout.addWidget(customer_header, 0, 1, 1, -1, Qt.AlignTop | Qt.AlignHCenter)

        # Customer info section
        customer_info = CustomerInfoWidget(customer, game)
        customer_info.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        customer_info.setStyleSheet(
            "margin: 10px 30px 0px 30px;"
        )
        layout.addWidget(customer_info, 1, 1, Qt.AlignTop)

        # Order ticket image
        order_ticket = CustomImageLabel(customer.game_info[game.name]["Order"])
        order_ticket.resize_by_scale_factor(1.1)
        layout.addWidget(order_ticket, 1, 0, Qt.AlignHCenter)
