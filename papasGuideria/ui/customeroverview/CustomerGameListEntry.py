from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QGridLayout, QFrame, QLabel, QHBoxLayout, QSizePolicy

from ..MainWindow import MainWindow
from ..customergameinfo.CustomerInfoScreen import CustomerInfoScreen
from ..generic.CustomImageLabel import CustomImageLabel
from ...data.Customer import Customer
from ...data.Game import Game
from ...resources.ResourceManager import ResourceManager


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

        # ---- Unlock text label ----
        # Check to see if customer is absent from the game
        unlock_text_colour = ResourceManager.get_colour("text_dark_grey")

        try:
            unlock_text = customer.game_info[game.name]["Unlock"]
        except KeyError:
            # If customer doesn't appear in a game, make the button unavailable
            self._clickable = False
            game_icon.greyscale(True)
            unlock_text = "Absent"
            unlock_text_colour = ResourceManager.get_colour("text_light_grey")

        # If the customer is special for that game, display that instead of their unlock
        try:
            customer_title = customer.game_info[game.name]["Title"].lower()
        except (KeyError, AttributeError):
            customer_title = ""

        if customer_title is None:
            customer_title = ""

        if "closer" in customer_title:
            unlock_text = "Closer"
            unlock_text_colour = ResourceManager.get_colour("closer_red")
        elif "food critic" in customer_title:
            unlock_text = "Food Critic"
            unlock_text_colour = ResourceManager.get_colour("jojo_blue")
        elif "worker" in customer_title:
            unlock_text = "Worker"

        # Unlock label
        unlock_label = QLabel(unlock_text, self)
        unlock_label.setStyleSheet(
            f"font: 25px '{ResourceManager.get_font('body')}';" +
            f"color: '{unlock_text_colour}';" +
            "padding: 0px 10px 0px 0px;"
        )
        frame_layout.addWidget(unlock_label)

        # Terminate here if the customer is absent, so the button isn't clickable
        if not self._clickable:
            return

        # Make click cursor appear
        self.setCursor(Qt.PointingHandCursor)

        # Arrow icon
        arrow_image = CustomImageLabel("general/forward_arrow")
        arrow_image.resize_image(30, 30)
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
