import inspect
import os
import sys
import unittest
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from project_src.database.DatabaseManager import DatabaseManager
from project_src.models.AdminModel import AdminModel


class AdminModelTest(unittest.TestCase):
    """
    Unit tests for the AdminModel class to ensure it handles admin authorization,
    registration, and admin ID retrieval correctly.

    @Author: Asaad Katbeh
    """

    def setUp(self):
        """
        Prepare resources for each test.
        """
        self.db_manager = MagicMock(spec=DatabaseManager)
        self.admin_model = AdminModel(self.db_manager)

    def test_authorize_success(self):
        """
        Test successful authorization where the correct credentials are provided.
        """
        self.db_manager.authorize_login.return_value = 1  # Mock return value for successful login
        result = self.admin_model.authorize('user', 'pass')
        self.assertTrue(result)
        self.assertEqual(self.admin_model.get_admin_id(), 1)

    def test_authorize_failure(self):
        """
        Test failed authorization where incorrect credentials are provided.
        """
        self.db_manager.authorize_login.return_value = -1  # Mock return value for failed login
        result = self.admin_model.authorize('user', 'wrongpass')
        self.assertFalse(result)
        self.assertIsNone(self.admin_model.get_admin_id())

    def test_register_success(self):
        """
        Test successful registration of a new admin.
        """
        self.db_manager.register_admin.return_value = 2  # Mock return value for successful registration
        result = self.admin_model.register('newuser', 'newpass')
        self.assertTrue(result)
        self.assertEqual(self.admin_model.get_admin_id(), 2)

    def test_register_failure(self):
        """
        Test failed registration where the username might already exist.
        """
        self.db_manager.register_admin.return_value = -1  # Mock return value for failed registration
        result = self.admin_model.register('user', 'pass')
        self.assertFalse(result)
        self.assertIsNone(self.admin_model.get_admin_id())

    def test_get_admin_id_not_set(self):
        """
        Test the retrieval of admin ID when no admin is logged in or registered.
        """
        # No login or registration attempted; _admin_id should be None
        self.assertIsNone(self.admin_model.get_admin_id())

    def test_method_existence(self):
        """
        Tests that all expected methods exist in the AdminModel class.
        """
        expected_methods = ['authorize', 'register', 'get_admin_id']
        actual_methods = [method for method in dir(self.admin_model) if
                          callable(getattr(self.admin_model, method)) and not method.startswith('__')]

        for method in expected_methods:
            self.assertIn(method, actual_methods, f"Expected method {method} not found in AdminModel class.")

    def test_private_method_naming(self):
        """
        Verifies that all intended private methods in the AdminModel class start with an underscore, adhering to the
        naming convention for private methods.
        """
        # Assuming '_admin_id' should be accessed via a getter and is therefore treated as private
        private_attributes = ['_admin_id']
        for attr in private_attributes:
            self.assertTrue(attr.startswith('_'), f"Attribute {attr} should be private (start with an underscore).")

    def test_public_method_naming(self):
        """
        Verifies that all intended public methods in the AdminModel class do not start with an underscore,
        following the naming convention for public methods.
        """
        public_methods = ['authorize', 'register', 'get_admin_id']
        for method in public_methods:
            self.assertFalse(method.startswith('_'),
                             f"Method {method} should be public (not start with an underscore).")

    def test_method_signatures(self):
        """
        Verifies that the method signatures for key methods in the AdminModel class match the expected parameter
        names, ensuring consistency and clarity in method definitions.
        """
        signatures = {'authorize': ['username', 'password'], 'register': ['username', 'password'], 'get_admin_id': []}

        for method, expected_params in signatures.items():
            with self.subTest(method=method):
                actual_params = list(inspect.signature(getattr(self.admin_model, method)).parameters.keys())
                self.assertEqual(expected_params, actual_params, f"Signature for method {method} is incorrect.")

    def tearDown(self):
        """
        Clean up resources after each test.
        """
        pass


if __name__ == '__main__':
    unittest.main()
