import tkinter as tk
from tkinter import messagebox
import os


class RegisterView:
    """
    A register window for register new admin to the quiz system by username and password.

    Author: Amal Abueshareik
    """

    def __init__(self):
        """
        Initialize the register form
        """
        self.root = tk.Tk()
        self.root.title("Register Form")
        self.root.resizable(width=False, height=False)

        # Create widgets
        self.create_widgets()

        # Center the window
        self.center_window()

    def create_widgets(self):
        """ Create and place widgets in the view """
        # Create register form logo
        logo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'resources', 'register.png'))
        logo = tk.PhotoImage(file=logo_path)
        self.root.logo_label = tk.Label(self.root, image=logo, background="#f0f0f0")
        self.root.logo_label.image = logo

        # Create title label and add properties
        self.root.title_label = tk.Label(text="Register", font=("Source Serif Pro", 18), fg="#333", bg="#f0f0f0")

        # Create username label and entry and add properties
        self.root.username_label = tk.Label(self.root, text="Username:", font=("Source Serif Pro", 14, "italic"),
                                            fg="#333", bg="#f0f0f0")
        self.root.username_entry = tk.Entry(self.root, font=("Source Serif Pro", 14, "italic"))

        # Create password label and entry and add properties
        self.root.password_label = tk.Label(self.root, text="Password:", font=("Source Serif Pro", 14, "italic"),
                                            fg="#333", bg="#f0f0f0")
        self.root.password_entry = tk.Entry(self.root, show="*", font=("Source Serif Pro", 14, "italic"))
        # Create confirm password label and entry and add properties
        self.root.confirm_password_label = tk.Label(self.root, text="Confirm Password:", font=("Source Serif Pro", 14, "italic"),
                                            fg="#333", bg="#f0f0f0")
        self.root.confirm_password_entry = tk.Entry(self.root, show="*", font=("Source Serif Pro", 14, "italic"))

        # Create register button and add properties
        self.root.register_button = tk.Button(self.root, text="Register", bg="#90CAF9")

        # Placing the widgets in the view
        self.root.logo_label.grid(row=0, columnspan=2, pady=20)
        self.root.title_label.grid(row=1, columnspan=2, padx=160)
        self.root.username_label.grid(row=2, sticky="w", pady=(0, 5), padx=(70, 0))
        self.root.username_entry.grid(row=3, sticky="ew", padx=(70, 20))
        self.root.password_label.grid(row=4, sticky="w", pady=(0, 5), padx=(70, 0))
        self.root.password_entry.grid(row=5, sticky="ew", padx=(70, 20))
        self.root.confirm_password_label.grid(row=6, sticky="w", pady=(0, 5), padx=(70, 0))
        self.root.confirm_password_entry.grid(row=7, sticky="ew", padx=(70, 20))
        self.root.register_button.grid(row=8, pady=15, ipadx=50, ipady=5, padx=(70, 20))

    def get_username(self):
        """ Method to retrieve the username from the register form. """
        return self.root.username_entry.get()

    def get_password(self):
        """ Method to retrieve the password from the register form. """
        return self.root.password_entry.get()

    def get_confirm_password(self):
        """ Method to retrieve the confirmed password from the register form. """
        return self.root.confirm_password_entry.get()

    def register_button_callback(self, callback):
        """
        Callback method to the register button.
        This method should handle the event to register to the quiz system as admin.
        """
        self.root.register_button.config(command=callback)

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
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # The view width
        view_width = 400
        # The view height
        view_height = 450

        x = (screen_width - view_width) // 2
        y = (screen_height - view_height) // 2

        # Set the geometry of the window
        self.root.geometry(f"{view_width}x{view_height}+{x}+{y}")
