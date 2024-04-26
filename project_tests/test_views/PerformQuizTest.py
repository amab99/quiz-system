import unittest
from unittest.mock import MagicMock
import tkinter as tk
from unittest.mock import patch
from unittest.mock import Mock
import inspect
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from project_src.views.PerformQuizView import PerformQuizView


class TestPerformQuizView(unittest.TestCase):
    """
    Class that contains unit tests for the PerformQuizView class to ensure the
    widgets creation, the functionality of the options selection, the functionality of the callback methods,
    and to ensure that all the required methods exists in the class.

    Author: Amal Abueshareik
    """

    def setUp(self):
        """ Setup method to create a perform quiz view instance before each test. """
        self.root = tk.Tk()
        self.quiz_view = PerformQuizView()

    def tearDown(self):
        """ Method to destroy the Tk root window after each test. """
        self.root.destroy()

    def test_set_question_text(self):
        """
        Test method to test the functionality of setting the question text to the label.

        Raises:
        - AssertionError: If error when set the question text
        """
        self.quiz_view.root.question_label = MagicMock()
        question = "What is the capital of Sweden?"
        self.quiz_view.set_question_text(question)
        self.quiz_view.root.question_label.config.assert_called_once_with(text=question)

    def test_set_option1(self):
        """ Test method to ensure the functionality of setting the first option correct to the radio button. """
        self.quiz_view.root.opt1 = MagicMock()
        options = ["Paris", "Berlin", "Rome", "Madrid"]
        self.quiz_view.set_answer_options(options)
        self.quiz_view.root.opt1.config.assert_called_once_with(text=options[0])

    def test_set_option2(self):
        """ Test method to ensure the functionality of setting the second option correct to the radio button. """
        self.quiz_view.root.opt2 = MagicMock()
        options = ["Paris", "Berlin", "Rome", "Madrid"]
        self.quiz_view.set_answer_options(options)
        self.quiz_view.root.opt2.config.assert_called_once_with(text=options[1])

    def test_set_option3(self):
        """ Test method to ensure the functionality of setting the third option correct to the radio button. """
        self.quiz_view.root.opt3 = MagicMock()
        options = ["Paris", "Berlin", "Rome", "Madrid"]
        self.quiz_view.set_answer_options(options)
        self.quiz_view.root.opt3.config.assert_called_once_with(text=options[2])

    def test_set_option4(self):
        """ Test method to ensure the functionality of setting the fourth option correct to the radio button. """
        self.quiz_view.root.opt4 = MagicMock()
        options = ["Paris", "Berlin", "Rome", "Madrid"]
        self.quiz_view.set_answer_options(options)
        self.quiz_view.root.opt4.config.assert_called_once_with(text=options[3])

    def test_set_selected_option(self):
        """ Test method to ensure the selection of an option. """
        # Mock the third option
        self.quiz_view.root.opt3 = MagicMock()
        self.quiz_view.root.option_var = MagicMock()
        # Mock the text string of the third option
        self.quiz_view.root.opt3.cget.return_value = "Test option"
        self.quiz_view.set_selected_option("Test option")
        self.quiz_view.root.option_var.set.assert_called_once_with(3)

    def test_clear_selected_options(self):
        """ Test method to ensure the functionality of clear the selection of the options. """
        self.quiz_view.root.option_var = MagicMock()
        self.quiz_view.clear_selected_options()
        self.quiz_view.root.option_var.set.assert_called_once_with(0)

    def test_prev_button_callback(self):
        """ Test the previous button callback functionality. """
        callback_mock = Mock()
        self.quiz_view.add_prev_button_callback(callback_mock)
        self.quiz_view.root.prev_button.invoke()
        callback_mock.assert_called_once()

    def test_next_button_callback(self):
        """ Test the next button callback functionality. """
        callback_mock = Mock()
        self.quiz_view.add_next_button_callback(callback_mock)
        self.quiz_view.root.next_button.invoke()
        callback_mock.assert_called_once()

    def test_submit_button_callback(self):
        """ Test the submit button callback functionality. """
        callback_mock = Mock()
        self.quiz_view.add_submit_button_callback(callback_mock)
        self.quiz_view.root.submit_button.invoke()
        callback_mock.assert_called_once()

    def test_set_prev_button_enabled(self):
        """ Test method to ensure the functionality of setting the previous button to enabled state. """
        self.quiz_view.set_prev_button_enabled(True)
        self.assertEqual(self.quiz_view.root.prev_button.cget("state"), "normal")

    def test_set_next_button_enabled(self):
        """ Test method to ensure the functionality of setting the next button to enabled state. """
        self.quiz_view.set_next_button_enabled(True)
        self.assertEqual(self.quiz_view.root.next_button.cget("state"), "normal")

    def test_option1_button_callback(self):
        """ Test the first option radio button callback functionality. """
        callback_mock = Mock()
        self.quiz_view.add_option_button_callback(callback_mock)
        self.quiz_view.root.opt1.invoke()
        callback_mock.assert_called_once_with("Option 1")

    def test_option2_button_callback(self):
        """ Test the second option radio button callback functionality. """
        callback_mock = Mock()
        self.quiz_view.add_option_button_callback(callback_mock)
        self.quiz_view.root.opt2.invoke()
        callback_mock.assert_called_once_with("Option 2")

    def test_option3_button_callback(self):
        """ Test the third option radio button callback functionality. """
        callback_mock = Mock()
        self.quiz_view.add_option_button_callback(callback_mock)
        self.quiz_view.root.opt3.invoke()
        callback_mock.assert_called_once_with("Option 3")

    def test_option4_button_callback(self):
        """ Test the fourth option radio button callback functionality. """
        callback_mock = Mock()
        self.quiz_view.add_option_button_callback(callback_mock)
        self.quiz_view.root.opt4.invoke()
        callback_mock.assert_called_once_with("Option 4")

    def test_get_selected_option1(self):
        """ Test the functionality of retrieve the text of the selected option 1."""
        self.quiz_view.root.option_var = MagicMock()
        self.quiz_view.root.opt1 = MagicMock()
        self.quiz_view.root.opt1.cget.return_value = "Stockholm"
        self.quiz_view.root.option_var.get.return_value = 1
        self.assertEqual(self.quiz_view.get_selected_option(), "Stockholm")

    def test_get_selected_option2(self):
        """ Test the functionality of retrieve the text of the selected option 2."""
        self.quiz_view.root.option_var = MagicMock()
        self.quiz_view.root.opt2 = MagicMock()
        self.quiz_view.root.opt2.cget.return_value = "Berlin"
        self.quiz_view.root.option_var.get.return_value = 2
        self.assertEqual(self.quiz_view.get_selected_option(), "Berlin")

    def test_get_selected_option3(self):
        """ Test the functionality of retrieve the text of the selected option 3."""
        self.quiz_view.root.option_var = MagicMock()
        self.quiz_view.root.opt3 = MagicMock()
        self.quiz_view.root.opt3.cget.return_value = "Paris"
        self.quiz_view.root.option_var.get.return_value = 3
        self.assertEqual(self.quiz_view.get_selected_option(), "Paris")

    def test_get_selected_option4(self):
        """ Test the functionality of retrieve the text of the selected option 4."""
        self.quiz_view.root.option_var = MagicMock()
        self.quiz_view.root.opt4 = MagicMock()
        self.quiz_view.root.opt4.cget.return_value = "Rome"
        self.quiz_view.root.option_var.get.return_value = 4
        self.assertEqual(self.quiz_view.get_selected_option(), "Rome")

    @patch('tkinter.Tk.winfo_screenwidth', return_value=1200)
    @patch('tkinter.Tk.winfo_screenheight', return_value=1000)
    def test_center_window(self, screen_width: int, screen_height: int):
        """
        Test the behaviour of center the view on the center of the screen.

        Parameters:
        - screen_width (int): The screen width mocked
        - screen_height (int): The screen height mocked

        Raises:
        - AssertionError: If error when centering the window
        """
        self.quiz_view.center_window()
        self.quiz_view.root.update_idletasks()

        # Expected center coordinates based on mocked screen width and height
        x = (1200 - 800) // 2
        y = (1000 - 600) // 2

        self.assertEqual(self.quiz_view.root.winfo_x(), x)
        self.assertEqual(self.quiz_view.root.winfo_y(), y)

    def test_that_method_exist(self):
        """
        Tests that all expected methods exist in the class.

        Raises:
        - AssertionError: If the methods does not exists.
        """
        expected_methods = [
            'create_widgets',
            'set_question_text',
            'set_answer_options',
            'set_selected_option',
            'set_prev_button_enabled',
            'set_next_button_enabled',
            'add_prev_button_callback',
            "add_next_button_callback",
            "add_submit_button_callback",
            "add_option_button_callback",
            "clear_selected_options",
            "get_selected_option",
            "center_window",
        ]
        class_methods = [method for method in dir(self.quiz_view) if callable(getattr(self.quiz_view, method))]

        for method in expected_methods:
            self.assertIn(method, class_methods, f"The method {method} does not exist in the PerformQuizView class.")

    def test_method_parameters(self):
        """
        Tests that all expected methods in the class have the expected parameter.

        Raises:
        - AssertionError: If the methods does have the expected parameters.
        """
        methods_parameters = {
            "create_widgets": [],
            "set_question_text": ['text'],
            "set_answer_options": ['options'],
            "set_selected_option": ['option'],
            "set_prev_button_enabled": ['enabled'],
            "set_next_button_enabled": ['enabled'],
            "add_prev_button_callback": ['callback'],
            "add_next_button_callback": ['callback'],
            "add_submit_button_callback": ['callback'],
            "add_option_button_callback": ['callback'],
            "clear_selected_options": [],
            "get_selected_option": [],
            "center_window": [],
        }
        for method, exp_params in methods_parameters.items():
            with self.subTest(method=method):
                actual_params = list(inspect.signature(getattr(self.quiz_view, method)).parameters.keys())
                self.assertEqual(exp_params, actual_params, f"The parameter for the method {method} is incorrect.")


if __name__ == '__main__':
    unittest.main()
