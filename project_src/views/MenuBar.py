import tkinter as tk
from tkinter import messagebox


class MenuBar(tk.Menu):
    """
    A menu bar, this menu bar contains a 'Info' menu option.
    This menu offers usage guide for the quiz system application.

    Author: Amal Abueshareik
    """

    def __init__(self, parent):
        super().__init__(parent)

        # Create the menu bar with the usage guide option
        self.create_menu_bar()

    def create_menu_bar(self):
        """ Method used to create the menu bar including the usage guide menu option. """
        # Create the menu bar
        menu_bar = tk.Menu(self, tearoff=0)

        # Add the 'Info' menu to the menu bar
        self.add_cascade(label='Info', menu=menu_bar)

        # Create Usage Guide menu option
        menu_bar.add_command(label='Usage Guide', command=self.usage_guide_option)

    @staticmethod
    def usage_guide_option():
        """ Message box showing the applications usage guide. """
        messagebox.showinfo("Usage Guide", "Welcome to the Quiz System\n\n"
                                           "Below are the instructions for using the quiz system application:\n\n"
                                           "In the start view, you can choose to:\n"
                                           "- Start the quiz\n"
                                           "- Login as an admin\n"
                                           "- Register as an admin\n\n"
                                           "Starting the Quiz:\n"
                                           "- The quiz consists of 20 multiple-choice questions and includes a timer "
                                           "to track your completion time.\n"
                                           "- Select the correct answer for each question and navigate through the "
                                           "quiz using the 'Next' and 'Previous' buttons.\n "
                                           "- Upon submitting the quiz, your final score and the time taken will be "
                                           "displayed.\n\n "
                                           "Registering as a New Admin:\n"
                                           "- In the registration view, enter a username and password "
                                           "to register as an admin.\n\n "
                                           "Logging in as Admin:\n"
                                           "- After logging in, the admin dashboard will be displayed.\n"
                                           "- As an admin, you can:\n"
                                           "- Select a specific question from the table to update or delete.\n"
                                           "- Add new questions by entering the question text, four options, "
                                           "and indicating the correct option number. Then, click the 'Add' "
                                           "button.\n\n "
                                           "Logging Out:\n"
                                           "- Click 'Logout' to log out of the system. The application will then close.")
