import tkinter as tk
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from project_src.models.QuizModel import QuizModel
from project_src.views.AdminView import AdminView

class AdminController:
    """
    AdminController class responsible for handling admin actions such as managing quiz questions.

    Author: Asaad Katbeh
    """

    def __init__(self, root: tk.Tk, quiz_model: QuizModel, admin_view: AdminView):
        """
        Initializes the AdminController with the main root window, the QuizModel, and the AdminView.

        Parameters:
            root (tk.Tk): The main root window of the application.
            quiz_model (QuizModel): The QuizModel instance to manage quiz operations.
            admin_view (AdminView): The AdminView instance to manage admin interactions.
        """
        self.root = root
        self.quiz_model = quiz_model
        self.admin_view = admin_view

        # Set up window close event handler
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.admin_view.add_button_callback(self.add_question)
        self.admin_view.update_button_callback(self.update_question)
        self.admin_view.delete_button_callback(self.delete_question)
        self.admin_view.clear_button_callback(self.clear_entries)
        self.admin_view.bind_table_row_click(self.on_table_row_click)

        # Load initial questions
        self.load_questions()

    def on_closing(self):
        """
        Handle the window close event.
        """
        self.quit()
        self.destroy()

    def load_questions(self):
        """
        Load all quiz questions and update the view.
        """
        self.questions = self.quiz_model.retrieve_all_questions()
        formatted_questions = [
            [q['questionId'], q['questionText'], q['options']['option1'], q['options']['option2'],
             q['options']['option3'], q['options']['option4'],
             q['correctOption']]
            for q in self.questions
        ]

        self.admin_view.update_table(formatted_questions)

    def add_question(self):
        """
        Handle adding a new quiz question.
        """
        question_text = self.admin_view.get_question_text()
        options = [
            self.admin_view.get_first_option(),
            self.admin_view.get_second_option(),
            self.admin_view.get_third_option(),
            self.admin_view.get_fourth_option()
        ]
        correct_option = self.admin_view.get_correct_option()

        success = self.quiz_model.create_question(question_text, options, correct_option)
        if success:
            self.admin_view.clear_input_entries()
            self.load_questions()
        else:
            self.admin_view.display_error_message("Failed to add question.")

    def update_question(self):
        """
        Handle updating an existing quiz question.
        """
        selected_row = self.admin_view.get_table_row()
        if selected_row is None:
            self.admin_view.display_error_message("No question selected.")
            return

        question_id = self.questions[selected_row - 1]['questionId']
        new_text = self.admin_view.get_question_text()
        new_options = [
            self.admin_view.get_first_option(),
            self.admin_view.get_second_option(),
            self.admin_view.get_third_option(),
            self.admin_view.get_fourth_option()
        ]
        new_correct_option = self.admin_view.get_correct_option()

        success = self.quiz_model.update_question(question_id, new_text, new_options, new_correct_option)
        if success:
            self.admin_view.clear_input_entries()
            self.load_questions()
        else:
            self.admin_view.display_error_message("Failed to update question.")

    def delete_question(self):
        """
        Handle deleting a quiz question.
        """
        selected_row = self.admin_view.get_table_row()
        if selected_row is None:
            self.admin_view.display_error_message("No question selected.")
            return

        question_id = self.questions[selected_row - 1]['questionId']
        success = self.quiz_model.delete_question(question_id)
        if success:
            self.admin_view.clear_input_entries()
            self.load_questions()
        else:
            self.admin_view.display_error_message("Failed to delete question.")

    def clear_entries(self):
        """
        Handle clearing all input entries in the view.
        """
        self.admin_view.clear_input_entries()

    def on_table_row_click(self, event):
        """
        Handle clicking on a table row to load the question data into the input fields.

        Parameters:
            event (Event): The event object containing information about the click event.
        """
        selected_row = self.admin_view.get_table_row()
        if selected_row is None:
            return

        question_data = self.quiz_model.retrieve_all_questions()[selected_row - 1]
        self.admin_view.set_question_text(question_data['questionText'])
        self.admin_view.set_first_option(question_data['options']['option1'])
        self.admin_view.set_second_option(question_data['options']['option2'])
        self.admin_view.set_third_option(question_data['options']['option3'])
        self.admin_view.set_fourth_option(question_data['options']['option4'])
        self.admin_view.set_correct_option(question_data['correctOption'])
