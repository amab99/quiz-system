import tkinter as tk
from tkinter.ttk import Treeview
from tkinter import ttk
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import messagebox


class AdminView(tk.Toplevel):
    """
    This class represents the view for the admin to manage the quiz questions data.
    This view contains a Treeview with columns representing the questions with its id, options and correct options.
    It contains entries to the question text, the four options and the correct option.
    This view also contains buttons for add new question, update question, delete question, clear entries and logout.

    @Author: Amal Abueshareik
    """

    # Defined class attributes.
    table: Treeview
    question_label: Label
    question_entry: Entry
    option1_label: Label
    option1_entry: Entry
    option2_label: Label
    option2_entry: Entry
    option3_label: Label
    option3_entry: Entry
    option4_label: Label
    option4_entry: Entry
    correct_option_label: Label
    correct_option_entry: Entry
    add_btn: Button
    clear_btn: Button
    delete_btn: Button
    update_btn: Button
    logout_btn: Button

    def __init__(self):
        """
        Initialize the Admin View
        """
        super().__init__()
        self.title("Admin View")
        self.resizable(width=False, height=False)

        # Create widgets
        self.create_widgets()
        # Center the window
        self.center_window()

    def create_widgets(self):
        """
        Method used to create the widgets by initializing the create Treeview,
        create entries and create buttons methods.
        """
        self.create_tree_view()
        self.create_entries()
        self.create_buttons()

    def create_tree_view(self):
        """ Create Treeview-widget with columns and heading used to display the quiz questions data. """
        style = ttk.Style()
        style.map('Treeview', background=[('selected', '#90CAF9')])
        self.table = ttk.Treeview(self)
        self.table.grid(row=0, column=0, columnspan=6, sticky="news")
        self.table['columns'] = (
            'ID', 'Question', "Option 1", "Option 2", "Option 3", "Option 4", "Correct Option")

        # Create columns
        self.table.column("#0", width=0, stretch=tk.NO)
        self.table.column("ID", anchor=tk.W, width=15)
        self.table.column("Question", anchor=tk.W, width=340)
        self.table.column("Option 1", anchor=tk.W, width=150)
        self.table.column("Option 2", anchor=tk.W, width=150)
        self.table.column("Option 3", anchor=tk.W, width=150)
        self.table.column("Option 4", anchor=tk.W, width=150)
        self.table.column("Correct Option", anchor=tk.W, width=150)

        # Create headings
        self.table.heading("ID", text="ID")
        self.table.heading("Question",  text="Question")
        self.table.heading("Option 1", text="Option 1")
        self.table.heading("Option 2", text="Option 2")
        self.table.heading("Option 3", text="Option 3")
        self.table.heading("Option 4", text="Option 4")
        self.table.heading("Correct Option", text="Correct Option")

    def create_entries(self):
        """
        Create a entries frame including the labels and entries for the question text,
        the four options and the correct option text.
        """
        entries_frame = tk.Frame(self,bg="#f0f0f0", pady=15)
        entries_frame.grid(row=1, column=1, padx=190, pady=10, sticky="news")

        self.question_label = tk.Label(entries_frame, text="Question Text:", font=("Source Serif Pro", 14), fg="#333")
        self.question_label.grid(row=1, column=0, sticky="w")

        self.question_entry = tk.Entry(entries_frame, width=60, font=("Source Serif Pro", 11))
        self.question_entry.grid(row=1, column=1, sticky="w")

        self.option1_label = tk.Label(entries_frame, text="Option 1:", font=("Source Serif Pro", 14), fg="#333")
        self.option1_label.grid(row=2, column=0, sticky="w")

        self.option1_entry = tk.Entry(entries_frame, width=60, font=("Source Serif Pro", 11))
        self.option1_entry.grid(row=2, column=1, sticky="w")

        self.option2_label = tk.Label(entries_frame, text="Option 2:", font=("Source Serif Pro", 14), fg="#333")
        self.option2_label.grid(row=3, column=0, sticky="w")

        self.option2_entry = tk.Entry(entries_frame, width=60, font=("Source Serif Pro", 11))
        self.option2_entry.grid(row=3, column=1, sticky="w")

        self.option3_label = tk.Label(entries_frame, text="Option 3:", font=("Source Serif Pro", 14), fg="#333")
        self.option3_label.grid(row=4, column=0, sticky="w")

        self.option3_entry = tk.Entry(entries_frame, width=60, font=("Source Serif Pro", 11))
        self.option3_entry.grid(row=4, column=1, sticky="w")

        self.option4_label = tk.Label(entries_frame, text="Option 4:", font=("Source Serif Pro", 14), fg="#333")
        self.option4_label.grid(row=5, column=0, sticky="w")

        self.option4_entry = tk.Entry(entries_frame, width=60, font=("Source Serif Pro", 11))
        self.option4_entry.grid(row=5, column=1, sticky="w")

        self.correct_option_label = tk.Label(entries_frame, text="Correct Option:", font=("Source Serif Pro", 14),
                                             fg="#333")
        self.correct_option_label.grid(row=6, column=0, sticky="w")

        self.correct_option_entry = tk.Entry(entries_frame, width=60, font=("Source Serif Pro", 11))
        self.correct_option_entry.grid(row=6, column=1, sticky="w")

    def create_buttons(self):
        """
        Create a navigation frame including the buttons for add new question,
        update existing question, delete question, clear text entries and logout.
        """
        nav_frame = tk.Frame(self,bg="#f0f0f0", pady=15, highlightbackground="#90CAF9", highlightthickness=1)
        nav_frame.grid(row=8, column=1, padx=190, pady=10, sticky="news")

        self.add_btn = tk.Button(nav_frame, text="Add Question", font=("Arial", 12, "italic"), bg="#90CAF9")
        self.add_btn.grid(row=0, column=0, padx=5)

        self.clear_btn = tk.Button(nav_frame, text="Clear Entries", font=("Arial", 12, "italic"), bg="#90CAF9")
        self.clear_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(nav_frame, text="Delete Question", font=("Arial", 12, "italic"), bg="#90CAF9")
        self.delete_btn.grid(row=0, column=2, padx=5)

        self.update_btn = tk.Button(nav_frame, text="Update Question", font=("Arial", 12, "italic"), bg="#90CAF9")
        self.update_btn.grid(row=0, column=3, padx=5)

        self.logout_btn = tk.Button(nav_frame, text="Logout", font=("Arial", 12, "italic"), bg="red")
        self.logout_btn.grid(row=0, column=4, padx=5)

    def get_question_text(self) -> str:
        """
        Method used to get the question text from the text entry.

        Returns:
        - str: A string represents the question text written in the text entry.
        """
        return self.question_entry.get()

    def get_first_option(self) -> str:
        """
        Method used to get the text of the first option from the text entry.

        Returns:
        - str: A string represents the first option written in the text entry.
        """
        return self.option1_entry.get()

    def get_second_option(self) -> str:
        """
        Method used to get the text of the second option from the text entry.

        Returns:
        - str: A string represents the second option written in the text entry.
        """
        return self.option2_entry.get()

    def get_third_option(self) -> str:
        """
        Method used to get the text of the third option from the text entry.

        Returns:
        - str: A string represents the third option written in the text entry.
        """
        return self.option3_entry.get()

    def get_fourth_option(self) -> str:
        """
        Method used to get the text of the fourth option from the text entry.

        Returns:
        - str: A string represents the fourth option written in the text entry.
        """
        return self.option4_entry.get()

    def get_correct_option(self) -> int:
        """
        Method used to get the text of the correct option from the text entry.

        Returns:
        - int: A integer represents the correct option written in the text entry.
        """
        return int(self.correct_option_entry.get())

    def get_table(self) -> ttk.Treeview:
        """
        Method used to get the questions data table.

        Returns:
        - ttk.TreeView: The Treeview widget object with the questions data.
        """
        return self.table

    def get_table_row(self) -> int | None:
        """
        Method used to get the index of the table row selected.

        Returns:
        - int: The index of the selected row, returns none if no row selected.
        """
        selected = self.table.selection()
        if selected:
            return int(selected[0])
        else:
            return None

    def bind_table_row_click(self, callback: callable):
        """
        Method used to handle the click event on a table row.

        Parameters:
        - callback (callable): The mouse click event callback
        """
        self.table.bind("<ButtonRelease-1>", callback)

    def add_button_callback(self, callback: callable):
        """
        Callback method to the add button.
        This method should handle the event to add a new question data to the table.

        Parameters:
        - callback (callable) : The add button click event callback
        """
        self.add_btn.config(command=callback)

    def clear_button_callback(self, callback: callable):
        """
        Callback method to the clear button.
        This method should handle the event to clear the text entries.

        Parameters:
        - callback (callable) : The clear button click event callback
        """
        self.clear_btn.config(command=callback)

    def delete_button_callback(self, callback: callable):
        """
        Callback method to the delete button.
        This method should handle the event to delete a selected table row.

        Parameters:
        - callback (callable) : The delete button click event callback
        """
        self.delete_btn.config(command=callback)

    def update_button_callback(self, callback: callable):
        """
        Callback method to the the update button.
        This method should handle the event to update the table data.

        Parameters:
        - callback (callable) : The update button click event callback
         """
        self.update_btn.config(command=callback)

    def logout_button_callback(self, callback: callable):
        """
        Callback method to the the logout button.
        This method should handle the event to logout.

        Parameters:
        - callback (callable) : The logout button click event callback
        """
        self.logout_btn.config(command=callback)

    def update_table(self, data: list[list[int, str, str, str, str, str, int]]):
        """
        Method used to update the table with the questions data.

        Parameters:
        - data (list[list[int, str, str, str, str, str, int]]): An nested list with integer
        represents the correct option and strings representing the questions values in each row in the table.
        """
        self.table.delete(*self.table.get_children())
        for i, question in enumerate(data, start=1):
            self.table.insert("", "end", iid=i, values=question)

    def clear_input_entries(self):
        """ Method used to clear the text entries. """
        self.question_entry.delete(0, tk.END)
        self.option1_entry.delete(0, tk.END)
        self.option2_entry.delete(0, tk.END)
        self.option3_entry.delete(0, tk.END)
        self.option4_entry.delete(0, tk.END)
        self.correct_option_entry.delete(0, tk.END)

    def set_question_text(self, text: str):
        """
        Method to set the question text in the entry field.

        Parameters:
            text (str): The text to be set in the question entry field.
        """
        self.question_entry.delete(0, tk.END)
        self.question_entry.insert(0, text)

    def set_first_option(self, text: str):
        """
        Method to set the first option text in the entry field.

        Parameters:
            text (str): The text to be set in the first option entry field.
        """
        self.option1_entry.delete(0, tk.END)
        self.option1_entry.insert(0, text)

    def set_second_option(self, text: str):
        """
        Method to set the second option text in the entry field.

        Parameters:
            text (str): The text to be set in the second option entry field.
        """
        self.option2_entry.delete(0, tk.END)
        self.option2_entry.insert(0, text)

    def set_third_option(self, text: str):
        """
        Method to set the third option text in the entry field.

        Parameters:
            text (str): The text to be set in the third option entry field.
        """
        self.option3_entry.delete(0, tk.END)
        self.option3_entry.insert(0, text)

    def set_fourth_option(self, text: str):
        """
        Method to set the fourth option text in the entry field.

        Parameters:
            text (str): The text to be set in the fourth option entry field.
        """
        self.option4_entry.delete(0, tk.END)
        self.option4_entry.insert(0, text)

    def set_correct_option(self, value: int):
        """
        Method to set the correct option value in the entry field.

        Parameters:
            value (int): The value to be set in the correct option entry field.
        """
        self.correct_option_entry.delete(0, tk.END)
        self.correct_option_entry.insert(0, str(value))

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
        view_width = 1090
        # The view height
        view_height = 620

        x = (screen_width - view_width) // 2
        y = (screen_height - view_height) // 2

        # Set the geometry of the window
        self.geometry(f"{view_width}x{view_height}+{x}+{y}")
