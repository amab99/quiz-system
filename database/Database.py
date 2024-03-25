import os
import sqlite3


class DatabaseSetup:
    """
    DatabaseSetup class responsible for setup the connection to the database,
    and create the database schema from the SQL file to store the admin data and quiz questions.

    Author: Amal Abueshareik
    """

    def __init__(self):
        """
        Initialize the SQLite database and the SQL schema file.
        """
        self.db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils', 'quiz_app.db'))
        self.sql_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils', 'tables.sql'))
        self.conn = None

    def connect_to_db(self):
        """
        Connect to the database and create the schemas in the sql file.

        Raises:
        - RuntimeError: If error occurs when connecting to database
        """
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.create_db_schema()
        except sqlite3.Error as e:
            raise RuntimeError("Error when connecting to database: ", e)

    def close_connection(self):
        """
        Close the database connection.

        Raises:
        - RuntimeError: If closing the database connection failed
        """
        if self.conn:
            self.conn.close()
            self.conn = None
        else:
            raise RuntimeError("Closing database connection failed")

    def create_db_schema(self):
        """
        Read the SQL-commands from the sql file and execute them to
        create the tables in the database.

        Raises:
        - RuntimeError: If error occurs when creating the tables
        """
        try:
            cursor = self.conn.cursor()
            # Read the SQL-commands from the file and execute them
            with open(self.sql_file, 'r') as file:
                sql = file.read()
                cursor.executescript(sql)
            self.conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Error when creating tables: {e}")


