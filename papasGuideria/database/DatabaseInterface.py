from __future__ import annotations
import sqlite3


class DatabaseInterface:
    """An interface with GuideDatabase.db."""
    _DATABASE_PATH = "papasGuideria/resources/GuideDatabase.db"       # Path from main.py
    _INSTANCE: DatabaseInterface = None

    def __init__(self):
        self.connection: sqlite3.Connection | None = None
        try:
            self.connection = sqlite3.connect(DatabaseInterface._DATABASE_PATH)
            self.connection.row_factory = sqlite3.Row
        except sqlite3.Error as e:
            raise Exception(str(e))

        self.cursor: sqlite3.Cursor | None = None
        if self.connection is not None:
            self.cursor = self.connection.cursor()

    @classmethod
    def get_cursor(cls) -> sqlite3.Cursor:
        """Returns the cursor for the database connection."""
        if DatabaseInterface._INSTANCE is None:
            DatabaseInterface._INSTANCE = DatabaseInterface()

        return DatabaseInterface._INSTANCE.cursor

    @classmethod
    def create_connection(cls, custom_path: str = None) -> sqlite3.Connection:
        """Creates a new connection to the database."""
        if custom_path is None:
            path = cls._DATABASE_PATH
        else:
            path = custom_path

        try:
            connection = sqlite3.connect(path)
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA foreign_keys = 1")   # Turns foreign key constraints on
            return connection
        except sqlite3.Error as e:
            raise Exception(str(e))

    @classmethod
    def close_connection(cls) -> None:
        """Closes the database connection."""
        if DatabaseInterface._INSTANCE is None:
            return

        DatabaseInterface._INSTANCE.connection.close()
