import os
import sys
from typing import List, Dict, Union

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from project_src.database.DatabaseManager import DatabaseManager


class QuizModel:
    """
    QuizModel class provides functionalities to manage quiz questions
    with operations such as creation, retrieval, updating, and deletion
    by interacting with the DatabaseManager.

    Author: Asaad Katbeh
    """

    def __init__(self, db_manager: DatabaseManager):
        """
        Initializes the QuizModel with a specific DatabaseManager.

        Parameters:
            db_manager (DatabaseManager): The database manager instance to manage database interactions.
        """
        self.db_manager = db_manager

    def create_question(self, question_text: str, options: List[str], correct_option: int) -> bool:
        """
        Create a new quiz question.

        Parameters:
            question_text (str): The text of the new question.
            options (List[str]): A list of four options for the question.
            correct_option (int): Index of the correct option (1 to 4).

        Returns:
            bool: True if the question is successfully created, False otherwise.
        """
        if len(options) != 4:
            print("Error: There must be exactly four options.")
            return False

        if correct_option < 1 or correct_option > 4:
            print("Error: Correct option index must be between 1 and 4.")
            return False

        try:
            self.db_manager.add_question(question_text, options, correct_option)
            return True
        except Exception as e:
            print(f"Error creating question: {e}")
            return False

    def retrieve_all_questions(self) -> List[Dict[str, Union[int, str, Dict[str, str]]]]:
        """
        Retrieve all quiz questions from the database.

        Returns:
            List[Dict]: A list of dictionaries representing quiz questions.
        """
        return self.db_manager.retrieve_quiz_questions()

    def update_question(self, question_id: int, new_text: str, new_options: List[str], new_correct_option: int) -> bool:
        """
        Update an existing quiz question.

        Parameters:
            question_id (int): The ID of the question to be updated.
            new_text (str): The updated text of the question.
            new_options (List[str]): The updated options for the question.
            new_correct_option (int): The index of the updated correct option (1 to 4).

        Returns:
            bool: True if the question is successfully updated, False otherwise.
        """
        if len(new_options) != 4:
            print("Error: There must be exactly four options.")
            return False

        if new_correct_option < 1 or new_correct_option > 4:
            print("Error: Correct option index must be between 1 and 4.")
            return False

        try:
            self.db_manager.update_question(question_id, new_text, new_options, new_correct_option)
            return True
        except Exception as e:
            print(f"Error updating question: {e}")
            return False

    def delete_question(self, question_id: int) -> bool:
        """
        Delete a quiz question.

        Parameters:
            question_id (int): The ID of the question to be deleted.

        Returns:
            bool: True if the question is successfully deleted, False otherwise.
        """
        try:
            self.db_manager.delete_question(question_id)
            return True
        except Exception as e:
            print(f"Error deleting question: {e}")
            return False
