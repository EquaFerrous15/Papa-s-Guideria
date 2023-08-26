from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QGridLayout, QFrame, QLabel, QHBoxLayout, QSizePolicy

from ..MainWindow import MainWindow
from ..customergameinfo.CustomerInfoScreen import CustomerInfoScreen
from ..generic.CustomImageLabel import CustomImageLabel
from ...data.Customer import Customer
from ...data.Game import Game


class CustomerGameListEntry(QFrame):
    """An entry in the customer game list. Displays the games a customer is in and their unlock."""
    
    def __init__(self, customer: Customer, game: Game, parent=None):
        super().__init__(parent)

        self._clickable = True
        self._customer = customer
        self._game = game

        # Main frame
        self.setObjectName("MainFrame")
        self.setStyleSheet(
            "*{background-color: '#dedede';}" +
            f"QFrame#{self.objectName()}" +
            "{border-radius: 15px;" +
            "min-width: 400px;}"
        )

        # Frame layout
        frame_layout = QHBoxLayout(self)

        # Game icon
        game_icon = CustomImageLabel(game.icon)
        game_icon.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        game_icon.setStyleSheet(
            "padding: 2px 0px 2px 5px;"
        )
        frame_layout.addWidget(game_icon)

        # Check unlock text to see if customer is absent
        try:
            unlock_text = customer.game_info[game.name]["Unlock"]
        except KeyError:
            unlock_text = "Absent"
            self._clickable = False
        # Unlock text label
        unlock_label = QLabel(unlock_text, self)
        unlock_label.setStyleSheet(
            "font: 25px;" +
            "padding: 0px 10px 0px 0px;"
        )
        frame_layout.addWidget(unlock_label)

        # If the customer is absent, do not proceed
        if not self._clickable:
            return

        # Make click cursor appear
        self.setCursor(Qt.PointingHandCursor)

        # Arrow icon
        arrow_image = CustomImageLabel("general/forward_arrow")
        arrow_image.resize_by_scale_factor(0.75)
        arrow_image.setStyleSheet(
            "margin: 0px 10px 0px 10px;"
        )
        frame_layout.addWidget(arrow_image)

    def mousePressEvent(self, event: QMouseEvent):
        super().mousePressEvent(event)

        if not self._clickable:
            return

        main_window: MainWindow = self.window()
        main_window.show_new_screen(CustomerInfoScreen(self._customer, self._game))
