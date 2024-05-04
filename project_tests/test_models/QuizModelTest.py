import inspect
import os
import sys
import unittest
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from project_src.database.DatabaseManager import DatabaseManager
from project_src.models.QuizModel import QuizModel


class QuizModelTest(unittest.TestCase):
    """
    Unit tests for the QuizModel class to ensure it handles quiz question creation,
    retrieval, updating, and deletion correctly.

    Author: Asaad Katbeh
    """

    def setUp(self):
        """
        Prepare resources for each test.
        """
        self.db_manager = MagicMock(spec=DatabaseManager)
        self.quiz_model = QuizModel(self.db_manager)

    def test_create_question_success(self):
        """
        Test successful creation of a new quiz question.
        """
        self.db_manager.add_question.return_value = None
        result = self.quiz_model.create_question("What is the capital of Sweden?",
                                                 ["London", "Stockholm", "Berlin", "Madrid"], 2)
        self.assertTrue(result)
        self.db_manager.add_question.assert_called_once_with("What is the capital of Sweden?",
                                                             ["London", "Stockholm", "Berlin", "Madrid"], 2)

    def test_create_question_failure_invalid_option_count(self):
        """
        Test failed creation due to incorrect number of options.
        """
        result = self.quiz_model.create_question("What is the capital of Sweden?",
                                                 ["Stockholm", "Berlin"], 1)
        self.assertFalse(result)

    def test_create_question_failure_invalid_correct_option(self):
        """
        Test failed creation due to an invalid index for the correct option.
        """
        result = self.quiz_model.create_question("What is the capital of Sweden?",
                                                 ["London", "Stockholm", "Berlin", "Madrid"], 5)
        self.assertFalse(result)

    def test_retrieve_all_questions(self):
        """
        Test retrieval of all quiz questions.
        """
        questions = [{'questionId': 1, 'questionText': "What is the capital of Sweden?",
                      'options': {'option1': "London", 'option2': "Stockholm", 'option3': "Berlin",
                                  'option4': "Madrid"}, 'correctOption': 2}]
        self.db_manager.retrieve_quiz_questions.return_value = questions

        result = self.quiz_model.retrieve_all_questions()
        self.assertEqual(result, questions)

    def test_update_question_success(self):
        """
        Test successful updating of an existing quiz question.
        """
        self.db_manager.update_question.return_value = None
        result = self.quiz_model.update_question(1, "What is the capital of Germany?",
                                                 ["London", "Berlin", "Paris", "Madrid"], 2)
        self.assertTrue(result)
        self.db_manager.update_question.assert_called_once_with(1, "What is the capital of Germany?",
                                                                ["London", "Berlin", "Paris", "Madrid"], 2)

    def test_update_question_failure_invalid_option_count(self):
        """
        Test failed update due to incorrect number of options.
        """
        result = self.quiz_model.update_question(1, "What is the capital of Germany?",
                                                 ["Berlin", "Paris"], 1)
        self.assertFalse(result)

    def test_update_question_failure_invalid_correct_option(self):
        """
        Test failed update due to an invalid index for the correct option.
        """
        result = self.quiz_model.update_question(1, "What is the capital of Germany?",
                                                 ["London", "Berlin", "Paris", "Madrid"], 5)
        self.assertFalse(result)

    def test_delete_question(self):
        """
        Test deletion of a quiz question.
        """
        self.db_manager.delete_question.return_value = None
        result = self.quiz_model.delete_question(1)
        self.assertTrue(result)
        self.db_manager.delete_question.assert_called_once_with(1)

    def test_method_existence(self):
        """
        Tests that all expected methods exist in the QuizModel class.
        """
        expected_methods = ['create_question', 'retrieve_all_questions', 'update_question', 'delete_question']
        actual_methods = [method for method in dir(self.quiz_model) if
                          callable(getattr(self.quiz_model, method)) and not method.startswith('__')]

        for method in expected_methods:
            self.assertIn(method, actual_methods, f"Expected method {method} not found in QuizModel class.")

    def test_method_signatures(self):
        """
        Verifies that the method signatures for key methods in the QuizModel class match the expected parameter names.
        """
        signatures = {'create_question': ['question_text', 'options', 'correct_option'], 'retrieve_all_questions': [],
                      'update_question': ['question_id', 'new_text', 'new_options', 'new_correct_option'],
                      'delete_question': ['question_id']}

        for method, expected_params in signatures.items():
            with self.subTest(method=method):
                actual_params = list(inspect.signature(getattr(self.quiz_model, method)).parameters.keys())
                self.assertEqual(expected_params, actual_params, f"Signature for method {method} is incorrect.")

    def tearDown(self):
        """
        Clean up resources after each test.
        """
        pass


if __name__ == '__main__':
    unittest.main()
