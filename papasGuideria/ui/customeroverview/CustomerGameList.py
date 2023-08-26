from PyQt5.QtWidgets import QVBoxLayout, QWidget

from .CustomerGameListEntry import CustomerGameListEntry
from ...data.Customer import Customer
from ...data.Game import Game


class CustomerGameList(QWidget):
    """A widget displaying all games a customer is in and their unlock."""

    def __init__(self, customer: Customer, parent=None):
        super().__init__(parent)

        # Main layout
        layout = QVBoxLayout(self)

        # Set up game entries
        for game in Game.get_game_dict().values():
            game_entry = CustomerGameListEntry(customer, game)
            layout.addWidget(game_entry)
