from PyQt5.QtWidgets import QGridLayout, QScrollArea, QWidget, QVBoxLayout, QSizePolicy
from ..generic.AbstractScreen import AbstractScreen
from .CustomerListEntry import CustomerListEntry
from papasGuideria.data.Customer import Customer


class CustomerListScreen(AbstractScreen):
    """Screen showing a list of all customers."""

    def create_ui(self):
        # Main layout
        layout = QGridLayout(self)

        # Scrolling area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area, 0, 0)

        # Customer list widget
        customer_list_widget = QWidget()
        customer_list_widget.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        scroll_area.setWidget(customer_list_widget)

        # Customer list layout
        customer_list_layout = QVBoxLayout(customer_list_widget)

        # Customer entries
        for customer in Customer.get_customer_dict().values():
            new_entry = CustomerListEntry(customer)
            new_entry.setStyleSheet(
                "margin: 5px 0px 5px 0px;"
            )
            customer_list_layout.addWidget(new_entry)

        # Ensure the scroll area is big enough without having a horizontal scroll bar
        scroll_area.setMinimumSize(int(customer_list_widget.sizeHint().width() + 25), 500)

