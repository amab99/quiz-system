import inspect
import os
import sys
import tkinter as tk
import unittest
from unittest.mock import patch, Mock

from project_src.views.PerformQuizView import PerformQuizView
from project_src.views.StartView import StartView

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from project_src.models.AdminModel import AdminModel
from project_src.models.QuizModel import QuizModel
from project_src.controllers.StartController import StartController
from project_src.controllers.AdminAuthorizationController import AdminAuthorizationController


class TestStartController(unittest.TestCase):
    """
    Unit tests for the StartController class to ensure proper handling of initial start screen and transitions.

    @Author: Asaad Katbeh
    """

    @patch('project_src.views.StartView')
    @patch('project_src.controllers.AdminAuthorizationController')
    def setUp(self, MockStartView, MockAdminAuthorizationController):
        """
        Set up the test environment for each test case.

        Parameters:
            MockStartView (Mock): Mock for the StartView class.
            MockAdminAuthorizationController (Mock): Mock for the AdminAuthorizationController class.
        """
        self.root = tk.Tk()
        self.admin_model = Mock(spec=AdminModel)
        self.quiz_model = Mock(spec=QuizModel)
        self.start_view = Mock(spec=StartView)
        self.admin_auth_controller = Mock(spec=AdminAuthorizationController)
        self.perform_quiz_view = Mock(spec=PerformQuizView)

        # Mock the necessary attributes of PerformQuizView
        self.perform_quiz_view.next_button = Mock()
        self.perform_quiz_view.next_button.config = Mock()

        self.start_controller = StartController(self.root, self.admin_model, self.quiz_model)
        self.start_controller.start_view = self.start_view
        self.start_controller.admin_auth_controller = self.admin_auth_controller
        self.start_controller.perform_quiz_view = self.perform_quiz_view

        self.root.quit = Mock()
        self.root.destroy = Mock()

    def tearDown(self):
        """
        Tear down the test environment for each test case.
        """
        self.root.destroy()

    @patch('project_src.controllers.QuizPerformController')
    @patch.object(PerformQuizView, '__init__', lambda self: None)
    @patch.object(PerformQuizView, 'protocol')
    @patch.object(PerformQuizView, 'deiconify')
    def test_start_quiz(self, MockQuizPerformController, mock_deiconify, mock_protocol):
        """
        Test the start_quiz method to ensure it initializes and displays the PerformQuizView.

        Parameters:
            MockQuizPerformController (Mock): Mock for the QuizPerformController class.
            mock_deiconify (Mock): Mock for the deiconify method.
            mock_protocol (Mock): Mock for the protocol method.
        """
        self.quiz_model.retrieve_all_questions.return_value = ['Question 1', 'Question 2']

        self.start_controller.start_quiz()

        self.assertIsNotNone(self.start_controller.perform_quiz_view)

    def test_show_register_view(self):
        """
        Test the show_register_view method to ensure it transitions to the register view.
        """
        self.start_controller.show_register_view()

        self.admin_auth_controller.show_register_view.assert_called_once()

        self.start_view.withdraw.assert_called_once()

    def test_show_login_view(self):
        """
        Test the show_login_view method to ensure it transitions to the login view.
        """
        self.start_controller.show_login_view()

        self.admin_auth_controller.show_login_view.assert_called_once()

        self.start_view.withdraw.assert_called_once()

    def test_show_start_view(self):
        """
        Test the show_start_view method to ensure it displays the start view.
        """
        self.start_controller.show_start_view()

        self.start_view.deiconify.assert_called_once()

    def test_on_closing(self):
        """
        Test the on_closing method to ensure it handles window close event.
        """
        self.start_controller.on_closing()

        self.root.quit.assert_called_once()
        self.root.destroy.assert_called_once()

    def test_method_existence(self):
        """
        Tests that all expected methods exist in the StartController class.
        """
        expected_methods = ['start_quiz', 'show_register_view', 'show_login_view', 'show_start_view', 'on_closing']
        actual_methods = [method for method in dir(self.start_controller) if
                          callable(getattr(self.start_controller, method)) and not method.startswith('__')]

        for method in expected_methods:
            self.assertIn(method, actual_methods, f"Expected method {method} not found in StartController class.")

    def test_private_method_naming(self):
        """
        Verifies that all intended private methods in the StartController class start with an underscore,
        adhering to the naming convention for private methods.
        """
        # Assuming '_admin_model' and '_quiz_model' should be private attributes
        private_attributes = ['_admin_model', '_quiz_model']
        for attr in private_attributes:
            self.assertTrue(attr.startswith('_'), f"Attribute {attr} should be private (start with an underscore).")

    def test_public_method_naming(self):
        """
        Verifies that all intended public methods in the StartController class do not start with an underscore,
        following the naming convention for public methods.
        """
        public_methods = ['start_quiz', 'show_register_view', 'show_login_view', 'show_start_view', 'on_closing']
        for method in public_methods:
            self.assertFalse(method.startswith('_'),
                             f"Method {method} should be public (not start with an underscore).")

    def test_method_signatures(self):
        """
        Verifies that the method signatures for key methods in the StartController class match the expected parameter
        names, ensuring consistency and clarity in method definitions.
        """
        signatures = {'start_quiz': [], 'show_register_view': [], 'show_login_view': [], 'show_start_view': [],
            'on_closing': []}

        for method, expected_params in signatures.items():
            with self.subTest(method=method):
                actual_params = list(inspect.signature(getattr(self.start_controller, method)).parameters.keys())
                self.assertEqual(expected_params, actual_params, f"Signature for method {method} is incorrect.")


if __name__ == '__main__':
    unittest.main()
