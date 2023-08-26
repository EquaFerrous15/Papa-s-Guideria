from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy, QGridLayout
from ..generic.CustomImageLabel import CustomImageLabel
from papasGuideria.data.Customer import Customer
from ..MainWindow import MainWindow
from ..customeroverview.CustomerOverviewScreen import CustomerOverviewScreen


class CustomerListEntry(QFrame):
    """Entry of a customer to be displayed in the customer list."""

    def __init__(self, customer: Customer, parent=None):
        super().__init__(parent)
        self._customer = customer

        self.setCursor(Qt.PointingHandCursor)

        # Main frame
        self.setObjectName("MainFrame")
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        self.setStyleSheet(
            "*{background-color: '#dedede';}" +
            f"QFrame#{self.objectName()}" +
            "{border-radius: 20px;" +
            "min-width: 400px;}"
        )

        # Frame layout
        frame_layout = QHBoxLayout(self)

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
        arrow_image = CustomImageLabel("general/forward_arrow")
        arrow_image.setStyleSheet(
            "margin: 0px 10px 0px 10px;"
        )
        frame_layout.addWidget(arrow_image)

    # Move to the overview screen for the customer
    def mousePressEvent(self, event: QMouseEvent):
        super().mousePressEvent(event)

        main_window: MainWindow = self.window()
        main_window.show_new_screen(CustomerOverviewScreen(self._customer))

