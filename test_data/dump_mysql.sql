-- MySQL dump 10.13
--
-- Host: localhost    Database: webapp

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `username`, `password`, `name`) VALUES
(1, 'alice@example.com', 'alice', 'hunter2', 'Alice Smith'),
(2, 'bob@example.com', 'bob_jones', 'p@ssw0rd', 'Bob Jones'),
(3, 'charlie@test.org', 'charlie', 'qwerty123', 'Charlie Brown');

INSERT INTO `users` (`id`, `email`, `username`, `password`, `name`) VALUES (4, 'dave@corp.net', 'dave', 'letmein', 'Dave Wilson');
