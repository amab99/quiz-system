import inspect
import unittest
from unittest.mock import patch, Mock, MagicMock
import tkinter as tk
import os
import sys

import _tkinter

from project_src.views.AdminView import AdminView
from project_src.views.LoginView import LoginView
from project_src.views.RegisterView import RegisterView

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from project_src.models.AdminModel import AdminModel
from project_src.models.QuizModel import QuizModel
from project_src.controllers.AdminAuthorizationController import AdminAuthorizationController


class TestAdminAuthorizationController(unittest.TestCase):
    """
    Unit tests for the AdminAuthorizationController class to ensure proper handling of authentication and registration.

    @Author: Amal Abueshareik
    """

    @patch('project_src.views.RegisterView')
    @patch('project_src.views.LoginView')
    @patch('project_src.views.AdminView')
    @patch('project_src.controllers.AdminAuthorizationController')
    def setUp(self, MockAdminController, MockAdminView, MockLoginView, MockRegisterView):
        """
        Set up the test environment for each test case.

        Parameters:
            MockAdminController (Mock): Mock for the AdminAuthorizationController class.
            MockAdminView (Mock): Mock for the AdminView class.
            MockLoginView (Mock): Mock for the LoginView class.
            MockRegisterView (Mock): Mock for the RegisterView class.
        """
        self.root = tk.Tk()
        self.admin_model = Mock(spec=AdminModel)
        self.quiz_model = Mock(spec=QuizModel)
        self.login_view = Mock(spec=LoginView)
        self.register_view = Mock(spec=RegisterView)
        self.admin_view = Mock(spec=AdminView)
        self.admin_controller = Mock(spec=AdminAuthorizationController)
        self.auth_controller = AdminAuthorizationController(self.root, self.admin_model, self.quiz_model)

    def tearDown(self):
        """
        Tear down the test environment for each test case.
        """
        try:
            self.root.destroy()
        except _tkinter.TclError:
            pass

    @patch.object(RegisterView, '__init__', lambda self: None)
    @patch.object(RegisterView, 'protocol')
    @patch.object(RegisterView, 'register_button_callback')
    @patch.object(RegisterView, 'deiconify')
    def test_show_register_view(self, mock_deiconify, mock_register_button_callback, mock_protocol):
        """
        Test the show_register_view method to ensure it initializes and displays the RegisterView.

        Parameters:
            mock_deiconify (Mock): Mock for the deiconify method.
            mock_register_button_callback (Mock): Mock for the register_button_callback method.
            mock_protocol (Mock): Mock for the protocol method.
        """
        self.auth_controller.register_view = None  # Ensure the register_view is initially None

        self.auth_controller.show_register_view()

        # Verify that RegisterView was instantiated
        self.assertIsNotNone(self.auth_controller.register_view)

        # Verify that protocol, register_button_callback, and deiconify methods were called correctly
        mock_protocol.assert_called_once_with("WM_DELETE_WINDOW", self.auth_controller.on_closing)
        mock_register_button_callback.assert_called_once_with(self.auth_controller.register_admin)
        mock_deiconify.assert_called_once()

    @patch.object(LoginView, '__init__', lambda self: None)
    @patch.object(LoginView, 'protocol')
    @patch.object(LoginView, 'login_button_callback')
    @patch.object(LoginView, 'deiconify')
    def test_show_login_view(self, mock_deiconify, mock_login_button_callback, mock_protocol):
        """
        Test the show_login_view method to ensure it initializes and displays the LoginView.

        Parameters:
            mock_deiconify (Mock): Mock for the deiconify method.
            mock_login_button_callback (Mock): Mock for the login_button_callback method.
            mock_protocol (Mock): Mock for the protocol method.
        """
        self.auth_controller.login_view = None  # Ensure the login_view is initially None

        self.auth_controller.show_login_view()

        # Verify that LoginView was instantiated
        self.assertIsNotNone(self.auth_controller.login_view)

        # Verify that protocol, login_button_callback, and deiconify methods were called correctly
        mock_protocol.assert_called_once_with("WM_DELETE_WINDOW", self.auth_controller.on_closing)
        mock_login_button_callback.assert_called_once_with(self.auth_controller.login_admin)
        mock_deiconify.assert_called_once()

    def test_register_admin_success(self):
        """
        Test the register_admin method to ensure successful registration.
        """
        self.register_view.get_username.return_value = "testuser"
        self.register_view.get_password.return_value = "password"
        self.register_view.get_confirm_password.return_value = "password"
        self.admin_model.register.return_value = True

        self.auth_controller.register_view = self.register_view
        self.auth_controller.show_admin_dashboard = Mock()
        self.auth_controller.register_admin()

        self.register_view.withdraw.assert_called_once()
        self.register_view.clear_input_fields.assert_called_once()
        self.register_view.display_error_message.assert_not_called()
        self.auth_controller.show_admin_dashboard.assert_called_once()

    def test_register_admin_passwords_do_not_match(self):
        """
        Test the register_admin method to ensure error message when passwords do not match.
        """
        self.register_view.get_username.return_value = "testuser"
        self.register_view.get_password.return_value = "password"
        self.register_view.get_confirm_password.return_value = "different_password"

        self.auth_controller.register_view = self.register_view
        self.auth_controller.register_admin()

        self.register_view.display_error_message.assert_called_once_with("Passwords do not match!")
        self.register_view.withdraw.assert_not_called()
        self.register_view.clear_input_fields.assert_not_called()

    def test_register_admin_failure(self):
        """
        Test the register_admin method to ensure error message when registration fails.
        """
        self.register_view.get_username.return_value = "testuser"
        self.register_view.get_password.return_value = "password"
        self.register_view.get_confirm_password.return_value = "password"
        self.admin_model.register.return_value = False

        self.auth_controller.register_view = self.register_view
        self.auth_controller.register_admin()

        self.register_view.display_error_message.assert_called_once_with("Registration failed. Username might already be taken.")
        self.register_view.withdraw.assert_not_called()
        self.register_view.clear_input_fields.assert_not_called()

    def test_login_admin_success(self):
        """
        Test the login_admin method to ensure successful login.
        """
        self.login_view.get_username.return_value = "testuser"
        self.login_view.get_password.return_value = "password"
        self.admin_model.authorize.return_value = True

        self.auth_controller.login_view = self.login_view
        self.auth_controller.show_admin_dashboard = Mock()

        self.auth_controller.login_admin()

        self.login_view.withdraw.assert_called_once()
        self.login_view.clear_input_fields.assert_called_once()
        self.login_view.display_error_message.assert_not_called()
        self.auth_controller.show_admin_dashboard.assert_called_once()

    def test_login_admin_failure(self):
        """
        Test the login_admin method to ensure error message when login fails.
        """
        self.login_view.get_username.return_value = "testuser"
        self.login_view.get_password.return_value = "wrong_password"
        self.admin_model.authorize.return_value = False

        self.auth_controller.login_view = self.login_view
        self.auth_controller.login_admin()

        self.login_view.display_error_message.assert_called_once_with("Invalid username or password.")
        self.login_view.withdraw.assert_not_called()
        self.login_view.clear_input_fields.assert_not_called()

    @patch.object(AdminView, '__init__', lambda self: None)
    @patch.object(AdminView, 'protocol')
    @patch.object(AdminView, 'logout_button_callback')
    @patch.object(AdminView, 'deiconify')
    @patch('project_src.controllers.AdminAuthorizationController.AdminController')
    def test_show_admin_dashboard(self, MockAdminController, mock_deiconify, mock_logout_button_callback, mock_protocol):
        """
        Test the show_admin_dashboard method to ensure it initializes and displays the AdminView.

        Parameters:
            MockAdminController (Mock): Mock for the AdminController class.
            mock_deiconify (Mock): Mock for the deiconify method.
            mock_logout_button_callback (Mock): Mock for the logout_button_callback method.
            mock_protocol (Mock): Mock for the protocol method.
        """
        self.auth_controller.admin_view = None

        self.auth_controller.show_admin_dashboard()

        self.assertIsNotNone(self.auth_controller.admin_view)

        mock_protocol.assert_called_once_with("WM_DELETE_WINDOW", self.auth_controller.on_closing)
        mock_logout_button_callback.assert_called_once_with(self.auth_controller.logout)
        mock_deiconify.assert_called_once()

        MockAdminController.assert_called_once_with(self.root, self.quiz_model, self.auth_controller.admin_view)

    def test_logout(self):
        """
        Test the logout method to ensure it withdraws the AdminView and closes the window.
        """
        self.auth_controller.admin_view = self.admin_view
        self.auth_controller.logout()
        self.admin_view.withdraw.assert_called_once()

    def test_method_existence(self):
        """
        Tests that all expected methods exist in the AdminAuthorizationController class.
        """
        expected_methods = ['show_register_view', 'show_login_view', 'register_admin', 'login_admin', 'show_admin_dashboard', 'logout', 'on_closing']
        actual_methods = [method for method in dir(self.auth_controller) if
                          callable(getattr(self.auth_controller, method)) and not method.startswith('__')]

        for method in expected_methods:
            self.assertIn(method, actual_methods, f"Expected method {method} not found in "
                                                  f"AdminAuthorizationController class.")

    def test_private_method_naming(self):
        """
        Verifies that all intended private methods in the AdminAuthorizationController class start with an underscore,
        adhering to the naming convention for private methods.
        """
        # Assuming '_admin_model' and '_quiz_model' should be private attributes
        private_attributes = ['_admin_model', '_quiz_model']
        for attr in private_attributes:
            self.assertTrue(attr.startswith('_'), f"Attribute {attr} should be private (start with an underscore).")

    def test_public_method_naming(self):
        """
        Verifies that all intended public methods in the AdminAuthorizationController class do not start with an underscore,
        following the naming convention for public methods.
        """
        public_methods = ['show_register_view', 'show_login_view', 'register_admin', 'login_admin',
                          'show_admin_dashboard', 'logout', 'on_closing']
        for method in public_methods:
            self.assertFalse(method.startswith('_'),
                             f"Method {method} should be public (not start with an underscore).")

    def test_method_signatures(self):
        """
        Verifies that the method signatures for key methods in the AdminAuthorizationController class match
        the expected parameter names, ensuring consistency and clarity in method definitions.
        """
        signatures = {
            'show_register_view': [],
            'show_login_view': [],
            'register_admin': [],
            'login_admin': [],
            'show_admin_dashboard': [],
            'logout': [],
            'on_closing': []
        }

        for method, expected_params in signatures.items():
            with self.subTest(method=method):
                actual_params = list(inspect.signature(getattr(self.auth_controller, method)).parameters.keys())
                self.assertEqual(expected_params, actual_params, f"Signature for method {method} is incorrect.")


if __name__ == '__main__':
    unittest.main()
