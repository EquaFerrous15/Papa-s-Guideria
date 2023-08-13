from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy, QGridLayout
from ..generic.AbstractCustomWidget import AbstractCustomWidget
from ..generic.CustomImageLabel import CustomImageLabel
from papasGuideria.data.Customer import Customer


class CustomerListEntry(AbstractCustomWidget):
    """Entry of a customer to be displayed in the customer list."""

    def __init__(self, customer: Customer, parent=None):
        super().__init__(parent, customer)
        self._customer = customer

    def create_ui(self, customer: Customer):
        self.setCursor(Qt.PointingHandCursor)

        # Main layout
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Main frame
        frame = QFrame()
        frame.setObjectName("MainFrame")
        frame.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        frame.setStyleSheet(
            "*{background-color: '#dedede';}" +
            f"QFrame#{frame.objectName()}" +
            "{border-radius: 20px;" +
            "min-width: 400px;}"
        )
        layout.addWidget(frame)

        # Frame layout
        frame_layout = QHBoxLayout(frame)

        # Customer portrait
        portrait = CustomImageLabel(customer.main_portrait)
        portrait.resize_by_scale_factor(1.5)
        portrait.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        portrait.setStyleSheet(
            "border: 2px solid '#505050';" +
            "margin: 2px;"
        )
        frame_layout.addWidget(portrait)

        # Customer name
        name_label = QLabel(customer.name)
        name_label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        name_label.setStyleSheet(
            "color: '#505050';" +
            "font: 30px Helvetica;" +
            "margin: 0px 0px 0px 10px;"
        )
        frame_layout.addWidget(name_label)

        # Arrow icon
        arrow_image = CustomImageLabel("papasGuideria/resources/images/general/forward_arrow.png")
        arrow_image.setStyleSheet(
            "margin: 0px 10px 0px 10px;"
        )
        frame_layout.addWidget(arrow_image)

    # Move to the overview screen for the customer
    def mousePressEvent(self, event: QMouseEvent):
        super().mousePressEvent(event)
        print(f"Show overview screen {self._customer.name}")

