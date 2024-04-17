import unittest
import os
import sys
import tkinter as tk
from unittest.mock import patch
from unittest.mock import MagicMock

from project_src.views.MenuBar import MenuBar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


class MenuBarTest(unittest.TestCase):

    """
    Class that contains unit tests for the MenuBar class to ensure menu bar creation,
    including the child widgets and the messagebox creation.

    Author: Amal Abueshareik
    """

    def setUp(self):
        """ Setup method to create a menu bar instance before each test. """
        self.root = tk.Tk()
        self.menu_bar = MenuBar(self.root)

    def tearDown(self):
        """ Method to destroy the Tk root window after each test. """
        self.root.destroy()

    def test_create_menu_bar(self):
        """
        Test method to test the creation of the menu bar including 2 child widgets.

         Raises:
        - AssertionError: If error when creating the menu bar or any child widget
        """

        self.menu_bar.create_menu_bar()
        self.assertEqual(len(self.menu_bar.winfo_children()), 2)
        self.assertIsInstance(self.menu_bar.winfo_children()[0], tk.Menu)
        self.assertIsInstance(self.menu_bar.winfo_children()[1], tk.Menu)

    @patch('tkinter.messagebox.showinfo')
    def test_usage_guide_option(self, mock_messagebox: MagicMock):
        """
        Test the creation of the message box.

         Parameters:
        - mock (MagickMock): MagicMock object to mock the messagebox
        """
        self.menu_bar.usage_guide_option()
        mock_messagebox.assert_called_once()


if __name__ == '__main__':
    unittest.main()
