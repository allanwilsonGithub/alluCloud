-- MySQL dump 10.13  Distrib 5.6.14, for Win64 (x86_64)
--
-- Host: localhost    Database: eventdb
-- ------------------------------------------------------
-- Server version	5.6.14

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
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events` (
  `eventID` int(11) NOT NULL AUTO_INCREMENT,
  `eventType` int(11) DEFAULT '0',
  `eventName` varchar(255) DEFAULT '0',
  `date` date DEFAULT '2000-00-20',
  `year` year(4) DEFAULT '2020',
  `recurring` int(11) DEFAULT '0',
  `comment` varchar(255) DEFAULT '0',
  PRIMARY KEY (`eventID`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES (1,1,'Allan Wilson','2017-01-13',1974,1,'My birthday'),(2,1,'Paula Wilson','2016-10-13',1974,1,'Vaimoni'),(3,2,'Post Dads book','2012-04-16',2020,0,'At Iso Omena'),(4,3,'Juhannuspaiva','2017-06-24',2020,1,'correct for2016'),(5,1,'Ania Grajek','2017-04-21',2020,1,'Polish lass'),(6,4,'Sampo caring 4-6','2012-04-15',2020,0,'Paula at swimming'),(7,5,'New towel to work','2012-04-16',2020,0,'Cos old one is smelly'),(8,3,'Vappu','2017-05-01',2020,1,'Naantali 2016'),(10,3,'Christmas Day','2016-12-25',2020,1,''),(11,1,'Elaine Wilson','2017-04-03',1971,1,'Sisko'),(12,1,'Erik Kohl','2016-11-05',2020,1,'Wee German boy!'),(13,1,'Murdo Wilson','2017-01-03',1943,1,'Dad'),(14,1,'Joyce Wilson','2017-09-16',1947,1,'Mum'),(15,1,'Viia','2017-07-13',2020,1,'Lahti Satu and Samis girl'),(16,1,'Douglas Exton','2017-07-10',1976,1,'Erics man'),(17,1,'Lena Stevenson','2017-09-02',2020,1,'Gran'),(18,1,'Laura Hangasvaara','2017-01-07',2020,1,'Paulas sister'),(19,1,'Rhona Gibson','2017-01-29',2020,1,'Mogs wife'),(20,1,'Mari Pekkala','2017-03-03',2020,1,'Kemi'),(22,1,'Eric Burrows','2017-05-21',2020,1,'Best man'),(23,1,'Michael Gibson','2017-07-18',2020,1,'Mog'),(24,1,'Philip Gibson','2017-09-02',2020,1,'Mog\'s boy'),(25,1,'Eilidh Wilson','2016-10-13',2020,1,'Forfar'),(26,1,'Fraser Wilson','2017-03-27',2020,1,'Forfar'),(27,1,'Hanna Kantola','2016-10-13',2020,1,'Paulan aiti'),(28,1,'Ari Hangasvaara','2016-10-13',2020,1,'Lauras ex'),(29,1,'Rachel Salmon','2016-11-17',2020,1,'Jordie'),(30,1,'Rauno Kantola','2016-12-13',2020,1,'Paulan isä'),(32,1,'Seba Friberg','2016-11-14',2020,1,'Seba'),(33,1,'Sampo James Ensio Wilson','2016-11-15',2011,1,'Born 11:18pm'),(34,1,'Thomas Kohl','2017-01-15',2020,1,'German bloke'),(36,1,'Antti Leppäkorpi','2016-10-23',2020,1,'Jyvaskyla'),(37,3,'New Years Day','2017-01-01',2020,1,'Party time'),(39,1,'Catriona MacKenzie Lawson','2016-09-27',2020,1,'Aberdeen Uni'),(40,1,'Craig Duncanson','2017-06-15',2020,1,'Pud'),(41,1,'Dawn Alexander','2017-08-30',2020,1,'NZ'),(43,1,'Emrys Kirby','2017-09-06',2020,1,'Aberdeen Uni'),(44,1,'Ewan Cameron-Nielsen','2017-05-22',2020,1,'School'),(46,3,'Valentines Day','2017-02-14',2020,1,'Buy flowers!'),(47,4,'Wilson Anniversary','2017-07-03',2020,1,'Our Anniversary'),(48,1,'Lotta Kallioinen','2017-02-14',2020,1,'Born on valentine\'s day!'),(49,3,'Mothers Day UK','2017-03-18',2020,1,'Might be different each year'),(50,4,'Sampo caring','2012-04-14',2020,0,'Paulas at gym'),(51,1,'Juha Isonikkilä','2017-04-24',2020,1,'Kemi'),(52,3,'Mothers Day FI','2017-05-08',2020,1,'Correct for 2016'),(53,4,'Eddie Izzard','2013-04-11',2020,0,'Force Majeure'),(54,1,'Timo Viipuri','2017-05-14',2020,1,'Fly guy'),(55,3,'J.L. Runeberg Day','2017-02-05',2020,1,'Flag day'),(56,4,'Tour De Helsinki 2012','2012-09-02',2020,0,'140 kms cycle ride'),(59,4,'One year at home starts','2012-12-22',2020,0,'0'),(60,1,'Check kitchen sink pipes','2013-02-22',2020,0,'Check for any leaks every 4 months'),(61,4,'Antti and Anna\'s Wedding reception','2013-02-23',2020,0,'Mikkeli?'),(62,4,'Jungle Junction','2013-02-01',2020,0,'0'),(63,4,'Mum and Dad arrive','2013-02-06',2020,0,'0'),(64,4,'Mum and Dad fly home','2013-02-18',2020,0,'0'),(65,3,'Vauvakiino','2013-03-14',2020,0,'0'),(66,4,'Tour De Helsinki 2013','2013-09-01',2020,0,'140 kms cycle ride'),(67,4,'GiroD Espoo','2013-05-26',2020,0,'111 kms cycle ride'),(68,5,'Register for Suomea testi','2013-06-03',2020,0,'Testipaiva on 31.8.. but confirm this'),(69,4,'Keskitaso testi','2013-08-31',2020,0,'suomen kieli'),(70,5,'Webinar','2013-06-25',2013,0,'I think it was about 2pm'),(71,5,'Leave for Scotland','2013-06-29',2013,0,'Holidays start!'),(72,4,'Ulrasound','2013-08-27',2013,0,''),(73,5,'Bank meeting','2013-07-17',2013,0,'12:30 Heidi Rahka'),(74,2,'Cancel Netflix','2013-09-03',2013,0,''),(75,1,'Marjo Ala-Poikela','2016-10-20',2020,1,'Birthday for Marjo'),(76,5,'Mum and Dad anniversary','2016-10-19',2020,1,'.'),(77,4,'Birth of our baby girl','2014-01-08',2014,0,''),(78,2,'Refresh work backup','2014-05-01',2014,0,','),(79,3,'Easter Friday','2017-03-25',2020,1,'correct for 2016'),(80,3,'Easter Sunday','2017-03-27',2020,1,'correct for 2016'),(81,3,'Easter Monday','2017-03-28',2020,1,'correct for 2016'),(82,3,'Helatorstai','2017-05-25',2020,1,'correct for 2017'),(83,4,'Itsenaisyyspaiva','2016-12-06',2020,1,'Day off'),(84,4,'Fly to Lapland','2014-06-27',2014,0,'Summer hols start!'),(85,4,'Allan flies home','2014-07-06',2014,0,'Solo flight home'),(86,4,'Paula, Laura, Sampo and Seela fly home','2014-07-15',2014,0,''),(87,4,'Fly to Scotland!','2014-07-19',2014,0,''),(88,4,'Fly home from Scotland','2014-08-01',2014,0,'Summer hols ending :('),(89,4,'Spring concert','2014-05-24',2014,0,'Sampo nursery'),(90,4,'Fathers Day UK 2014','2014-06-15',2014,0,'correct for 2014'),(91,3,'James Bach Testing Evening','2014-10-30',2014,0,'Check date'),(92,4,'Eurostar Conference','2014-09-16',2014,0,'All day'),(95,5,'Meet Timo 2pm','2015-01-03',2015,0,'Still to decide where. Maybe angry birds park 2pm'),(96,4,'Seela Birthday party','2015-01-10',2015,0,''),(97,4,'SLASH GIG','2015-05-28',2015,0,'Starts at 19:00'),(98,5,'Isanpaiva FI','2016-11-08',2015,1,'Correct for 2015'),(99,1,'Seela Elaine Auroora Wilson','2017-01-12',2014,1,'19:44 3000g 48cms Jorvi '),(100,2,'Dentist','2015-04-27',2015,0,'11:15 for 15 mins rmember kela discount'),(101,5,'Ebook','2015-05-20',2015,0,'[Double eBook] Programming for Testers v1.0 & How to assess your Test Manager'),(102,5,'Webinar','2015-05-27',2015,0,'Complicated Testing'),(103,5,'Fathers Day UK','2017-06-19',2016,1,'Correct for 2016'),(104,2,'Test','2015-09-08',2015,0,'Mums present'),(105,4,'Boys Night','2015-09-11',2015,0,''),(106,5,'Choose cabins on Christmas train','2015-10-20',2015,0,''),(107,2,'test','2015-11-21',2015,0,''),(108,5,'Rachel Salmons Wedding','2016-06-11',2016,0,'0'),(109,2,'Go To Work','2016-01-20',2016,0,''),(110,2,'Pay Carousel','2016-02-10',2016,0,''),(111,2,'Pay carousel March','2016-03-10',2016,0,''),(112,2,'Clean Windows','2016-03-20',2016,0,''),(113,3,'Burns Night','2017-01-25',2017,1,''),(114,3,'Mothers Day UK','2017-03-26',2017,1,'Correct for 2017'),(115,2,'Pay Carousel','2016-05-10',2016,0,''),(116,2,'Pay carousel','2016-06-10',2016,0,''),(117,2,'Pay Carousel','2016-07-10',2016,0,''),(118,5,'Sanna Teemu Linus grilling','2016-06-18',2016,0,'4pm. Take beer and Czech stuff'),(119,4,'To Scotland','2016-07-03',2016,0,''),(120,5,'Library books and CD','2016-07-18',2016,0,'I can renew them again online'),(121,2,'WINDOWS INSIDE','2016-08-10',2016,0,''),(122,2,'Testing the DATE','2016-08-16',2016,0,''),(123,2,'DATE TEST 2','2017-09-14',2018,0,''),(124,4,'Sampo and Seela school photo','2016-08-31',2016,0,''),(125,5,'Webinar 4pm','2016-09-14',2016,0,'4pm - 5pm Selenium 3.0'),(126,4,'Testing Assembly Day','2016-09-21',2016,0,'Wholde day event'),(127,5,'Go To Neuvola to check Seelas rokotus','2016-09-28',2016,0,''),(128,5,'Help Thomas move house','2016-09-23',2016,0,'');
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eventtypes`
--

DROP TABLE IF EXISTS `eventtypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `eventtypes` (
  `eventTypeID` int(11) NOT NULL AUTO_INCREMENT,
  `typeName` varchar(200) NOT NULL,
  `comment` varchar(255) DEFAULT '0',
  PRIMARY KEY (`eventTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventtypes`
--

LOCK TABLES `eventtypes` WRITE;
/*!40000 ALTER TABLE `eventtypes` DISABLE KEYS */;
INSERT INTO `eventtypes` VALUES (1,'Birthday','Set recurring to 1'),(2,'Task','Set recurring 0'),(3,'PublicEvent','Recurring to 1 for these'),(4,'PersonalEvent','Probably doesn\'t recur'),(5,'Reminder','No recurring probably');
/*!40000 ALTER TABLE `eventtypes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-22 23:55:39
