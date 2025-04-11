-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: northwind
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `CustomerID` int NOT NULL AUTO_INCREMENT,
  `CustomerName` varchar(50) DEFAULT NULL,
  `ContactName` varchar(50) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `City` varchar(20) DEFAULT NULL,
  `PostalCode` varchar(10) DEFAULT NULL,
  `Country` varchar(15) DEFAULT NULL,
  `DateOfBirth` year DEFAULT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (2,'Ana Trujillo Emparedados y helados','Ana Trujillo','Avda. de la Constitución 2222','México D.F.','0','Mexico',NULL),(3,'Antonio Moreno Taquería','Antonio Moreno','Mataderos 2312','México D.F.','0','Mexico',NULL),(4,'Around the Horn','Thomas Hardy','120 Hanover Sq.','London','WA1 1DP','UK',NULL),(5,'Berglunds snabbköp','Christina Berglund','Berguvsvägen 8','Luleå','S-958 22','Sweden',NULL),(6,'Blauer See Delikatessen','Hanna Moos','Forsterstr. 57','Mannheim','68306','Germany',NULL),(7,'Blondel père et fils','Frédérique Citeaux','24, place Kléber','Strasbourg','67000','France',NULL),(8,'Bólido Comidas preparadas','Martín Sommer','C/ Araquil, 67','Madrid','28023','Spain',NULL),(9,'Bon app\'\'','Laurence Lebihans','12, rue des Bouchers','Marseille','13008','France',NULL),(10,'Bottom-Dollar Marketse','Elizabeth Lincoln','23 Tsawassen Blvd.','Tsawassen','T2F 8M4','Canada',NULL),(11,'B\'\'s Beverages','Victoria Ashworth','Fauntleroy Circus','London','EC2 5NT','UK',NULL),(12,'Cactus Comidas para llevar','Patricio Simpson','Cerrito 333','Buenos Aires','1010','Argentina',NULL),(13,'Centro comercial Moctezuma','Francisco Chang','Sierras de Granada 9993','México D.F.','0','Mexico',NULL),(14,'Chop-suey Chinese','Yang Wang','Hauptstr. 29','Bern','3012','Switzerland',NULL),(15,'Comércio Mineiro','Pedro Afonso','Av. dos Lusíadas, 23','São Paulo','05432-043','Brazil',NULL),(16,'Consolidated Holdings','Elizabeth Brown','Berkeley Gardens 12 Brewery','London','WX1 6LT','UK',NULL),(17,'Drachenblut Delikatessend','Sven Ottlieb','Walserweg 21','Aachen','52066','Germany',NULL),(18,'Du monde entier','Janine Labrune','67, rue des Cinquante Otages','Nantes','44000','France',NULL),(19,'Eastern Connection','Ann Devon','35 King George','London','WX3 6FW','UK',NULL),(20,'Ernst Handel','Roland Mendel','Kirchgasse 6','Graz','8010','Austria',NULL),(21,'Familia Arquibaldo','Aria Cruz','Rua Orós, 92','São Paulo','05442-030','Brazil',NULL),(22,'FISSA Fabrica Inter. Salchichas S.A.','Diego Roel','C/ Moralzarzal, 86','Madrid','28034','Spain',NULL),(23,'Folies gourmandes','Martine Rancé','184, chaussée de Tournai','Lille','59000','France',NULL),(24,'Folk och fä HB','Maria Larsson','Åkergatan 24','Bräcke','S-844 67','Sweden',NULL),(25,'Frankenversand','Peter Franken','Berliner Platz 43','München','80805','Germany',NULL),(26,'France restauration','Carine Schmitt','54, rue Royale','Nantes','44000','France',NULL),(27,'Franchi S.p.A.','Paolo Accorti','Via Monte Bianco 34','Torino','10100','Italy',NULL),(28,'Furia Bacalhau e Frutos do Mar','Lino Rodriguez','Jardim das rosas n. 32','Lisboa','1675','Portugal',NULL),(29,'Galería del gastrónomo','Eduardo Saavedra','Rambla de Cataluña, 23','Barcelona','8022','Spain',NULL),(30,'Godos Cocina Típica','José Pedro Freyre','C/ Romero, 33','Sevilla','41101','Spain',NULL),(31,'Gourmet Lanchonetes','André Fonseca','Av. Brasil, 442','Campinas','04876-786','Brazil',NULL),(32,'Great Lakes Food Market','Howard Snyder','2732 Baker Blvd.','Eugene','97403','USA',NULL),(33,'GROSELLA-Restaurante','Manuel Pereira','5ª Ave. Los Palos Grandes','Caracas','1081','Venezuela',NULL),(34,'Hanari Carnes','Mario Pontes','Rua do Paço, 67','Rio de Janeiro','05454-876','Brazil',NULL),(35,'HILARIÓN-Abastos','Carlos Hernández','Carrera 22 con Ave. Carlos Soublette #8-35','San Cristóbal','5022','Venezuela',NULL),(36,'Hungry Coyote Import Store','Yoshi Latimer','City Center Plaza 516 Main St.','Elgin','97827','USA',NULL),(37,'Hungry Owl All-Night Grocers','Patricia McKenna','8 Johnstown Road','Cork','','Ireland',NULL),(38,'Island Trading','Helen Bennett','Garden House Crowther Way','Cowes','PO31 7PJ','UK',NULL),(39,'Königlich Essen','Philip Cramer','Maubelstr. 90','Brandenburg','14776','Germany',NULL),(40,'La corne d\'\'abondance','Daniel Tonini','67, avenue de l\'\'Europe','Versailles','78000','France',NULL),(41,'La maison d\'\'Asie','Annette Roulet','1 rue Alsace-Lorraine','Toulouse','31000','France',NULL),(42,'Laughing Bacchus Wine Cellars','Yoshi Tannamuri','1900 Oak St.','Vancouver','V3F 2K1','Canada',NULL),(43,'Lazy K Kountry Store','John Steel','12 Orchestra Terrace','Walla Walla','99362','USA',NULL),(44,'Lehmanns Marktstand','Renate Messner','Magazinweg 7','Frankfurt a.M.','60528','Germany',NULL),(45,'Let\'\'s Stop N Shop','Jaime Yorres','87 Polk St. Suite 5','San Francisco','94117','USA',NULL),(46,'LILA-Supermercado','Carlos González','Carrera 52 con Ave. Bolívar #65-98 Llano Largo','Barquisimeto','3508','Venezuela',NULL),(47,'LINO-Delicateses','Felipe Izquierdo','Ave. 5 de Mayo Porlamar','I. de Margarita','4980','Venezuela',NULL),(48,'Lonesome Pine Restaurant','Fran Wilson','89 Chiaroscuro Rd.','Portland','97219','USA',NULL),(49,'Magazzini Alimentari Riuniti','Giovanni Rovelli','Via Ludovico il Moro 22','Bergamo','24100','Italy',NULL),(50,'Maison Dewey','Catherine Dewey','Rue Joseph-Bens 532','Bruxelles','B-1180','Belgium',NULL),(51,'Mère Paillarde','Jean Fresnière','43 rue St. Laurent','Montréal','H1J 1C3','Canada',NULL),(52,'Morgenstern Gesundkost','Alexander Feuer','Heerstr. 22','Leipzig','4179','Germany',NULL),(53,'North/South','Simon Crowther','South House 300 Queensbridge','London','SW7 1RZ','UK',NULL),(54,'Océano Atlántico Ltda.','Yvonne Moncada','Ing. Gustavo Moncada 8585 Piso 20-A','Buenos Aires','1010','Argentina',NULL),(55,'Old World Delicatessen','Rene Phillips','2743 Bering St.','Anchorage','99508','USA',NULL),(56,'Ottilies Käseladen','Henriette Pfalzheim','Mehrheimerstr. 369','Köln','50739','Germany',NULL),(57,'Paris spécialités','Marie Bertrand','265, boulevard Charonne','Paris','75012','France',NULL),(58,'Pericles Comidas clásicas','Guillermo Fernández','Calle Dr. Jorge Cash 321','México D.F.','0','Mexico',NULL),(59,'Piccolo und mehr','Georg Pipps','Geislweg 14','Salzburg','5020','Austria',NULL),(60,'Princesa Isabel Vinhoss','Isabel de Castro','Estrada da saúde n. 58','Lisboa','1756','Portugal',NULL),(61,'Que Delícia','Bernardo Batista','Rua da Panificadora, 12','Rio de Janeiro','02389-673','Brazil',NULL),(62,'Queen Cozinha','Lúcia Carvalho','Alameda dos Canàrios, 891','São Paulo','05487-020','Brazil',NULL),(63,'QUICK-Stop','Horst Kloss','Taucherstraße 10','Cunewalde','1307','Germany',NULL),(64,'Rancho grande','Sergio Gutiérrez','Av. del Libertador 900','Buenos Aires','1010','Argentina',NULL),(65,'Rattlesnake Canyon Grocery','Paula Wilson','2817 Milton Dr.','Albuquerque','87110','USA',NULL),(66,'Reggiani Caseifici','Maurizio Moroni','Strada Provinciale 124','Reggio Emilia','42100','Italy',NULL),(67,'Ricardo Adocicados','Janete Limeira','Av. Copacabana, 267','Rio de Janeiro','02389-890','Brazil',NULL),(68,'Richter Supermarkt','Michael Holz','Grenzacherweg 237','Genève','1203','Switzerland',NULL),(69,'Romero y tomillo','Alejandra Camino','Gran Vía, 1','Madrid','28001','Spain',NULL),(70,'Santé Gourmet','Jonas Bergulfsen','Erling Skakkes gate 78','Stavern','4110','Norway',NULL),(71,'Save-a-lot Markets','Jose Pavarotti','187 Suffolk Ln.','Boise','83720','USA',NULL),(72,'Seven Seas Imports','Hari Kumar','90 Wadhurst Rd.','London','OX15 4NB','UK',NULL),(73,'Simons bistro','Jytte Petersen','Vinbæltet 34','København','1734','Denmark',NULL),(74,'Spécialités du monde','Dominique Perrier','25, rue Lauriston','Paris','75016','France',NULL),(75,'Split Rail Beer & Ale','Art Braunschweiger','P.O. Box 555','Lander','82520','USA',NULL),(76,'Suprêmes délices','Pascale Cartrain','Boulevard Tirou, 255','Charleroi','B-6000','Belgium',NULL),(77,'The Big Cheese','Liz Nixon','89 Jefferson Way Suite 2','Portland','97201','USA',NULL),(78,'The Cracker Box','Liu Wong','55 Grizzly Peak Rd.','Butte','59801','USA',NULL),(79,'Toms Spezialitäten','Karin Josephs','Luisenstr. 48','Münster','44087','Germany',NULL),(80,'Tortuga Restaurante','Miguel Angel Paolino','Avda. Azteca 123','México D.F.','0','Mexico',NULL),(81,'Tradição Hipermercados','Anabela Domingues','Av. Inês de Castro, 414','São Paulo','05634-030','Brazil',NULL),(82,'Trail\'\'s Head Gourmet Provisioners','Helvetius Nagy','722 DaVinci Blvd.','Kirkland','98034','USA',NULL),(83,'Vaffeljernet','Palle Ibsen','Smagsløget 45','Århus','8200','Denmark',NULL),(84,'Victuailles en stock','Mary Saveley','2, rue du Commerce','Lyon','69004','France',NULL),(85,'Vins et alcools Chevalier','Paul Henriot','59 rue de l\'\'Abbaye','Reims','51100','France',NULL),(86,'Die Wandernde Kuh','Rita Müller','Adenauerallee 900','Stuttgart','70563','Germany',NULL),(87,'Wartian Herkku','Pirkko Koskitalo','Torikatu 38','Oulu','90110','Finland',NULL),(88,'Wellington Importadora','Paula Parente','Rua do Mercado, 12','Resende','08737-363','Brazil',NULL),(89,'White Clover Markets','Karl Jablonski','305 - 14th Ave. S. Suite 3B','Seattle','98128','USA',NULL),(90,'Wilman Kala','Matti Karttunen','Keskuskatu 45','Helsinki','21240','Finland',NULL),(91,'Wolski','Zbyszek','ul. Filtrowa 68','Walla','01-012','Poland',NULL),(92,'Cardinal','Tom B. Erichsen','Skagen 21','Stavanger','4006','Norway',NULL),(93,'Cardinal',NULL,NULL,'Stavanger',NULL,'Norway',NULL);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-25  9:46:34
