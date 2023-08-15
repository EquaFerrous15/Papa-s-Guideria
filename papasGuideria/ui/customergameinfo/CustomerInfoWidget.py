from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QLabel, QSizePolicy

from ..generic.AbstractCustomWidget import AbstractCustomWidget
from ...data.Customer import Customer
from ...data.Game import Game


class CustomerInfoWidget(AbstractCustomWidget):
    """Widget displaying all game information for a customer."""

    def __init__(self, customer: Customer, game: Game, parent=None):
        super().__init__(parent, customer, game)

    def create_ui(self, customer: Customer, game: Game):
        # Main layout
        layout = QGridLayout(self)
        layout.setHorizontalSpacing(50)

        # Set up info grid
        info_dict = customer.game_info[game.name]
        dont_display_list = Customer.INFO_DONT_DISPLAY
        grid_row = 0
        for item in info_dict.items():
            # Don't display the info items specified
            if item[0] in dont_display_list:
                continue
            # If info is empty, don't display
            if item[1] is None:
                continue

            # Info item name
            info_name_label = QLabel(item[0])
            info_name_label.setStyleSheet(
                "color: '#505050';" +
                "font: 25px;"
            )
            layout.addWidget(info_name_label, grid_row, 0)

            # Actual info text
            info_label = QLabel(item[1])
            info_label.setStyleSheet(
                "color: '#7a7a7a';" +
                "font: 25px;"
            )
            layout.addWidget(info_label, grid_row, 1, Qt.AlignRight)

            grid_row += 1




