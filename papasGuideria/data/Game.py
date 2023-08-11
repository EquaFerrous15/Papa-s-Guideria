from __future__ import annotations
from papasGuideria.database.DatabaseInterface import DatabaseInterface


class Game:
    """Class containing data pertaining to a gameria."""
    _GAME_DICT: dict[str, Game] = {}

    def __init__(self, game_name: str):
        self.name = game_name

    @classmethod
    def get_game_dict(cls):
        """Returns the game dictionary."""
        # Sets up the dictionary if not already done so.
        if len(Game._GAME_DICT) == 0:
            Game._setup_game_dict()

        return Game._GAME_DICT

    @classmethod
    def _setup_game_dict(cls):
        """Sets up the game dictionary with values from the database."""
        Game._GAME_DICT = {}

        db_cursor = DatabaseInterface.get_cursor()
        db_cursor.execute("SELECT * FROM games")
        game_rows = db_cursor.fetchall()

        for row in game_rows:
            game_name = row["name"]
            new_game = Game(game_name)
            Game._GAME_DICT[game_name] = new_game
