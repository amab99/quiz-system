import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from project_src.database.DatabaseManager import DatabaseManager


class AdminModel:
    """
    AdminModel class provides functionalities to manage admin credentials with
    operations such as authorization and registration by interacting with the
    DatabaseManager.

    Author: Asaad Katbeh
    """

    def __init__(self, db_manager: DatabaseManager):
        """
        Initializes the AdminModel with a specific DatabaseManager.

        Parameters:
            db_manager (DatabaseManager): The database manager instance to manage database interactions.
        """
        self.db_manager = db_manager
        self._admin_id = None

    def authorize(self, username: str, password: str) -> bool:
        """
        Attempts to authorize an admin using provided credentials. If successful, stores the admin's ID.

        Parameters:
            username (str): The admin's username.
            password (str): The admin's password.

        Returns:
            bool: True if authorization is successful and admin ID is stored, False otherwise.
        """
        admin_id = self.db_manager.authorize_login(username, password)
        if admin_id > 0:
            self._admin_id = admin_id
            return True
        else:
            return False

    def register(self, username: str, password: str) -> bool:
        """
        Registers a new admin with the given username and password. If successful, stores the new admin's ID.

        Parameters:
            username (str): Username for the new admin.
            password (str): Password for the new admin.

        Returns:
            bool: True if registration is successful and admin ID is stored, False otherwise.
        """
        result = self.db_manager.register_admin(username, password)
        if result > 0:
            self._admin_id = result
            return True
        else:
            return False

    def get_admin_id(self) -> int:
        """
        Safely retrieves the stored admin ID.

        Returns:
            int: The admin ID if an admin is logged-in or registered, None otherwise.
        """
        return self._admin_id