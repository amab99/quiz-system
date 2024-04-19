import os
import sqlite3
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from project_src.database.DatabaseManager import DatabaseManager


class DatabaseManagerTest(unittest.TestCase):
    """
    DatabaseManagerTest class contains unit tests for testing all CRUD operations
    on the quiz database handled by the DatabaseManager class. This ensures each function
    correctly interacts with the database, accurately reflecting expected behaviors and data handling.

    Author: Asaad Katbeh
    """

    def setUp(self):
        """
        Set up the test environment by creating an in-memory SQLite database and initializing
        the DatabaseManager with this connection. Also, create the necessary database tables
        for the tests.
        """
        self.connection = sqlite3.connect(':memory:')  # use an in-memory database for tests
        self.cursor = self.connection.cursor()
        self.db_manager = DatabaseManager(self.connection)
        self.create_tables()

    def create_tables(self):
        """
        Create tables in the in-memory database for testing. This includes tables for admins and
        quiz questions, closely mirroring the actual database schema used in production.
        """
        self.cursor.execute("""
        CREATE TABLE Admins (
            adminId INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
        """)
        self.cursor.execute("""
        CREATE TABLE Questions (
            questionId INTEGER PRIMARY KEY AUTOINCREMENT,
            questionText TEXT UNIQUE NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correctOption INTEGER NOT NULL
        );
        """)
        self.connection.commit()

    def test_authorize_login_successful(self):
        """
        Verify that a valid login returns a positive integer representing the admin's ID.
        This test ensures that the `authorize_login` method correctly identifies valid login credentials.
        """
        self.cursor.execute("INSERT INTO Admins (username, password) VALUES (?, ?)", ('admin', 'pass'))
        self.connection.commit()
        result = self.db_manager.authorize_login('admin', 'pass')
        self.assertGreater(result, 0)

    def test_authorize_login_failed(self):
        """
        Ensure that an invalid login attempt returns -1, indicating the login was unsuccessful.
        This test checks that the `authorize_login` method properly handles incorrect credentials.
        """
        result = self.db_manager.authorize_login('admin', 'wrongpass')
        self.assertEqual(result, -1)

    def test_register_admin_successful(self):
        """
        Test successful registration of a new admin. The method should return a new admin ID greater than zero,
        confirming that the admin was added to the database without issues.
        """
        result = self.db_manager.register_admin('newadmin', 'newpass')
        self.assertGreater(result, 0)

    def test_register_admin_failed_due_to_integrity_error(self):
        """
        Confirm that attempting to register an admin with an already existing username results in -1.
        This tests the handling of integrity constraints for the `register_admin` method.
        """
        self.cursor.execute("INSERT INTO Admins (username, password) VALUES (?, ?)", ('admin', 'pass'))
        self.connection.commit()
        result = self.db_manager.register_admin('admin', 'pass')
        self.assertEqual(result, -1)

    def test_retrieve_quiz_questions_empty(self):
        """
        Verify that retrieving quiz questions from an empty database returns an empty list.
        This confirms the method's ability to handle cases where no data exists.
        """
        questions = self.db_manager.retrieve_quiz_questions()
        self.assertEqual(len(questions), 0)

    def test_retrieve_quiz_questions_not_empty(self):
        """
        Test that multiple quiz questions are retrieved correctly when the database is not empty.
        This method checks that each added question is retrieved accurately, matching the details provided.
        """
        questions_to_add = [('What is the capital of France?', ['Paris', 'London', 'Berlin', 'Madrid'], 1),
            ('What is the capital of Italy?', ['Rome', 'Milan', 'Naples', 'Venice'], 1),
            ('What is the capital of Germany?', ['Berlin', 'Hamburg', 'Munich', 'Cologne'], 1),
            ('What is the capital of Spain?', ['Madrid', 'Barcelona', 'Seville', 'Valencia'], 1)]

        for question_text, options, correct_option in questions_to_add:
            self.db_manager.add_question(question_text, options, correct_option)

        # Retrieve questions and verify the count matches the number added
        retrieved_questions = self.db_manager.retrieve_quiz_questions()
        self.assertEqual(len(retrieved_questions), len(questions_to_add))

        # Verify that retrieved questions match what was added
        for question, added_question in zip(retrieved_questions, questions_to_add):
            self.assertEqual(question['questionText'], added_question[0])
            self.assertEqual(question['options']['option1'], added_question[1][0])
            self.assertEqual(question['options']['option2'], added_question[1][1])
            self.assertEqual(question['options']['option3'], added_question[1][2])
            self.assertEqual(question['options']['option4'], added_question[1][3])
            self.assertEqual(question['correctOption'], added_question[2])

    def test_add_question(self):
        """
        Test adding a quiz question to the database. Verifies that the question is added correctly
        and can be retrieved, ensuring the database operations handle new question insertion as expected.
        """
        self.db_manager.add_question('What is the capital of France?',
                                     ['Paris', 'London', 'Berlin', 'Madrid'], 1)
        questions = self.db_manager.retrieve_quiz_questions()
        self.assertEqual(len(questions), 1)
        self.assertEqual(questions[0]['questionText'], 'What is the capital of France?')

    def test_update_question(self):
        """
        Test updating an existing quiz question's text and options. Verifies that the update is applied correctly
        and reflects in subsequent retrievals, confirming that update operations are handled properly.
        """
        self.db_manager.add_question('What is the capital of France?',
                                     ['Paris', 'London', 'Berlin', 'Madrid'], 1)
        question_id = self.db_manager.retrieve_quiz_questions()[0]['questionId']
        self.db_manager.update_question(question_id, 'What is the capital of Germany?',
                                        ['Berlin', 'Paris', 'London', 'Madrid'], 1)
        updated_question = self.db_manager.retrieve_quiz_questions()[0]
        self.assertEqual(updated_question['questionText'], 'What is the capital of Germany?')

    def test_delete_question(self):
        """
        Test the deletion of a quiz question from the database. Verifies that the question is removed
        correctly and no longer retrievable, ensuring delete operations are functioning as intended.
        """
        self.db_manager.add_question('What is the capital of France?',
                                     ['Paris', 'London', 'Berlin', 'Madrid'], 1)
        question_id = self.db_manager.retrieve_quiz_questions()[0]['questionId']
        self.db_manager.delete_question(question_id)
        questions = self.db_manager.retrieve_quiz_questions()
        self.assertEqual(len(questions), 0)

    def test_update_option(self):
        """
        Test updating a specific option of an existing quiz question. Verifies that the option update is
        applied correctly and reflects in subsequent retrievals, confirming that specific field updates
        within records are handled properly.
        """
        self.db_manager.add_question('What is the capital of France?',
                                     ['Paris', 'London', 'Berlin', 'Madrid'], 1)
        question_id = self.db_manager.retrieve_quiz_questions()[0]['questionId']
        self.db_manager.update_option(question_id, 2, 'Rome')
        updated_options = self.db_manager.retrieve_quiz_questions()[0]['options']
        self.assertEqual(updated_options['option2'], 'Rome')

    def tearDown(self):
        """
        Clean up the test environment by closing the database connection after each test method.
        """
        self.connection.close()


if __name__ == '__main__':
    unittest.main()
