import tkinter as tk
from tkinter import Button
from tkinter import Label

from project_src.views.MenuBar import MenuBar


class StartView(tk.Tk):

    """
    A start window for the quiz system, this window contains three buttons
    for start the quiz, admin login and register a new admin.

    Author: Amal Abueshareik
    """

    # Defined class attributes.
    title_label: Label
    start_button: Button
    login_button: Button
    register_button: Button

    def __init__(self):
        """ Initialize the Start view of the quiz system. """
        super().__init__()
        self.title("Quiz System")
        self.resizable(width=False, height=False)
        self.configure(bg="#f0f0f0")

        # Add a menu bar instance to the view
        menu_bar = MenuBar(self)
        self.config(menu=menu_bar)

        # Create widgets
        self.create_widgets()

        # Center the window
        self.center_window()

    def create_widgets(self):
        """ Create and place the widgets in the view. """

        # Create title label and add properties
        self.title_label = self.create_label("Welcome to Quiz System")
        # Create the start, login and register buttons with the properties
        self.start_button = self.create_button("Start Quiz")
        self.login_button = self.create_button("Login As Admin")
        self.register_button = self.create_button("Register New Admin")

        # Placing the widgets in the view
        self.title_label.grid(row=0, padx=160)
        self.start_button.grid(row=1, pady=10)
        self.login_button.grid(row=2, pady=10)
        self.register_button.grid(row=3, pady=10)

    def create_label(self, text: str) -> tk.Label:
        """
        Create label with the properties.

        Parameters:
        - text (str): The label text 'Name'

        Returns:
        - A label with specified priorities
        """
        label = tk.Label(self, text=text, font=("Source Serif Pro", 18), bg="#f0f0f0")
        return label

    def create_button(self, text: str) -> tk.Button:
        """
        Create button with the properties.

        Parameters:
        - text (str): The button text 'Name'

        Returns:
        - A button with specified priorities
         """
        button = tk.Button(self, text=text, font=("Arial", 12, "italic"), width=20, height=2, bg="#90CAF9")
        return button

    def start_button_callback(self, callback):
        """
        Callback method to the start quiz button.
        This method should handle the event to start the quiz.

        Parameters:
        . callback: The button click event callback
        """
        self.start_button.config(command=callback)

    def login_button_callback(self, callback):
        """
        Callback method to the login as admin button.
        This method should handle the event to login to the quiz system as admin.

        Parameters:
        . callback: The button click event callback
        """
        self.login_button.config(command=callback)

    def register_button_callback(self, callback):
        """
        Callback method to the register new admin button.
        This method should handle the event to register a new admin to the quiz system.

        Parameters:
        . callback: The button click event callback
        """
        self.register_button.config(command=callback)

    def center_window(self):
        """ Method used to center the window on the center of the screen. """
        # Retrieve the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # The view width
        window_width = 600
        # The view height
        window_height = 300

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the geometry of the window
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

