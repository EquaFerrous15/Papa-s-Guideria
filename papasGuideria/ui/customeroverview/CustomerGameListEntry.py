from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QGridLayout, QFrame, QLabel, QHBoxLayout, QSizePolicy

from ..generic.AbstractCustomWidget import AbstractCustomWidget
from ..generic.CustomImageLabel import CustomImageLabel
from ...data.Customer import Customer
from ...data.Game import Game


class CustomerGameListEntry(AbstractCustomWidget):
    """An entry in the customer game list. Displays the games a customer is in and their unlock."""
    
    def __init__(self, customer: Customer, game: Game, parent=None):
        self._clickable = True
        self._customer = customer
        self._game = game
        super().__init__(parent, customer, game)
    
    def create_ui(self, customer: Customer, game: Game):
        # Dummy layout
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Main frame
        frame = QFrame()
        frame.setObjectName("MainFrame")
        frame.setStyleSheet(
            "*{background-color: '#dedede';}" +
            f"QFrame#{frame.objectName()}" +
            "{border-radius: 30px;" +
            "min-width: 300px;}"
        )
        layout.addWidget(frame, 0, 0)

        # Frame layout
        frame_layout = QHBoxLayout(frame)

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
        unlock_label = QLabel(unlock_text, frame)
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
        arrow_image = CustomImageLabel("papasGuideria/resources/images/general/forward_arrow.png")
        arrow_image.resize_by_scale_factor(0.75)
        arrow_image.setStyleSheet(
            "margin: 0px 10px 0px 10px;"
        )
        frame_layout.addWidget(arrow_image)

    def mousePressEvent(self, event: QMouseEvent):
        super().mousePressEvent(event)

        if not self._clickable:
            return
        print(f"Move to info screen - {self._customer.name} {self._game.name}")


