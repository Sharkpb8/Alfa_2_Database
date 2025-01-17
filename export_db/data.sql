start transaction;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 18.199.158.215    Database: Cinema
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (1,'Adam','Hlaváčik',_binary '\0',100.00,'2025-01-11'),(2,'John','Doe',_binary '\0',0.00,'2025-01-01'),(3,'Jane','Smith',_binary '',250.00,'2025-01-02'),(4,'Alice','Johnson',_binary '\0',0.00,'2025-01-03'),(19,'Ondra','Kabrt',_binary '\0',0.00,'2025-01-12'),(52,'dirty','write',_binary '\0',666.00,'1900-01-01');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Genre`
--

LOCK TABLES `Genre` WRITE;
/*!40000 ALTER TABLE `Genre` DISABLE KEYS */;
INSERT INTO `Genre` VALUES (2,'Action'),(3,'Comedy'),(4,'Drama'),(5,'Horror'),(1,'Sci-fi');
/*!40000 ALTER TABLE `Genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Hall`
--

LOCK TABLES `Hall` WRITE;
/*!40000 ALTER TABLE `Hall` DISABLE KEYS */;
INSERT INTO `Hall` VALUES (1,'Main Hall','Standartní'),(2,'VIP Lounge','VIP');
/*!40000 ALTER TABLE `Hall` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Movie`
--

LOCK TABLES `Movie` WRITE;
/*!40000 ALTER TABLE `Movie` DISABLE KEYS */;
INSERT INTO `Movie` VALUES (1,1,'Fast and Furious',120,150.00,'2025-01-01'),(2,2,'The Hangover',100,130.00,'2025-01-02'),(3,3,'The Shawshank Redemption',142,200.00,'2025-01-03'),(4,4,'It',135,180.00,'2025-01-04');
/*!40000 ALTER TABLE `Movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Points`
--

LOCK TABLES `Points` WRITE;
/*!40000 ALTER TABLE `Points` DISABLE KEYS */;
INSERT INTO `Points` VALUES (2,52,0.00,'2025-01-17','Založení účtu'),(3,3,-100.00,'2025-01-17','Převod'),(4,1,100.00,'2025-01-17','Převod');
/*!40000 ALTER TABLE `Points` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Rezervation`
--

LOCK TABLES `Rezervation` WRITE;
/*!40000 ALTER TABLE `Rezervation` DISABLE KEYS */;
INSERT INTO `Rezervation` VALUES (12,1,1,'2025-01-05',2,300.00),(13,2,2,'2025-01-06',3,390.00),(14,3,3,'2025-01-07',1,200.00),(17,19,3,'2025-01-06',2,400.00),(19,2,2,'2026-11-11',7,910.00);
/*!40000 ALTER TABLE `Rezervation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Screening`
--

LOCK TABLES `Screening` WRITE;
/*!40000 ALTER TABLE `Screening` DISABLE KEYS */;
INSERT INTO `Screening` VALUES (1,1,1,'2025-01-10 18:00:00'),(2,2,1,'2025-01-11 20:00:00'),(3,3,2,'2025-01-12 19:00:00'),(4,4,2,'2025-01-13 21:00:00');
/*!40000 ALTER TABLE `Screening` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `temp_customer`
--

LOCK TABLES `temp_customer` WRITE;
/*!40000 ALTER TABLE `temp_customer` DISABLE KEYS */;
INSERT INTO `temp_customer` VALUES (52,'dirty','write',_binary '\0',666.00,'1900-01-01');
/*!40000 ALTER TABLE `temp_customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-17 23:40:08
COMMIT;