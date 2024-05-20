import os
import sys
import time
import tkinter as tk

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from project_src.models.QuizModel import QuizModel
from project_src.views.PerformQuizView import PerformQuizView


class QuizPerformController:
    """
    QuizPerformController class responsible for handling the quiz performance actions such as starting the quiz,
    loading questions, handling user answers, and showing the results.

    Author: Asaad Katbeh
    """

    def __init__(self, root: tk.Tk, quiz_model: QuizModel, perform_quiz_view: PerformQuizView):
        """
        Initializes the QuizPerformController with the main root window, the QuizModel, and the PerformQuizView.

        Parameters:
            root (tk.Tk): The main root window of the application.
            quiz_model (QuizModel): The QuizModel instance to manage quiz operations.
            perform_quiz_view (PerformQuizView): The PerformQuizView instance to manage quiz interactions.
        """
        self.root = root
        self.quiz_model = quiz_model
        self.perform_quiz_view = perform_quiz_view

        # Set up window close event handler
        self.perform_quiz_view.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Initialize quiz variables
        self.current_question_index = 0
        self.correct_answers = 0
        self.questions = self.quiz_model.retrieve_all_questions()
        self.user_answers = [None] * len(self.questions)  # List to store user answers
        self.start_time = None
        self.timer_running = False

        # Set up callbacks for the view
        self.perform_quiz_view.add_next_button_callback(self.next_question)
        self.perform_quiz_view.add_prev_button_callback(self.prev_question)
        self.perform_quiz_view.add_submit_button_callback(self.submit_quiz)

        # Load the first question and start the timer
        self.start_quiz()

    def on_closing(self):
        """
        Handle the window close event.
        """
        self.root.quit()
        self.root.destroy()

    def start_quiz(self):
        """
        Start the quiz and the timer.
        """
        self.start_time = time.time()
        self.timer_running = True
        self.update_timer()
        self.load_question()

    def update_timer(self):
        """
        Update the timer label every second.
        """
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            minutes, seconds = divmod(elapsed_time, 60)
            self.perform_quiz_view.update_timer(f"Time: {minutes:02}:{seconds:02}")
            self.root.after(1000, self.update_timer)

    def load_question(self):
        """
        Load the current question and update the view.
        """
        question = self.questions[self.current_question_index]
        self.perform_quiz_view.update_question(question['questionText'], question['options']['option1'],
            question['options']['option2'], question['options']['option3'], question['options']['option4'])

        # Set previously selected answer if available
        if self.user_answers[self.current_question_index] is not None:
            self.perform_quiz_view.set_selected_option(self.user_answers[self.current_question_index])
        else:
            self.perform_quiz_view.clear_selected_options()

        # Enable/disable buttons based on question index
        self.perform_quiz_view.set_prev_button_enabled(self.current_question_index > 0)
        self.perform_quiz_view.set_next_button_enabled(self.current_question_index < len(self.questions) - 1)

    def next_question(self):
        """
        Handle the event of moving to the next question.
        """
        # Save the current answer
        self.user_answers[self.current_question_index] = self.perform_quiz_view.get_selected_option()

        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.load_question()

    def prev_question(self):
        """
        Handle the event of moving to the previous question.
        """
        # Save the current answer
        self.user_answers[self.current_question_index] = self.perform_quiz_view.get_selected_option()

        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.load_question()

    def submit_quiz(self):
        """
        Handle the event of submitting the entire quiz.
        """
        # Save the current answer
        self.user_answers[self.current_question_index] = self.perform_quiz_view.get_selected_option()

        # Calculate correct answers
        self.correct_answers = 0
        for index, question in enumerate(self.questions):
            if self.user_answers[index] == question['options'][f"option{question['correctOption']}"]:
                self.correct_answers += 1

        self.timer_running = False  # Stop the timer
        self.show_results()

    def show_results(self):
        """
        Show the quiz results in the view.
        """
        elapsed_time = int(time.time() - self.start_time)
        minutes, seconds = divmod(elapsed_time, 60)
        result_message = f"You answered {self.correct_answers} out of {len(self.questions)} questions correctly.\n" \
                         f"Time taken: {minutes:02}:{seconds:02}"
        self.perform_quiz_view.show_results(result_message)
