import os
import tkinter as tk
from tkinter import Label
from tkinter import Entry
from tkinter import messagebox
from tkinter import Button


class LoginView(tk.Tk):
    """
    A login window for login to the quiz system using username and password.

    Author: Amal Abueshareik
    """

    # Defined class attributes.
    logo_label: Label
    title_label: Label
    username_label: Label
    username_entry: Entry
    password_label: Label
    password_entry: Entry
    login_button: Button

    def __init__(self):
        """
        Initialize the login form
        """
        super().__init__()
        self.title("Login Form")
        self.resizable(width=False, height=False)

        # Create widgets
        self.create_widgets()

        # Center the window
        self.center_window()

    def create_widgets(self):
        """ Create and place widgets in the view """
        # Create login form logo
        logo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'resources', 'login.png'))
        logo = tk.PhotoImage(file=logo_path)
        self.logo_label = tk.Label(self, image=logo, background="#f0f0f0")
        self.logo_label.image = logo

        # Create title label and add properties
        self.title_label = tk.Label(text="Login", font=("Source Serif Pro", 18), fg="#333", bg="#f0f0f0")

        # Create username label and entry and add properties
        self.username_label = tk.Label(self, text="Username:", font=("Source Serif Pro", 14, "italic"), fg="#333",
                                       bg="#f0f0f0")
        self.username_entry = tk.Entry(self, font=("Source Serif Pro", 14, "italic"))

        # Create password label and entry and add properties
        self.password_label = tk.Label(self, text="Password:", font=("Source Serif Pro", 14, "italic"), fg="#333",
                                       bg="#f0f0f0")
        self.password_entry = tk.Entry(self, show="*", font=("Source Serif Pro", 14, "italic"))

        # Create login button and add properties
        self.login_button = tk.Button(self, text="Login", bg="#90CAF9")

        # Placing the widgets in the view
        self.logo_label.grid(row=0, columnspan=2, pady=20)
        self.title_label.grid(row=1, columnspan=2, padx=160)
        self.username_label.grid(row=2, sticky="w", pady=(0, 5), padx=(90, 0))
        self.username_entry.grid(row=3, sticky="ew", padx=(90, 20))
        self.password_label.grid(row=4, sticky="w", pady=(0, 5), padx=(90, 0))
        self.password_entry.grid(row=5, sticky="ew", padx=(90, 20))
        self.login_button.grid(row=6, pady=15, ipadx=50, ipady=5, padx=(90, 20))

    def get_username(self):
        """ Method to retrieve the username from the login form """
        return self.username_entry.get()

    def get_password(self):
        """ Method to retrieve the password from the login form """
        return self.password_entry.get()

    def login_button_callback(self, callback):
        """
        Callback method to the login button.
        This method should handle the event to login to the admin dashboard.
        """
        self.login_button.config(command=callback)

    @staticmethod
    def display_error_message(error: str):
        """
        Method used to display an error message in a message box.

        Parameters:
        - error (str): The error message
        """
        messagebox.showerror("Error", error)

    def center_window(self):
        """ Method used to center the view window on the center of the screen. """
        # Retrieve the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # The view width
        view_width = 400
        # The view height
        view_height = 450

        x = (screen_width - view_width) // 2
        y = (screen_height - view_height) // 2

        # Set the geometry of the window
        self.geometry(f"{view_width}x{view_height}+{x}+{y}")
