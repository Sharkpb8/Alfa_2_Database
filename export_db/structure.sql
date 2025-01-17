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
-- Temporary view structure for view `All_rezervations`
--

DROP TABLE IF EXISTS `All_rezervations`;
/*!50001 DROP VIEW IF EXISTS `All_rezervations`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `All_rezervations` AS SELECT 
 1 AS `Name`,
 1 AS `Last_name`,
 1 AS `Rezervation_date`,
 1 AS `Ticket_ammount`,
 1 AS `Movie_name`,
 1 AS `Hall_name`,
 1 AS `Hall_type`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Last_name` varchar(30) NOT NULL,
  `Loyalty_program` bit(1) DEFAULT (0),
  `Loyalty_points` decimal(10,2) NOT NULL DEFAULT (0),
  `Registry_date` date NOT NULL DEFAULT (curdate()),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Genre`
--

DROP TABLE IF EXISTS `Genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Genre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Name` (`Name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Hall`
--

DROP TABLE IF EXISTS `Hall`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Hall` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Type` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Name` (`Name`),
  CONSTRAINT `Hall_chk_1` CHECK ((`Type` in (_utf8mb4'Standartní',_utf8mb4'VIP')))
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `Hall_Type_Summary`
--

DROP TABLE IF EXISTS `Hall_Type_Summary`;
/*!50001 DROP VIEW IF EXISTS `Hall_Type_Summary`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `Hall_Type_Summary` AS SELECT 
 1 AS `Type`,
 1 AS `Name`,
 1 AS `Total_revenue`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Movie`
--

DROP TABLE IF EXISTS `Movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Movie` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Genre_id` int NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Lenght` int NOT NULL,
  `Price` decimal(10,2) NOT NULL,
  `Premiere_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Name` (`Name`),
  KEY `Genre_id` (`Genre_id`),
  CONSTRAINT `Movie_ibfk_1` FOREIGN KEY (`Genre_id`) REFERENCES `Genre` (`id`),
  CONSTRAINT `Movie_chk_1` CHECK ((`Lenght` > 0)),
  CONSTRAINT `Movie_chk_2` CHECK ((`Price` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `MovieSummary`
--

DROP TABLE IF EXISTS `MovieSummary`;
/*!50001 DROP VIEW IF EXISTS `MovieSummary`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `MovieSummary` AS SELECT 
 1 AS `Movie_Name`,
 1 AS `Number_of_Reservations`,
 1 AS `Total_Revenue`,
 1 AS `Average_ticket_ammount`,
 1 AS `Average_Rezervation_Price`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `NextScreeningCustomers`
--

DROP TABLE IF EXISTS `NextScreeningCustomers`;
/*!50001 DROP VIEW IF EXISTS `NextScreeningCustomers`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `NextScreeningCustomers` AS SELECT 
 1 AS `Name`,
 1 AS `Last_name`,
 1 AS `Purchase_date`,
 1 AS `Ticket_ammount`,
 1 AS `Total_price`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Points`
--

DROP TABLE IF EXISTS `Points`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Points` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Customer_id` int DEFAULT NULL,
  `ammount` decimal(10,2) DEFAULT NULL,
  `date` date DEFAULT (curdate()),
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Customer_id` (`Customer_id`),
  CONSTRAINT `Points_ibfk_1` FOREIGN KEY (`Customer_id`) REFERENCES `Customer` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Rezervation`
--

DROP TABLE IF EXISTS `Rezervation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rezervation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Customer_id` int NOT NULL,
  `Screening_id` int NOT NULL,
  `Date` date NOT NULL,
  `Ticket_ammount` int NOT NULL DEFAULT (0),
  `Total_price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Customer_id` (`Customer_id`),
  KEY `Screening_id` (`Screening_id`),
  CONSTRAINT `Rezervation_ibfk_1` FOREIGN KEY (`Customer_id`) REFERENCES `Customer` (`id`),
  CONSTRAINT `Rezervation_ibfk_2` FOREIGN KEY (`Screening_id`) REFERENCES `Screening` (`id`),
  CONSTRAINT `Rezervation_chk_1` CHECK ((`Ticket_ammount` > 0)),
  CONSTRAINT `Rezervation_chk_2` CHECK ((`Total_price` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Screening`
--

DROP TABLE IF EXISTS `Screening`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Screening` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Movie_id` int NOT NULL,
  `Hall_id` int NOT NULL,
  `Date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Movie_id` (`Movie_id`),
  KEY `Hall_id` (`Hall_id`),
  CONSTRAINT `Screening_ibfk_1` FOREIGN KEY (`Movie_id`) REFERENCES `Movie` (`id`),
  CONSTRAINT `Screening_ibfk_2` FOREIGN KEY (`Hall_id`) REFERENCES `Hall` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `TotalMovieTickets`
--

DROP TABLE IF EXISTS `TotalMovieTickets`;
/*!50001 DROP VIEW IF EXISTS `TotalMovieTickets`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `TotalMovieTickets` AS SELECT 
 1 AS `Name`,
 1 AS `ammount`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `temp_customer`
--

DROP TABLE IF EXISTS `temp_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `temp_customer` (
  `id` int NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Last_name` varchar(30) DEFAULT NULL,
  `Loyalty_program` bit(1) DEFAULT (0),
  `Loyalty_points` decimal(10,2) DEFAULT NULL,
  `Registry_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping routines for database 'Cinema'
--
/*!50003 DROP PROCEDURE IF EXISTS `CreateCustomer` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`admin`@`%` PROCEDURE `CreateCustomer`(IN _Name varchar(30), IN _Last_name varchar(30), In _Loyalty_program bit, In _Loyalty_points varchar(30),_Registry_date date)
BEGIN
    insert into Customer(Name, Last_name, Loyalty_program, Loyalty_points,Registry_date) values(_Name,_Last_name,_Loyalty_program,_Loyalty_points,_Registry_date);
	insert into Points(Customer_id,ammount,description) values(LAST_INSERT_ID(),_Loyalty_points,'Založení účtu');
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `InsertRezervation` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`admin`@`%` PROCEDURE `InsertRezervation`(IN _Customer_id int,IN _Screening_id int,IN _Date date,IN _Ticket_ammount int)
BEGIN
    DECLARE _Movie_id INT;
	Declare _price decimal(10,2);
    
    SELECT id INTO _Movie_id
    FROM Screening
    WHERE id = _Screening_id;
    
    select Price into _price
    from Movie
    where id = _Movie_id;
    
    set _price = _price*_Ticket_ammount;
    
    insert into Rezervation(Customer_id,Screening_id,Date,Ticket_ammount,Total_price) values(_Customer_id,_Screening_id,_Date,_Ticket_ammount,_price);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `TransferPoints` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`admin`@`%` PROCEDURE `TransferPoints`(IN _from_id int,IN _to_id int,IN _ammount int)
BEGIN
    UPDATE Customer 
    SET Loyalty_points = Loyalty_points-_ammount WHERE id = _from_id;
    
	insert into Points(Customer_id,ammount,description) values(_from_id,-_ammount,'Převod');
    
	UPDATE Customer 
    SET Loyalty_points = Loyalty_points+_ammount WHERE id = _to_id;
    
    insert into Points(Customer_id,ammount,description) values(_to_id,_ammount,'Převod');
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UpdateCustomer` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`admin`@`%` PROCEDURE `UpdateCustomer`(IN _id int)
begin
	UPDATE Customer AS c
	JOIN temp_customer AS t ON t.id = c.id
	SET c.Name = t.Name,
		c.Last_name = t.Last_name,
		c.Loyalty_program = t.Loyalty_program,
		c.Loyalty_points = t.Loyalty_points,
		c.Registry_date = t.Registry_date
	where c.id = _id;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UpdateRezervation` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`admin`@`%` PROCEDURE `UpdateRezervation`(IN _id int,IN _Customer_id int,IN _Screening_id int,IN _Date date,IN _Ticket_ammount int)
BEGIN
    DECLARE _Movie_id INT;
	Declare _price decimal(10,2);
    
    SELECT id INTO _Movie_id
    FROM Screening
    WHERE id = _Screening_id;
    
    select Price into _price
    from Movie
    where id = _Movie_id;
    
    set _price = _price*_Ticket_ammount;
    
    update Rezervation
    set Customer_id = _Customer_id,Screening_id = _Screening_id,Date = _Date,Ticket_ammount=_Ticket_ammount,Total_price=_price
    where id = _id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `All_rezervations`
--

/*!50001 DROP VIEW IF EXISTS `All_rezervations`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `All_rezervations` AS select `c`.`Name` AS `Name`,`c`.`Last_name` AS `Last_name`,`r`.`Date` AS `Rezervation_date`,`r`.`Ticket_ammount` AS `Ticket_ammount`,`m`.`Name` AS `Movie_name`,`h`.`Name` AS `Hall_name`,`h`.`Type` AS `Hall_type` from ((((`Customer` `c` join `Rezervation` `r` on((`r`.`Customer_id` = `c`.`id`))) join `Screening` `s` on((`r`.`Screening_id` = `s`.`id`))) join `Movie` `m` on((`s`.`Movie_id` = `m`.`id`))) join `Hall` `h` on((`s`.`Hall_id` = `h`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `Hall_Type_Summary`
--

/*!50001 DROP VIEW IF EXISTS `Hall_Type_Summary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `Hall_Type_Summary` AS select `h`.`Type` AS `Type`,`g`.`Name` AS `Name`,sum(`r`.`Total_price`) AS `Total_revenue` from ((((`Rezervation` `r` join `Screening` `s` on((`r`.`Screening_id` = `s`.`id`))) join `Movie` `m` on((`s`.`Movie_id` = `m`.`id`))) join `Genre` `g` on((`m`.`Genre_id` = `g`.`id`))) join `Hall` `h` on((`s`.`Hall_id` = `h`.`id`))) group by `h`.`Type`,`g`.`Name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `MovieSummary`
--

/*!50001 DROP VIEW IF EXISTS `MovieSummary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `MovieSummary` AS select `m`.`Name` AS `Movie_Name`,count(`r`.`id`) AS `Number_of_Reservations`,sum(`r`.`Total_price`) AS `Total_Revenue`,round(avg(`r`.`Ticket_ammount`),2) AS `Average_ticket_ammount`,round(avg(`r`.`Total_price`),2) AS `Average_Rezervation_Price` from ((`Movie` `m` join `Screening` `s` on((`m`.`id` = `s`.`Movie_id`))) join `Rezervation` `r` on((`s`.`id` = `r`.`Screening_id`))) group by `m`.`Name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `NextScreeningCustomers`
--

/*!50001 DROP VIEW IF EXISTS `NextScreeningCustomers`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `NextScreeningCustomers` AS select `c`.`Name` AS `Name`,`c`.`Last_name` AS `Last_name`,`r`.`Date` AS `Purchase_date`,`r`.`Ticket_ammount` AS `Ticket_ammount`,`r`.`Total_price` AS `Total_price` from ((`Customer` `c` join `Rezervation` `r` on((`r`.`Customer_id` = `c`.`id`))) join `Screening` `s` on((`r`.`Screening_id` = `s`.`id`))) where (`s`.`id` = (select `Screening`.`id` from `Screening` where (`Screening`.`Date` > curtime()) limit 1)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `TotalMovieTickets`
--

/*!50001 DROP VIEW IF EXISTS `TotalMovieTickets`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `TotalMovieTickets` AS select `m`.`Name` AS `Name`,sum(`r`.`Ticket_ammount`) AS `ammount` from ((`Movie` `m` join `Screening` `s` on((`s`.`Movie_id` = `m`.`id`))) join `Rezervation` `r` on((`r`.`Screening_id` = `s`.`id`))) group by `m`.`Name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-17 23:40:28
COMMIT;