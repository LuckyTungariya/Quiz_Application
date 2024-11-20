A simple and interactive quiz application built with CustomTkinter for the graphical user interface (GUI) and MySQL for the backend. 
This application allows users to log in, manage their profiles, take quizzes, and save their responses for later review.

Features
User Login: Secure login system for registered users.
Profile Management: Users can view and manage their profiles.
Quiz: Take quizzes with multiple-choice questions (MCQs).
Save Responses: Save user responses for analysis or later review.
Timer: A countdown timer for each quiz session.
Score Calculation: Automatic score calculation at the end of the quiz.
Database Integration: User data and quiz results are saved in a MySQL database.

Requirements
Python CustomTkinter module (for GUI)  
MySQL (for the database backend)
Pillow (for image handling)
pymysql (for MySQL connectivity)

To install required modules run command
pip install customtkinter pymysql pillow

To Clone repository run command
git clone https://github.com/your-username/quiz-application.git

To import the database file
"Create database [new database name];"   #If not already created

Import the database dump
mysql -u [username] -p [new_database_name] < database/database_dump.sql
Replace [username] with your MySQL username, [new_database_name] with the database name,
and ensure database/database_dump.sql is the path to the dump file.
