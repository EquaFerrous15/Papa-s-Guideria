from __future__ import annotations
import os
from papasGuideria.database.DatabaseInterface import DatabaseInterface
from papasGuideria.resources.ResourceManager import ResourceManager


class Customer:
    """Class containing data pertaining to a customer."""
    _CUSTOMER_DICT: dict[str, Customer] = {}
    INFO_DONT_DISPLAY = ["Title", "Portrait", "Order"]       # Which game info bits to not display in the info widget.

    def __init__(self, customer_name: str):
        self.name = customer_name
        self.main_portrait = ""
        self.overall_title = ""
        self.game_info: dict[str, dict[str, str]] = {}

        # Set up main picture
        self.normalised_name = self.name.lower().replace(" ", "_")
        portrait_path = f"customer_portraits/{self.normalised_name}"
        if ResourceManager.image_exists(portrait_path):
            self.main_portrait = portrait_path
        else:
            self.main_portrait = "customer_portraits/default"

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

            # Format unlock text
            unlock = game_specific_info["Unlock"]
            # If unlock text is just a number, prefix it with "Rank"
            try:
                int(unlock)
                new_unlock = f"Rank {unlock}"
                game_specific_info["Unlock"] = new_unlock
            except (ValueError, TypeError):
                # Don't do anything if it is not just a number
                pass

            # Find portrait images
            game_normalised_name = row["game"].lower().replace(" ", "_")
            game_portrait_path = f"customer_portraits/{game_normalised_name}/{self.normalised_name}"
            if ResourceManager.image_exists(game_portrait_path):
                game_specific_info["Portrait"] = game_portrait_path
            else:
                game_specific_info["Portrait"] = "customer_portraits/default"

            # Find order ticket images
            order_ticket_path = f"order_tickets/{game_normalised_name}/{self.normalised_name}"
            if ResourceManager.image_exists(order_ticket_path):
                game_specific_info["Order"] = order_ticket_path
            else:
                game_specific_info["Order"] = "order_tickets/default"

            # Finalise the info dictionary
            self.game_info[row["game"]] = game_specific_info

        self.overall_title = self._get_customer_overall_title()

    def _get_customer_overall_title(self):
        """Gets the customer's overall title."""
        overall_title = ""
        for game_name, game_info in self.game_info.items():
            customer_title = game_info["Title"]
            if customer_title is None:
                customer_title = ""

            customer_title = customer_title.lower()
            # If a customer works at a gameria, it takes highest priority.
            if "worker" in customer_title:
                overall_title = f"{game_name} Worker"
                break
            # Jojo
            elif "food critic" in customer_title:
                overall_title = "Food Critic"
                break
            # if a customer is still a closer as of the latest game, their title is "closer", otherwise "ex-closer".
            elif "closer" in customer_title:
                overall_title = "Closer"
            elif (overall_title == "Closer") and ("closer" not in customer_title):
                overall_title = "Ex-closer"

        return overall_title



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

