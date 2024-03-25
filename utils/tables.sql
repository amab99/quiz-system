-- Table: Admins
--
-- This table stores data about the Admins of the quiz application
-- Each admin have a unique id, unique username, and a password for authentication
CREATE TABLE IF NOT EXISTS Admins (
    adminId INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);


-- Table: Questions
--
-- This table stores data about the Questions in the quiz application
-- Each question have a unique id, unique question text, four options and one correct option.
CREATE TABLE IF NOT EXISTS Questions (
    questionId INTEGER PRIMARY KEY,
    questionText TEXT UNIQUE NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    correctOption INTIGER NOT NULL
);