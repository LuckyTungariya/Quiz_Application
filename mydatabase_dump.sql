-- MySQL dump 10.12
--
-- Host: localhost    Database: projects
-- ------------------------------------------------------
-- Server version	6.0.0-alpha-community-nt-debug

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `c_questions`
--

DROP TABLE IF EXISTS `c_questions`;
CREATE TABLE `c_questions` (
  `Srno` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `option1` varchar(50) DEFAULT NULL,
  `option2` varchar(50) DEFAULT NULL,
  `option3` varchar(50) DEFAULT NULL,
  `option4` varchar(50) DEFAULT NULL,
  `correct_option` int(11) DEFAULT NULL,
  PRIMARY KEY (`Srno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `c_questions`
--

LOCK TABLES `c_questions` WRITE;
/*!40000 ALTER TABLE `c_questions` DISABLE KEYS */;
INSERT INTO `c_questions` VALUES (1,'. Which of the following is the correct syntax of including a user defined header files in C++?','#include [userdefined]',' #include \"userdefined\"',' #include <userdefined.h>',' #include <userdefined>',2),(2,'Which of the following is used for comments in C++?',' /* comment */',') // comment */','// comment',' both // comment or /* comment */',4),(3,'Which of the following is a correct identifier in C++?',' VAR_1234',' $var_name','7VARNAME','7var_name',1),(4,' Which of the following is not a type of Constructor in C++?',' Default constructor','Parameterized constructor','Copy constructor',' Friend constructor',4),(5,'. By default, all the files in C++ are opened in _________ mode.','Binary','VTC','Text','ISCII',3),(6,'. Which of the following correctly declares an array in C++?',' array{10};',' array array[10];',' int array;',' int array[10];',4),(7,'The extension for C++ is','.cpp','.py','.java','.html',1),(8,'Which keyword is used to define the macros in c++?','#macro','#define','macro','define',2),(9,'The C++ code which causes abnormal termination/behaviour of a program should be written under _________ block.',' catch','throw','try','finally',3),(10,'What is Inheritance in C++?','Deriving new classes from existing classes',' Overloading of classes','Classes with same names','Wrapping of data into a single class',1);
/*!40000 ALTER TABLE `c_questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `java_questions`
--

DROP TABLE IF EXISTS `java_questions`;
CREATE TABLE `java_questions` (
  `Srno` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `option1` varchar(50) DEFAULT NULL,
  `option2` varchar(50) DEFAULT NULL,
  `option3` varchar(50) DEFAULT NULL,
  `option4` varchar(50) DEFAULT NULL,
  `correct_option` int(11) DEFAULT NULL,
  PRIMARY KEY (`Srno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `java_questions`
--

LOCK TABLES `java_questions` WRITE;
/*!40000 ALTER TABLE `java_questions` DISABLE KEYS */;
INSERT INTO `java_questions` VALUES (1,'Which component is used to compile, debug and execute the java programs?','JRE','JIT','JDK','JVM',3),(2,'Which of the following is not an OOPS concept in Java?','Polymorphism','Inheritance','Compilation','Encapsulation',3),(3,'Which of the following is a type of polymorphism in Java Programming?',' Multiple polymorphism','Compile time polymorphism','Multilevel polymorphism','Execution time polymorphism',2),(4,'Which exception is thrown when java is out of memory?','MemoryError','OutOfMemoryError','MemoryOutOfBoundsException',' MemoryFullException',2),(5,' Which of the following is a superclass of every class in Java?','ArrayList','Abstract class','Object class','String',3),(6,'Which of these packages contains the exception Stack Overflow in Java?','java.io','java.system','java.lang','java.util',3),(7,'What is the numerical range of a char data type in Java?','0 to 256','-128 to 127','0 to 65535','0 to 32767',3),(8,'Which of the following classes can catch all exceptions which cannot be caught?','RuntimeException','Error','Exception','ParentException',2),(9,'Which part of code gets executed whether exception is caught or not?','finally','try','catch','throw',1),(10,' Which of these are selection statements in Java?','break','continue','for()','if()',4);
/*!40000 ALTER TABLE `java_questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `python_questions`
--

DROP TABLE IF EXISTS `python_questions`;
CREATE TABLE `python_questions` (
  `Srno` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `option1` varchar(20) DEFAULT NULL,
  `option2` varchar(20) DEFAULT NULL,
  `option3` varchar(20) DEFAULT NULL,
  `option4` varchar(20) DEFAULT NULL,
  `correct_option` int(11) DEFAULT NULL,
  PRIMARY KEY (`Srno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `python_questions`
--

LOCK TABLES `python_questions` WRITE;
/*!40000 ALTER TABLE `python_questions` DISABLE KEYS */;
INSERT INTO `python_questions` VALUES (1,'Which type of Programming does Python support?',' object-oriented','structured','functional','all',4),(2,'Is Python case sensitive when dealing with identifiers?','no','yes','machine dependent','none',2),(3,'Which of the following is used to define a block of code in Python language?','Indentation','Key','Brackets','All mentioned',1),(4,'Which keyword is used for function in Python language?','Function','def','fun','public static',2),(5,' Python supports the creation of anonymous functions at runtime, using a construct called __________','pi','anonymous','lambda','none',3),(6,'What will be the output of the following Python code snippet if x=1?  x<<2','4','2','1','8',1),(7,'Which of the following functions is a built-in function in python?','factorial()','round()','pow()','print()',4),(8,' Which of the following is not a core data type in Python programming?','Tuples','Lists','Class','Dictionary',3),(9,' What will be the output of the following Python function?  len([\"hello\",2, 4, 6])','Error','6','4','3',3),(10,'What will be the output of the following Python statement?  >>>\"a\"+\"bc\"','bc','abc','a','bca',2);
/*!40000 ALTER TABLE `python_questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
CREATE TABLE `questions` (
  `Srno` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `option1` varchar(20) DEFAULT NULL,
  `option2` varchar(20) DEFAULT NULL,
  `option3` varchar(20) DEFAULT NULL,
  `option4` varchar(20) DEFAULT NULL,
  `correct_option` int(11) DEFAULT NULL,
  PRIMARY KEY (`Srno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,'Which of the following is a mutable data type in Python?','String','Tuple','List','Integer',3),(2,'Single line comment in python is done using?','#','//','<--!>','\'\'\'',1),(3,'What is a variable in programming used for?','Displaying output','Storing data','Creating graphics','Managing files',2),(4,'What is the term for a set of well-defined rules governing the structure and behavior of a program?','Syntax','Algorithm','Variable','Compiler',1),(5,'Which programming language is known for its simplicity and is often used as a beginner\'s language?','Ruby','Java','C++','Python',4),(6,' In programming, what is the term for a predefined, named block of code that performs a specific task?','Loop','Variable','Function','Class',3),(7,'In programming, what is the term for a predefined class or interface that other classes can inherit properties and methods from?','Object','Method','Inheritance','Interface',3),(8,'Keyword used for declaring a function in python?','fun','main','public void','def',4),(9,'Which SQL statement is used to retrieve data from a database?','GET','SELECT','EXTRACT','FIND',2),(10,'Which of the following MySQL statements is used to update existing records in a table?','MODIFY','UPDATE','CHANGE','EDIT',2);
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `responses`
--

DROP TABLE IF EXISTS `responses`;
CREATE TABLE `responses` (
  `domain` varchar(20) DEFAULT NULL,
  `played_date` varchar(50) DEFAULT NULL,
  `played_time` varchar(50) DEFAULT NULL,
  `score` varchar(50) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `responseid` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`responseid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `responses`
--

LOCK TABLES `responses` WRITE;
/*!40000 ALTER TABLE `responses` DISABLE KEYS */;
INSERT INTO `responses` VALUES ('PYTHON','16/11/24','07:44:03 PM','2',1,3),('JAVA','16/11/24','08:12:17 PM','1',1,4),('SQL','16/11/24','08:12:56 PM','0',1,5),('PYTHON','16/11/24','08:13:36 PM','2',1,6),('JAVA','16/11/24','08:15:50 PM','1',2,7),('PYTHON','16/11/24','08:16:20 PM','3',2,8),('C++','17/11/24','02:57:49 PM','3',1,9),('PYTHON','17/11/24','03:15:31 PM','10',3,10),('PYTHON','18/11/24','11:23:09 AM','0',1,11),('JAVA','18/11/24','12:05:55 PM','0',1,12),('SQL','18/11/24','12:24:54 PM','0',1,13),('C++','18/11/24','12:35:16 PM','0',4,14),('JAVA','18/11/24','02:19:51 PM','2',1,15),('C++','19/11/24','10:41:48 PM','0',1,16),('JAVA','20/11/24','03:30:15 PM','0',1,17),('PYTHON','20/11/24','03:41:47 PM','10',1,18);
/*!40000 ALTER TABLE `responses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sql_questions`
--

DROP TABLE IF EXISTS `sql_questions`;
CREATE TABLE `sql_questions` (
  `Srno` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `option1` varchar(50) DEFAULT NULL,
  `option2` varchar(50) DEFAULT NULL,
  `option3` varchar(50) DEFAULT NULL,
  `option4` varchar(50) DEFAULT NULL,
  `correct_option` int(11) DEFAULT NULL,
  PRIMARY KEY (`Srno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sql_questions`
--

LOCK TABLES `sql_questions` WRITE;
/*!40000 ALTER TABLE `sql_questions` DISABLE KEYS */;
INSERT INTO `sql_questions` VALUES (1,'What command is used to create a new table in SQL?','CREATE TABLE','BUILD TABLE','GENERATE TABLE','None',1),(2,'Which of the following operators is used to compare two values in SQL?','+','=','<>','&',3),(3,'What is the purpose of the SQL keyword \"DISTINCT\" in a SELECT statement?','To retrieve unique values from a column','To filter NULL values',' To delete duplicate records','To sort the result set',1),(4,'Which of the following tasks CANNOT be accomplished using SQL?','Creating and modifying database structures','Writing complex algorithms for data analysis','Retrieving specific data from a database','Adding new data to a database',2),(5,'Which of the following is basis for SQL?','SQL Server','DBMS','RDBMS','Oracle',3),(6,'Which statement(s) are mandatory in a simple SQL SELECT statement?','Select, From','Select, OrderBy','Select, Where',' Select, GroupBy',1),(7,'Which of the following is a default join type?','Right join','Left join','Inner join','Outer join',3),(8,'Which of the following SQL statement selects only unique values from section column of table school?','SELECT section FROM school','SELECT DISTINCT section FROM school','SELECT * FROM school','SELECT ALL section FROM school',2),(9,' In SQL, which of the following constraint is used to establish a link between two tables?','PRIMARY KEY','LINK','FOREIGN KEY','CANDIDATE KEY',3),(10,'Which of the following datatype is used to display a combination of date and time information?',' DATETIME','DATE','TIME','TIMESTAMP',1);
/*!40000 ALTER TABLE `sql_questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_details`
--

DROP TABLE IF EXISTS `user_details`;
CREATE TABLE `user_details` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

LOCK TABLES `user_details` WRITE;
/*!40000 ALTER TABLE `user_details` DISABLE KEYS */;
INSERT INTO `user_details` VALUES (1,'lucky','luck@#123'),(2,'Gautam','gautam@#123'),(3,'Dev','Dev123'),(4,'Siddhu','sidd'),(5,'Chandu','123'),(6,'NARAYAN','shreekrishna');
/*!40000 ALTER TABLE `user_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-20 10:41:37
