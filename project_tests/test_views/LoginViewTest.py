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

from project_src.views.LoginView import LoginView


class TestLoginView(unittest.TestCase):

    """
    Class that contains unit tests for the LoginView class to ensure the
    views and widgets creation, and the functionality of retrieving
    username and password and to ensure that all the required methods exists in the class.

    Author: Amal Abueshareik
    """

    def setUp(self):
        """ Setup method to create a login view instance before each test. """
        self.loginView = LoginView()

    def tearDown(self):
        """ Method to destroy the login view instance after each test. """
        self.loginView.destroy()

    def test_create_widgets(self):
        """
        Test that the PhotoImage, label, Entry and Button widgets is created in the view.

         Raises:
        - AssertionError: If error when creating the widget
         """
        self.assertIsInstance(self.loginView.logo_label.image, PhotoImage)
        self.assertIsInstance(self.loginView.logo_label, Label)
        self.assertIsInstance(self.loginView.title_label, Label)
        self.assertIsInstance(self.loginView.username_label, Label)
        self.assertIsInstance(self.loginView.username_entry, Entry)
        self.assertIsInstance(self.loginView.password_label, Label)
        self.assertIsInstance(self.loginView.password_entry, Entry)
        self.assertIsInstance(self.loginView.login_button, Button)

    def test_widgets_properties(self):
        """
        Test that the widgets in the view have correct properties.

         Raises:
        - AssertionError: If error with creation the widgets with the specific properties
        """
        self.assertEqual(self.loginView.title_label['text'], "Login")
        self.assertEqual(self.loginView.title_label['font'], "{Source Serif Pro} 18")
        self.assertEqual(self.loginView.username_label['text'], "Username:")
        self.assertEqual(self.loginView.username_label['font'], "{Source Serif Pro} 14 italic")
        self.assertEqual(self.loginView.password_label['text'], "Password:")
        self.assertEqual(self.loginView.password_label['font'], "{Source Serif Pro} 14 italic")
        self.assertEqual(self.loginView.login_button['text'], "Login")
        self.assertEqual(self.loginView.login_button['background'], "#90CAF9")

    def test_Logo_Label_position(self):
        """
        Test the logo label position in the view.

         Raises:
        - AssertionError: If error with the logo label position
        """
        logo_label_position = self.loginView.logo_label.grid_info()
        self.assertEqual(logo_label_position['row'], 0)
        self.assertEqual(logo_label_position['column'], 0)
        self.assertEqual(logo_label_position['columnspan'], 2)

    def test_title_Label_position(self):
        """
        Test the title label position in the view.

        Raises:
        - AssertionError: If error with the title label position
        """
        title_label_position = self.loginView.title_label.grid_info()
        self.assertEqual(title_label_position['row'], 1)
        self.assertEqual(title_label_position['column'], 0)
        self.assertEqual(title_label_position['columnspan'], 2)

    def test_username_Label_position(self):
        """
        Test the username label position in the view.

        Raises:
        - AssertionError: If error with the username label position
        """
        username_label_position = self.loginView.username_label.grid_info()
        self.assertEqual(username_label_position['row'], 2)
        self.assertEqual(username_label_position['column'], 0)
        self.assertEqual(username_label_position['columnspan'], 1)

    def test_username_entry_position(self):
        """
        Test the username entry position in the view.

        Raises:
        - AssertionError: If error with the username entry position
        """
        username_entry_position = self.loginView.username_entry.grid_info()
        self.assertEqual(username_entry_position['row'], 3)
        self.assertEqual(username_entry_position['column'], 0)
        self.assertEqual(username_entry_position['columnspan'], 1)

    def test_password_Label_position(self):
        """
        Test the password label position in the view.

        Raises:
        - AssertionError: If error with the password label position
        """
        password_label_position = self.loginView.password_label.grid_info()
        self.assertEqual(password_label_position['row'], 4)
        self.assertEqual(password_label_position['column'], 0)
        self.assertEqual(password_label_position['columnspan'], 1)

    def test_password_entry_position(self):
        """
        Test the password entry position in the view.

        Raises:
        - AssertionError: If error with the password entry position
        """
        password_entry_position = self.loginView.password_entry.grid_info()
        self.assertEqual(password_entry_position['row'], 5)
        self.assertEqual(password_entry_position['column'], 0)
        self.assertEqual(password_entry_position['columnspan'], 1)

    def test_login_button_position(self):
        """
        Test the login button position in the view.

        Raises:
        - AssertionError: If error with the login button position
        """
        button_position = self.loginView.login_button.grid_info()
        self.assertEqual(button_position['row'], 6)
        self.assertEqual(button_position['column'], 0)
        self.assertEqual(button_position['columnspan'], 1)

    def test_get_username(self):
        """
        Test the username retrieve from the username entry's functionality.

         Raises:
        - AssertionError: If error when retrieve the username
        """
        self.loginView.username_entry.insert(0, "admin")
        self.assertEqual(self.loginView.get_username(), "admin")

    def test_get_password(self):
        """
        Test the password retrieve from the password entry's functionality.

        Raises:
        - AssertionError: If error when retrieve the password
        """
        self.loginView.password_entry.insert(0, "1234")
        self.assertEqual(self.loginView.get_password(), "1234")

    def test_login_button_callback(self):
        """ Test the button callback functionality """
        # Mocking the callback function
        mock = Mock()
        # Call the method with the mocked callback
        self.loginView.login_button_callback(mock)
        # Trigger the button press event
        self.loginView.login_button.invoke()
        # Check if the function was called
        mock.assert_called_once()

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
        self.loginView.center_window()
        self.loginView.update_idletasks()

        # Expected center coordinates based on mocked screen width and height
        x = (800 - 400) // 2
        y = (600 - 450) // 2

        self.assertEqual(self.loginView.winfo_x(), x)
        self.assertEqual(self.loginView.winfo_y(), y)

    @patch.object(messagebox, 'showerror')
    def test_display_error_message(self, mock: MagicMock):
        """
        Test the displaying of error message functionality.

        Parameters:
        - mock (MagickMock): MagicMock object used to mock the showerror method
        """
        self.loginView.display_error_message("Login In Failed, Invalid username or password")
        mock.assert_called_once_with("Error", "Login In Failed, Invalid username or password")

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
            'login_button_callback',
            'display_error_message',
            'center_window',
        ]
        class_methods = [method for method in dir(self.loginView) if callable(getattr(self.loginView, method))]

        for method in expected_methods:
            self.assertIn(method, class_methods, f"The method {method} does not exist in the LoginView class.")

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
            "login_button_callback": ['callback'],
            "display_error_message": ['error'],
            "center_window": [],
        }
        for method, exp_params in methods_parameters.items():
            with self.subTest(method=method):
                actual_params = list(inspect.signature(getattr(self.loginView, method)).parameters.keys())
                self.assertEqual(exp_params, actual_params, f"The parameter for the method {method} is incorrect.")


if __name__ == '__main__':
    unittest.main()