-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: flight_booking_system
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings` (
  `Flight_ID` int DEFAULT NULL,
  `Passenger_ID` int DEFAULT NULL,
  `Class` varchar(20) DEFAULT NULL,
  `Seat_No` int DEFAULT NULL,
  `Luggage` varchar(20) DEFAULT NULL,
  `Status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
INSERT INTO `bookings` VALUES (23671,154,'Economy',22,'9kg','Late'),(56123,103,'Economy',1,'5kg','Boarded'),(76549,98,'Economy',9,'8kg','Missed'),(23671,118,'First Class',65,'23kg','Boarded'),(23671,1842,'Economy',37,'6kg','Boarded'),(111,199,'Buisness',13,'10kg','Boarded');
/*!40000 ALTER TABLE `bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flights`
--

DROP TABLE IF EXISTS `flights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flights` (
  `Flight_No` int DEFAULT NULL,
  `Flight_Name` varchar(20) DEFAULT NULL,
  `Origin` varchar(20) DEFAULT NULL,
  `Destination` varchar(20) DEFAULT NULL,
  `Departure_Date` date DEFAULT NULL,
  `Departure_Time` time DEFAULT NULL,
  `Arrival_Time` time DEFAULT NULL,
  `Status` varchar(20) DEFAULT NULL,
  `Route_ID` int NOT NULL,
  PRIMARY KEY (`Route_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flights`
--

LOCK TABLES `flights` WRITE;
/*!40000 ALTER TABLE `flights` DISABLE KEYS */;
INSERT INTO `flights` VALUES (76549,'Qatar Airlines','Delhi','Dubai','2024-10-27','20:00:00','20:25:00','Arrived',102),(21353,'AirIndo','Indonesia','Delhi','2024-10-29','09:00:00','12:00:00','Delayed',103),(111,'AirHigh','London','Kolkata','2024-11-23','14:00:00','02:00:00','Arrived',105),(23671,'AirAsia','Mumbai','New York','2024-11-19','10:00:00','03:00:00','Delayed',106);
/*!40000 ALTER TABLE `flights` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passengers`
--

DROP TABLE IF EXISTS `passengers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passengers` (
  `Passenger_ID` int DEFAULT NULL,
  `Passenger_Name` varchar(20) DEFAULT NULL,
  `DateOfBirth` date DEFAULT NULL,
  `Contact_No` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passengers`
--

LOCK TABLES `passengers` WRITE;
/*!40000 ALTER TABLE `passengers` DISABLE KEYS */;
INSERT INTO `passengers` VALUES (103,'Mrs. Sushmita ','1999-12-03',748174912),(118,'Ms. Anushka','2000-04-28',530725964),(98,'Ms. Akriti','2007-08-28',110284728),(172,'Mr. Sushant','2002-09-26',193163926),(1842,'Mr. Ravinder','1982-06-01',103728492),(891,'Mr. Ravi','1992-02-22',218495038),(199,'Mrs. Harris','1994-09-23',923148639);
/*!40000 ALTER TABLE `passengers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-26  0:30:06
