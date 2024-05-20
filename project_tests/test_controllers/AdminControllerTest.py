import inspect
import unittest
from unittest.mock import patch, Mock
import tkinter as tk
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from project_src.controllers.AdminController import AdminController

class TestAdminController(unittest.TestCase):
    """
    Unit tests for the AdminController class to ensure proper handling of admin actions.

    @Author: Asaad Katbeh
    """

    @patch('project_src.views.AdminView')
    @patch('project_src.models.QuizModel')
    def setUp(self, MockQuizModel, MockAdminView):
        """
        Set up the test environment for each test case.

        Parameters:
            MockQuizModel (Mock): Mock for the QuizModel class.
            MockAdminView (Mock): Mock for the AdminView class.
        """
        self.root = tk.Tk()
        self.quiz_model = MockQuizModel()
        self.admin_view = MockAdminView()
        self.controller = AdminController(self.root, self.quiz_model, self.admin_view)

    def tearDown(self):
        """
        Tear down the test environment for each test case.
        """
        self.root.destroy()

    def test_load_questions(self):
        """
        Test the load_questions method to ensure it retrieves and updates the view with questions.
        """
        sample_questions = [
            {'questionId': 1, 'questionText': 'Sample Question 1', 'options': {'option1': 'A', 'option2': 'B', 'option3': 'C', 'option4': 'D'}, 'correctOption': 'A'},
            {'questionId': 2, 'questionText': 'Sample Question 2', 'options': {'option1': 'A', 'option2': 'B', 'option3': 'C', 'option4': 'D'}, 'correctOption': 'B'},
        ]
        self.quiz_model.retrieve_all_questions.return_value = sample_questions

        self.admin_view.reset_mock()

        self.controller.load_questions()

        formatted_questions = [
            [1, 'Sample Question 1', 'A', 'B', 'C', 'D', 'A'],
            [2, 'Sample Question 2', 'A', 'B', 'C', 'D', 'B']
        ]
        self.admin_view.update_table.assert_called_once_with(formatted_questions)

    def test_add_question_success(self):
        """
        Test the add_question method to ensure it adds a question successfully.
        """
        self.admin_view.get_question_text.return_value = "New Question"
        self.admin_view.get_first_option.return_value = "A"
        self.admin_view.get_second_option.return_value = "B"
        self.admin_view.get_third_option.return_value = "C"
        self.admin_view.get_fourth_option.return_value = "D"
        self.admin_view.get_correct_option.return_value = "A"
        self.quiz_model.create_question.return_value = True

        self.controller.add_question()

        self.admin_view.clear_input_entries.assert_called_once()
        self.admin_view.display_error_message.assert_not_called()
        self.quiz_model.create_question.assert_called_once_with("New Question", ["A", "B", "C", "D"], "A")

    def test_add_question_failure(self):
        """
        Test the add_question method to ensure it handles failure.
        """
        self.admin_view.get_question_text.return_value = "New Question"
        self.admin_view.get_first_option.return_value = "A"
        self.admin_view.get_second_option.return_value = "B"
        self.admin_view.get_third_option.return_value = "C"
        self.admin_view.get_fourth_option.return_value = "D"
        self.admin_view.get_correct_option.return_value = "A"
        self.quiz_model.create_question.return_value = False

        self.controller.add_question()

        self.admin_view.display_error_message.assert_called_once_with("Failed to add question.")
        self.admin_view.clear_input_entries.assert_not_called()

    def test_update_question_success(self):
        """
        Test the update_question method to ensure it updates a question successfully.
        """
        sample_questions = [{'questionId': 1, 'questionText': 'Old Question', 'options': {'option1': 'A', 'option2': 'B', 'option3': 'C', 'option4': 'D'}, 'correctOption': 'A'}]
        self.controller.questions = sample_questions
        self.admin_view.get_table_row.return_value = 1
        self.admin_view.get_question_text.return_value = "Updated Question"
        self.admin_view.get_first_option.return_value = "A"
        self.admin_view.get_second_option.return_value = "B"
        self.admin_view.get_third_option.return_value = "C"
        self.admin_view.get_fourth_option.return_value = "D"
        self.admin_view.get_correct_option.return_value = "A"
        self.quiz_model.update_question.return_value = True

        self.controller.update_question()

        self.admin_view.clear_input_entries.assert_called_once()
        self.admin_view.display_error_message.assert_not_called()
        self.quiz_model.update_question.assert_called_once_with(1, "Updated Question", ["A", "B", "C", "D"], "A")

    def test_update_question_failure(self):
        """
        Test the update_question method to ensure it handles failure.
        """
        sample_questions = [{'questionId': 1, 'questionText': 'Old Question', 'options': {'option1': 'A', 'option2': 'B', 'option3': 'C', 'option4': 'D'}, 'correctOption': 'A'}]
        self.controller.questions = sample_questions
        self.admin_view.get_table_row.return_value = 1
        self.admin_view.get_question_text.return_value = "Updated Question"
        self.admin_view.get_first_option.return_value = "A"
        self.admin_view.get_second_option.return_value = "B"
        self.admin_view.get_third_option.return_value = "C"
        self.admin_view.get_fourth_option.return_value = "D"
        self.admin_view.get_correct_option.return_value = "A"
        self.quiz_model.update_question.return_value = False

        self.controller.update_question()

        self.admin_view.display_error_message.assert_called_once_with("Failed to update question.")
        self.admin_view.clear_input_entries.assert_not_called()

    def test_delete_question_success(self):
        """
        Test the delete_question method to ensure it deletes a question successfully.
        """
        sample_questions = [{'questionId': 1, 'questionText': 'Old Question', 'options': {'option1': 'A', 'option2': 'B', 'option3': 'C', 'option4': 'D'}, 'correctOption': 'A'}]
        self.controller.questions = sample_questions
        self.admin_view.get_table_row.return_value = 1
        self.quiz_model.delete_question.return_value = True

        self.controller.delete_question()

        self.admin_view.clear_input_entries.assert_called_once()
        self.admin_view.display_error_message.assert_not_called()
        self.quiz_model.delete_question.assert_called_once_with(1)

    def test_delete_question_failure(self):
        """
        Test the delete_question method to ensure it handles failure.
        """
        sample_questions = [{'questionId': 1, 'questionText': 'Old Question', 'options': {'option1': 'A', 'option2': 'B', 'option3': 'C', 'option4': 'D'}, 'correctOption': 'A'}]
        self.controller.questions = sample_questions
        self.admin_view.get_table_row.return_value = 1
        self.quiz_model.delete_question.return_value = False

        self.controller.delete_question()

        self.admin_view.display_error_message.assert_called_once_with("Failed to delete question.")
        self.admin_view.clear_input_entries.assert_not_called()

    def test_clear_entries(self):
        """
        Test the clear_entries method to ensure it clears input entries.
        """
        self.controller.clear_entries()
        self.admin_view.clear_input_entries.assert_called_once()

    def test_on_table_row_click(self):
        """
        Test the on_table_row_click method to ensure it loads the correct question data into input fields.
        """
        sample_questions = [{'questionId': 1, 'questionText': 'Sample Question', 'options': {'option1': 'A', 'option2': 'B', 'option3': 'C', 'option4': 'D'}, 'correctOption': 'A'}]
        self.quiz_model.retrieve_all_questions.return_value = sample_questions
        self.admin_view.get_table_row.return_value = 1

        event = Mock()
        self.controller.on_table_row_click(event)

        self.admin_view.set_question_text.assert_called_once_with('Sample Question')
        self.admin_view.set_first_option.assert_called_once_with('A')
        self.admin_view.set_second_option.assert_called_once_with('B')
        self.admin_view.set_third_option.assert_called_once_with('C')
        self.admin_view.set_fourth_option.assert_called_once_with('D')
        self.admin_view.set_correct_option.assert_called_once_with('A')



    def test_method_existence(self):
        """
        Tests that all expected methods exist in the AdminController class.
        """
        expected_methods = ['load_questions', 'add_question', 'update_question', 'delete_question', 'clear_entries', 'on_table_row_click']
        actual_methods = [method for method in dir(self.controller) if
                          callable(getattr(self.controller, method)) and not method.startswith('__')]

        for method in expected_methods:
            self.assertIn(method, actual_methods, f"Expected method {method} not found in AdminController class.")

    def test_private_method_naming(self):
        """
        Verifies that all intended private methods in the AdminController class start with an underscore,
        adhering to the naming convention for private methods.
        """
        private_attributes = ['_root', '_quiz_model', '_admin_view']
        for attr in private_attributes:
            self.assertTrue(attr.startswith('_'), f"Attribute {attr} should be private (start with an underscore).")

    def test_public_method_naming(self):
        """
        Verifies that all intended public methods in the AdminController class do not start with an underscore,
        following the naming convention for public methods.
        """
        public_methods = ['load_questions', 'add_question', 'update_question', 'delete_question', 'clear_entries', 'on_table_row_click']
        for method in public_methods:
            self.assertFalse(method.startswith('_'),
                             f"Method {method} should be public (not start with an underscore).")

    def test_method_signatures(self):
        """
        Verifies that the method signatures for key methods in the AdminController class match the expected parameter
        names, ensuring consistency and clarity in method definitions.
        """
        signatures = {
            'load_questions': [],
            'add_question': [],
            'update_question': [],
            'delete_question': [],
            'clear_entries': [],
            'on_table_row_click': ['event']
        }

        for method, expected_params in signatures.items():
            with self.subTest(method=method):
                actual_params = list(inspect.signature(getattr(self.controller, method)).parameters.keys())
                self.assertEqual(expected_params, actual_params, f"Signature for method {method} is incorrect.")


if __name__ == '__main__':
    unittest.main()
