from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QHBoxLayout, QSpacerItem, QWidget

from .CustomerInfoWidget import CustomerInfoWidget
from ..generic.CustomImageLabel import CustomImageLabel
from ..generic.CustomerNameHeader import CustomerNameHeader
from ...data.Customer import Customer
from ...data.Game import Game


class CustomerInfoScreen(QWidget):
    """A screen showing info about the customer from a particular game."""

    def __init__(self, customer: Customer, game: Game, parent=None):
        super().__init__(parent)

        # Main layout
        layout = QHBoxLayout(self)

        # Left layout
        left_layout = QVBoxLayout()
        layout.addLayout(left_layout)

        # Customer game portrait
        game_portrait = CustomImageLabel(customer.game_info[game.name]["Portrait"])
        game_portrait.resize_by_scale_factor(3)
        left_layout.addWidget(game_portrait)

        # Order ticket image
        order_ticket = CustomImageLabel(customer.game_info[game.name]["Order"])
        order_ticket.resize_by_scale_factor(1.1)
        left_layout.addWidget(order_ticket, alignment=Qt.AlignHCenter)

        # Right layout
        right_layout = QVBoxLayout()
        layout.addLayout(right_layout)

        # Customer header
        customer_header = CustomerNameHeader(customer.name, customer.game_info[game.name]["Title"])
        customer_header.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        right_layout.addWidget(customer_header)

        # Game icon
        game_icon = CustomImageLabel(game.icon)
        game_icon.setStyleSheet(
            "margin: 15px 0px 0px 0px;"
        )
        right_layout.addWidget(game_icon, alignment=Qt.AlignCenter)

        # Customer info section
        customer_info = CustomerInfoWidget(customer, game)
        customer_info.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        customer_info.setStyleSheet(
            "margin: 10px 30px 0px 30px;"
        )
        right_layout.addWidget(customer_info)

        # Right spacer moves everything up
        right_layout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
