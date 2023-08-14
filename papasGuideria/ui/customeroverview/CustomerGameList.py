from PyQt5.QtWidgets import QVBoxLayout

from .CustomerGameListEntry import CustomerGameListEntry
from ..generic.AbstractCustomWidget import AbstractCustomWidget
from ...data.Customer import Customer
from ...data.Game import Game


class CustomerGameList(AbstractCustomWidget):
    """A widget displaying all games a customer is in and their unlock."""

    def __init__(self, customer: Customer, parent=None):
        super().__init__(parent, customer)

    def create_ui(self, customer: Customer):
        # Main layout
        layout = QVBoxLayout(self)

        # Set up game entries
        for game in Game.get_game_dict().values():
            game_entry = CustomerGameListEntry(customer, game)
            layout.addWidget(game_entry)