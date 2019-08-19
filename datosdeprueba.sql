-- MySQL dump 10.13  Distrib 8.0.15, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: empacadoralitoral
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (3,'descabezado'),(7,'Javier'),(6,'Jorge'),(4,'prueba2'),(1,'pruebaEditar'),(5,'pruebaMaziza'),(2,'Supervisor de hielo');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,105),(2,1,106),(3,1,107),(4,1,108),(5,1,154),(235,2,25),(236,2,26),(234,2,28),(232,2,29),(233,2,30),(231,2,32),(225,2,33),(226,2,34),(224,2,36),(259,2,45),(247,2,46),(245,2,48),(243,2,53),(244,2,54),(241,2,56),(49,2,65),(50,2,66),(48,2,68),(238,2,77),(239,2,78),(240,2,79),(237,2,80),(35,2,89),(38,2,90),(34,2,92),(30,2,105),(31,2,106),(33,2,107),(28,2,108),(44,2,121),(46,2,122),(43,2,124),(41,2,145),(40,2,146),(39,2,148),(32,2,154),(261,2,155),(262,2,156),(266,2,158),(265,2,159),(263,2,160),(29,2,161),(36,2,162),(37,2,163),(42,2,166),(47,2,167),(45,2,168),(223,2,169),(227,2,170),(242,2,171),(264,2,172),(73,3,1),(74,3,2),(75,3,3),(76,3,4),(77,3,5),(78,3,6),(79,3,7),(80,3,8),(81,3,9),(82,3,10),(83,3,11),(84,3,12),(85,3,13),(86,3,14),(87,3,15),(88,3,16),(89,3,17),(90,3,18),(91,3,19),(92,3,20),(93,3,21),(94,3,22),(95,3,23),(96,3,24),(97,3,25),(98,3,26),(99,3,27),(100,3,28),(101,3,29),(102,3,30),(103,3,31),(104,3,32),(105,3,33),(106,3,34),(107,3,35),(108,3,36),(109,3,37),(110,3,38),(111,3,39),(112,3,40),(113,3,41),(114,3,42),(115,3,43),(116,3,44),(117,3,45),(118,3,46),(119,3,47),(120,3,48),(121,3,49),(122,3,50),(123,3,51),(124,3,52),(125,3,53),(126,3,54),(127,3,55),(128,3,56),(129,3,57),(130,3,58),(131,3,59),(132,3,60),(133,3,61),(134,3,62),(135,3,63),(136,3,64),(137,3,65),(138,3,66),(139,3,67),(140,3,68),(141,3,69),(142,3,70),(143,3,71),(144,3,72),(145,3,73),(146,3,74),(147,3,75),(148,3,76),(149,3,77),(150,3,78),(151,3,79),(152,3,80),(153,3,81),(154,3,82),(155,3,83),(156,3,84),(157,3,85),(158,3,86),(159,3,87),(160,3,88),(161,3,89),(162,3,90),(163,3,91),(164,3,92),(165,3,93),(166,3,94),(167,3,95),(168,3,96),(169,3,97),(170,3,98),(171,3,99),(172,3,100),(173,3,101),(174,3,102),(175,3,103),(176,3,104),(177,3,105),(178,3,106),(179,3,107),(180,3,108),(181,3,109),(182,3,110),(183,3,111),(184,3,112),(185,3,113),(186,3,114),(187,3,115),(188,3,116),(62,3,117),(63,3,118),(64,3,119),(65,3,120),(66,3,121),(67,3,122),(68,3,123),(69,3,124),(70,3,125),(71,3,126),(72,3,127),(51,3,128),(52,3,129),(53,3,130),(54,3,131),(55,3,132),(56,3,133),(57,3,134),(58,3,135),(59,3,136),(189,3,137),(190,3,138),(191,3,139),(192,3,140),(193,3,141),(194,3,142),(195,3,143),(196,3,144),(197,3,145),(198,3,146),(199,3,147),(200,3,148),(201,3,149),(202,3,150),(203,3,151),(204,3,152),(205,3,153),(206,3,154),(207,3,155),(208,3,156),(209,3,157),(210,3,158),(211,3,159),(212,3,160),(213,3,161),(214,3,162),(215,3,163),(216,3,164),(217,3,165),(218,3,166),(60,3,167),(61,3,168),(248,4,1),(249,4,2),(250,4,3),(251,4,4),(252,5,1),(253,5,2),(255,6,77),(256,6,78),(257,6,79),(254,6,80),(258,7,1);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$m7qrGWlVWgGT$wYWlOuCk10tiBmghMpNUBtmjxUUUPeYyOI19ISB9X2k=','2019-08-07 08:21:29.098459',1,'admin','Jorge','Escoto','jorgeescoto18@gmail.com',1,1,'2019-04-05 20:11:34.000000'),(2,'pbkdf2_sha256$150000$dlTpkhG7ouWg$SD8uxLZseIEF/NwcyrxLXNFEV5YQRcSQFjRuGNWDI5g=','2019-07-13 19:36:35.881336',0,'obek','','','',0,1,'2019-05-21 19:57:54.000000'),(3,'pbkdf2_sha256$150000$qDRZc2wkZzDB$zBs3zzv9uvIO4XhHs3n/ZFaPSgEF3ODYamyZpMuks4w=',NULL,0,'nicol','','','',0,1,'2019-07-12 07:45:15.000000'),(4,'pbkdf2_sha256$150000$1RjSjhqBjWma$/4Bj2io38a9tvkr3LR2LI4Yv3LVxEMbaHBr9FhkQLis=','2019-07-15 20:22:21.635317',0,'kenssy','Kenssy12','Medina','kenssymedina2016@gmail.com',1,1,'2019-07-14 17:32:30.000000'),(5,'pbkdf2_sha256$150000$TF4wK5g50mkj$GHUVPYp9/xvF3XuFy9eTlxiLD1Zkeq9iyXmAfBfgLeU=',NULL,0,'kenssy2','Kenssy','Medina','kenssymedina@gmail.com',0,1,'2019-07-14 17:47:33.791306'),(6,'pbkdf2_sha256$150000$bcy3DhpXNkew$R55GyMPSQktFJSdT8c5qufPokulgKu7VGiKVhX5P6Gw=',NULL,0,'kevin','Kevin','Escoto','escotokevin1@gmail.com',0,1,'2019-07-14 20:14:17.003820'),(7,'pbkdf2_sha256$150000$ExXECvhlP8m6$f8BoDZIw4vYrYyr8H04qoOSIgXVeux2PVI2oUPm64to=',NULL,0,'kevin2','Kevin','Escoto','',0,1,'2019-07-14 20:17:52.000000'),(8,'pbkdf2_sha256$150000$lIknW4aflqBs$T5LoPVIJZMCSrjGCUgq6t7X32mtT6McQLaQeRrEaNYM=',NULL,0,'kevin3','Kevin','Escoto','',0,1,'2019-07-14 20:20:05.000000'),(9,'pbkdf2_sha256$150000$eKdX0NpLvyZ5$gHCgH09/Zb6pipQ8XKWQAlDNzlABkwNYLFzMBHSfNp4=',NULL,0,'kevin4','Kevin','Escoto','',0,0,'2019-07-14 21:42:42.000000'),(13,'pbkdf2_sha256$150000$Ehy8nbgrx1G9$6yM6OdORBIKtAB9pQ3y2lNlfRjzO7FzLrVA4WgElJnQ=',NULL,0,'kevin5','Kevin','Escoto','ikaromaster18@gmail.com',0,1,'2019-07-14 22:07:34.000000'),(14,'pbkdf2_sha256$150000$ZHRfdJEb6Oy3$E9dr5rmzujbx52lEYghAJvuwvLeuu1t1Or4lYbRATlo=',NULL,0,'NicolGiron','Nicol','Giron','gironkeyla7@gmail.com',0,1,'2019-07-14 22:56:23.196848'),(15,'pbkdf2_sha256$150000$L0m0GPC9IdJq$hHOwngibV5dDp3UxV3qLgInDzXpME2wPo/EKuJUSfak=',NULL,0,'NicolGiron1','Nicol','Giron','',0,1,'2019-07-14 23:06:43.000000'),(16,'pbkdf2_sha256$150000$LmgCUcn9kRcy$oLl3G/mqSyuivdrhICAgA+vf6BWLMHjDmcav/RrWLOo=',NULL,0,'MArtyu','Obek','Escoto','ikaromaster18@gmail.com',0,1,'2019-07-14 23:15:32.000000'),(17,'pbkdf2_sha256$150000$cCbatqB4uW2e$mbVTRxBmPh4dHKCFsQztity6XFAoGHBaZOJYoT3HlLY=',NULL,0,'MArtyuu','Obek','Escoto Ponce','jorgeescoto18@gmail.com',0,0,'2019-07-14 23:18:57.161398'),(18,'pbkdf2_sha256$150000$s1vCMhK7Foyi$E4QIHMoTuvu0UUZIvQodFJF2pivUlP83PS6nkyrd9GQ=','2019-08-09 18:15:32.198622',0,'kenner','Kenner','Mendez','',0,1,'2019-07-16 00:34:43.000000'),(19,'pbkdf2_sha256$150000$1LdFy39DbisD$QLtdeEIszQEm6eATKyvDgeNCK4TJpSIxe+wBusJ2EII=','2019-07-29 15:00:27.624109',0,'Edgar_Jair','Edgar','Ordoñez','jordonez@empacadoralitoral.com',0,1,'2019-07-29 14:52:36.326163'),(20,'pbkdf2_sha256$150000$ns9Saod8Uo30$jKuh3jLdx7XvgrCgXfB5PIB955L4lElevK06kStfRtU=','2019-07-29 19:22:51.533114',0,'Maryori','Maryori','Burke','mburke@empacadoralitoral.com',0,1,'2019-07-29 19:21:21.778164');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,1),(2,3,2),(3,8,2),(4,9,2),(8,13,2),(9,14,2),(10,15,2),(11,16,2),(12,17,2),(13,18,2),(14,19,3),(15,20,2);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (3,18,1);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `camaron_cosecha`
--

LOCK TABLES `camaron_cosecha` WRITE;
/*!40000 ALTER TABLE `camaron_cosecha` DISABLE KEYS */;
INSERT INTO `camaron_cosecha` VALUES ('008856','2019-07-07','01:02:52.000000','06:00:00.000000',1,'f1',1,'000006'),('51101','2019-07-18','00:00:00.000000','00:01:00.000000',909090,'f1',18,'000001'),('fff','2019-07-11','22:00:00.000000','00:00:00.000000',1,'f1',1,'000002');
/*!40000 ALTER TABLE `camaron_cosecha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `camaron_detallecosecha`
--

LOCK TABLES `camaron_detallecosecha` WRITE;
/*!40000 ALTER TABLE `camaron_detallecosecha` DISABLE KEYS */;
INSERT INTO `camaron_detallecosecha` VALUES (21,15,800.00,'','fff',5),(24,10,100.00,'si se pudo lograr lo que se esperaba realizar.','008856',6),(25,6,140.00,'si se pudo','008856',7),(26,10,100.00,'','51101',1),(27,20,200.00,'','51101',2);
/*!40000 ALTER TABLE `camaron_detallecosecha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `compania_compania`
--

LOCK TABLES `compania_compania` WRITE;
/*!40000 ALTER TABLE `compania_compania` DISABLE KEYS */;
INSERT INTO `compania_compania` VALUES (1,'Cultivos Marinos Del Sur','Choluteca','CULMASA',1,1),(2,'CARGIL S.A','choluteca, choluteca,honduras',NULL,2,1),(3,'Cultivos Marinos','choluteca,honduras, san marcos de colon,choluteca,honduras','CUMAR',1,1),(4,'Obek Escoto','choluteca,honduras, san marcos de colon,choluteca,honduras',NULL,2,1);
/*!40000 ALTER TABLE `compania_compania` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `compania_finca`
--

LOCK TABLES `compania_finca` WRITE;
/*!40000 ALTER TABLE `compania_finca` DISABLE KEYS */;
INSERT INTO `compania_finca` VALUES ('05','nuevo2','nv','aya por cedeño',1),('06f4','LITORAL','LIT','choluteca, choluteca,honduras',3),('1q2','cacaroto','acc','choluteca, choluteca,honduras',1),('1q2c','cacaroto','cc','choluteca, choluteca,honduras',1),('45fl','EL ORO MARINO','CMA','tegucigalpa,honduras',1),('45fl1','EL ORO MARINO','CMA','tegucigalpa,honduras',1);
/*!40000 ALTER TABLE `compania_finca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `compania_laguna`
--

LOCK TABLES `compania_laguna` WRITE;
/*!40000 ALTER TABLE `compania_laguna` DISABLE KEYS */;
INSERT INTO `compania_laguna` VALUES ('f1',100,'aya por cedeno','unica finca de prueba','05'),('F6',100,'aya por cedeñito jaajajaj','una laguna bien grande','05'),('F7',3,'aya por cedeñito jaajajaj','una laguna bien grande','06f4'),('F8',10,'aya por cedeñito jaajajaj','una laguna bien grande','1q2');
/*!40000 ALTER TABLE `compania_laguna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `compania_tipocompania`
--

LOCK TABLES `compania_tipocompania` WRITE;
/*!40000 ALTER TABLE `compania_tipocompania` DISABLE KEYS */;
INSERT INTO `compania_tipocompania` VALUES (1,'CAMARONERA'),(2,'Flete');
/*!40000 ALTER TABLE `compania_tipocompania` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `conductor_conductor`
--

LOCK TABLES `conductor_conductor` WRITE;
/*!40000 ALTER TABLE `conductor_conductor` DISABLE KEYS */;
INSERT INTO `conductor_conductor` VALUES ('0000-0000-00001','Juan','Roberto','Molina','Mendoza','2019-08-16',99999999,1),('0801-1997-17105','Jorge','Obek','Escoto','Ponce','2019-07-20',98118623,1),('1111-1111-11111','Jorge',NULL,'Escoto',NULL,NULL,94763554,1);
/*!40000 ALTER TABLE `conductor_conductor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `empleado_cargo`
--

LOCK TABLES `empleado_cargo` WRITE;
/*!40000 ALTER TABLE `empleado_cargo` DISABLE KEYS */;
INSERT INTO `empleado_cargo` VALUES (1,'Supervisor de hielo',2),(2,'Descabezado',3),(3,'Descabezado',3),(4,'pruebaMaziza',5),(5,'Jorge',6),(6,'Javier',7);
/*!40000 ALTER TABLE `empleado_cargo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `empleado_empleado`
--

LOCK TABLES `empleado_empleado` WRITE;
/*!40000 ALTER TABLE `empleado_empleado` DISABLE KEYS */;
INSERT INTO `empleado_empleado` VALUES (1,'0801-1997-17105','Jorge','94763554',1,1,1,'escoto',NULL,NULL),(2,'0801-1997-17100','Obek','94763554',1,2,1,'escoto',NULL,NULL),(118,'0611198900693','Maryori','',1,20,1,'Burke','Ortiz','yanini'),(1000,'0615199700410','Kenssy12','99999999',0,4,1,'Medina','Izaguirre','Abigail'),(1231,NULL,'Kevin','',0,7,1,'Escoto',NULL,NULL),(1232,NULL,'Kevin','',0,8,1,'Escoto',NULL,NULL),(1233,NULL,'Kevin','',0,9,1,'Escoto',NULL,NULL),(1234,'080120019850','Nicol','94763554',0,3,1,'escoto',NULL,NULL),(1235,NULL,'Kevin','',0,13,1,'Escoto',NULL,NULL),(1360,'0601198500064','Edgar','',1,19,2,'Ordoñez','Motiño','Jair'),(12311,NULL,'Kevin','',0,6,1,'Escoto',NULL,NULL),(23456,NULL,'Nicol','',0,14,1,'Giron',NULL,NULL),(23457,NULL,'Nicol','',0,15,1,'Giron',NULL,NULL),(51101,'0801199717105','Kenssy','94763554',0,5,1,'Medina','Izaguirre','Abigail'),(678956,NULL,'Obek','',0,16,1,'Escoto','Escoto','Jorge'),(678957,NULL,'Obek','94763554',0,17,1,'Escoto Ponce','Escoto Ponce','Jorge'),(909090,'9090990','Kenner2','999090909',1,18,1,'Mendez2','Ponce2','Aaron2');
/*!40000 ALTER TABLE `empleado_empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `equipo_baseequipo`
--

LOCK TABLES `equipo_baseequipo` WRITE;
/*!40000 ALTER TABLE `equipo_baseequipo` DISABLE KEYS */;
INSERT INTO `equipo_baseequipo` VALUES (1,'Bin'),(2,'Pallet'),(3,'Canasta');
/*!40000 ALTER TABLE `equipo_baseequipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `equipo_color`
--

LOCK TABLES `equipo_color` WRITE;
/*!40000 ALTER TABLE `equipo_color` DISABLE KEYS */;
INSERT INTO `equipo_color` VALUES (1,'Blanco'),(2,'Negro'),(3,'Azul');
/*!40000 ALTER TABLE `equipo_color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `equipo_equipo`
--

LOCK TABLES `equipo_equipo` WRITE;
/*!40000 ALTER TABLE `equipo_equipo` DISABLE KEYS */;
INSERT INTO `equipo_equipo` VALUES (1,11,'EQEL-1-11-2-3-1','ahora si',2,3,1,2),(2,1,'EQEL-2-1-3-1-1','',2,1,2,3),(3,2,'EQEL-1-2-2-3-1','el men que lo agg lo arreglo',1,3,1,2),(4,3,'EQEL-1-3-2-3-1','esta bueno',1,3,1,2),(5,4,'EQEL-1-4-2-3-1','esta medio bueno',1,3,1,2),(6,5,'EQEL-1-5-1-3-1','hhh',2,3,1,1),(7,7,'EQEL-1-7-2-3-1','gghh',2,3,1,2),(8,12,'EQEL-1-12-3-3-1','bin en buen estado',2,3,1,3),(9,15,'EQEL-1-15-3-3-1','jjj',1,3,1,3),(10,101,'EQEL-1-101-1-3-1','',2,3,1,1),(11,100,'EQEL-1-100-1-3-1','',2,3,1,1),(12,100,'EQEL-1-100-1-1-1','',1,1,1,1);
/*!40000 ALTER TABLE `equipo_equipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `equipo_estado`
--

LOCK TABLES `equipo_estado` WRITE;
/*!40000 ALTER TABLE `equipo_estado` DISABLE KEYS */;
INSERT INTO `equipo_estado` VALUES (1,'Asignado'),(2,'Disponible'),(3,'Fuera de Servicio');
/*!40000 ALTER TABLE `equipo_estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `equipo_tamano`
--

LOCK TABLES `equipo_tamano` WRITE;
/*!40000 ALTER TABLE `equipo_tamano` DISABLE KEYS */;
INSERT INTO `equipo_tamano` VALUES (1,'Grande'),(2,'Pequeño'),(3,'Normal');
/*!40000 ALTER TABLE `equipo_tamano` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `hielo_proceso_departamentoproceso`
--

LOCK TABLES `hielo_proceso_departamentoproceso` WRITE;
/*!40000 ALTER TABLE `hielo_proceso_departamentoproceso` DISABLE KEYS */;
INSERT INTO `hielo_proceso_departamentoproceso` VALUES (2,'Maquina 1'),(3,'Maquina 2'),(4,'Maquina 3'),(5,'Maquina 4'),(6,'Empaque fresco'),(7,'Descabezado'),(8,'Reenhielado'),(9,'Clasificado'),(10,'Reproceso'),(11,'Langosta'),(12,'Pelado'),(13,'Descongelado');
/*!40000 ALTER TABLE `hielo_proceso_departamentoproceso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `hielo_proceso_detallehieloproceso`
--

LOCK TABLES `hielo_proceso_detallehieloproceso` WRITE;
/*!40000 ALTER TABLE `hielo_proceso_detallehieloproceso` DISABLE KEYS */;
INSERT INTO `hielo_proceso_detallehieloproceso` VALUES (16,10,2,1,0,0,0,0,0,0),(17,10,3,0,2,0,0,0,0,0),(18,11,3,3,1,0,0,0,0,0),(19,12,2,1,1,0,0,0,0,0),(20,11,2,1,3,0,0,0,0,0),(58,26,10,1,1,1,1,1,1,1),(59,27,2,0,0,0,0,0,0,0),(60,27,3,0,1,4,6,5,2,3),(61,27,4,1,2,3,1,0,1,0),(62,31,2,10,10,10,0,8,10,10);
/*!40000 ALTER TABLE `hielo_proceso_detallehieloproceso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `hielo_proceso_hieloproceso`
--

LOCK TABLES `hielo_proceso_hieloproceso` WRITE;
/*!40000 ALTER TABLE `hielo_proceso_hieloproceso` DISABLE KEYS */;
INSERT INTO `hielo_proceso_hieloproceso` VALUES (10,'2019-06-29',1),(11,'2019-06-30',1),(12,'2019-06-28',1),(26,'2019-07-05',1),(27,'2019-07-04',1),(28,'2019-07-20',909090),(29,'2019-07-21',909090),(30,'2019-07-22',909090),(31,'2019-08-01',1);
/*!40000 ALTER TABLE `hielo_proceso_hieloproceso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `prestamos_detalleprestamoequipo`
--

LOCK TABLES `prestamos_detalleprestamoequipo` WRITE;
/*!40000 ALTER TABLE `prestamos_detalleprestamoequipo` DISABLE KEYS */;
INSERT INTO `prestamos_detalleprestamoequipo` VALUES (21,NULL,14,3,'000011'),(25,'el thortas',16,6,'111111'),(26,'el to',12,7,'111111'),(33,NULL,15,9,'000015'),(34,'la tapita',10,8,'000013'),(37,'se presto un bin',111,5,'000012'),(38,'se prestaron 1 bin',10,1,'000001'),(39,NULL,11,2,'000001'),(41,'la tapita',10,4,'000016'),(42,'glglglgg',12,5,'000016'),(43,NULL,1,9,'018501');
/*!40000 ALTER TABLE `prestamos_detalleprestamoequipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `prestamos_estadoprestamo`
--

LOCK TABLES `prestamos_estadoprestamo` WRITE;
/*!40000 ALTER TABLE `prestamos_estadoprestamo` DISABLE KEYS */;
INSERT INTO `prestamos_estadoprestamo` VALUES (1,'Activo'),(2,'Anulado'),(3,'Asignado'),(4,'Terminado');
/*!40000 ALTER TABLE `prestamos_estadoprestamo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `prestamos_prestamoequipo`
--

LOCK TABLES `prestamos_prestamoequipo` WRITE;
/*!40000 ALTER TABLE `prestamos_prestamoequipo` DISABLE KEYS */;
INSERT INTO `prestamos_prestamoequipo` VALUES ('000001','14:14:16.000000','2019-04-08',NULL,'el camion salio con las intenciones de llegar :v',1,'0000-0000-00001',1,4,'HCH0001'),('000002','01:01:00.000000','2019-06-06',NULL,'',3,'0000-0000-00001',1,2,'HCH0001'),('000011','20:11:30.000000','2019-03-24',NULL,'ese men lo hizo de nuevo',1,'0000-0000-00001',1,3,'HCH0001'),('000012','14:14:16.000000','2019-03-29',NULL,'ese men solo esta probando',1,'0000-0000-00001',1,4,'HCH0001'),('000013','20:11:30.000000','2019-03-29',NULL,'gggg',1,'0000-0000-00001',1,2,'HCH0001'),('000015','23:00:00.000000','2019-06-19','2019-07-17','sin comentarios',3,'0000-0000-00001',1,4,'HCH0001'),('000016','00:00:00.000000','2019-07-19','2019-07-24','ddddddd',3,'0801-1997-17105',909090,1,'HCH0003'),('018501','22:02:00.000000','2019-07-29','2019-07-30','',1,'0801-1997-17105',1,3,'HCH0001'),('111111','04:00:00.000000','2019-05-17',NULL,'esta mara',3,'0000-0000-00001',2,4,'HCH0001');
/*!40000 ALTER TABLE `prestamos_prestamoequipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `remision_detalleremision`
--

LOCK TABLES `remision_detalleremision` WRITE;
/*!40000 ALTER TABLE `remision_detalleremision` DISABLE KEYS */;
INSERT INTO `remision_detalleremision` VALUES (9,15,0,1,'000003',1),(101,10,0,1,'000008',1),(109,12,0,1,'000007',1),(110,13,0,2,'000007',1),(111,100,0,1,'000006',1),(115,150,0,1,'000002',1),(131,10,8,2,'000001',1),(132,11,10,1,'000001',1),(134,150,50,1,'018197',1),(135,10,0,1,'000010',1),(136,100,0,1,'000111',1);
/*!40000 ALTER TABLE `remision_detalleremision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `remision_estadoremision`
--

LOCK TABLES `remision_estadoremision` WRITE;
/*!40000 ALTER TABLE `remision_estadoremision` DISABLE KEYS */;
INSERT INTO `remision_estadoremision` VALUES (1,'Activo'),(2,'Terminado'),(3,'Anulado');
/*!40000 ALTER TABLE `remision_estadoremision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `remision_hielo`
--

LOCK TABLES `remision_hielo` WRITE;
/*!40000 ALTER TABLE `remision_hielo` DISABLE KEYS */;
INSERT INTO `remision_hielo` VALUES (1,'Limpio',60.00),(2,'Sucio',10.00);
/*!40000 ALTER TABLE `remision_hielo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `remision_medida`
--

LOCK TABLES `remision_medida` WRITE;
/*!40000 ALTER TABLE `remision_medida` DISABLE KEYS */;
INSERT INTO `remision_medida` VALUES (1,'Masa','Quintal','Q');
/*!40000 ALTER TABLE `remision_medida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `remision_remision`
--

LOCK TABLES `remision_remision` WRITE;
/*!40000 ALTER TABLE `remision_remision` DISABLE KEYS */;
INSERT INTO `remision_remision` VALUES ('000001',1,'2019-04-08',2,1,'0000-0000-00001',1,'HCH0001','000001',1,''),('000002',101010,'2019-04-01',2,1,'0000-0000-00001',1,'HCH0001','000012',1,''),('000003',101011,'2019-04-01',3,1,'0000-0000-00001',1,'HCH0001',NULL,1,NULL),('000006',100000,'2019-05-10',2,3,'0000-0000-00001',2,'HCH0001','111111',1,''),('000007',NULL,'2019-05-25',3,3,'0000-0000-00001',1,'HCH0001',NULL,1,NULL),('000008',NULL,'2019-05-04',3,1,'0000-0000-00001',1,'HCH0001',NULL,1,NULL),('000010',NULL,'2019-05-23',2,3,'0000-0000-00001',1,'HCH0001',NULL,1,''),('000111',NULL,'2019-08-13',1,1,'0000-0000-00001',1,'HCH0001',NULL,1,''),('018197',NULL,'2019-07-29',1,1,'0801-1997-17105',1,'HCH0001','018501',1,'');
/*!40000 ALTER TABLE `remision_remision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `remision_tiporemision`
--

LOCK TABLES `remision_tiporemision` WRITE;
/*!40000 ALTER TABLE `remision_tiporemision` DISABLE KEYS */;
INSERT INTO `remision_tiporemision` VALUES (1,'Maquila');
/*!40000 ALTER TABLE `remision_tiporemision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `vehiculo_vehiculo`
--

LOCK TABLES `vehiculo_vehiculo` WRITE;
/*!40000 ALTER TABLE `vehiculo_vehiculo` DISABLE KEYS */;
INSERT INTO `vehiculo_vehiculo` VALUES ('HCH0001','TOYOTA','CARGO',1994,1,2),('HCH0003','Toyota','Cargo',1976,2,2);
/*!40000 ALTER TABLE `vehiculo_vehiculo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-19 14:47:09
