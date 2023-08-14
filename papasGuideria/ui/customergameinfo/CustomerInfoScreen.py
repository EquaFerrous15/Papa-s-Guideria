from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout

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
        layout.addWidget(game_portrait, 0, 0, -1, 1)

        # Customer header
        customer_header = CustomerNameHeader(customer.name, customer.game_info[game.name]["Title"])
        layout.addWidget(customer_header, 0, 1, 1, -1, Qt.AlignTop)
