from ..generic.AbstractScreen import AbstractScreen
from ...data.Customer import Customer
from ...data.Game import Game


class CustomerInfoScreen(AbstractScreen):
    """A screen showing info about the customer from a particular game."""

    def __init__(self, customer: Customer, game: Game, parent=None):
        super().__init__(parent, customer, game)

    def create_ui(self, customer: Customer, game: Game):
        pass
