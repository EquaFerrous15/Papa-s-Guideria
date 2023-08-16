from __future__ import annotations
import os
from papasGuideria.database.DatabaseInterface import DatabaseInterface


class Customer:
    """Class containing data pertaining to a customer."""
    _CUSTOMER_DICT: dict[str, Customer] = {}
    INFO_DONT_DISPLAY = ["Title", "Portrait", "Order"]       # Which game info bits to not display in the info widget.

    def __init__(self, customer_name: str):
        self.name = customer_name
        self.main_portrait = ""
        self.main_title = ""
        self.game_info: dict[str, dict[str, str]] = {}

        # Set up main picture
        self.normalised_name = self.name.lower().replace(" ", "_")
        portrait_path = f"papasGuideria/resources/images/customer_portraits/{self.normalised_name}.png"
        if os.path.exists(portrait_path):
            self.main_portrait = portrait_path
        else:
            self.main_portrait = "papasGuideria/resources/images/customer_portraits/default.png"

        # Set up game info dictionary
        db_cursor = DatabaseInterface.get_cursor()
        db_cursor.execute("SELECT * FROM customer_game_info WHERE customer=?", (self.name,))
        game_data_rows = db_cursor.fetchall()
        for row in game_data_rows:
            # Get general info
            game_specific_info: dict[str, str] = {
                "Title": row["title"],
                "Unlock": row["unlock"],
                "Favourite Holiday": row["favourite_holiday"],
                "Group": row["customer_group"]
            }

            # Find portrait images
            game_normalised_name = row["game"].lower().replace(" ", "_")
            game_portrait_path = ("papaGuideria/resources/images/customer_portraits/" +
                                  f"{game_normalised_name}/{self.normalised_name}.png")
            if os.path.exists(game_portrait_path):
                game_specific_info["Portrait"] = game_portrait_path
            else:
                game_specific_info["Portrait"] = "papasGuideria/resources/images/customer_portraits/default.png"

            # Find order ticket images
            order_ticket_path = ("papasGuideria/resources/images/order_tickets/" +
                                 f"{game_normalised_name}/{self.normalised_name}.png")
            if os.path.exists(order_ticket_path):
                game_specific_info["Order"] = order_ticket_path
            else:
                order_default_path = ("papasGuideria/resources/images/order_tickets/" +
                                      f"{game_normalised_name}/default.png")
                if os.path.exists(order_default_path):
                    game_specific_info["Order"] = order_default_path
                else:
                    game_specific_info["Order"] = "papasGuideria/resources/images/order_tickets/default.png"

            # Finalise the info dictionary
            self.game_info[row["game"]] = game_specific_info

    @classmethod
    def get_customer_dict(cls):
        """Returns the customer dictionary."""
        # Sets up the dictionary if not already done so.
        if len(Customer._CUSTOMER_DICT) == 0:
            Customer._setup_customer_dict()

        return Customer._CUSTOMER_DICT

    @classmethod
    def _setup_customer_dict(cls) -> None:
        """Sets up the customer dictionary with values from the database."""
        Customer._CUSTOMER_DICT = {}

        db_cursor = DatabaseInterface.get_cursor()
        db_cursor.execute("SELECT * FROM customers")
        customer_rows = db_cursor.fetchall()

        for row in customer_rows:
            customer_name = row["name"]
            new_customer = Customer(customer_name)
            Customer._CUSTOMER_DICT[customer_name] = new_customer

