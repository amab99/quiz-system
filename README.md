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

In accordance with the principles of the MVC pattern, started by setting up the project structure. The 'project_src' package was created containing models, views, and controller sub-packages, and for the database the 'database' sub-package was created. Since this project is test-driven, the 'project_tests' package was also created containing four sub test packages for each package. Below is a more detailed explanation of each sub-package class implementation separately.

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

### Models package

This package represents the data and business logic for the quiz system. It contains the classes 'AdminModel' and 'QuizModel' which handle admin authorization and management of the quiz questions by interacting with the DatabaseManager.

To manage the admin credentials when login or registering to the application, the 'AdminModel' class was implemented with its associated unit test class 'AdminModelTest'.The 'AdminModelTest' class was implemented with associated unit tests using mocking to test the successful admin authorization and register, and also tested failed authorization and registration, and also implemented integrity tests for the class design. The responsibility of the 'AdminModel' class is to manage admins' data with authorization and registration by interacting with the DatabaseManager. This class contains the method 'authorize' which attempts to authorize the admin using the provided username and password. It also contains the method 'register' which is used to register a new admin to the database, this method takes username and password as parameters, if registration is successful the new admin's ID is saved to the database. The method 'get_admin_id()' is used to retrieve the stored admin ID.

Then, the 'QuizModelTest' class was implemented with associated unit tests using mocking. This class contains unit tests to test the creation of questions, retrieval of the questions, updating the questions and the options, deleting a question, and integrity tests for the class design. The responsibility of the 'QuizModel' class is to manage the quiz questions creation, retrieval, updating, and deletion by interacting with the DatabaseManager. The 'create_question()' method is used to create a new question, it takes the question text, options list, and correct option index as parameters. The 'retrieve_all_questions()' method returns all quiz questions from the database in the form of a list of dictionaries. The method 'update_question()' takes the question to be updated ID, the updated question text, and the index of the updated correct option as a parameter and returns true if updating the question succeeded. The 'delete_question' method takes the question to be deleted ID as a parameter and returns true if deleting the question succeeded.

### Controllers package

In this package, the classes that handle the control of the quiz system and the communication between the models and the views in the application were implemented. This package contains 4 classes for the controllers, these are 'AdminAuthorizationController', 'AdminController', 'QuizPerformController', 'StartController'.

To handle the user authentication and registration in the application, the 'AdminAuthorizationController was implemented with the associated unit test class 'TestAdminAuthorizationController''. The 'TestAdminAuthorizationController' class contains unit tests to ensure proper handling of authentication and registration. It contains tests to ensure that the admin registers success and that the login to the quiz system is successful. This class also contains tests to ensure the initialization of the login view, the register view and the admin dashboard view and also integrity tests for the AdminAuthorizationController class.

Then, the 'AdminAuthorizationController' class was implemented. This class is responsible for handling the user authentication and registration process in the quiz system. In this class, the 'init()' first initializes the main root window for the application, the admin model to manage the admin operations related to authentication and registration, and the quiz model to manage the quiz operations. Then, the 'show_register_view()' was implemented, this method is used to display the register view to allow the user to register as admin. The 'show_login_view()' was implemented to display the login view to allow the admin to login to the quiz system. The 'show_admin_dashboard()' was implemented to display the admin dashboard to the admin when logging in, and the 'logout()' method used to handle the logout process. After that, the methods to handle the registration and the login were implemented. The 'register_admin()' method checks if the password entered in the password and confirms entry does not match, it displays an error message, then if the register is successful it displays the admin view where the admin can manage the quiz questions. Note that each admin must have a unique username, so if the user enters a username that is already taken, an error message is displayed. The 'login_admin()' interacts with the AdminModel to authorize the admin using the provided username and password, if the authorization succeeds it closes the login view and logs in to the quiz system and displays the admin view.

To handle admin actions and manage the quiz questions through the GUI, 'AdminController' was implemented with the associated unit test class 'TestAdminController'. First, the 'TestAdminController' class, this class contains unit tests to ensure proper handling of the admin actions. This class contains tests to ensure the retrieval of the quiz questions, the success of adding new questions to the application, the success of updating a question, the success of deleting a question, and a test to ensure that the correct question loads to the input fields when clicked on a table row. Integrity tests are also implemented for the AdminController class.

In the 'AdminController' class, the '**init**()' initializes the main root window of the application, the QuizModel to manage the quiz operations, and the AdminView to handle the user interactions. This class contains the method 'load_questions()' used to handle loading the quiz questions and update the table with the questions on the view, the 'add_question()' method used to add new questions to the table, this method takes the question text and the four options from the input text fields and interacts with the QuizModel to crate the new question with its options, if it succeeds it clears the input fields and loads the new question to the view. The 'update_question()' method handles updating an existing question from the questions table. The 'delete_question()' method is used to delete an existing question from the view. To handle the table row click in the view and load the question data into the input fields, the 'on_table_row_click()' method was implemented.

After that, a controller to manage the quiz performance actions was implemented, represented in the class 'QuizPerformController', and the associated unit test class 'TestQuizPerformController'. The unit test class was implemented to ensure proper handling of quiz performance actions. This test class contains unit tests to ensure the updating of the timer in the view and the questions loading in the view. It also contains unit tests to ensure the navigation between the next and previous question in the quiz, and the submission of the quiz. Integrity tests were also implemented for the QuizPerformController class.

The class 'QuizPerformController' was implemented including methods to manage the actions involved in performing a quiz. The 'init()' initialized the main root window of the application, the QuizModel instance to manage the quiz data operations, and the performQuizView instance to manage the GUI quiz interactions. In this class, methods were implemented to handle starting the quiz, updating the timer, loading the questions, navigating through the questions in the view, submitting the quiz, and displaying the user's result on the view. The 'Start_quiz()' method is initialized in 'init() ' to start the quiz with the first question and start the timer. To update the timer in the quiz, the method 'update_timer()' was implemented. This method starts the timer from zero and updates it every second. To update the view with the questions, the method 'load_question()' was implemented, this method updates the view with the current question and its answer options and sets the user's selected answer to the view. The 'next_question()', 'prev_question()', and 'submit_quiz()' methods are used to handle the events to move to the next question, and the previous question, and submit the quiz. When the user submits the quiz, a message is displayed that shows the results and the time taken to submit the quiz, this is handled through the 'show_results()' method.

Finally, in the controller package, the controller for the initial start page of the application was implemented, the class 'StartController' with its associated unit test class 'TestStartController'. In the 'TestStartController' class, unit tests were implemented to ensure proper handling of the initial start screen and transition from the start screen to the login view, register view, and the perform quiz view. This class also contains unit tests to ensure the window closing event and Integrity tests for the StartController class.

In the 'startController' class, methods were implemented to take care of the initial start screen and transition to the other controllers. The 'init()' initializes the start controller with the main root window, the AdminModel instance to manage the admin data operations, and the QuizModel instance to manage the quiz data operations. The 'start_quiz()' method is triggered when the user presses the "Start quiz" button, it initializes the performQuizView and the QuizPerformController to open the quiz view and start the quiz. To register a new admin, the method 'show_register_view()' is triggered, which initializes the AminAuthorizationController to display the register view. The method 'show_login_view()' initializes the AminAuthorizationController to display the login view. Finally, the 'show_start_view()' method is used to display the star view with an info message box that contains a description of how the application's Usage guide can be displayed.

Finally, the entry point of the quiz system application, the main(), was implemented. This method initializes the database connection, the quiz and admin models, and the startController. It also initializes the application's initial GUI and starts the application's main loop to handle the user's interactions.

## User manual

This is a quiz system application. When this program is launched a start screen will be displayed.

In the start screen, you can choose to:

- Start the quiz
- Login as an admin
- Register as new admin

If you choose to start the quiz:

- The quiz perform screen will be displayed and the quiz consisting of 20 multiple-choice questions and a timer and includes a timer to track your completion time will start
- In the quiz performance screen you should select the correct answer for each question, and click on ‘Next’ button to navigate to the next question. If you want to navigate to the previous questions, you can click on the ‘previous’ button.
- To submit the quiz, click on the ‘Submit’ button. When submitting, your final score and the time taken will be displayed on the screen.

If you choose to register as an admin:

- A registration screen will be displayed, enter username and password to add registered as admin to the application and be able to manage the quiz system's quiz data.
- When you have registered, the admin dashboard will be displayed.

If you choose to log in as an admin:

- A login screen will be displayed, enter username and password to login to the admin dashboard and be able to manage the quiz system's quiz data.
- When you have logged in, the admin dashboard will be displayed.

As an admin, you can:

- Select a specific question from the table to update or delete.
- Add new questions by entering the question text, four options and indicating the correct option number. Then, click the 'Add' button.
- Click 'Logout' to log out of the system. The application will then close.

## Discussion

### Purpose Fulfillment

The purpose of this project was to develop a quiz system application using Python Tkinter GUI where the user can interact with the application in a group collaboration by using the kanban board on Trello to administer and coordinate the work. This application was implemented according to Test Driven Development (TDD), by starting with creating the tests for the method before implementing the actual method for the solution. Several unit tests were created and passed with a high test coverage where every method to be created was covered, even error handling was tested to reduce the risk of unwanted bugs, which fulfilled the purpose.

This application uses the MVC design pattern by having 4 different sub-packages "models", "views", "controllers" and "database" where each of these sub-packages contains classes that separate the models from the views and make the interaction happen in the controllers. The database sub-package was implemented to separate database connections and manage the database CRUD operations from the rest of the models, since SQLite database was used for quiz data and admin data management.

This quiz system includes the features below that also have fulfilled the purpose of the project:

- Interact with the system as a user without login: When the application is run, a start screen is displayed where the user can choose to start the quiz and perform it. This fulfills the purpose of interacting with the application and performing the quiz without login to the system. The quiz contains only multiple-choice questions.
- The user interacts with the program through a GUI: The application is implemented using Python Tkinter, which allows the user to interact with the program through the GUI.
- Admin authentication and register: In the start screen, the user can choose to log in to the quiz system through entering username and password. This is to be able to interact with the quiz data and view already existing questions, add quiz questions, update an already existing quiz question, and delete questions. If the user is not already an admin, they can choose to register as an admin on the start screen to be able to edit the quiz data.

### Alternative Approaches

An alternative approach to developing this project is to implement various features in the quiz system by e.g. making the integration between the user and the quiz system only possible by logging into the system as a student. This by implementing a dashboard for students where they can see the available quizzes to do that have been added from admin, perform a quiz, and see what grades the student has received in previously done quizzes. A student should not be able to perform an already performed quiz again.

### Personal Reflections

In this project, the focus has been more on group work and how we as a group should be able to plan a project, and then fully follow the project idea and the goals that we have added to the project using the Kanban board in Trello to administer and coordinate the work. This project has been very educational, we as a group have both learned how a collaboration Python project work can be implemented, what obstacles can arise in such a collaboration project, and how they can be solved. For us it was the first time that we both implemented a python project using MVC and GUI, we have learned how Tkinter works and how it differs from Java Swing, which we have used in previous projects.

Finally, this project allowed our group to gain valuable skills in Python programming using Tkinter, MVC, database management, and TDD. We enjoyed working on this project and implementing the various features.
