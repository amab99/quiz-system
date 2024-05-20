import inspect
import tkinter.ttk
import unittest

import os
import sys
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox

from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from project_src.views.AdminView import AdminView


class AdminViewTest(unittest.TestCase):
    """
    Class contains unit tests for the AdminView class to ensure the widgets creation,
    the functionality of the updating the table, the functionality of the get methods,
    the functionality of the callback methods, and to ensure that all the required methods exists in the class.

    @Author: Amal Abueshareik
    """

    def setUp(self):
        """ Setup method to create a admin view instance before each test. """
        self.admin_view = AdminView()

    def tearDown(self):
        """ Method to destroy the view after each test. """
        self.admin_view.destroy()

    def test_create_widgets(self):
        """
        Test that the labels, entries and buttons widgets is created in the view.

        Raises:
        - AssertionError: If error when creating the widget
        """
        self.assertIsInstance(self.admin_view.table, tkinter.ttk.Treeview)
        self.assertIsInstance(self.admin_view.question_label, Label)
        self.assertIsInstance(self.admin_view.question_entry, Entry)
        self.assertIsInstance(self.admin_view.option1_label, Label)
        self.assertIsInstance(self.admin_view.option1_entry, Entry)
        self.assertIsInstance(self.admin_view.option2_label, Label)
        self.assertIsInstance(self.admin_view.option2_entry, Entry)
        self.assertIsInstance(self.admin_view.option3_label, Label)
        self.assertIsInstance(self.admin_view.option3_entry, Entry)
        self.assertIsInstance(self.admin_view.option4_label, Label)
        self.assertIsInstance(self.admin_view.option4_entry, Entry)
        self.assertIsInstance(self.admin_view.correct_option_label, Label)
        self.assertIsInstance(self.admin_view.correct_option_entry, Entry)
        self.assertIsInstance(self.admin_view.add_btn, Button)
        self.assertIsInstance(self.admin_view.delete_btn, Button)
        self.assertIsInstance(self.admin_view.clear_btn, Button)
        self.assertIsInstance(self.admin_view.update_btn, Button)
        self.assertIsInstance(self.admin_view.logout_btn, Button)

    def test_get_question_text(self):
        """
        Test the question retrieve from the question entry's functionality.

        Raises:
        - AssertionError: If error when retrieve the question text
        """
        self.admin_view.question_entry.insert(0, "What is the capital of Sweden?")
        self.assertEqual(self.admin_view.get_question_text(), "What is the capital of Sweden?")

    def test_get_first_option(self):
        """
        Test the functionality of retrieving the text from the first option entry

        Raises:
        - AssertionError: If error when retrieve the first option text
        """
        self.admin_view.option1_entry.insert(0, "option 1")
        self.assertEqual(self.admin_view.get_first_option(), "option 1")

    def test_get_second_option(self):
        """
        Test the functionality of retrieving the text from the second option entry

        Raises:
        - AssertionError: If error when retrieve the second option text
        """
        self.admin_view.option2_entry.insert(0, "option 2")
        self.assertEqual(self.admin_view.get_second_option(), "option 2")

    def test_get_third_option(self):
        """
        Test the functionality of retrieving the text from the third option entry

        Raises:
        - AssertionError: If error when retrieve the third option text
        """
        self.admin_view.option3_entry.insert(0, "option 3")
        self.assertEqual(self.admin_view.get_third_option(), "option 3")

    def test_get_fourth_option(self):
        """
        Test the functionality of retrieving the text from the fourth option entry

        Raises:
        - AssertionError: If error when retrieve the fourth option text
        """
        self.admin_view.option4_entry.insert(0, "option 4")
        self.assertEqual(self.admin_view.get_fourth_option(), "option 4")

    def test_get_correct_option(self):
        """
        Test the functionality of retrieving the index from the correct option entry

        Raises:
        - AssertionError: If error when retrieve the correct option index
        """
        self.admin_view.correct_option_entry.insert(0, 2)
        self.assertEqual(self.admin_view.get_correct_option(), 2)

    def test_add_button_callback(self):
        """ Test the add button callback functionality. """
        callback_mock = Mock()
        self.admin_view.add_button_callback(callback_mock)
        self.admin_view.add_btn.invoke()
        callback_mock.assert_called_once()

    def test_clear_button_callback(self):
        """ Test the clear button callback functionality. """
        callback_mock = Mock()
        self.admin_view.clear_button_callback(callback_mock)
        self.admin_view.clear_btn.invoke()
        callback_mock.assert_called_once()

    def test_delete_button_callback(self):
        """ Test the delete button callback functionality. """
        callback_mock = Mock()
        self.admin_view.delete_button_callback(callback_mock)
        self.admin_view.delete_btn.invoke()
        callback_mock.assert_called_once()

    def test_update_button_callback(self):
        """ Test the update button callback functionality. """
        callback_mock = Mock()
        self.admin_view.update_button_callback(callback_mock)
        self.admin_view.update_btn.invoke()
        callback_mock.assert_called_once()

    def test_logout_button_callback(self):
        """ Test the logout button callback functionality. """
        callback_mock = Mock()
        self.admin_view.logout_button_callback(callback_mock)
        self.admin_view.logout_btn.invoke()
        callback_mock.assert_called_once()

    def test_bind_row_click(self):
        """ Test that the method correctly binds the callback function to the click event. """
        callback_mock = Mock()
        self.admin_view.bind_table_row_click(callback_mock)
        self.admin_view.table.event_generate("<ButtonRelease-1>")
        callback_mock.assert_called_once()

    def test_clear_entries(self):
        """ Test method to ensure the functionality of clearing the text entries. """
        # First inserting text to the entry and check that the entry is not empty
        self.admin_view.question_entry.insert(0, "What is the chemical symbol for water?")
        self.assertNotEqual(self.admin_view.question_entry.get(), "")
        # Clear the entry
        self.admin_view.clear_input_entries()
        self.assertEqual(self.admin_view.question_entry.get(), "")

    def test_update_table(self):
        """ Test method used to verify the update of the table with the data. """
        data = [[1, "What is the chemical symbol for water?", "HO", "H", "H2O", "O", 3],
                [2, "What is the capital of Sweden?", "Helsingborg", "Laholm", "Stockholm", "Landskrona", 3]]
        self.admin_view.update_table(data)
        self.assertEqual(len(self.admin_view.table.get_children()), len(data))
        for i, question in enumerate(data, start=1):
            item = self.admin_view.table.item(i)
            self.assertEqual(item['values'], question)

    def test_get_selected_row(self):
        """ Test method used to test the revert of the selected row from the table."""
        self.assertIsNone(self.admin_view.get_table_row())
        data = [[1, "What is the chemical symbol for water?", "HO", "H", "H2O", "O", 3],
                [2, "What is the capital of Sweden?", "Helsingborg", "Laholm", "Stockholm", "Borås", 3]]
        self.admin_view.update_table(data)
        self.admin_view.table.selection_set(2)
        self.assertEqual(self.admin_view.get_table_row(), 2)

    @patch.object(messagebox, 'showerror')
    def test_display_error_message(self, mock: MagicMock):
        """
        Test the displaying of error message functionality.

        Parameters:
        - mock (MagickMock): MagicMock object to mock used to mock the showerror method
        """
        self.admin_view.display_error_message("Add question Failed, please fill all the text entries")
        mock.assert_called_once_with("Error", "Add question Failed, please fill all the text entries")

    @patch('tkinter.Tk.winfo_screenwidth', return_value=1200)
    @patch('tkinter.Tk.winfo_screenheight', return_value=1000)
    @patch.object(AdminView, 'winfo_x', return_value=55)
    @patch.object(AdminView, 'winfo_y', return_value=190)
    def test_center_window(self, mock_winfo_x, mock_winfo_y, screen_width: int, screen_height: int):
        """
        Test the behaviour of center the view on the center of the screen.

        Parameters:
        - mock_winfo_x (Mock): Mocked method for window X coordinate
        - mock_winfo_y (Mock): Mocked method for window Y coordinate
        - screen_width (int): Mocked screen width
        - screen_height (int): Mocked screen height

        Raises:
        - AssertionError: If error when centering the window
        """
        self.admin_view.center_window()
        self.admin_view.update_idletasks()

        # Expected center coordinates based on mocked screen width and height
        x = (1200 - 1090) // 2
        y = (1000 - 620) // 2

        self.assertEqual(self.admin_view.winfo_x(), x)
        self.assertEqual(self.admin_view.winfo_y(), y)


    def test_set_question_text(self):
        """
        Test the functionality of setting the question text in the entry field.

        Raises:
        - AssertionError: If error when setting the question text
        """
        self.admin_view.set_question_text("What is the capital of France?")
        self.assertEqual(self.admin_view.question_entry.get(), "What is the capital of France?")

    def test_set_first_option(self):
        """
        Test the functionality of setting the first option text in the entry field.

        Raises:
        - AssertionError: If error when setting the first option text
        """
        self.admin_view.set_first_option("Paris")
        self.assertEqual(self.admin_view.option1_entry.get(), "Paris")

    def test_set_second_option(self):
        """
        Test the functionality of setting the second option text in the entry field.

        Raises:
        - AssertionError: If error when setting the second option text
        """
        self.admin_view.set_second_option("Lyon")
        self.assertEqual(self.admin_view.option2_entry.get(), "Lyon")

    def test_set_third_option(self):
        """
        Test the functionality of setting the third option text in the entry field.

        Raises:
        - AssertionError: If error when setting the third option text
        """
        self.admin_view.set_third_option("Marseille")
        self.assertEqual(self.admin_view.option3_entry.get(), "Marseille")

    def test_set_fourth_option(self):
        """
        Test the functionality of setting the fourth option text in the entry field.

        Raises:
        - AssertionError: If error when setting the fourth option text
        """
        self.admin_view.set_fourth_option("Nice")
        self.assertEqual(self.admin_view.option4_entry.get(), "Nice")

    def test_set_correct_option(self):
        """
        Test the functionality of setting the correct option value in the entry field.

        Raises:
        - AssertionError: If error when setting the correct option value
        """
        self.admin_view.set_correct_option(1)
        self.assertEqual(self.admin_view.correct_option_entry.get(), "1")

    def test_that_method_exist(self):
        """
        Tests that all expected methods exist in the class.

        Raises:
        - AssertionError: If the methods does not exists.
        """
        expected_methods = [
            "create_widgets",
            "create_tree_view",
            "create_entries",
            "create_buttons",
            "get_question_text",
            "get_first_option",
            "get_second_option",
            "get_third_option",
            "get_fourth_option",
            "get_correct_option",
            "get_table",
            "get_table_row",
            "bind_table_row_click",
            "add_button_callback",
            "clear_button_callback",
            "delete_button_callback",
            "update_button_callback",
            "logout_button_callback",
            "update_table",
            "clear_input_entries",
            "display_error_message",
            "center_window",
            "set_question_text",
            "set_first_option",
            "set_second_option",
            "set_third_option",
            "set_fourth_option",
            "set_correct_option"
        ]
        class_methods = [method for method in dir(self.admin_view) if callable(getattr(self.admin_view, method))]

        for method in expected_methods:
            self.assertIn(method, class_methods, f"The method {method} does not exist in the AdminView class.")

    def test_method_parameters(self):
        """
        Tests that all expected methods in the class have the expected parameter.

        Raises:
        - AssertionError: If the methods does have the expected parameters.
        """
        methods_parameters = {
            "create_widgets": [],
            "create_tree_view": [],
            "create_entries": [],
            "create_buttons": [],
            "get_question_text": [],
            "get_first_option": [],
            "get_second_option": [],
            "get_third_option": [],
            "get_fourth_option": [],
            "get_correct_option": [],
            "get_table": [],
            "get_table_row": [],
            "bind_table_row_click": ['callback'],
            "add_button_callback": ['callback'],
            "clear_button_callback": ['callback'],
            "delete_button_callback": ['callback'],
            "update_button_callback": ['callback'],
            "logout_button_callback": ['callback'],
            "update_table": ['data'],
            "clear_input_entries": [],
            "display_error_message": ['error'],
            "center_window": [],
            "set_question_text": ['text'],
            "set_first_option": ['text'],
            "set_second_option": ['text'],
            "set_third_option": ['text'],
            "set_fourth_option": ['text'],
            "set_correct_option": ['value']
        }
        for method, exp_params in methods_parameters.items():
            with self.subTest(method=method):
                actual_params = list(inspect.signature(getattr(self.admin_view, method)).parameters.keys())
                self.assertEqual(exp_params, actual_params, f"The parameter for the method {method} is incorrect.")


if __name__ == '__main__':
    unittest.main()
