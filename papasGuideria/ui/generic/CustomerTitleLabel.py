from PyQt5.QtWidgets import QLabel

from papasGuideria.data.Customer import Customer
from papasGuideria.data.Game import Game
from papasGuideria.resources.ResourceManager import ResourceManager


class CustomerTitleLabel(QLabel):
    """A label to display a customer's title with special formatting depending on the title."""

    def __init__(self, customer: Customer, game: Game = None, parent=None):
        super().__init__(parent)

        if game is None:
            # If the title is being used for an overview screen.
            customer_title = customer.overall_title
        else:
            # If the title is being used for a game info screen.
            try:
                customer_title = customer.game_info[game.name]["Title"]
            except KeyError:
                customer_title = ""
            # Only display normal customer on game info screens.
            if customer_title is None:
                customer_title = "Normal Customer"

        customer_title = customer_title.title()
        title_lower = customer_title.lower()

        # Choose text colour
        # Ordered so "local closer" prioritises 'closer' colouring over 'local' colouring
        if "food critic" in title_lower:
            text_colour = ResourceManager.get_colour("jojo_blue")
        elif "closer" in title_lower:
            text_colour = ResourceManager.get_colour("closer_red")
        elif "local" in title_lower:
            text_colour = ResourceManager.get_colour("local")
        elif "worker" in title_lower:
            if game is not None:
                text_colour = game.colour
            else:
                # If used in an overview screen, we don't have 'game', so must manually find the game using the title.
                game_name = customer_title.rstrip(" Worker")
                text_colour = Game.get_game_dict()[game_name].colour
        else:
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

