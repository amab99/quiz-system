import inspect
import os
import sys
import tkinter as tk
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from project_src.controllers.QuizPerformController import QuizPerformController


class TestQuizPerformController(unittest.TestCase):
    """
    Unit tests for the QuizPerformController class to ensure proper handling of quiz performance actions.

    @Author: Asaad Katbeh
    """

    @patch('project_src.views.PerformQuizView')
    @patch('project_src.models.QuizModel')
    def setUp(self, MockQuizModel, MockPerformQuizView):
        """
        Set up the test environment for each test case.

        Parameters:
            MockQuizModel (Mock): Mock for the QuizModel class.
            MockPerformQuizView (Mock): Mock for the PerformQuizView class.
        """
        self.root = tk.Tk()
        self.quiz_model = MockQuizModel()
        self.perform_quiz_view = MockPerformQuizView()

        # Mock the questions to ensure they are populated
        self.sample_questions = [
            {'questionText': 'Question 1', 'options': {'option1': 'A', 'option2': 'B', 'option3': 'C', 'option4': 'D'},
             'correctOption': '1'},
            {'questionText': 'Question 2', 'options': {'option1': 'A', 'option2': 'B', 'option3': 'C', 'option4': 'D'},
             'correctOption': '2'}]
        self.quiz_model.retrieve_all_questions.return_value = self.sample_questions

        self.controller = QuizPerformController(self.root, self.quiz_model, self.perform_quiz_view)

    def tearDown(self):
        """
        Tear down the test environment for each test case.
        """
        self.root.destroy()

    def test_start_quiz(self):
        """
        Test the start_quiz method to ensure it initializes and starts the quiz correctly.
        """
        with patch('time.time', return_value=1000):
            self.controller.start_quiz()
            self.assertEqual(self.controller.start_time, 1000)
            self.assertTrue(self.controller.timer_running)
            self.perform_quiz_view.update_timer.assert_called()
            self.perform_quiz_view.update_question.assert_called()

    def test_update_timer(self):
        """
        Test the update_timer method to ensure it updates the timer correctly.
        """
        with patch('time.time', return_value=1000):
            self.controller.start_time = 990
            self.controller.timer_running = True
            self.controller.update_timer()
            self.perform_quiz_view.update_timer.assert_called_with("Time: 00:10")

    def test_load_question(self):
        """
        Test the load_question method to ensure it loads the current question correctly.
        """
        self.controller.current_question_index = 0
        self.controller.user_answers[0] = None

        # Reset mock call history
        self.perform_quiz_view.reset_mock()

        self.controller.load_question()

        self.perform_quiz_view.update_question.assert_called_once_with('Question 1', 'A', 'B', 'C', 'D')
        self.perform_quiz_view.clear_selected_options.assert_called_once()
        self.perform_quiz_view.set_prev_button_enabled.assert_called_once_with(False)
        self.perform_quiz_view.set_next_button_enabled.assert_called_once_with(True)

    def test_next_question(self):
        """
        Test the next_question method to ensure it moves to the next question correctly.
        """
        self.controller.current_question_index = 0
        self.perform_quiz_view.get_selected_option.return_value = 'A'

        self.controller.next_question()

        self.assertEqual(self.controller.current_question_index, 1)
        self.perform_quiz_view.update_question.assert_called_with('Question 2', 'A', 'B', 'C', 'D')
        self.assertEqual(self.controller.user_answers[0], 'A')

    def test_prev_question(self):
        """
        Test the prev_question method to ensure it moves to the previous question correctly.
        """
        self.controller.current_question_index = 1
        self.perform_quiz_view.get_selected_option.return_value = 'B'

        self.controller.prev_question()

        self.assertEqual(self.controller.current_question_index, 0)
        self.perform_quiz_view.update_question.assert_called_with('Question 1', 'A', 'B', 'C', 'D')
        self.assertEqual(self.controller.user_answers[1], 'B')

    def test_submit_quiz(self):
        """
        Test the submit_quiz method to ensure it handles quiz submission and shows the results correctly.
        """
        self.controller.current_question_index = 1
        self.perform_quiz_view.get_selected_option.return_value = 'B'
        self.controller.user_answers = ['A', 'B']

        with patch('time.time', return_value=1010):
            self.controller.start_time = 1000
            self.controller.submit_quiz()

            self.assertFalse(self.controller.timer_running)
            self.assertEqual(self.controller.correct_answers, 2)
            self.perform_quiz_view.show_results.assert_called_once_with(
                "You answered 2 out of 2 questions correctly.\nTime taken: 00:10")

    def test_method_existence(self):
        """
        Tests that all expected methods exist in the QuizPerformController class.
        """
        expected_methods = ['start_quiz', 'update_timer', 'load_question', 'next_question', 'prev_question',
                            'submit_quiz']
        actual_methods = [method for method in dir(self.controller) if
                          callable(getattr(self.controller, method)) and not method.startswith('__')]

        for method in expected_methods:
            self.assertIn(method, actual_methods, f"Expected method {method} not found in QuizPerformController class.")

    def test_private_method_naming(self):
        """
        Verifies that all intended private methods in the QuizPerformController class start with an underscore,
        adhering to the naming convention for private methods.
        """
        private_attributes = ['_root', '_quiz_model', '_perform_quiz_view', '_start_time', '_timer_running',
                              '_current_question_index', '_user_answers', '_correct_answers']
        for attr in private_attributes:
            self.assertTrue(attr.startswith('_'), f"Attribute {attr} should be private (start with an underscore).")

    def test_public_method_naming(self):
        """
        Verifies that all intended public methods in the QuizPerformController class do not start with an underscore,
        following the naming convention for public methods.
        """
        public_methods = ['start_quiz', 'update_timer', 'load_question', 'next_question', 'prev_question',
                          'submit_quiz']
        for method in public_methods:
            self.assertFalse(method.startswith('_'),
                             f"Method {method} should be public (not start with an underscore).")

    def test_method_signatures(self):
        """
        Verifies that the method signatures for key methods in the QuizPerformController class match the expected
        parameter
        names, ensuring consistency and clarity in method definitions.
        """
        signatures = {'start_quiz': [], 'update_timer': [], 'load_question': [], 'next_question': [],
            'prev_question': [], 'submit_quiz': []}

        for method, expected_params in signatures.items():
            with self.subTest(method=method):
                actual_params = list(inspect.signature(getattr(self.controller, method)).parameters.keys())
                self.assertEqual(expected_params, actual_params, f"Signature for method {method} is incorrect.")


if __name__ == '__main__':
    unittest.main()
