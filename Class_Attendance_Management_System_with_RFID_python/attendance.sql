-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 04, 2020 at 03:37 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `attendance`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
CREATE TABLE IF NOT EXISTS `attendance` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` varchar(255) NOT NULL,
  `attendance_status` int(11) NOT NULL,
  `current_dater` date NOT NULL,
  `current_timer` time NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`ID`, `student_id`, `attendance_status`, `current_dater`, `current_timer`) VALUES
(7, 'j17-9014-2016', 1, '2020-11-04', '13:11:17'),
(6, 'j17-9015-2016', 1, '2020-11-04', '12:20:21');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
CREATE TABLE IF NOT EXISTS `students` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` varchar(255) NOT NULL,
  `firstname` varchar(30) DEFAULT NULL,
  `secondname` varchar(30) DEFAULT NULL,
  `surname` varchar(30) DEFAULT NULL,
  `attendance_status` int(11) NOT NULL DEFAULT '0',
  `member_id` varchar(20) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `member_id` (`member_id`),
  UNIQUE KEY `student_id` (`student_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`ID`, `student_id`, `firstname`, `secondname`, `surname`, `attendance_status`, `member_id`) VALUES
(1, 'j17-9014-2016', 'titus', 'kemboi', 'cheserem', 0, '2519180581'),
(2, 'j17-9015-2016', 'john', 'omollo', 'chakran', 0, '3006698810');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
