import tkinter as tk

from project_src.views.MenuBar import MenuBar


class StartView:

    """
    A start window for the quiz system, this window contains three buttons
    for start the quiz, admin login and register a new admin.

    Author: Amal Abueshareik
    """

    def __init__(self):
        """ Initialize the Start view of the quiz system. """
        self.root = tk.Tk()
        self.root.title("Quiz System")
        self.root.resizable(width=False, height=False)
        self.root.configure(bg="#f0f0f0")

        # Add a menu bar instance to the view
        menu_bar = MenuBar(self.root)
        self.root.config(menu=menu_bar)

        # Create widgets
        self.create_widgets()

        # Center the window
        self.center_window()

    def create_widgets(self):
        """ Create and place the widgets in the view. """

        # Create title label and add properties
        self.root.title_label = self.create_label("Welcome to Quiz System")
        # Create the start, login and register buttons with the properties
        self.root.start_button = self.create_button("Start Quiz")
        self.root.login_button = self.create_button("Login As Admin")
        self.root.register_button = self.create_button("Register New Admin")

        # Placing the widgets in the view
        self.root.title_label.grid(row=0, padx=160)
        self.root.start_button.grid(row=1, pady=10)
        self.root.login_button.grid(row=2, pady=10)
        self.root.register_button.grid(row=3, pady=10)

    def create_label(self, text: str) -> tk.Label:
        """
        Create label with the properties.

        Parameters:
        - text (str): The label text 'Name'

        Returns:
        - A label with specified priorities
        """
        label = tk.Label(self.root, text=text, font=("Source Serif Pro", 18), bg="#f0f0f0")
        return label

    def create_button(self, text: str) -> tk.Button:
        """
        Create button with the properties.

        Parameters:
        - text (str): The button text 'Name'

        Returns:
        - A button with specified priorities
         """
        button = tk.Button(self.root, text=text, font=("Arial", 12, "italic"), width=20, height=2, bg="#90CAF9")
        return button

    def start_button_callback(self, callback):
        """
        Callback method to the start quiz button.
        This method should handle the event to start the quiz.

        Parameters:
        . callback: The button click event callback
        """
        self.root.start_button.config(command=callback)

    def login_button_callback(self, callback):
        """
        Callback method to the login as admin button.
        This method should handle the event to login to the quiz system as admin.

        Parameters:
        . callback: The button click event callback
        """
        self.root.login_button.config(command=callback)

    def register_button_callback(self, callback):
        """
        Callback method to the register new admin button.
        This method should handle the event to register a new admin to the quiz system.

        Parameters:
        . callback: The button click event callback
        """
        self.root.register_button.config(command=callback)

    def center_window(self):
        """ Method used to center the window on the center of the screen. """
        # Retrieve the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # The view width
        window_width = 600
        # The view height
        window_height = 300

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the geometry of the window
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

