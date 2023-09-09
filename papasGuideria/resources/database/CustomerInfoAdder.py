import sqlite3

from papasGuideria.database.DatabaseInterface import DatabaseInterface


def create_customer_info(customer_name: str, game_name: str, title: str = None, unlock: str = None):
    """Creates a new record in customer_game_info for the specified customer and game."""
    db_connection = DatabaseInterface.create_connection("../GuideDatabase.db")
    with db_connection:
        db_cursor = db_connection.cursor()

        sql = "INSERT INTO customer_game_info(customer, game, title, unlock) VALUES(?,?,?,?)"
        values = (customer_name, game_name, title, unlock)

        try:
            db_cursor.execute(sql, values)
            db_connection.commit()
            print(values)
        except sqlite3.IntegrityError as error:
            print(f"{error.sqlite_errorname} - {customer_name}")
            if "primarykey" not in error.sqlite_errorname.lower():
                raise error


if __name__ == "__main__":
    with open("customer_info.txt", "r") as file:
        game_line = file.readline()
        game_line = game_line.rstrip("\n")
        game_name = game_line.lstrip("game = ")

        for line in file.readlines():
            if line[0] == "#":
                continue
            line = line.rstrip("\n")
            line = line.rstrip(")")

            customer_name, unlock = line.split(" (")

            if "Starter" in unlock:
                unlock = "Start"
            elif "After" in unlock:
                unlock = "Tutorial"
            elif "Rank" in unlock:
                unlock = unlock.lstrip("Rank ")

            create_customer_info(customer_name, game_name, unlock=unlock)

    print("Done")
