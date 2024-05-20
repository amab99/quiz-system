import tkinter as tk
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from project_src.models.AdminModel import AdminModel
from project_src.models.QuizModel import QuizModel
from project_src.views.RegisterView import RegisterView
from project_src.views.LoginView import LoginView
from project_src.views.AdminView import AdminView
from project_src.controllers.AdminController import AdminController


class AdminAuthorizationController:
    """
    AdminAuthorizationController class responsible for handling the user authentication and registration processes.

    Author: Amal Abueshareik
    """

    def __init__(self, root: tk.Tk, admin_model: AdminModel, quiz_model: QuizModel):
        """
        Initializes the AdminAuthorizationController with the main root window, the AdminModel, and the QuizModel.

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

        # Defer initialization of AdminView, RegisterView, and LoginView until needed
        self.admin_view = None
        self.register_view = None
        self.login_view = None

    def on_closing(self):
        """
        Handle the window close event.
        """
        self.root.quit()
        self.root.destroy()

    def show_register_view(self):
        """
        Show the register view to allow a new admin to register.
        """
        if self.register_view is None:
            self.register_view = RegisterView()
            self.register_view.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.register_view.register_button_callback(self.register_admin)
        self.register_view.deiconify()

    def show_login_view(self):
        """
        Show the login view to allow an admin to log in.
        """
        if self.login_view is None:
            self.login_view = LoginView()
            self.login_view.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.login_view.login_button_callback(self.login_admin)
        self.login_view.deiconify()

    def register_admin(self):
        """
        Handle the registration of a new admin.
        """
        username = self.register_view.get_username()
        password = self.register_view.get_password()
        confirm_password = self.register_view.get_confirm_password()

        if password != confirm_password:
            self.register_view.display_error_message("Passwords do not match!")
            return

        success = self.admin_model.register(username, password)
        if success:
            self.register_view.withdraw()
            self.register_view.clear_input_fields()
            self.show_admin_dashboard()
        else:
            self.register_view.display_error_message("Registration failed. Username might already be taken.")

    def login_admin(self):
        """
        Handle the admin login process.
        """
        username = self.login_view.get_username()
        password = self.login_view.get_password()

        success = self.admin_model.authorize(username, password)
        if success:
            self.login_view.withdraw()
            self.login_view.clear_input_fields()
            self.show_admin_dashboard()
        else:
            self.login_view.display_error_message("Invalid username or password.")

    def show_admin_dashboard(self):
        """
        Show the admin dashboard view.
        """
        if self.admin_view is None:
            self.admin_view = AdminView()
            self.admin_view.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.admin_controller = AdminController(self.root, self.quiz_model, self.admin_view)
            self.admin_view.logout_button_callback(self.logout)
        self.admin_view.deiconify()

    def logout(self):
        """
        Handle the logout process.
        """
        self.admin_view.withdraw()
        self.on_closing()

