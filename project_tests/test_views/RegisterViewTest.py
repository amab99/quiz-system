import unittest
import inspect
import os
import sys
from tkinter import messagebox
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import PhotoImage
from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from project_src.views.RegisterView import RegisterView


class RegisterViewTest(unittest.TestCase):
    """
    Class that contains unit tests for the RegisterView class to ensure the
    views and widgets creation, and the functionality of retrieving
    username and password. This class also have unit tests to ensure the functionality of the callback method,
    and that all the required methods exists in the class.

    Author: Amal Abueshareik
    """

    def setUp(self):
        """ Setup method to create a register view instance before each test. """
        self.register_view = RegisterView()

    def tearDown(self):
        """ Method to destroy the register view root after each test. """
        self.register_view.root.destroy()

    def test_create_widgets(self):
        """
        Test that the PhotoImage, label, Entry and Button widgets is created in the view.

         Raises:
        - AssertionError: If error when creating the widget
         """
        self.assertIsInstance(self.register_view.root.logo_label.image, PhotoImage)
        self.assertIsInstance(self.register_view.root.logo_label, Label)
        self.assertIsInstance(self.register_view.root.title_label, Label)
        self.assertIsInstance(self.register_view.root.username_label, Label)
        self.assertIsInstance(self.register_view.root.username_entry, Entry)
        self.assertIsInstance(self.register_view.root.password_label, Label)
        self.assertIsInstance(self.register_view.root.confirm_password_label, Label)
        self.assertIsInstance(self.register_view.root.password_entry, Entry)
        self.assertIsInstance(self.register_view.root.confirm_password_entry, Entry)
        self.assertIsInstance(self.register_view.root.register_button, Button)

    def test_get_username(self):
        """
        Test the username retrieve from the username entry's functionality.

         Raises:
        - AssertionError: If error when retrieve the username
        """
        self.register_view.root.username_entry.insert(0, "admin1")
        self.assertEqual(self.register_view.get_username(), "admin1")

    def test_get_password(self):
        """
        Test the functionality of retrieve the password from the password entry.

        Raises:
        - AssertionError: If error when retrieve the password
        """
        self.register_view.root.password_entry.insert(0, "1234")
        self.assertEqual(self.register_view.get_password(), "1234")

    def test_get_confirmed_password(self):
        """
        Test the functionality of retrieve the entered confirmation password from the confirm password entry.

        Raises:
        - AssertionError: If error when retrieve the password
        """
        self.register_view.root.confirm_password_entry.insert(0, "1234")
        self.assertEqual(self.register_view.get_confirm_password(), "1234")

    def test_register_button_callback(self):
        """ Test the register button callback functionality """
        mock = Mock()
        self.register_view.register_button_callback(mock)
        self.register_view.root.register_button.invoke()
        mock.assert_called_once()

    @patch.object(messagebox, 'showerror')
    def test_display_error_message(self, mock: MagicMock):
        """
        Test the displaying of error message functionality.

        Parameters:
        - mock (MagickMock): MagicMock object to mock used to mock the showerror method
        """
        self.register_view.display_error_message("Register Failed, passwords do not match!")
        mock.assert_called_once_with("Error", "Register Failed, passwords do not match!")

    @patch('tkinter.Tk.winfo_screenwidth', return_value=800)
    @patch('tkinter.Tk.winfo_screenheight', return_value=600)
    def test_center_window(self, screen_width: int, screen_height: int):
        """
        Test the behaviour of center the view window on the center of the screen.

        Parameters:
        - screen_width (int): The screen width mocked
        - screen_height (int): The screen height mocked

        Raises:
        - AssertionError: If error when centering the window
        """
        self.register_view.center_window()
        self.register_view.root.update_idletasks()

        # Expected center coordinates based on mocked screen width and height
        x = (800 - 400) // 2
        y = (600 - 450) // 2

        self.assertEqual(self.register_view.root.winfo_x(), x)
        self.assertEqual(self.register_view.root.winfo_y(), y)

    def test_that_method_exist(self):
        """
        Tests that all expected methods exist in the class.

        Raises:
        - AssertionError: If the methods does not exists.
        """
        expected_methods = [
            'create_widgets',
            'get_username',
            'get_password',
            'register_button_callback',
            'display_error_message',
            'center_window',
        ]
        class_methods = [method for method in dir(self.register_view) if callable(getattr(self.register_view, method))]

        for method in expected_methods:
            self.assertIn(method, class_methods, f"The method {method} does not exist in the RegisterView class.")

    def test_method_parameters(self):
        """
        Tests that all expected methods in the class have the expected parameter.

        Raises:
        - AssertionError: If the methods does have the expected parameters.
        """
        methods_parameters = {
            "create_widgets": [],
            "get_username": [],
            "get_password": [],
            "register_button_callback": ['callback'],
            "display_error_message": ['error'],
            "center_window": [],
        }
        for method, exp_params in methods_parameters.items():
            with self.subTest(method=method):
                actual_params = list(inspect.signature(getattr(self.register_view, method)).parameters.keys())
                self.assertEqual(exp_params, actual_params, f"The parameter for the method {method} is incorrect.")


if __name__ == '__main__':
    unittest.main()
