import unittest

import tkinter as tk
from unittest.mock import patch, MagicMock
from unittest.mock import Mock
from tkinter import Label
from tkinter import Button
import inspect
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from project_src.views.StartView import StartView


class StartViewTest(unittest.TestCase):
    """
    Class that contains unit tests for the StartView class to ensure the
    widgets creation, and the functionality of callback methods and
    to ensure that all the required methods exists in the class.

    Author: Amal Abueshareik
    """

    def setUp(self):
        """ Setup method to create a start view instance before each test. """
        self.start_view = StartView()

    def tearDown(self):
        """ Method to destroy the start view instance after each test. """
        self.start_view.destroy()

    def test_menu_bar_exists(self):
        """
        Test that the start view contains a menu bar instance.

        Raises:
        - AssertionError: If the menu bar does not exists in the view

        Returns:
        - True: If the menu bar instance exists in the view, returns false if not
        """

        exists = False
        for child in self.start_view.winfo_children():
            if isinstance(child, tk.Menu):
                exists = True
                break
        self.assertTrue(exists)

    def test_widgets_exists(self):
        """
        Test that the titel label, and Button widgets is created in the view.

         Raises:
        - AssertionError: If error when creating the widget
         """
        self.assertIsInstance(self.start_view.title_label, Label)
        self.assertIsInstance(self.start_view.start_button, Button)
        self.assertIsInstance(self.start_view.login_button, Button)
        self.assertIsInstance(self.start_view.register_button, Button)

    def test_Label_properties(self):
        """
        Test that the label widget in the view have correct properties.

        Raises:
        - AssertionError: If error with creation the label with the specific properties
        """

        label = self.start_view.create_label("label")

        # Assert that the returned value is a label
        self.assertIsInstance(label, tk.Label)

        # Assert that the label properties are set correctly
        self.assertEqual(label['text'], "label")
        self.assertEqual(label['font'], "{Source Serif Pro} 18")
        self.assertEqual(label['bg'], "#f0f0f0")

    def test_button_properties(self):
        """
        Test that the button widget in the view have correct properties.

        Raises:
        - AssertionError: If error with creation the button with the specific properties
        """

        button = self.start_view.create_button("button")

        # Assert that the returned value is a Button
        self.assertIsInstance(button, tk.Button)

        # Assert that the button properties are set correctly
        self.assertEqual(button['text'], "button")
        self.assertEqual(button['font'], "Arial 12 italic")
        self.assertEqual(button['width'], 20)
        self.assertEqual(button['height'], 2)
        self.assertEqual(button['bg'], "#90CAF9")

    def test_title_Label_position(self):
        """
        Test the title label position in the view.

         Raises:
        - AssertionError: If error with the title label position
        """
        title_label_position = self.start_view.title_label.grid_info()
        self.assertEqual(title_label_position['row'], 0)
        self.assertEqual(title_label_position['padx'], 160)

    def test_start_button_position(self):
        """
        Test the start button position in the view.

        Raises:
        - AssertionError: If error with the start button position
        """
        start_button_position = self.start_view.start_button.grid_info()
        self.assertEqual(start_button_position['row'], 1)
        self.assertEqual(start_button_position['pady'], 10)

    def test_login_button_position(self):
        """
        Test the login button position in the view.

        Raises:
        - AssertionError: If error with the login button position
        """
        login_button_position = self.start_view.login_button.grid_info()
        self.assertEqual(login_button_position['row'], 2)
        self.assertEqual(login_button_position['pady'], 10)

    def test_register_button_position(self):
        """
        Test the register new admin button position in the view.

        Raises:
        - AssertionError: If error with the register button position
        """
        register_button_position = self.start_view.register_button.grid_info()
        self.assertEqual(register_button_position['row'], 3)
        self.assertEqual(register_button_position['pady'], 10)

    def test_start_button_callback(self):
        """ Test the start quiz button callback functionality. """
        mock = Mock()
        # Call the method with the mocked callback
        self.start_view.start_button_callback(mock)
        # Trigger the button press event
        self.start_view.start_button.invoke()
        mock.assert_called_once()

    def test_login_button_callback(self):
        """ Test the login as admin button callback functionality """
        mock = Mock()
        # Call the method with the mocked callback
        self.start_view.login_button_callback(mock)
        # Trigger the button press event
        self.start_view.login_button.invoke()
        mock.assert_called_once()

    def test_register_button_callback(self):
        """ Test the register new admin button callback functionality """
        mock = Mock()
        # Call the method with the mocked callback
        self.start_view.register_button_callback(mock)
        # Trigger the button press event
        self.start_view.register_button.invoke()
        mock.assert_called_once()

    @patch('tkinter.Tk.winfo_screenwidth', return_value=800)
    @patch('tkinter.Tk.winfo_screenheight', return_value=600)
    def test_center_window(self, screen_width: int, screen_height: int):
        """
        Test the behaviour of center the view on the center of the screen.

        Parameters:
        - screen_width (int): The screen width mocked
        - screen_height (int): The screen height mocked

        Raises:
        - AssertionError: If error when centering the window
        """
        self.start_view.center_window()
        self.start_view.update_idletasks()

        # Expected center coordinates based on mocked screen width and height
        x = (800 - 600) // 2
        y = (600 - 300) // 2

        self.assertEqual(self.start_view.winfo_x(), x)
        self.assertEqual(self.start_view.winfo_y(), y)

    @patch('tkinter.messagebox.showinfo')
    def test_usage_guide_option(self, mock_messagebox: MagicMock):
        """
        Test the creation of the message box.

         Parameters:
        - mock (MagickMock): MagicMock object to mock the messagebox
        """
        self.start_view.show_information()
        mock_messagebox.assert_called_once()

    def test_that_method_exist(self):
        """
        Tests that all expected methods exist in the class.

        Raises:
        - AssertionError: If the methods does not exists.
        """
        expected_methods = [
            'create_widgets',
            'create_label',
            'create_button',
            'start_button_callback',
            'login_button_callback',
            'register_button_callback',
            'center_window',
            'show_information',
        ]
        class_methods = [method for method in dir(self.start_view) if callable(getattr(self.start_view, method))]

        for method in expected_methods:
            self.assertIn(method, class_methods, f"The method {method} does not exist in the StartView class.")

    def test_method_parameters(self):
        """
        Tests that all expected methods in the class have the expected parameter.

        Raises:
        - AssertionError: If the methods does have the expected parameters.
        """
        methods_parameters = {
            "create_widgets": [],
            "create_label": ['text'],
            "create_button": ['text'],
            "start_button_callback": ['callback'],
            "login_button_callback": ['callback'],
            "register_button_callback": ['callback'],
            "center_window": [],
            "show_information": [],
        }
        for method, exp_params in methods_parameters.items():
            with self.subTest(method=method):
                actual_params = list(inspect.signature(getattr(self.start_view, method)).parameters.keys())
                self.assertEqual(exp_params, actual_params, f"The parameter for the method {method} is incorrect.")


if __name__ == '__main__':
    unittest.main()
