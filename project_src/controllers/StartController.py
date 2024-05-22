import os
import sys
import tkinter as tk

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from project_src.models.AdminModel import AdminModel
from project_src.models.QuizModel import QuizModel
from project_src.views.StartView import StartView
from project_src.controllers.AdminAuthorizationController import AdminAuthorizationController
from project_src.controllers.QuizPerformController import QuizPerformController
from project_src.views.PerformQuizView import PerformQuizView


class StartController:
    """
    StartController class responsible for handling the initial start screen and transitions to other controllers.

    Author: Asaad Katbeh
    """

    def __init__(self, root: tk.Tk, admin_model: AdminModel, quiz_model: QuizModel):
        """
        Initializes the StartController with the main root window, the AdminModel, and the QuizModel.

        Parameters:
            root (tk.Tk): The main root window of the application.
            admin_model (AdminModel): The AdminModel instance to manage admin operations.
            quiz_model (QuizModel): The QuizModel instance to manage quiz operations.
        """
        self.root = root
        self.admin_model = admin_model
        self.quiz_model = quiz_model

        # Set up window close event handler
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Initialize the StartView
        self.start_view = StartView()
        self.start_view.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.start_view.start_button_callback(self.start_quiz)
        self.start_view.login_button_callback(self.show_login_view)
        self.start_view.register_button_callback(self.show_register_view)

        # Initialize AdminAuthorizationController and defer initialization of PerformQuizView until needed
        self.admin_auth_controller = AdminAuthorizationController(root, admin_model, quiz_model)
        self.perform_quiz_view = None

        # Show the StartView initially
        self.start_view.deiconify()

    def on_closing(self):
        """
        Handle the window close event.
        """
        self.root.quit()
        self.root.destroy()

    def start_quiz(self):
        """
        Start the quiz. Initialize PerformQuizView and QuizPerformController if not already done.
        """
        if self.perform_quiz_view is None:
            self.perform_quiz_view = PerformQuizView()
            self.perform_quiz_view.protocol("WM_DELETE_WINDOW", self.on_closing)
            QuizPerformController(self.root, self.quiz_model, self.perform_quiz_view)
        self.perform_quiz_view.deiconify()
        self.start_view.withdraw()

    def show_register_view(self):
        """
        Show the register view through the AdminAuthorizationController.
        """
        self.admin_auth_controller.show_register_view()
        self.start_view.withdraw()

    def show_login_view(self):
        """
        Show the login view through the AdminAuthorizationController.
        """
        self.admin_auth_controller.show_login_view()
        self.start_view.withdraw()

    def show_start_view(self):
        """
        Show the start view.
        """
        self.start_view.deiconify()
        self.start_view.show_information()
