import os
import sqlite3
import sys
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import mock_open

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from project_src.database.Database import DatabaseSetup


class TestDatabase(unittest.TestCase):
    """
    Class that contains unit tests for the DatabaseSetup class to ensure database connection,
    and creation of schemas functionality.

    Author: Amal Abueshareik
    """

    def tearDown(self):
        """ Stop the patches after each test. """
        patch.stopall()

    @patch('project_src.database.Database.DatabaseSetup.connect_to_db')
    def test_successful_connection(self, mock_connect: MagicMock):
        """
        Test method to ensure the database connection.

        Parameters:
        - mock_connect (MagicMock): MagicMock object to mock the database connection method

        Raises:
        - AssertionError: If error when connecting to the database
        """
        db = DatabaseSetup()
        db.connect_to_db()
        mock_connect.assert_called_once()
        patch.stopall()

    @patch('project_src.database.Database.DatabaseSetup.connect_to_db')
    def test_failed_connection(self, mock_connect: MagicMock):
        """
        Ensure proper handling of a failed database connection.

        Parameters:
        - mack_connect (MagickMock): MagicMock object to mack the database connection method

        Raises:
        - sqlite3.Error: If the database connection fails.
        """
        mock_connect.side_effect = sqlite3.Error("Error when connecting to database")

        db = DatabaseSetup()

        # Ensure that connect_to_db() raises sqlite3.Error
        with self.assertRaises(sqlite3.Error) as context:
            db.connect_to_db()

        self.assertEqual(str(context.exception), "Error when connecting to database")
        mock_connect.assert_called_once()

    @patch('project_src.database.Database.DatabaseSetup.connect_to_db')
    @patch('project_src.database.Database.DatabaseSetup.close_connection')
    def test_successful_close_connection(self, mock_connect: MagicMock, mock_close: MagicMock):
        """
        Test method to ensure closing the the database connection.

        Parameters:
        - mack_connect (MagickMock): MagicMock object to mack the database connection method
        - mock_close (MagickMock): MagicMock object to mack the close connection method

        Raises:
        - AssertionError: If the database connection is not successfully closed.
        """
        db = DatabaseSetup()
        db.connect_to_db()
        db.close_connection()
        # Assert that the connect method was called
        mock_connect.assert_called_once()
        # Assert that the close connection method was called
        mock_close.assert_called_once()

    @patch('project_src.database.Database.DatabaseSetup.connect_to_db')
    @patch('project_src.database.Database.DatabaseSetup.close_connection')
    def test_failed_close_connection(self, mock_close: MagicMock, mock_connect: MagicMock):
        """
        Ensure proper handling of a failed database close connection.

        Parameters:
        - mock_close (MagickMock): MagicMock object to mock the close connection method
        - mack_connect (MagickMock): MagicMock object to mock the database connection method

        Raises:
        - AssertionError: If the database connection fails
        """
        mock_connect.side_effect = RuntimeError("Closing database connection failed")

        db = DatabaseSetup()
        # Ensure that connect_to_db() raises RuntimeError
        with self.assertRaises(RuntimeError):
            db.connect_to_db()

        mock_connect.assert_called_once()
        mock_close.assert_not_called()

    @patch('builtins.open', new_callable=mock_open, read_data='tables')
    def test_successful_schema_creation(self, mock_open: MagicMock):
        """
        Test successful creation of the database schema.

        Parameters:
        - mock_open (MagicMock): A MagicMock object to mock the built-in open function.

        Raises:
        - AssertionError: If the schema creation fails.
        """
        db = DatabaseSetup()
        db.conn = MagicMock()
        db.create_db_schema()
        db.conn.cursor().executescript.assert_called_once_with('tables')
        mock_open.assert_called_once_with(db.sql_file, 'r')

    @patch('builtins.open', side_effect=RuntimeError("Failed to open schema file"))
    def test_failed_schema_creation(self, mock_open: MagicMock):
        """
        Ensure proper handling of a failed schema creation.

        Parameters:
            mock_open (MagicMock): A MagicMock object to mock the built-in open function.

        Raises:
            Exception: If opening schema file failed.
        """
        db = DatabaseSetup()
        db.conn = MagicMock()

        with self.assertRaises(RuntimeError) as context:
            db.create_db_schema()

        self.assertEqual(str(context.exception), "Failed to open schema file")
        mock_open.assert_called_once_with(db.sql_file, 'r')


if __name__ == '__main__':
    unittest.main()
