import tkinter as tk


class PerformQuizView:
    """
    This class represents the view for performing the quiz.
    This view contains A question label for the quiz question and four Radio button for the answer's options,
    three buttons for previous, next and submit, and a label for the timer.

    Author: Amal Abueshareik
    """

    def __init__(self):
        """ Initialize the view for performing the quiz. """
        self.root = tk.Tk()
        self.root.title("Perform Quiz")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Create widgets
        self.create_widgets()
        # Center the window
        self.center_window()

    def create_widgets(self):
        """ Create and place the widgets in the view. """

        # Create the main frame with the question label and options radio buttons and add properties
        self.root.main_frame = tk.Frame(background="#f0f0f0", pady=15, highlightbackground="#90CAF9",
                                        highlightthickness=1)
        self.root.question_label = tk.Label(self.root.main_frame, text="Question Text ", font=("Source Serif Pro", 15))
        self.root.option_var = tk.IntVar(value=None)
        self.root.opt1 = tk.Radiobutton(self.root.main_frame, variable=self.root.option_var, value=1, text="Option 1",
                                        font=("Arial", 12, "italic"))
        self.root.opt2 = tk.Radiobutton(self.root.main_frame, variable=self.root.option_var, value=2, text="Option 2",
                                        font=("Arial", 12, "italic"))
        self.root.opt3 = tk.Radiobutton(self.root.main_frame, variable=self.root.option_var, value=3, text="Option 3",
                                        font=("Arial", 12, "italic"))
        self.root.opt4 = tk.Radiobutton(self.root.main_frame, variable=self.root.option_var, value=4, text="Option 4",
                                        font=("Arial", 12, "italic"))

        # Create the navigation frame including the buttons and the timer label with its properties
        self.root.nav_frame = tk.Frame(background="#f0f0f0", pady=15, highlightbackground="#90CAF9",
                                       highlightthickness=1)
        self.root.prev_button = tk.Button(self.root.nav_frame, text="Previous", width=10, font=("Arial", 12, "italic"),
                                          background="#90CAF9")
        self.root.next_button = tk.Button(self.root.nav_frame, text="Next", width=10, font=("Arial", 12, "italic"),
                                          background="#90CAF9")
        self.root.submit_button = tk.Button(self.root.nav_frame, text="Submit", width=10, font=("Arial", 12, "italic"),
                                            background="#90CAF9")
        self.root.timer_label = tk.Label(self.root.nav_frame, text="Time: 00:00", font=("Arial", 12))

        # Placing the widgets in the view
        self.root.main_frame.grid(row=0, column=1, padx=20, pady=5, sticky="news")
        self.root.nav_frame.grid(row=1, column=1, padx=180, pady=10, sticky="news")
        self.root.question_label.grid(row=0, column=0, padx=10, pady=25)
        self.root.opt1.grid(row=1, column=0, padx=10, pady=(0, 60), sticky="w")
        self.root.opt2.grid(row=2, column=0, padx=10, pady=(0, 60), sticky="w")
        self.root.opt3.grid(row=3, column=0, padx=10, pady=(0, 60), sticky="w")
        self.root.opt4.grid(row=4, column=0, padx=10, pady=(0, 60), sticky="w")
        self.root.prev_button.grid(row=0, column=0, padx=5)
        self.root.next_button.grid(row=0, column=1, padx=5)
        self.root.submit_button.grid(row=0, column=2, padx=5)
        self.root.timer_label.grid(row=0, column=3, padx=5)

    def set_question_text(self, text: str):
        """
        Method used to set the question text to the label.

        Parameters:
        - text (str): The questions text to be displayed on the label.
        """
        self.root.question_label.config(text=text)

    def set_answer_options(self, options: list):
        """
        Method used to set the answers options text to the radio buttons.

        Parameters:
        - options (list): A list of strings representing the options text for the radio buttons.
        """
        self.root.opt1.config(text=options[0])
        self.root.opt2.config(text=options[1])
        self.root.opt3.config(text=options[2])
        self.root.opt4.config(text=options[3])

    def set_selected_option(self, option: str):
        """
        Method used to set the selected option.

        Parameters:
        - option (str): A string representing the option to be selected.
        """
        if option == self.root.opt1.cget("text"):
            self.root.option_var.set(1)
        elif option == self.root.opt2.cget("text"):
            self.root.option_var.set(2)
        elif option == self.root.opt3.cget("text"):
            self.root.option_var.set(3)
        elif option == self.root.opt4.cget("text"):
            self.root.option_var.set(4)

    def add_prev_button_callback(self, callback: callable):
        """
        Callback method to the previous button.

        Parameters:
        - callback (callable): The previous button click event callback
        """
        self.root.prev_button.config(command=callback)

    def add_next_button_callback(self, callback: callable):
        """
        Callback method to the next button.

        Parameters:
        - callback (callable): The next button click event callback
        """
        self.root.next_button.config(command=callback)

    def add_submit_button_callback(self, callback: callable):
        """
        Callback method to the submit button.

        Parameters:
        - callback (callable): The submit button click event callback
        """
        self.root.submit_button.config(command=callback)

    def set_prev_button_enabled(self, enabled: bool):
        """
        Method used to set the previous button to enabled state.

        Parameters:
        - enabled (bool): Boolean flag indicating whether the previous button should be enabled or disabled.
        """
        if enabled:
            self.root.prev_button.config(state="normal")
        else:
            self.root.prev_button.config(state="disabled")

    def set_next_button_enabled(self, enabled: bool):
        """
        Method used to set the next button to enabled state.

        Parameters:
        - enabled (bool): Boolean flag indicating whether the next button should be enabled or disabled.
        """
        if enabled:
            self.root.next_button.config(state="normal")
        else:
            self.root.next_button.config(state="disabled")

    def add_option_button_callback(self, callback: callable):
        """
        Callback methods to the options radio buttons.

        Parameters:
        - callback (callable): The options radio buttons click event callback
        """
        self.root.opt1.config(command=lambda: callback(self.root.opt1.cget("text")))
        self.root.opt2.config(command=lambda: callback(self.root.opt2.cget("text")))
        self.root.opt3.config(command=lambda: callback(self.root.opt3.cget("text")))
        self.root.opt4.config(command=lambda: callback(self.root.opt4.cget("text")))

    def clear_selected_options(self):
        """ Method used to clear the selection of the options. """
        self.root.option_var.set(0)

    def get_selected_option(self) -> str | None:
        """
        Method used to get text of the selected option, by mapping the value to the selected text.

        Returns:
        - str: A string representing the selected option text, returns null if no option selected.
        """
        selected = self.root.option_var.get()
        if selected == 1:
            return self.root.opt1.cget("text")
        elif selected == 2:
            return self.root.opt2.cget("text")
        elif selected == 3:
            return self.root.opt3.cget("text")
        elif selected == 4:
            return self.root.opt4.cget("text")
        else:
            return None

    def center_window(self):
        """ Method used to center the view window on the center of the screen. """
        # Retrieve the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Define the width and height of the view
        window_width = 800
        window_height = 600
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the geometry of the window
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")