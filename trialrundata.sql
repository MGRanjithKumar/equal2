-- phpMyAdmin SQL Dump
-- version 4.0.10.14
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: Feb 25, 2017 at 11:03 AM
-- Server version: 5.6.33-cll-lve
-- PHP Version: 5.6.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `HOD_vision17`
--

-- --------------------------------------------------------

--
-- Table structure for table `equalto_vision17_users`
--

CREATE TABLE IF NOT EXISTS `equalto_vision17_users` (
  `uID` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(200) DEFAULT NULL,
  `startTime` bigint(20) DEFAULT NULL,
  `endTime` bigint(20) DEFAULT NULL,
  `count` int(11) NOT NULL DEFAULT '0',
  `score` int(11) NOT NULL DEFAULT '0',
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  `q5` int(11) DEFAULT NULL,
  `q6` int(11) DEFAULT NULL,
  `q7` int(11) DEFAULT NULL,
  `q8` int(11) DEFAULT NULL,
  `q9` int(11) DEFAULT NULL,
  `q10` int(11) DEFAULT NULL,
  `q11` int(11) DEFAULT NULL,
  `q12` int(11) DEFAULT NULL,
  `q13` int(11) DEFAULT NULL,
  `q14` int(11) DEFAULT NULL,
  `q15` int(11) DEFAULT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`uID`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=42 ;

--
-- Dumping data for table `equalto_vision17_users`
--

INSERT INTO `equalto_vision17_users` (`uID`, `email`, `startTime`, `endTime`, `count`, `score`, `q1`, `q2`, `q3`, `q4`, `q5`, `q6`, `q7`, `q8`, `q9`, `q10`, `q11`, `q12`, `q13`, `q14`, `q15`, `last_update`) VALUES
(23, 'reuben.mathew1995@gmail.com', 1488039963, 1488041763, 15, 5, 3, 2, 4, 1, 4, 4, 3, 1, 2, 4, 2, 1, 1, 1, 2, '2017-02-25 16:30:22'),
(22, 'vwthala0@gmail.com', 1488039940, 1488041740, 11, 0, 1, 1, 3, 4, 1, 1, 2, 2, 2, 3, 1, NULL, NULL, NULL, NULL, '2017-02-25 16:27:28'),
(20, 'k.sourabi.1996@gmail.com', 1488039549, 1488041349, 15, 2, 1, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, '2017-02-25 16:22:25'),
(21, 'rsreekailash95@gmail.com', 1488039767, 1488041567, 15, 3, 1, 3, 1, 4, 2, 3, 2, 3, 1, 2, 1, 3, 4, 1, 2, '2017-02-25 16:23:38'),
(19, 'rkvigneswaran@gmail.com', 1488031838, 1488033638, 15, 6, 1, 3, 2, 1, 3, 2, 3, 3, 3, 4, 1, 4, 3, 3, 1, '2017-02-25 14:11:42'),
(24, 'arunpandi984353@gmail.com', 1488039973, 1488041773, 15, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, '2017-02-25 16:31:47'),
(25, 'wasted1508@gmail.com', 1488040246, 1488042046, 1, 0, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2017-02-25 16:31:29'),
(26, 'ranjithmg21@gmail.com', 1488040524, 1488042324, 5, 0, 2, 3, 1, 1, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2017-02-25 16:36:15'),
(27, 'sivasivacsc@gmail.com', 1488040541, 1488042341, 2, 0, 4, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2017-02-25 16:51:05'),
(28, 'srimathi1312@gmail.com', 1488040589, 1488042389, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2017-02-25 16:36:29'),
(29, 'athickvijay@gmail.com', 1488040664, 1488042464, 15, 3, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, '2017-02-25 16:39:29'),
(30, 'raginivenkatakrishnan@gmail.com', 1488040749, 1488042549, 15, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, '2017-02-25 16:41:14'),
(31, 'vgn.sanjana@gmail.com', 1488041429, 1488043229, 15, 6, 1, 2, 4, 1, 2, 2, 3, 4, 1, 2, 3, 4, 1, 3, 4, '2017-02-25 16:55:02'),
(32, 'poojakuppan@gmail.com', 1488041468, 1488043268, 15, 3, 1, 2, 2, 1, 2, 1, 1, 2, 4, 4, 2, 3, 1, 3, 1, '2017-02-25 16:54:00'),
(33, 'vicky25796@gmail.com', 1488041475, 1488043275, 15, 4, 2, 1, 4, 3, 2, 1, 3, 1, 4, 3, 1, 1, 2, 4, 3, '2017-02-25 16:54:09'),
(34, 'usrini9795@gmail.com', 1488041747, 1488043547, 14, 4, 1, 1, 2, 3, 4, 1, 3, 4, 2, 3, 1, 4, 2, 3, NULL, '2017-02-25 17:25:52'),
(35, 'skyisyello@gmail.com', 1488041839, 1488043639, 15, 4, 1, 2, 1, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, '2017-02-25 17:01:14'),
(36, 'rajnivas711@gmail.com', 1488041965, 1488043765, 1, 0, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2017-02-25 16:59:52'),
(37, 'sharuga.kiruba@gmail.com', 1488042140, 1488043940, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2017-02-25 17:02:20'),
(38, 'mukundmathers@gmail.com', 1488042724, 1488044524, 15, 2, 4, 3, 2, 1, 4, 3, 3, 4, 2, 2, 1, 4, 3, 4, 4, '2017-02-25 17:13:12'),
(39, 'chintukarthi@gmail.com', 1488043383, 1488045183, 15, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, '2017-02-25 17:26:06'),
(40, 'mmfaizal97@gmail.com', 1488043538, 1488045338, 15, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, '2017-02-25 17:27:26'),
(41, 'hari.blogscripts@gmail.com', 1488043613, 1488045413, 5, 0, 4, 3, 3, 1, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2017-02-25 17:27:58');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
