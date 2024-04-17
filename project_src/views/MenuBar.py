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
        # TODO write the application's usage guide in the messagebox when the application is implemented
        messagebox.showinfo("Usage Guide", "The quiz system usage guide")
