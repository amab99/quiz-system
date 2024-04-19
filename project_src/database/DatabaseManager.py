import sqlite3
from typing import List, Dict, Union


class DatabaseManager:
    """
    DatabaseManager class responsible for managing CRUD operations on the quiz database.
    This includes handling operations such as registering admins, logging in, managing quiz questions,
    and updating specific options.

    Author: Asaad Katbeh
    """

    def __init__(self, connection: sqlite3.Connection):
        """
        Initialize the DatabaseManager with an active database connection.

        Parameters:
        - connection (sqlite3.Connection): The active database connection.
        """
        self.conn = connection
        self.cursor = self.conn.cursor()

    def authorize_login(self, username: str, password: str) -> int:
        """
        Authorize admin login and return admin ID if successful, -1 otherwise.

        Parameters:
        - username (str): The admin's username.
        - password (str): The admin's password.

        Returns:
        - int: The admin ID if credentials are correct, -1 if login fails.

        Raises:
        - sqlite3.Error: If a database error occurs during the login process.
        """
        try:
            query = "SELECT adminId FROM Admins WHERE username=? AND password=?"
            self.cursor.execute(query, (username, password))
            admin = self.cursor.fetchone()
            return admin[0] if admin else -1
        except sqlite3.Error as e:
            print(f"Database error during login: {e}")
            return -1

    def register_admin(self, username: str, password: str) -> int:
        """
        Register a new admin and return the new admin ID, -1 if failed.

        Parameters:
        - username (str): The new admin's username.
        - password (str): The new admin's password.

        Returns:
        - int: The new admin's ID on success, -1 if registration fails.

        Raises:
        - sqlite3.IntegrityError: If a uniqueness constraint is violated.
        - sqlite3.Error: If a database error occurs during registration.
        """
        try:
            query = "INSERT INTO Admins (username, password) VALUES (?, ?)"
            self.cursor.execute(query, (username, password))
            self.conn.commit()
            # Retrieve the last inserted ID, which is the user ID of the new admin
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Failed to register admin due to integrity error: {e}")
            return -1
        except sqlite3.Error as e:
            print(f"Database error during admin registration: {e}")
            return -1

    def retrieve_quiz_questions(self) -> List[Dict[str, Union[int, str, Dict[str, str]]]]:
        """
        Retrieve all quiz questions and return them as a list of dictionaries.

        Returns:
        - list of dict: A list of dictionaries, each representing a quiz question.

        Raises:
        - sqlite3.Error: If a database error occurs during the retrieval process.
        """
        try:
            query = "SELECT questionId, questionText, option1, option2, option3, option4, correctOption FROM Questions"
            self.cursor.execute(query)
            questions = self.cursor.fetchall()
            question_list = [{'questionId': question[0], 'questionText': question[1],
                'options': {'option1': question[2], 'option2': question[3], 'option3': question[4],
                    'option4': question[5]}, 'correctOption': question[6]} for question in questions]
            return question_list
        except sqlite3.Error as e:
            print(f"Database error during retrieving questions: {e}")
            return []

    def add_question(self, question_text: str, options: List[str], correct_option: int):
        """
        Add a new quiz question.

        Parameters:
        - question_text (str): The text of the question.
        - options (list): A list of options for the question.
        - correct_option (int): The index of the correct option.

        Raises:
        - sqlite3.Error: If a database error occurs during the addition of the question.
        """
        try:
            query = ("INSERT INTO Questions (questionText, option1, option2, option3, option4, correctOption) VALUES ("
                     "?, ?, ?, ?, ?, ?)")
            self.cursor.execute(query, (question_text, *options, correct_option))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error during adding question: {e}")
            self.conn.rollback()

    def update_question(self, question_id: int, new_text: str, new_options: List[str], new_correct_option: int):
        """
        Update an existing quiz question.

        Parameters:
        - question_id (int): The ID of the question to update.
        - new_text (str): The new text of the question.
        - new_options (list): A list of new options for the question.
        - new_correct_option (int): The index of the new correct option.

        Raises:
        - sqlite3.Error: If a database error occurs during the update process.
        """
        try:
            query = ("UPDATE Questions SET questionText=?, option1=?, option2=?, option3=?, option4=?, correctOption=? "
                     "WHERE questionId=?")
            self.cursor.execute(query, (new_text, *new_options, new_correct_option, question_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error during updating question: {e}")
            self.conn.rollback()

    def delete_question(self, question_id: int):
        """
        Delete a quiz question.

        Parameters:
        - question_id (int): The ID of the question to be deleted.

        Raises:
        - sqlite3.Error: If a database error occurs during the deletion process.
        """
        try:
            query = "DELETE FROM Questions WHERE questionId=?"
            self.cursor.execute(query, (question_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error during deleting question: {e}")
            self.conn.rollback()

    def update_option(self, question_id: int, option_number: int, new_text: str):
        """
        Update a specific option of a question.

        Parameters:
        - question_id (int): The ID of the question where the option will be updated.
        - option_number (int): The number of the option to update (1-4).
        - new_text (str): The new text for the option.

        Raises:
        - sqlite3.Error: If a database error occurs during the update of the option.
        """
        try:
            column = f"option{option_number}"
            query = f"UPDATE Questions SET {column}=? WHERE questionId=?"
            self.cursor.execute(query, (new_text, question_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error during updating option: {e}")
            self.conn.rollback()
