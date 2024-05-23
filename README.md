# Project 

## Environment & Tools

### Amal:
Computer: HP Pavilion 15-eg0036no - i7

Operating system: Windows 11 Home 64-bitar

IDE: Git version 2.33.0, Pycharm IDE version (2022.2.1)

### Asaad:
Computer: MacBook Pro, 13-inch, M1, 2020

Operating system: macOS Sonoma Version 14.2.1

IDE: git version 2.39.2, Pycharm IDE version (2023.3.3) 

#### Kanban board link:

https://trello.com/invite/b/76P4iYSF/ATTIcff07a63a665e7b6edf649d16b978778DF275A35/dt042g-project-group2

## Group Members
- Amal Abueshareik: amab2100@student.miun.se
- Asaad Katbeh: aska2200@student.miun.se

## Purpose
The purpose of this project is to develop a quiz system that tests the users knowledge and calculates the user's score using python. The application should be implemented using MVC, and SQLite will be used as a database. The application needs to be implemented according to Test Driven Development (TDD), this by starting with implementing the tests, then implementing the code to pass the tests. Also integrity tests for the class design need to be implemented.

This project needs to be implemented in a group collaboration, and the Kanban board on Trello needs to be used to administer and coordinate the work.

The application should have the features described below:
- Interact with the system and perform the quiz as user without login
- Admin authentication
- The application will consist of Multiple Choice Questions.
- Users interact with the program through a GUI
- The admin will be able to add quiz questions, edit an already existing quiz question, delete a question, and View all Questions

## Procedures

Since this project is a group work, the Kanban board on Trello was used to administer and coordinate the work. First, a manifest list was created, where the project description was written and guidelines for the implementation of the project were outlined. Below this list, cards were created that describe general information about the project, task guidelines, peer review guidelines, the code conventions each member needs to follow, and documentation guidelines. The project was broken down into tasks and added to the backlog card containing a description of the task, a checklist of completion criteria, and appropriate labels according to the guidelines described in the assignment guidelines. Git was also used for version control with feature branching and each task was implemented on a separate branch that was later merged into the master. Every task was then assigned to a member who moved the task to the 'In progress' list, created a branch, and started the implementation. When the implementation was complete, a pull request was created and the task was moved to the 'Review' list. The other team member reviewed the code and if everything looked good, the code was merged into the master, otherwise, a comment was made about what needed to be fixed according to the peer review guidelines, and the task was moved back to the backlog.

Since this project should follow the TDD principles, test classes were created for each class that is created. First, unit tests were written and then code that passes the test was implemented. For each class, the test classes were created with unit tests both for the behavior of the methods and integrity tests for the class design. After each class is fully implemented, the tests are run to ensure that all tests pass and no test fails.

In accordance with the principles of the MVC pattern, started by setting up the project structure. The 'project_src' package was created containing models, views, and controller sub-packages, and for the database the 'database' sub-package was created. Since this project is test-driven, the 'project_tests' package was also created containing four sub test packages for each package.  Below is a more detailed explanation of each sub-package class implementation separately.

### Database package
This package contains classes that manage connection to the database and the CRUD operations. Since TDD needed to be followed and the tests for the methods were to be implemented first, the 'testDatabase' class was created first and started by implementing each test followed by creating the method to pass that test in the 'DatabaseSetup' class. The class 'testDatabase' contains unit tests to ensure the database connection and successful creation of the database schema. Mocking was used In unit testing of the database, this isolates the testing from the actual behavior of the database connection. The class 'DatabaseSetup' initializes the SQLite database and the SQL schema file and contains methods that are responsible for setting up the connection to the database, and creating the database schema from the SQL-file to store the admin data and quiz questions data.

The 'DatabaseManagerTest' class was implemented with associated unit tests to test all database CRUD operations. This unittest class sets up the test environment by creating an in-memory SQLite database and then initializes the 'DatabaseManager' connected to this database. This class contains unit tests to verify admin login, unit tests to verify admin registration, unit tests to test that the quiz questions are retrieved correctly when the database is not empty, and unit tests for all CRUD operators. The responsibility of the 'DatabaseManager' class is to manage all CRUD operations in the database. In this class, the method to authorize admin login was implemented, this method takes username and password as parameters and returns an error message if an error occurs when login. This class also contains the method 'retrieve_quiz_questions()' to retrieve quiz questions as a list of dictionaries. Methods to add, update a specific question or questions answer options or to delete a question from the database was also implemented in this class.

### Views package 
This package represents the user interface to allow the user to integrate with the quiz system. This package contains 6 classes for the views, these are 'LoginView', 'MenuBar', 'StartView', 'RegisterView', 'PerformQuizView', and 'AdminView'.

Started with the view that represents the login form to the quiz system, where admins can log in to manage the quiz data. The 'LoginViewTest' class was implemented with associated unit tests to test the creation of all the widgets with the correct properties in the login view. It also has unit tests to test the functionality of retrieving the username and password from the view, and the buttons' callback in the view. This class also tests the behavior of centering the view on the screen and implements integrity tests for the class design. The 'LoginView' class represents the login window of the quiz system using username and password, this class contains the 'create_widgets()' method which creates and places the widgets, labels, and entries for username and password, and a button for login on the view. Getters for username and password were created, and a callback method to the login button to handle the event to login to the quiz system as admin. The method 'display_error_message()' is used to display any error that occurs when logging in, and the 'center_window()' method is used to place the view in the center of the screen.

The 'RegisterViewTest' class was implemented with associated unit tests to test the creation of all the widgets in the register view, it also has unit tests to test the functionality of retrieving the username and password from the view, and the register buttons' callback in the view. It also tests the behavior of centering the view on the screen and also implements integrity tests for the class design. The 'RegisterView' class represents the window for registering new admin of the quiz system by username and password. This class implementation is similar to the login view, the difference is that the register view also contains an entry to confirm the password.

The 'MenuBarTest' class was implemented with associated unit tests to test the creation of the menu bar including the child widgets and to ensure the message box creation. To ensure the message box creation mocking was used, this was to isolate the behavior of the 'usage_guide_option' method without displaying a real message box on the screen. The 'MenuBar' class represents the menu bar that will be used in the start view of the quiz system to display the usage guide of the application.

When the application runs, a start view with navigation to other views should be displayed. For this, the 'StartView' class was implemented with corresponding unit tests in the 'StartViewTest' class. The 'StartViewTest' class was implemented with associated unit tests to test the creation of all the widgets with the correct properties in the quiz system's start view, it also has unit tests to test the functionality of the buttons' callback in the view using mocking. It also tests the behavior of centering the view on the screen and implements integrity tests for the class design. The 'StartView' class represents the start view of the quiz system. This view contains a menu bar and three buttons, to start the quiz, log in as admin to the system, and register as admin. In this class, callback methods were implemented for all buttons in the view and method to center the view on the screen.

Then, the view was implemented where the user can perform the quiz. The class 'TestPerformQuizView' contains unit tests to ensure the functionality of setting the question text and the options to the radio buttons. This class also includes tests to ensure the functionality of selecting an option in the quiz system and retrieving the selected option. It also tests the buttons' callback functionality in the view, and the behavior of centering the view on the screen, and also implements integrity tests for the class design. 

The 'PerformQuizView' class represents the main view to perform the quiz in the application. This class contains to create and place the widgets in the view, a label for the question text, four radio buttons for answer options, three buttons, one to navigate to the previous question, one to go to the next question, and a button to submit quiz answers, and a label for the timer. This class contains a method to set question text to label in the view. The method 'set_answer_options()' takes options in the form of a list of strings as a parameter and is used to set the answer options text to the radio buttons. The 'set_selected_option()' method takes the option to be selected in the form of a string and sets the user's selected option. Callback methods and methods to set the buttons to enabled state were implemented for all buttons in the view. The method 'clear_selected_options()' is used to clear the selected options in the quiz, and the 'get_selected_option' method is used to get the text of the selected option, using if/else by mapping the value of the selected text. Finally, the method to center the view on the screen was implemented.

Finally, the admin view where the admin can manage all quiz data was implemented with its associated unit test class. The 'AdminViewTest' and 'AdminView' classes were implemented. The 'AdminViewTest' class contains unit tests to ensure that all needed widgets are created in the view. It also contains tests to ensure the retrieval of question text, the four options, and the correct option from the input entries. It also tests the buttons' callback functionality in the view and the behavior of clearing the text entries. This class also has unit tests to verify the update of the table with the questions data and tests the revert of the selected row from the table. Finally, it also contains tests to ensure the behavior of centering the view on the screen and also implements integrity tests for the class design.

Then the 'AdminView' class was implemented, this class represents the view for the admins, in this view admins can manage all quiz questions by being able to add new questions to the system, update an already existing question with its options, or delete a question from the system. In this class, a tree view was created that represents the table to display questions data in the system. This tree view contains columns showing all available questions with their ID, options, and correct options in the quiz system. In this view, a label was implemented to show the question text, four entries to display the different answer options, and one entry to display the correct option. Five buttons were implemented, one to add a new question, one to update a question from the table, one to delete a question, one to clear entries, and one to log out of the system. Callback methods were implemented for all buttons in the view, it also contains methods to retrieve the question text and the options from the entries in the view and a method to retrieve the questions data table. The method 'get_table_row()' retrieves the index of the selected row from the table, and the method 'update_table()' takes questions data as a nested list with integer representing the correct option and strings representing the questions values in each row in the table is responsible for updating the table with questions data. Finally, methods were implemented to clear input entries, display error messages, and to center the view on the screen.

## Discussion
### Purpose Fulfillment
[replace this with relevant information]

### Alternative Approaches
[replace this with relevant information]
