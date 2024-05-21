import tkinter as tk
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from project_src.database.Database import DatabaseSetup
from project_src.database.DatabaseManager import DatabaseManager
from project_src.models.AdminModel import AdminModel
from project_src.models.QuizModel import QuizModel
from project_src.controllers.StartController import StartController

def main():
    # Initialize the database
    db_setup = DatabaseSetup()
    db_setup.connect_to_db()

    # Create a DatabaseManager instance
    db_manager = DatabaseManager(db_setup.conn)

    # Create an AdminModel instance
    admin_model = AdminModel(db_manager)

    # Create a QuizModel instance
    quiz_model = QuizModel(db_manager)

    # Create the main root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Initialize the StartController
    start_controller = StartController(root, admin_model, quiz_model)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()