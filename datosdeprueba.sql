CREATE DATABASE  IF NOT EXISTS `empacadoralitoral` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci */;
USE `empacadoralitoral`;
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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (9,'Gerente de operaciones'),(2,'Supervisor de hielo');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=291 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (235,2,25),(236,2,26),(234,2,28),(232,2,29),(233,2,30),(231,2,32),(225,2,33),(226,2,34),(224,2,36),(259,2,45),(247,2,46),(245,2,48),(243,2,53),(244,2,54),(241,2,56),(49,2,65),(50,2,66),(48,2,68),(267,2,73),(268,2,74),(269,2,75),(270,2,76),(238,2,77),(239,2,78),(240,2,79),(237,2,80),(35,2,89),(38,2,90),(34,2,92),(30,2,105),(31,2,106),(33,2,107),(28,2,108),(44,2,121),(46,2,122),(43,2,124),(41,2,145),(40,2,146),(39,2,148),(32,2,154),(261,2,155),(262,2,156),(266,2,158),(265,2,159),(263,2,160),(29,2,161),(36,2,162),(37,2,163),(42,2,166),(47,2,167),(45,2,168),(223,2,169),(227,2,170),(242,2,171),(264,2,172),(287,9,145),(288,9,146),(289,9,147),(290,9,148),(286,9,166);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=174 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add laguna',7,'add_laguna'),(26,'Can change laguna',7,'change_laguna'),(27,'Can delete laguna',7,'delete_laguna'),(28,'Can view laguna',7,'view_laguna'),(29,'Can add finca',8,'add_finca'),(30,'Can change finca',8,'change_finca'),(31,'Can delete finca',8,'delete_finca'),(32,'Can view finca',8,'view_finca'),(33,'Can add Compañia',9,'add_compania'),(34,'Can change Compañia',9,'change_compania'),(35,'Can delete Compañia',9,'delete_compania'),(36,'Can view Compañia',9,'view_compania'),(37,'Can add Tipo de Compañia',10,'add_tipocompania'),(38,'Can change Tipo de Compañia',10,'change_tipocompania'),(39,'Can delete Tipo de Compañia',10,'delete_tipocompania'),(40,'Can view Tipo de Compañia',10,'view_tipocompania'),(41,'Can add permiso',11,'add_permiso'),(42,'Can change permiso',11,'change_permiso'),(43,'Can delete permiso',11,'delete_permiso'),(44,'Can view permiso',11,'view_permiso'),(45,'Can add empleado',12,'add_empleado'),(46,'Can change empleado',12,'change_empleado'),(47,'Can delete empleado',12,'delete_empleado'),(48,'Can view empleado',12,'view_empleado'),(49,'Can add Tipo de Empleado',13,'add_tipoempleado'),(50,'Can change Tipo de Empleado',13,'change_tipoempleado'),(51,'Can delete Tipo de Empleado',13,'delete_tipoempleado'),(52,'Can view Tipo de Empleado',13,'view_tipoempleado'),(53,'Can add conductor',14,'add_conductor'),(54,'Can change conductor',14,'change_conductor'),(55,'Can delete conductor',14,'delete_conductor'),(56,'Can view conductor',14,'view_conductor'),(57,'Can add color',15,'add_color'),(58,'Can change color',15,'change_color'),(59,'Can delete color',15,'delete_color'),(60,'Can view color',15,'view_color'),(61,'Can add tamano',16,'add_tamano'),(62,'Can change tamano',16,'change_tamano'),(63,'Can delete tamano',16,'delete_tamano'),(64,'Can view tamano',16,'view_tamano'),(65,'Can add equipo',17,'add_equipo'),(66,'Can change equipo',17,'change_equipo'),(67,'Can delete equipo',17,'delete_equipo'),(68,'Can view equipo',17,'view_equipo'),(69,'Can add estado',18,'add_estado'),(70,'Can change estado',18,'change_estado'),(71,'Can delete estado',18,'delete_estado'),(72,'Can view estado',18,'view_estado'),(73,'Can add base equipo',19,'add_baseequipo'),(74,'Can change base equipo',19,'change_baseequipo'),(75,'Can delete base equipo',19,'delete_baseequipo'),(76,'Can view base equipo',19,'view_baseequipo'),(77,'Can add vehiculo',20,'add_vehiculo'),(78,'Can change vehiculo',20,'change_vehiculo'),(79,'Can delete vehiculo',20,'delete_vehiculo'),(80,'Can view vehiculo',20,'view_vehiculo'),(81,'Can add detalle prestamo equipo',21,'add_detalleprestamoequipo'),(82,'Can change detalle prestamo equipo',21,'change_detalleprestamoequipo'),(83,'Can delete detalle prestamo equipo',21,'delete_detalleprestamoequipo'),(84,'Can view detalle prestamo equipo',21,'view_detalleprestamoequipo'),(85,'Can add estado prestamo',22,'add_estadoprestamo'),(86,'Can change estado prestamo',22,'change_estadoprestamo'),(87,'Can delete estado prestamo',22,'delete_estadoprestamo'),(88,'Can view estado prestamo',22,'view_estadoprestamo'),(89,'Can add prestamo equipo',23,'add_prestamoequipo'),(90,'Can change prestamo equipo',23,'change_prestamoequipo'),(91,'Can delete prestamo equipo',23,'delete_prestamoequipo'),(92,'Can view prestamo equipo',23,'view_prestamoequipo'),(93,'Can add hielo',24,'add_hielo'),(94,'Can change hielo',24,'change_hielo'),(95,'Can delete hielo',24,'delete_hielo'),(96,'Can view hielo',24,'view_hielo'),(97,'Can add detalle remision',25,'add_detalleremision'),(98,'Can change detalle remision',25,'change_detalleremision'),(99,'Can delete detalle remision',25,'delete_detalleremision'),(100,'Can view detalle remision',25,'view_detalleremision'),(101,'Can add medida',26,'add_medida'),(102,'Can change medida',26,'change_medida'),(103,'Can delete medida',26,'delete_medida'),(104,'Can view medida',26,'view_medida'),(105,'Can add remision',27,'add_remision'),(106,'Can change remision',27,'change_remision'),(107,'Can delete remision',27,'delete_remision'),(108,'Can view remision',27,'view_remision'),(109,'Can add tipo remision',28,'add_tiporemision'),(110,'Can change tipo remision',28,'change_tiporemision'),(111,'Can delete tipo remision',28,'delete_tiporemision'),(112,'Can view tipo remision',28,'view_tiporemision'),(113,'Can add estado remision',29,'add_estadoremision'),(114,'Can change estado remision',29,'change_estadoremision'),(115,'Can delete estado remision',29,'delete_estadoremision'),(116,'Can view estado remision',29,'view_estadoremision'),(117,'Can add recipiente',30,'add_recipiente'),(118,'Can change recipiente',30,'change_recipiente'),(119,'Can delete recipiente',30,'delete_recipiente'),(120,'Can view recipiente',30,'view_recipiente'),(121,'Can add hielo proceso',31,'add_hieloproceso'),(122,'Can change hielo proceso',31,'change_hieloproceso'),(123,'Can delete hielo proceso',31,'delete_hieloproceso'),(124,'Can view hielo proceso',31,'view_hieloproceso'),(125,'Can add departamento proceso',32,'add_departamentoproceso'),(126,'Can change departamento proceso',32,'change_departamentoproceso'),(127,'Can delete departamento proceso',32,'delete_departamentoproceso'),(128,'Can view departamento proceso',32,'view_departamentoproceso'),(129,'Can add recipiente detalle hielo proceso',33,'add_recipientedetallehieloproceso'),(130,'Can change recipiente detalle hielo proceso',33,'change_recipientedetallehieloproceso'),(131,'Can delete recipiente detalle hielo proceso',33,'delete_recipientedetallehieloproceso'),(132,'Can view recipiente detalle hielo proceso',33,'view_recipientedetallehieloproceso'),(133,'Can add detalle hielo proceso',34,'add_detallehieloproceso'),(134,'Can change detalle hielo proceso',34,'change_detallehieloproceso'),(135,'Can delete detalle hielo proceso',34,'delete_detallehieloproceso'),(136,'Can view detalle hielo proceso',34,'view_detallehieloproceso'),(137,'Can add entrada camaron',35,'add_entradacamaron'),(138,'Can change entrada camaron',35,'change_entradacamaron'),(139,'Can delete entrada camaron',35,'delete_entradacamaron'),(140,'Can view entrada camaron',35,'view_entradacamaron'),(141,'Can add detalle entrada camaron',36,'add_detalleentradacamaron'),(142,'Can change detalle entrada camaron',36,'change_detalleentradacamaron'),(143,'Can delete detalle entrada camaron',36,'delete_detalleentradacamaron'),(144,'Can view detalle entrada camaron',36,'view_detalleentradacamaron'),(145,'Can add cosecha',37,'add_cosecha'),(146,'Can change cosecha',37,'change_cosecha'),(147,'Can delete cosecha',37,'delete_cosecha'),(148,'Can view cosecha',37,'view_cosecha'),(149,'Can add detalle cosecha',38,'add_detallecosecha'),(150,'Can change detalle cosecha',38,'change_detallecosecha'),(151,'Can delete detalle cosecha',38,'delete_detallecosecha'),(152,'Can view detalle cosecha',38,'view_detallecosecha'),(153,'Puede terminar la remision de hielo',26,'terminar_remision'),(154,'Puede terminar la remision de hielo',27,'terminar_remision'),(155,'Can add cargo',39,'add_cargo'),(156,'Can change cargo',39,'change_cargo'),(157,'Can delete cargo',39,'delete_cargo'),(158,'Can view cargo',39,'view_cargo'),(159,'Puede restablecer la contraseña del empleado',12,'restablecer_contrasena'),(160,'Puede obtener la contraseña del empleado',12,'obtener_contrasena'),(161,'Puede generar reportes de remision de hielo',27,'generar_reportes'),(162,'Puede anular prestamos de equipo',23,'anular_prestamoequipo'),(163,'Puede terminar prestamos de equipo',23,'terminar_prestamoequipo'),(164,'Puede imprimir prestamos de equipo',23,'imprimir_prestamoequipo'),(165,'Puede generar reportes de prestamos de equipo',23,'reporte_prestamoequipo'),(166,'Puede imprimir las cosechas',37,'imprimir_cosecha'),(167,'Puede imprimir el consumo de hielo en proceso',31,'imprimir_hieloproceso'),(168,'Puede graficar el consumo de hielo en proceso',31,'grafico_hieloproceso'),(169,'Puede crear codigo qr para el inventario de equipo',17,'crearqr_equipo'),(170,'Puede cambiar el estado de la empresa',9,'estado_compania'),(171,'Puede cambiar el estado del conductor',14,'estado_conductor'),(172,'Puede cambiar el estado del empleado',12,'estado_empleado'),(173,'Puede devolver el equipo prestado',17,'devolver_equipo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_spanish_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_spanish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$m7qrGWlVWgGT$wYWlOuCk10tiBmghMpNUBtmjxUUUPeYyOI19ISB9X2k=','2019-10-31 10:38:09.612226',1,'admin','Jorge','Escoto','jorgeescoto18@gmail.com',1,1,'2019-04-05 20:11:34.000000'),(20,'pbkdf2_sha256$150000$ns9Saod8Uo30$jKuh3jLdx7XvgrCgXfB5PIB955L4lElevK06kStfRtU=','2019-07-29 19:22:51.533114',0,'Maryori','Maryori','Burke','mburke@empacadoralitoral.com',0,1,'2019-07-29 19:21:21.778164'),(41,'pbkdf2_sha256$150000$ndoEHfW0vjnn$Ms1l7/Q/BkSiBN6240BA1TI/pA3N0ekhwnplaDrHrTQ=','2019-10-31 11:08:59.047723',1,'kevin','Kevin','Escoto','escotokevin1@gmail.com',1,1,'2019-10-31 10:39:52.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (15,20,2),(34,41,2);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `camaron_cosecha`
--

DROP TABLE IF EXISTS `camaron_cosecha`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `camaron_cosecha` (
  `codCosecha` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `fecha` date NOT NULL,
  `horaInicio` time(6) NOT NULL,
  `horaFinal` time(6) NOT NULL,
  `entrego_id` int(11) NOT NULL,
  `laguna_id` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `registro_id` int(11) NOT NULL,
  `remision_id` varchar(6) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`codCosecha`),
  KEY `camaron_cosecha_entrego_id_bf66e5c9_fk_empleado_` (`entrego_id`),
  KEY `camaron_cosecha_laguna_id_c1e7cb15_fk_compania_laguna_codLaguna` (`laguna_id`),
  KEY `camaron_cosecha_registro_id_9ea3151f_fk_auth_user_id` (`registro_id`),
  KEY `camaron_cosecha_remision_id_e133b41c_fk_remision_` (`remision_id`),
  CONSTRAINT `camaron_cosecha_entrego_id_bf66e5c9_fk_empleado_` FOREIGN KEY (`entrego_id`) REFERENCES `empleado_empleado` (`codEmpleado`),
  CONSTRAINT `camaron_cosecha_laguna_id_c1e7cb15_fk_compania_laguna_codLaguna` FOREIGN KEY (`laguna_id`) REFERENCES `compania_laguna` (`codLaguna`),
  CONSTRAINT `camaron_cosecha_registro_id_9ea3151f_fk_auth_user_id` FOREIGN KEY (`registro_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `camaron_cosecha_remision_id_e133b41c_fk_remision_` FOREIGN KEY (`remision_id`) REFERENCES `remision_remision` (`numRemision`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `camaron_cosecha`
--

LOCK TABLES `camaron_cosecha` WRITE;
/*!40000 ALTER TABLE `camaron_cosecha` DISABLE KEYS */;
/*!40000 ALTER TABLE `camaron_cosecha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `camaron_detallecosecha`
--

DROP TABLE IF EXISTS `camaron_detallecosecha`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `camaron_detallecosecha` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `totalCanasta` int(10) unsigned NOT NULL,
  `libras` decimal(5,2) NOT NULL,
  `observaciones` longtext COLLATE utf8_spanish_ci,
  `cosecha_id` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `numeroBin_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `camaron_detallecosecha_numeroBin_id_0af50705_fk_equipo_equipo_id` (`numeroBin_id`),
  KEY `camaron_detallecosec_cosecha_id_e835fef8_fk_camaron_c` (`cosecha_id`),
  CONSTRAINT `camaron_detallecosec_cosecha_id_e835fef8_fk_camaron_c` FOREIGN KEY (`cosecha_id`) REFERENCES `camaron_cosecha` (`codCosecha`),
  CONSTRAINT `camaron_detallecosecha_numeroBin_id_0af50705_fk_equipo_equipo_id` FOREIGN KEY (`numeroBin_id`) REFERENCES `equipo_equipo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `camaron_detallecosecha`
--

LOCK TABLES `camaron_detallecosecha` WRITE;
/*!40000 ALTER TABLE `camaron_detallecosecha` DISABLE KEYS */;
/*!40000 ALTER TABLE `camaron_detallecosecha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compania_compania`
--

DROP TABLE IF EXISTS `compania_compania`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `compania_compania` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `direccion` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `abreviatura` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipoCompania_id` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `compania_compania_nombre_4c945be6_uniq` (`nombre`),
  UNIQUE KEY `compania_compania_abreviatura_0a650c4a_uniq` (`abreviatura`),
  KEY `compania_compania_tipoCompania_id_def61f1c_fk_compania_` (`tipoCompania_id`),
  CONSTRAINT `compania_compania_tipoCompania_id_def61f1c_fk_compania_` FOREIGN KEY (`tipoCompania_id`) REFERENCES `compania_tipocompania` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compania_compania`
--

LOCK TABLES `compania_compania` WRITE;
/*!40000 ALTER TABLE `compania_compania` DISABLE KEYS */;
INSERT INTO `compania_compania` VALUES (27,'Empresa Barjum','Choluteca','BARJUM',2,1),(28,'Rent A Car','Choluteca','RAC',2,1),(29,'Cargas Y Camiones S.a','Valle','CARGASA',2,1),(30,'Carguil S.a','Tegucigalpa','CARGUIL',2,1),(31,'Corporación Acuícola de Centroamérica S. A.','Choluteca','CACESA',1,1),(32,'Grupo Litoral','Golfo de Fonseca,Choluteca','GL',1,1),(33,'Grupo Granjas Marinas S. A. De C. V.','Choluteca','GGM',1,1);
/*!40000 ALTER TABLE `compania_compania` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compania_finca`
--

DROP TABLE IF EXISTS `compania_finca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `compania_finca` (
  `codFinca` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `abreviatura` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `direccion` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `compania_id` int(11) NOT NULL,
  PRIMARY KEY (`codFinca`),
  KEY `compania_finca_compania_id_2bef22f0_fk_compania_compania_id` (`compania_id`),
  CONSTRAINT `compania_finca_compania_id_2bef22f0_fk_compania_compania_id` FOREIGN KEY (`compania_id`) REFERENCES `compania_compania` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compania_finca`
--

LOCK TABLES `compania_finca` WRITE;
/*!40000 ALTER TABLE `compania_finca` DISABLE KEYS */;
INSERT INTO `compania_finca` VALUES ('1001','Cultivo De Camarones Del Mar','CULCAMAR','los Lirios, Marcovia, Las Conchas, Choluteca',31),('1002','Inmar','INMAR','Choluteca',31),('1003','Bodega Del Mar S. A.','BOMAR','Choluteca',31),('1101','Cultivos Marinos','CULMAR','Golfo De Fonseca',32),('1102','Cultivos Marinos Del Sur','CULMASA','Golfo De Fonseca',32),('1103','Camarones Y Derivados S. A.','CAYDESA','Golfo De Fonseca',32),('1104','Langostinos Del Pacifico S. A.','LANPACSA','Golfo De Fonseca',32),('1201','Granjas Marinas San Bernardo',NULL,'Golfo De Fonseca',33),('1202','Criaderos Marinos S. A.','CRIMASA','Golfo De Fonseca',33),('1203','Camaronera Del Pacifico','CADELPA','Golfo De Fonseca',33),('1205','Aquacultivos De Honduras','AQH','Golfo De Fonseca',33);
/*!40000 ALTER TABLE `compania_finca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compania_laguna`
--

DROP TABLE IF EXISTS `compania_laguna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `compania_laguna` (
  `codLaguna` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `tamano` int(11) DEFAULT NULL,
  `ubicacion` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `descripcion` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `finca_id` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`codLaguna`),
  KEY `compania_laguna_finca_id_da5aec11_fk_compania_finca_codFinca` (`finca_id`),
  CONSTRAINT `compania_laguna_finca_id_da5aec11_fk_compania_finca_codFinca` FOREIGN KEY (`finca_id`) REFERENCES `compania_finca` (`codFinca`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compania_laguna`
--

LOCK TABLES `compania_laguna` WRITE;
/*!40000 ALTER TABLE `compania_laguna` DISABLE KEYS */;
INSERT INTO `compania_laguna` VALUES ('AQH01',500,NULL,NULL,'1205'),('AQH02',500,NULL,NULL,'1205'),('BOM01',500,NULL,NULL,'1003'),('BOM02',500,NULL,NULL,'1003'),('CDP01',500,NULL,NULL,'1203'),('CDP02',540,NULL,NULL,'1203'),('CLM01',500,NULL,NULL,'1102'),('CLM02',540,NULL,NULL,'1102'),('CRM01',520,NULL,NULL,'1202'),('CRM02',500,NULL,NULL,'1202'),('CU01',500,NULL,NULL,'1001'),('CU02',500,NULL,NULL,'1101'),('CUL01',550,NULL,NULL,'1101'),('CUL02',600,NULL,NULL,'1001'),('CYD01',500,NULL,NULL,'1103'),('CYD02',500,NULL,NULL,'1103'),('INM01',550,NULL,NULL,'1002'),('INM02',500,NULL,NULL,'1002'),('LPC01',500,NULL,NULL,'1104'),('LPC02',500,NULL,NULL,'1104'),('NON01',500,NULL,NULL,'1201'),('NON02',500,NULL,NULL,'1201');
/*!40000 ALTER TABLE `compania_laguna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compania_tipocompania`
--

DROP TABLE IF EXISTS `compania_tipocompania`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `compania_tipocompania` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compania_tipocompania`
--

LOCK TABLES `compania_tipocompania` WRITE;
/*!40000 ALTER TABLE `compania_tipocompania` DISABLE KEYS */;
INSERT INTO `compania_tipocompania` VALUES (1,'CAMARONERA'),(2,'FLETE');
/*!40000 ALTER TABLE `compania_tipocompania` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conductor_conductor`
--

DROP TABLE IF EXISTS `conductor_conductor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `conductor_conductor` (
  `numIdentidad` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `nombre1` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `nombre2` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `apellido1` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `apellido2` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `celular` int(11) DEFAULT NULL,
  `activo` tinyint(1) NOT NULL,
  `disponible` tinyint(1) NOT NULL,
  PRIMARY KEY (`numIdentidad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conductor_conductor`
--

LOCK TABLES `conductor_conductor` WRITE;
/*!40000 ALTER TABLE `conductor_conductor` DISABLE KEYS */;
INSERT INTO `conductor_conductor` VALUES ('0601-1974-12245','Willian',NULL,'Rodriguez',NULL,'1974-07-12',95940613,1,0),('0601-1975-14223','Manuel',NULL,'Maradiaga',NULL,'1975-11-03',95967514,1,0),('0601-1975-16144','Kenneth',NULL,'Ponce',NULL,'1975-08-05',95967374,1,0),('0601-1981-12564','Brayan',NULL,'Portillo',NULL,'1973-06-06',98967543,1,1),('0601-1982-16012','Fernando',NULL,'Sandoval',NULL,'1982-06-04',95967514,1,0),('0615-1978-16314','Marcio',NULL,'Ponce',NULL,'1978-12-05',96967513,1,1),('0615-1981-16258','Elix',NULL,'Soriano',NULL,'1981-08-01',95951673,1,1),('0615-1983-16452','Fernando',NULL,'Rodriguez',NULL,'1983-06-05',75768898,1,1),('0615-1990-00415','Willson',NULL,'Betancourth',NULL,'1990-05-01',NULL,1,0),('0801-1973-15233','Hilder',NULL,'Mendez',NULL,'1973-11-05',98967568,1,1),('0801-1986-12983','Hernan',NULL,'Tabora',NULL,'1986-12-11',98964568,1,1);
/*!40000 ALTER TABLE `conductor_conductor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_spanish_ci,
  `object_repr` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_spanish_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=619 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-04-08 16:17:18.491825','1','Administrador',1,'[{\"added\": {}}]',13,1),(2,'2019-04-08 16:17:30.604683','1','1 -> Todo',1,'[{\"added\": {}}]',11,1),(3,'2019-04-08 16:17:37.829906','2','2 -> Ninguno',1,'[{\"added\": {}}]',11,1),(4,'2019-04-08 16:17:45.188535','1','Jorge Escoto Ponce',1,'[{\"added\": {}}]',12,1),(5,'2019-04-08 17:54:11.258349','1','Activo',1,'[{\"added\": {}}]',22,1),(6,'2019-04-08 17:54:27.967263','2','Anulado',1,'[{\"added\": {}}]',22,1),(7,'2019-04-08 17:54:35.141119','3','Terminado',1,'[{\"added\": {}}]',22,1),(8,'2019-04-08 19:59:52.565243','1','CAMARONERA',1,'[{\"added\": {}}]',10,1),(9,'2019-04-08 20:00:04.443118','1','CUMAR',1,'[{\"added\": {}}]',9,1),(10,'2019-04-08 20:01:10.651246','05','05 -> nuevo',1,'[{\"added\": {}}]',8,1),(11,'2019-04-08 20:02:39.953514','f1','05 -> nuevo -> f1',1,'[{\"added\": {}}]',7,1),(12,'2019-04-08 20:04:26.955757','0000-0000-00001','0000-0000-00001 - juan molina',1,'[{\"added\": {}}]',14,1),(13,'2019-04-08 20:05:08.904219','1','Bin',1,'[{\"added\": {}}]',19,1),(14,'2019-04-08 20:05:25.573431','1','Blanco',1,'[{\"added\": {}}]',15,1),(15,'2019-04-08 20:05:31.554851','2','Negro',1,'[{\"added\": {}}]',15,1),(16,'2019-04-08 20:05:42.679269','3','Azul',1,'[{\"added\": {}}]',15,1),(17,'2019-04-08 20:06:19.655289','1','Tamano object (1)',1,'[{\"added\": {}}]',16,1),(18,'2019-04-08 20:06:33.688239','2','Tamano object (2)',1,'[{\"added\": {}}]',16,1),(19,'2019-04-08 20:06:55.248873','1','Asignado',1,'[{\"added\": {}}]',18,1),(20,'2019-04-08 20:07:00.608016','2','Disponible',1,'[{\"added\": {}}]',18,1),(21,'2019-04-08 20:07:12.161523','3','Fuera de Servicio',1,'[{\"added\": {}}]',18,1),(22,'2019-04-08 20:07:17.460261','1','Equipo object (1)',1,'[{\"added\": {}}]',17,1),(23,'2019-04-08 20:09:17.333106','2','Pallet',1,'[{\"added\": {}}]',19,1),(24,'2019-04-08 20:09:29.730909','3','Normal',1,'[{\"added\": {}}]',16,1),(25,'2019-04-08 20:09:58.603242','2','Pallet - Normal > 1',1,'[{\"added\": {}}]',17,1),(26,'2019-04-08 20:13:57.526169','2','Flete',1,'[{\"added\": {}}]',10,1),(27,'2019-04-08 20:14:03.430313','2','CARGIL S.A',1,'[{\"added\": {}}]',9,1),(28,'2019-04-08 20:14:09.045796','HCH0001','HCH0001 -> Toyota Blanco',1,'[{\"added\": {}}]',20,1),(29,'2019-04-08 20:15:51.775463','000001','000001 -> CUMAR',1,'[{\"added\": {}}]',23,1),(30,'2019-04-08 20:17:43.518828','1','000001 -> CUMAR -> se prestaron 1 bin',1,'[{\"added\": {}}]',21,1),(31,'2019-04-08 20:18:19.296330','1','Masa -> Quintal',1,'[{\"added\": {}}]',26,1),(32,'2019-04-08 20:37:34.811773','1','Maquila',1,'[{\"added\": {}}]',28,1),(33,'2019-04-08 20:39:45.839004','000001','000001 -> CUMAR',1,'[{\"added\": {}}]',27,1),(34,'2019-04-08 20:42:39.572112','1','Limpio -> 60',1,'[{\"added\": {}}]',24,1),(35,'2019-04-08 20:42:47.722260','2','Sucio -> 10',1,'[{\"added\": {}}]',24,1),(36,'2019-04-08 20:43:19.953595','1','000001 -> CUMAR -> 10 :10',1,'[{\"added\": {}}]',25,1),(37,'2019-04-09 16:33:31.152668','2','(2)Pallet - Normal > 1',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',17,1),(38,'2019-04-09 16:40:47.166498','3','(3)Bin - Pequeño > 2',1,'[{\"added\": {}}]',17,1),(39,'2019-05-07 21:16:17.792994','22','12345 -> CUMAR -> None',3,'',21,1),(40,'2019-05-07 21:16:31.657026','12345','12345 -> CUMAR',3,'',23,1),(41,'2019-05-07 21:20:31.971114','000013','000013 -> CUMAR',3,'',23,1),(42,'2019-05-16 21:09:57.911914','000002','000002 -> CUMAR',3,'',27,1),(43,'2019-05-16 21:11:45.491288','000003','000003 -> CUMAR',3,'',27,1),(44,'2019-05-21 19:57:55.129132','2','obek',1,'[{\"added\": {}}]',4,1),(45,'2019-05-21 19:59:24.096495','2','Obek Ponce',1,'[{\"added\": {}}]',12,1),(46,'2019-05-23 17:20:53.915818','000006','000006 -> CUMAR',3,'',27,1),(47,'2019-05-23 18:27:34.433198','3','3 Asignado',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',22,1),(48,'2019-05-23 18:27:47.354686','4','4 Terminado',1,'[{\"added\": {}}]',22,1),(49,'2019-05-23 18:48:23.369195','000007','000007 -> CUMAR',3,'',27,1),(50,'2019-05-23 21:58:50.881362','000007','000007 -> CULMASA',3,'',27,1),(51,'2019-05-23 22:21:13.306176','000007','000007 -> CULMASA',3,'',27,1),(52,'2019-05-24 00:01:29.228041','000007','000007 -> CULMASA',3,'',27,1),(53,'2019-05-24 00:06:01.301509','000007','000007 -> CULMASA',3,'',27,1),(54,'2019-05-24 14:38:27.586133','000008','000008 -> CUMAR',3,'',27,1),(55,'2019-05-24 14:38:42.385256','000007','000007 -> CULMASA',3,'',27,1),(56,'2019-05-24 14:43:02.265223','000008','000008 -> CUMAR',3,'',27,1),(57,'2019-05-24 17:32:21.468840','000012','000012 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(58,'2019-05-24 17:32:47.336579','000001','000001 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(59,'2019-05-24 17:34:23.429760','000013','000013 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(60,'2019-05-24 17:35:14.445502','00005','00005 -> CUMAR',3,'',27,1),(61,'2019-05-24 18:14:09.081657','000008','000008 -> CULMASA',3,'',27,1),(62,'2019-05-24 18:17:39.110512','000007','000007 -> CULMASA',3,'',27,1),(63,'2019-05-24 18:19:50.546814','000007','000007 -> CULMASA',3,'',27,1),(64,'2019-05-24 18:22:13.639761','000007','000007 -> CUMAR',3,'',27,1),(65,'2019-05-24 18:39:09.413566','000011','000011 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(66,'2019-05-24 18:39:30.833823','000007','000007 -> CUMAR',3,'',27,1),(67,'2019-05-24 18:43:03.564033','000011','000011 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(68,'2019-05-24 18:43:07.127312','000007','000007 -> CUMAR',3,'',27,1),(69,'2019-05-24 18:43:54.850758','000011','000011 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(70,'2019-05-24 18:43:57.702397','000007','000007 -> CUMAR',3,'',27,1),(71,'2019-05-24 18:50:15.945513','000007','000007 -> CULMASA',3,'',27,1),(72,'2019-05-24 20:03:09.385995','000008','000008 -> CUMAR',3,'',27,1),(73,'2019-05-24 20:03:34.130159','000008','000008 -> CUMAR',3,'',27,1),(74,'2019-05-25 16:15:57.812245','111111','111111 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(75,'2019-05-26 19:03:47.432648','000008','000008 -> CUMAR',3,'',27,1),(76,'2019-05-26 21:36:34.955204','000008','000008 -> CUMAR',3,'',27,1),(77,'2019-05-26 21:40:06.867636','000008','000008 -> CUMAR',3,'',27,1),(78,'2019-05-26 21:48:14.698221','000008','000008 -> CUMAR',3,'',27,1),(79,'2019-05-26 22:02:01.172454','000011','000011 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(80,'2019-05-26 22:02:05.549998','000008','000008 -> CUMAR',3,'',27,1),(81,'2019-05-26 22:04:40.504359','000011','000011 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(82,'2019-05-26 22:34:05.760975','000011','000011 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(83,'2019-05-28 20:39:35.330167','000011','000011 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(84,'2019-05-29 17:25:47.858211','000009','000009 -> CUMAR',3,'',27,1),(85,'2019-05-29 22:23:56.515559','1','1 Activo',1,'[{\"added\": {}}]',29,1),(86,'2019-05-29 22:24:06.358178','2','2 Asignado',1,'[{\"added\": {}}]',29,1),(87,'2019-05-29 22:24:13.416656','3','3 Anulado',1,'[{\"added\": {}}]',29,1),(88,'2019-05-29 22:36:48.367741','000008','000008 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(89,'2019-05-29 22:39:49.251781','000007','000007 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(90,'2019-05-29 22:39:55.624082','000006','000006 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(91,'2019-05-29 22:40:02.612226','000003','000003 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(92,'2019-05-29 22:40:07.941348','000002','000002 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(93,'2019-05-29 22:40:12.753858','000001','000001 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(94,'2019-05-29 22:49:30.233064','000010','000010 -> CUMAR',3,'',27,1),(95,'2019-05-29 22:53:38.917091','000010','000010 -> CULMASA',3,'',27,1),(96,'2019-05-30 14:34:53.021218','000010','000010 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(97,'2019-05-30 14:35:03.385727','000008','000008 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(98,'2019-05-30 17:04:25.246213','000010','000010 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(99,'2019-05-30 17:04:37.667720','000008','000008 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(100,'2019-05-30 20:41:35.856169','000007','000007 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(101,'2019-05-31 18:09:04.544276','000010','000010 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(102,'2019-05-31 18:09:13.620865','000008','000008 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(103,'2019-05-31 18:09:23.448557','000007','000007 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(104,'2019-06-09 00:39:37.031366','2','2 Terminado',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',29,1),(105,'2019-06-09 01:30:41.309825','000007','000007 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(106,'2019-06-09 01:30:52.684339','000008','000008 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(107,'2019-06-09 02:00:52.799256','000008','000008 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(108,'2019-06-09 02:01:39.097447','000007','000007 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(109,'2019-06-09 02:15:40.686121','000008','000008 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(110,'2019-06-09 02:15:49.800112','000007','000007 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(111,'2019-06-09 03:04:09.513875','000008','000008 -> CUMAR',2,'[]',27,1),(112,'2019-06-13 02:32:22.690977','8','(8)Bin - Normal > 12',1,'[{\"added\": {}}]',17,1),(113,'2019-06-16 04:11:33.706836','000002','000002 -> CULMASA',3,'',23,1),(114,'2019-06-19 16:19:14.286608','30','000013 -> CUMAR -> None',2,'[{\"changed\": {\"fields\": [\"prestamoEquipo\"]}}]',21,1),(115,'2019-06-19 16:21:57.100747','4','(4)Bin - Pequeño > 3',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',17,1),(116,'2019-06-19 16:25:20.964768','31','000013 -> CUMAR -> None',2,'[{\"changed\": {\"fields\": [\"prestamoEquipo\"]}}]',21,1),(117,'2019-06-19 16:25:29.914290','29','000013 -> CUMAR -> None',2,'[{\"changed\": {\"fields\": [\"prestamoEquipo\"]}}]',21,1),(118,'2019-06-19 16:25:43.804560','28','000013 -> CUMAR -> la tapita',2,'[{\"changed\": {\"fields\": [\"prestamoEquipo\"]}}]',21,1),(119,'2019-06-19 16:26:02.033916','4','(4)Bin - Pequeño > 3',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',17,1),(120,'2019-06-19 16:26:03.616166','31','000013 -> CUMAR -> None',2,'[]',21,1),(121,'2019-06-19 16:26:22.851599','29','000013 -> CUMAR -> None',3,'',21,1),(122,'2019-06-19 16:26:35.897715','8','(8)Bin - Normal > 12',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',17,1),(123,'2019-06-19 16:26:38.194339','28','000013 -> CUMAR -> la tapita',2,'[]',21,1),(124,'2019-06-19 18:34:51.869647','8','(8)Bin - Normal > 12',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',17,1),(125,'2019-06-19 18:35:43.256637','000015','000015 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(126,'2019-06-19 18:35:45.755619','33','000015 -> CULMASA -> None',2,'[]',21,1),(127,'2019-06-19 18:38:21.862264','9','(9)Bin - Normal > 15',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',17,1),(128,'2019-06-19 18:38:24.517993','33','000015 -> CULMASA -> None',2,'[]',21,1),(129,'2019-06-20 18:34:56.980259','000015','000015 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"fechaEntrada\"]}}]',23,1),(130,'2019-06-20 20:33:16.738349','000015','000015 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(131,'2019-06-20 20:33:26.589338','000015','000015 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"fechaEntrada\"]}}]',23,1),(132,'2019-06-20 20:33:58.742860','9','(9)Bin - Normal > 15',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',17,1),(133,'2019-06-21 17:48:09.318468','000015','000015 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"fechaEntrada\", \"estadoPrestamo\"]}}]',23,1),(134,'2019-06-21 17:48:20.183494','9','(9)Bin - Normal > 15',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',17,1),(135,'2019-06-21 17:48:22.627225','33','000015 -> CULMASA -> None',2,'[]',21,1),(136,'2019-06-24 21:07:50.014160','1','admin',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]',4,1),(137,'2019-06-26 23:52:08.482775','000001','000001 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"observacion\"]}}]',27,1),(138,'2019-06-27 20:13:41.225508','1','Descabezado',1,'[{\"added\": {}}]',32,1),(139,'2019-06-27 20:16:12.563324','1','2019-06-27',1,'[{\"added\": {}}]',31,1),(140,'2019-06-27 20:16:57.588811','1','Descabezado',1,'[{\"added\": {}}]',34,1),(141,'2019-06-27 20:36:17.223168','1','Descabezado',3,'',32,1),(142,'2019-06-27 20:51:36.730581','1','Bin',1,'[{\"added\": {}}]',30,1),(143,'2019-06-27 20:52:12.390675','2','Descabezado',1,'[{\"added\": {}}]',32,1),(144,'2019-06-27 20:52:31.183304','2','2019-06-27 - Descabezado',1,'[{\"added\": {}}]',31,1),(145,'2019-06-27 20:53:21.880587','2','Bin = 2',1,'[{\"added\": {}}]',34,1),(146,'2019-06-27 21:00:12.553822','3','Bin = 4 -> 60.0000',1,'[{\"added\": {}}]',34,1),(147,'2019-06-27 21:02:08.148770','3','Bin = 4 -> 60.0000',3,'',34,1),(148,'2019-06-29 01:30:59.438718','2','2019-06-27 - Descabezado',3,'',31,1),(149,'2019-06-29 01:34:26.458691','3','2019-06-28',1,'[{\"added\": {}}]',31,1),(150,'2019-06-29 01:34:43.170164','4','Descabezado:Bin = 2 -> 30.0000',1,'[{\"added\": {}}]',34,1),(151,'2019-06-29 01:35:38.072560','2','Carreton',1,'[{\"added\": {}}]',30,1),(152,'2019-06-29 01:35:42.039290','5','Descabezado:Carreton = 2 -> 60.0000',1,'[{\"added\": {}}]',34,1),(153,'2019-06-29 02:03:47.219569','3','2019-06-28',3,'',31,1),(154,'2019-06-29 02:08:20.034338','4','2019-06-28',1,'[{\"added\": {}}]',31,1),(155,'2019-06-29 02:08:38.016599','5','2019-06-29',1,'[{\"added\": {}}]',31,1),(156,'2019-06-29 02:11:55.776836','6','2019-06-28 - Descabezado',1,'[{\"added\": {}}]',31,1),(157,'2019-06-29 02:18:37.328477','3','Pelado',1,'[{\"added\": {}}]',32,1),(158,'2019-06-29 02:18:43.887141','7','2019-06-28 - Pelado',1,'[{\"added\": {}}]',31,1),(159,'2019-06-29 02:19:07.888525','6','Bin = 1 -> 15.0000',1,'[{\"added\": {}}]',34,1),(160,'2019-06-29 02:19:19.921328','7','Carreton = 2 -> 60.0000',1,'[{\"added\": {}}]',34,1),(161,'2019-06-29 02:19:31.184287','8','Bin = 2 -> 30.0000',1,'[{\"added\": {}}]',34,1),(162,'2019-06-29 02:19:43.684700','9','Carreton = 4 -> 120.0000',1,'[{\"added\": {}}]',34,1),(163,'2019-06-29 02:29:24.105524','7','2019-06-28 - Pelado',3,'',31,1),(164,'2019-06-29 02:29:24.129752','6','2019-06-28 - Descabezado',3,'',31,1),(165,'2019-06-29 02:34:17.111066','8','2019-06-28',1,'[{\"added\": {}}]',31,1),(166,'2019-06-29 02:34:54.213739','10','Descabezado:Bin = 1 -> 15.0000',1,'[{\"added\": {}}]',34,1),(167,'2019-06-29 02:35:08.392948','11','Descabezado:Carreton = 2 -> 60.0000',1,'[{\"added\": {}}]',34,1),(168,'2019-06-29 02:36:51.386777','9','2019-06-29',1,'[{\"added\": {}}]',31,1),(169,'2019-06-29 02:37:13.364831','12','Descabezado:Bin = 12 -> 180.0000',1,'[{\"added\": {}}]',34,1),(170,'2019-06-29 04:34:26.563397','13','Pelado:Carreton = 10 -> 300.0000',1,'[{\"added\": {}}]',34,1),(171,'2019-06-29 14:42:27.787650','14','Pelado:Carreton = 8 -> 240.0000',1,'[{\"added\": {}}]',34,1),(172,'2019-06-29 15:22:56.313073','9','2019-06-29',3,'',31,1),(173,'2019-06-29 15:22:56.329524','8','2019-06-28',3,'',31,1),(174,'2019-06-29 15:29:51.477744','10','2019-06-29',1,'[{\"added\": {}}]',31,1),(175,'2019-06-29 15:31:52.314636','16','2019-06-29 = Descabezado -> 1',1,'[{\"added\": {}}]',34,1),(176,'2019-06-29 16:13:49.265770','17','2019-06-29 Pelado -> bin = 0,carreton = 2',1,'[{\"added\": {}}]',34,1),(177,'2019-06-29 16:14:02.569568','11','2019-06-30',1,'[{\"added\": {}}]',31,1),(178,'2019-06-29 16:14:12.486787','18','2019-06-30 Pelado -> bin = 3,carreton = 1',1,'[{\"added\": {}}]',34,1),(179,'2019-06-29 16:31:16.159570','12','2019-06-28',1,'[{\"added\": {}}]',31,1),(180,'2019-06-29 16:31:27.657392','19','2019-06-28 Descabezado -> bin = 1,carreton = 1',1,'[{\"added\": {}}]',34,1),(181,'2019-06-29 16:40:24.171483','20','2019-06-30 Descabezado -> bin = 1,carreton = 3',1,'[{\"added\": {}}]',34,1),(182,'2019-06-29 17:39:54.312558','2','Maquina 1',2,'[{\"changed\": {\"fields\": [\"departamento\"]}}]',32,1),(183,'2019-06-29 17:40:18.494805','3','Maquina 2',2,'[{\"changed\": {\"fields\": [\"departamento\"]}}]',32,1),(184,'2019-06-29 17:40:25.208229','4','Maquina 3',1,'[{\"added\": {}}]',32,1),(185,'2019-06-29 17:40:32.582188','5','Maquina 4',1,'[{\"added\": {}}]',32,1),(186,'2019-06-29 17:40:46.705337','6','Empaque fresco',1,'[{\"added\": {}}]',32,1),(187,'2019-06-29 17:41:00.897912','7','Descabezado',1,'[{\"added\": {}}]',32,1),(188,'2019-06-29 17:41:18.387645','8','Reenhielado',1,'[{\"added\": {}}]',32,1),(189,'2019-06-29 17:41:28.521939','9','Clasificado',1,'[{\"added\": {}}]',32,1),(190,'2019-06-29 17:41:37.082386','10','Reproceso',1,'[{\"added\": {}}]',32,1),(191,'2019-06-29 17:41:48.502253','11','Langosta',1,'[{\"added\": {}}]',32,1),(192,'2019-06-29 17:41:55.330556','12','Pelado',1,'[{\"added\": {}}]',32,1),(193,'2019-06-29 17:42:05.295668','13','Descongelado',1,'[{\"added\": {}}]',32,1),(194,'2019-06-29 17:54:48.215125','20','2019-06-30 Maquina 1 -> binGrande = 1 ...',2,'[]',34,1),(195,'2019-06-29 17:54:55.864067','19','2019-06-28 Maquina 1 -> binGrande = 1 ...',2,'[]',34,1),(196,'2019-07-02 17:12:45.360622','14','2019-07-01',3,'',31,1),(197,'2019-07-02 17:12:45.411436','13','2019-07-12',3,'',31,1),(198,'2019-07-02 17:33:57.255193','15','2019-07-01',3,'',31,1),(199,'2019-07-02 20:52:01.092248','17','2019-08-01',3,'',31,1),(200,'2019-07-02 20:52:01.134639','16','2019-07-28',3,'',31,1),(201,'2019-07-02 21:01:40.885535','20','2019-07-03',3,'',31,1),(202,'2019-07-02 21:01:40.900246','19','2019-07-02',3,'',31,1),(203,'2019-07-02 21:01:40.914597','18','2019-07-01',3,'',31,1),(204,'2019-07-02 21:08:57.761222','25','2019-07-05',3,'',31,1),(205,'2019-07-02 21:08:57.790191','24','2019-07-04',3,'',31,1),(206,'2019-07-02 21:08:57.803778','23','2019-07-03',3,'',31,1),(207,'2019-07-02 21:08:57.817831','22','2019-07-02',3,'',31,1),(208,'2019-07-02 21:08:57.838515','21','2019-07-01',3,'',31,1),(209,'2019-07-07 05:38:13.314037','1','1',1,'[{\"added\": {}}]',35,1),(210,'2019-07-07 05:39:26.263775','1','(1) (6)Bin - Grande > 5 -> 200',1,'[{\"added\": {}}]',36,1),(211,'2019-07-07 05:40:04.224646','2','(1) (7)Bin - Pequeño > 7 -> 78',1,'[{\"added\": {}}]',36,1),(212,'2019-07-07 06:18:21.805685','1','1',3,'',35,1),(213,'2019-07-07 07:04:28.051528','008856','008856',1,'[{\"added\": {}}]',37,1),(214,'2019-07-07 07:05:36.089979','1','(008856) (6)Bin - Grande > 5 -> -0.06',1,'[{\"added\": {}}]',38,1),(215,'2019-07-07 07:05:59.339924','1','(008856) (6)Bin - Grande > 5 -> 100',2,'[{\"changed\": {\"fields\": [\"libras\"]}}]',38,1),(216,'2019-07-07 07:06:32.601428','2','(008856) (7)Bin - Pequeño > 7 -> 140',1,'[{\"added\": {}}]',38,1),(217,'2019-07-07 22:33:06.508858','F6','05 -> nuevo -> F6',1,'[{\"added\": {}}]',7,1),(218,'2019-07-08 21:10:36.357119','ll','ll',3,'',37,1),(219,'2019-07-08 22:04:33.071491','111','111',3,'',37,1),(220,'2019-07-09 02:03:28.606677','000001','000001 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(221,'2019-07-09 02:03:41.835179','000001','000001 -> CUMAR',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(222,'2019-07-09 02:09:04.921034','111','111',3,'',37,1),(223,'2019-07-10 20:06:21.897595','4','(fff) (2)Pallet - Normal > 1 -> 20.00',3,'',38,1),(224,'2019-07-10 20:06:21.937106','3','(fff) (1)Bin - Pequeño > 1 -> 10.00',3,'',38,1),(225,'2019-07-10 22:53:54.885866','111111','111111 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(226,'2019-07-10 22:54:04.910594','000006','000006 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',27,1),(227,'2019-07-11 19:45:55.469925','1','Cultivos Marinos Del Sur',2,'[{\"changed\": {\"fields\": [\"nombre\", \"abreviatura\"]}}]',9,1),(228,'2019-07-12 05:01:47.241196','1','prueba1',1,'[{\"added\": {}}]',3,1),(229,'2019-07-12 05:02:08.653162','2','obek',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(230,'2019-07-12 06:33:40.111499','2','obek',2,'[{\"changed\": {\"fields\": [\"user_permissions\"]}}]',4,1),(231,'2019-07-12 06:36:03.043927','2','obek',2,'[{\"changed\": {\"fields\": [\"user_permissions\"]}}]',4,1),(232,'2019-07-12 06:37:11.611345','2','obek',2,'[{\"changed\": {\"fields\": [\"user_permissions\"]}}]',4,1),(233,'2019-07-12 06:41:44.835604','2','obek',2,'[{\"changed\": {\"fields\": [\"user_permissions\"]}}]',4,1),(234,'2019-07-12 06:56:57.761528','1','prueba1',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(235,'2019-07-12 07:42:20.532104','2','Supervisor de hielo',1,'[{\"added\": {}}]',3,1),(236,'2019-07-12 07:42:30.504919','1','1 -> Supervisor de Hielo',1,'[{\"added\": {}}]',39,1),(237,'2019-07-12 07:45:15.810965','3','nicol',1,'[{\"added\": {}}]',4,1),(238,'2019-07-12 07:45:32.476608','1234','Nicol Giron',1,'[{\"added\": {}}]',12,1),(239,'2019-07-12 07:50:59.416776','3','nicol',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(240,'2019-07-13 03:50:20.305583','3','nicol',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(241,'2019-07-14 20:19:41.155001','1','1 -> Supervisor de Hielo',2,'[{\"changed\": {\"fields\": [\"grupo\"]}}]',39,1),(242,'2019-07-14 21:53:09.439337','10','kevin5',3,'',4,1),(243,'2019-07-14 21:54:52.537370','11','kevin5',3,'',4,1),(244,'2019-07-14 22:06:23.094351','12','kevin5',3,'',4,1),(245,'2019-07-15 05:57:59.076551','1000','Kenssy Medina',2,'[{\"changed\": {\"fields\": [\"usuario\"]}}]',12,1),(246,'2019-07-15 05:59:44.147348','1000','Kenssy Medina',2,'[{\"changed\": {\"fields\": [\"usuario\"]}}]',12,1),(247,'2019-07-15 15:59:05.626243','15','NicolGiron1',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(248,'2019-07-15 16:10:14.939895','15','NicolGiron1',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(249,'2019-07-15 16:22:01.410533','3','nicol',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(250,'2019-07-15 16:22:13.816781','7','kevin2',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(251,'2019-07-15 16:22:38.177924','8','kevin3',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(252,'2019-07-15 16:34:25.364186','7','kevin2',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(253,'2019-07-15 16:34:37.385797','8','kevin3',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(254,'2019-07-15 16:34:44.664050','9','kevin4',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(255,'2019-07-15 16:34:52.573285','13','kevin5',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(256,'2019-07-15 16:35:13.061297','16','MArtyu',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(257,'2019-07-15 17:33:26.457782','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(258,'2019-07-15 17:35:27.171585','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(259,'2019-07-15 17:37:39.107531','2','Supervisor de hielo',2,'[]',3,1),(260,'2019-07-15 20:22:08.361606','4','kenssy',2,'[{\"changed\": {\"fields\": [\"is_staff\"]}}]',4,1),(261,'2019-07-15 22:59:07.273345','678956','Obek Escoto',2,'[{\"changed\": {\"fields\": [\"actualizoContrasena\"]}}]',12,1),(262,'2019-07-15 23:34:27.073803','678956','Obek Escoto',2,'[{\"changed\": {\"fields\": [\"actualizoContrasena\"]}}]',12,1),(263,'2019-07-17 19:22:59.223864','0000-0000-00001','juan molina',2,'[]',14,1),(264,'2019-07-24 03:55:24.143420','18','kenner',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]',4,1),(265,'2019-07-24 03:56:24.024313','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(266,'2019-07-24 03:58:44.939950','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(267,'2019-07-24 04:27:55.497467','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(268,'2019-07-24 04:42:36.446273','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(269,'2019-07-24 05:15:27.931864','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(270,'2019-07-24 17:46:30.475975','2','Supervisor de hielo',2,'[]',3,1),(271,'2019-07-24 18:06:25.821161','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(272,'2019-07-24 18:19:43.740248','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(273,'2019-07-24 20:48:30.523242','9','(9)Bin - Normal > 15',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',17,1),(274,'2019-07-24 20:48:39.078428','000015','000015 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(275,'2019-07-24 21:23:57.578838','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(276,'2019-07-24 21:26:10.347622','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(277,'2019-07-25 00:58:21.257055','000015','000015 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(278,'2019-07-25 00:58:34.231211','000016','000016 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(279,'2019-07-25 01:22:42.118100','000016','000016 -> CULMASA',2,'[{\"changed\": {\"fields\": [\"estadoPrestamo\"]}}]',23,1),(280,'2019-07-25 02:31:25.295878','4','(4)Bin - Pequeño > 3',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',17,1),(281,'2019-07-25 02:31:28.331377','40','000016 -> CULMASA -> la tapita',2,'[]',21,1),(282,'2019-07-25 04:54:43.735724','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(283,'2019-07-25 05:00:12.747985','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(284,'2019-07-28 15:02:43.952927','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(285,'2019-07-28 17:04:56.808466','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(286,'2019-07-28 18:20:43.830748','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(287,'2019-07-28 19:00:01.518007','2','Supervisor de hielo',2,'[]',3,1),(288,'2019-07-28 19:00:21.430602','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(289,'2019-07-28 19:33:24.555426','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(290,'2019-07-29 04:52:06.176395','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(291,'2019-07-29 05:02:41.683402','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(292,'2019-07-29 05:18:49.227048','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(293,'2019-07-29 05:41:56.416451','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(294,'2019-07-29 14:49:25.215666','3','descabezado',1,'[{\"added\": {}}]',3,1),(295,'2019-07-29 14:51:12.175012','2','2 -> Descabezado',1,'[{\"added\": {}}]',39,1),(296,'2019-07-29 14:51:12.231161','3','3 -> Descabezado',1,'[{\"added\": {}}]',39,1),(297,'2019-07-29 15:03:32.971645','3','descabezado',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(298,'2019-07-29 22:17:29.490341','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(299,'2019-07-29 23:01:25.185770','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(300,'2019-07-29 23:06:28.838456','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(301,'2019-08-01 17:06:14.778083','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(302,'2019-08-01 17:17:09.371588','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(303,'2019-08-05 08:10:04.422464','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(304,'2019-08-05 08:33:55.048691','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(305,'2019-08-05 08:53:47.491533','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(306,'2019-08-05 19:09:55.741341','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(307,'2019-08-05 19:15:36.698279','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(308,'2019-08-05 19:19:37.101451','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(309,'2019-08-05 19:40:17.790388','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(310,'2019-08-05 19:42:32.633185','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(311,'2019-08-05 19:43:54.484382','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(312,'2019-08-05 19:51:19.392613','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(313,'2019-08-05 19:51:35.358390','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(314,'2019-08-05 19:51:56.844824','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(315,'2019-08-05 20:15:44.902447','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(316,'2019-08-05 20:25:50.488890','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(317,'2019-08-05 20:32:28.353613','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(318,'2019-08-05 20:41:42.669061','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(319,'2019-08-05 20:49:31.223966','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(320,'2019-08-05 21:39:49.566454','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(321,'2019-08-06 02:11:19.785045','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(322,'2019-08-06 02:18:31.784328','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(323,'2019-08-06 02:45:07.404917','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(324,'2019-08-06 03:12:19.743433','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(325,'2019-08-06 03:37:02.521968','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(326,'2019-08-07 02:41:17.044122','18','kenner',2,'[{\"changed\": {\"fields\": [\"user_permissions\"]}}]',4,1),(327,'2019-08-07 03:19:32.866203','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(328,'2019-08-07 03:21:06.069778','2','Supervisor de hielo',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(329,'2019-09-09 21:24:27.185491','21','2  (Bin P.) ',2,'[{\"changed\": {\"fields\": [\"devuelto\"]}}]',21,1),(330,'2019-09-09 21:25:02.207439','41','3  (Bin P.) ',2,'[{\"changed\": {\"fields\": [\"devuelto\"]}}]',21,1),(331,'2019-09-09 21:25:12.233914','42','4  (Bin P.) ',2,'[{\"changed\": {\"fields\": [\"devuelto\"]}}]',21,1),(332,'2019-09-09 22:52:37.099168','46','100  (Bin G.) ',2,'[{\"changed\": {\"fields\": [\"devuelto\"]}}]',21,1),(333,'2019-09-09 22:53:04.776090','45','101  (Bin G.) ',2,'[{\"changed\": {\"fields\": [\"devuelto\"]}}]',21,1),(334,'2019-09-14 19:54:07.719569','7','Langostinos del Pacifico',3,'',9,1),(335,'2019-09-14 19:54:07.722076','6','Langostinos del Pacifico',3,'',9,1),(336,'2019-09-14 23:59:06.149590','13','Langostinos del Pacifico',3,'',9,1),(337,'2019-09-14 23:59:06.153367','12','Langostinos del Pacifico',3,'',9,1),(338,'2019-09-14 23:59:06.154499','11','Langostinos del Pacifico',3,'',9,1),(339,'2019-09-14 23:59:06.155390','10','Langostinos del Pacifico',3,'',9,1),(340,'2019-09-14 23:59:06.156216','9','Langostinos del Pacifico',3,'',9,1),(341,'2019-09-14 23:59:06.157007','8','Langostinos del Pacifico',3,'',9,1),(342,'2019-09-15 00:59:51.398367','15','Langostinos del Pacifico',3,'',9,1),(343,'2019-09-15 00:59:51.399639','14','Langostinos del Pacifico',3,'',9,1),(344,'2019-09-15 01:20:14.140261','17','Langostinos del Pacifico',3,'',9,1),(345,'2019-09-15 01:20:14.153022','16','Langostinos del Pacifico',3,'',9,1),(346,'2019-09-15 01:25:49.583238','5','Cooperativa Cafetalera Sanmarqueñas',2,'[{\"changed\": {\"fields\": [\"nombre\", \"abreviatura\"]}}]',9,1),(347,'2019-09-16 07:16:18.305715','0801-1997-16105','Javier Mendoza',3,'',14,1),(348,'2019-09-16 07:24:03.498090','0801-1997-16105','Javier Mendoza',3,'',14,1),(349,'2019-09-16 19:17:58.159790','199','Andrea Andrews',1,'[{\"added\": {}}]',12,1),(350,'2019-10-03 17:41:58.675690','30','2019-07-22',3,'',31,1),(351,'2019-10-03 17:41:58.706907','29','2019-07-21',3,'',31,1),(352,'2019-10-03 17:41:58.717541','28','2019-07-20',3,'',31,1),(353,'2019-10-12 22:25:46.127539','AAC1010','AAC1010',2,'[{\"changed\": {\"fields\": [\"disponible\"]}}]',20,1),(354,'2019-10-12 22:27:08.440000','0000-0000-00001','Juan Molina',2,'[{\"changed\": {\"fields\": [\"disponible\"]}}]',14,1),(355,'2019-10-17 01:11:59.847451','2','Venta',1,'[{\"added\": {}}]',28,1),(356,'2019-10-19 16:57:03.856505','76','101',2,'[{\"changed\": {\"fields\": [\"devuelto\", \"devueltoT\"]}}]',21,1),(357,'2019-10-19 17:21:04.638042','16','200',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',17,1),(358,'2019-10-31 08:21:32.948086','fff','fff',3,'',37,1),(359,'2019-10-31 08:21:32.965279','51101','51101',3,'',37,1),(360,'2019-10-31 08:21:32.967600','456789','456789',3,'',37,1),(361,'2019-10-31 08:21:32.970265','40000','40000',3,'',37,1),(362,'2019-10-31 08:21:32.973032','192018','192018',3,'',37,1),(363,'2019-10-31 08:21:32.976298','12346','12346',3,'',37,1),(364,'2019-10-31 08:21:32.978756','088334','088334',3,'',37,1),(365,'2019-10-31 08:21:32.981177','008856','008856',3,'',37,1),(366,'2019-10-31 08:21:32.983512','000020','000020',3,'',37,1),(367,'2019-10-31 08:28:09.831056','F8','F8',3,'',7,1),(368,'2019-10-31 08:28:09.855397','F7','F7',3,'',7,1),(369,'2019-10-31 08:28:09.858510','F6','F6',3,'',7,1),(370,'2019-10-31 08:28:09.862056','f1','f1',3,'',7,1),(371,'2019-10-31 08:28:09.864431','50','50',3,'',7,1),(372,'2019-10-31 08:28:09.868009','45','45',3,'',7,1),(373,'2019-10-31 08:28:09.872108','111','111',3,'',7,1),(374,'2019-10-31 08:28:09.876212','10','10',3,'',7,1),(375,'2019-10-31 08:28:34.284056','F14F','F14F | CAMORO',3,'',8,1),(376,'2019-10-31 08:28:34.287396','99','99 | ELME',3,'',8,1),(377,'2019-10-31 08:28:34.289767','789E','789E | SANJOS',3,'',8,1),(378,'2019-10-31 08:28:34.291972','78','78 | CADEOR',3,'',8,1),(379,'2019-10-31 08:28:34.294164','56F','56F | LAVE',3,'',8,1),(380,'2019-10-31 08:28:34.296371','45fl1','45fl1 | CMA',3,'',8,1),(381,'2019-10-31 08:28:34.299424','45fl','45fl | CMA',3,'',8,1),(382,'2019-10-31 08:28:34.302279','45F','45F | SALMA',3,'',8,1),(383,'2019-10-31 08:28:34.304551','1q2c','1q2c | cc',3,'',8,1),(384,'2019-10-31 08:28:34.306787','1q2','1q2 | acc',3,'',8,1),(385,'2019-10-31 08:28:34.309360','190','190 | LANUFI',3,'',8,1),(386,'2019-10-31 08:28:34.312123','177','177 | UFDPM',3,'',8,1),(387,'2019-10-31 08:28:34.315816','160','160 | LAMERA',3,'',8,1),(388,'2019-10-31 08:28:34.319889','113','113 | OFM',3,'',8,1),(389,'2019-10-31 08:28:34.322639','111','111 | OFP',3,'',8,1),(390,'2019-10-31 08:28:34.324781','104','104 | ELPO',3,'',8,1),(391,'2019-10-31 08:28:34.327026','101','101 | LAMISUR',3,'',8,1),(392,'2019-10-31 08:28:34.329760','100','100 | GRA',3,'',8,1),(393,'2019-10-31 08:28:34.334705','06f4','06f4 | LIT',3,'',8,1),(394,'2019-10-31 08:28:34.337399','056','056 | EMPR',3,'',8,1),(395,'2019-10-31 08:28:34.339968','05','05 | NV',3,'',8,1),(396,'2019-10-31 08:29:24.187412','2','FLETE',2,'[{\"changed\": {\"fields\": [\"tipo\"]}}]',10,1),(397,'2019-10-31 09:13:27.651521','4','TERMINADO',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',22,1),(398,'2019-10-31 09:13:39.074991','3','ASIGNADO',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',22,1),(399,'2019-10-31 09:13:48.147315','2','ANULADO',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',22,1),(400,'2019-10-31 09:13:59.026820','1','ACTIVO',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',22,1),(401,'2019-10-31 09:15:15.486456','4','Terminado',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',22,1),(402,'2019-10-31 09:15:25.703560','3','Asignado',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',22,1),(403,'2019-10-31 09:15:33.236294','2','Anulado',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',22,1),(404,'2019-10-31 09:15:40.364015','1','Activo',2,'[{\"changed\": {\"fields\": [\"estado\"]}}]',22,1),(405,'2019-10-31 09:16:45.528973','981186','981186',3,'',27,1),(406,'2019-10-31 09:16:45.532980','897066','897066',3,'',27,1),(407,'2019-10-31 09:16:45.540607','789067','789067',3,'',27,1),(408,'2019-10-31 09:16:45.555059','563413','563413',3,'',27,1),(409,'2019-10-31 09:16:45.560627','101112','101112',3,'',27,1),(410,'2019-10-31 09:16:45.565541','018199','018199',3,'',27,1),(411,'2019-10-31 09:16:45.591664','018197','018197',3,'',27,1),(412,'2019-10-31 09:16:45.595910','011111','011111',3,'',27,1),(413,'2019-10-31 09:16:45.599083','003004','003004',3,'',27,1),(414,'2019-10-31 09:16:45.602296','000998','000998',3,'',27,1),(415,'2019-10-31 09:16:45.608645','000933','000933',3,'',27,1),(416,'2019-10-31 09:16:45.612905','000123','000123',3,'',27,1),(417,'2019-10-31 09:16:45.615231','000111','000111',3,'',27,1),(418,'2019-10-31 09:16:45.617555','000078','000078',3,'',27,1),(419,'2019-10-31 09:16:45.620508','000020','000020',3,'',27,1),(420,'2019-10-31 09:16:45.623652','000010','000010',3,'',27,1),(421,'2019-10-31 09:16:45.626008','000008','000008',3,'',27,1),(422,'2019-10-31 09:16:45.628375','000007','000007',3,'',27,1),(423,'2019-10-31 09:16:45.631638','000006','000006',3,'',27,1),(424,'2019-10-31 09:16:45.635101','000004','000004',3,'',27,1),(425,'2019-10-31 09:16:45.638373','000003','000003',3,'',27,1),(426,'2019-10-31 09:16:45.640766','000002','000002',3,'',27,1),(427,'2019-10-31 09:16:45.643030','000001','000001',3,'',27,1),(428,'2019-10-31 09:18:48.263906','897870','897870',3,'',23,1),(429,'2019-10-31 09:18:48.278914','563412','563412',3,'',23,1),(430,'2019-10-31 09:18:48.282702','111111','111111',3,'',23,1),(431,'2019-10-31 09:18:48.285941','101112','101112',3,'',23,1),(432,'2019-10-31 09:18:48.289494','090901','090901',3,'',23,1),(433,'2019-10-31 09:18:48.291865','090890','090890',3,'',23,1),(434,'2019-10-31 09:18:48.295086','09019','09019',3,'',23,1),(435,'2019-10-31 09:18:48.299304','055557','055557',3,'',23,1),(436,'2019-10-31 09:18:48.302021','055556','055556',3,'',23,1),(437,'2019-10-31 09:18:48.305402','018501','018501',3,'',23,1),(438,'2019-10-31 09:18:48.307966','01001','01001',3,'',23,1),(439,'2019-10-31 09:18:48.310321','000955','000955',3,'',23,1),(440,'2019-10-31 09:18:48.318669','000922','000922',3,'',23,1),(441,'2019-10-31 09:18:48.323530','000416','000416',3,'',23,1),(442,'2019-10-31 09:18:48.327490','000055','000055',3,'',23,1),(443,'2019-10-31 09:18:48.340012','000022','000022',3,'',23,1),(444,'2019-10-31 09:18:48.348719','000019','000019',3,'',23,1),(445,'2019-10-31 09:18:48.355132','000016','000016',3,'',23,1),(446,'2019-10-31 09:18:48.362922','000015','000015',3,'',23,1),(447,'2019-10-31 09:18:48.367185','000013','000013',3,'',23,1),(448,'2019-10-31 09:18:48.370819','000012','000012',3,'',23,1),(449,'2019-10-31 09:18:48.375169','000011','000011',3,'',23,1),(450,'2019-10-31 09:18:48.380856','000002','000002',3,'',23,1),(451,'2019-10-31 09:18:48.385067','000001','000001',3,'',23,1),(452,'2019-10-31 09:19:09.442270','PCJ6462','PCJ6462',3,'',20,1),(453,'2019-10-31 09:19:09.446043','PCJ1019','PCJ1019',3,'',20,1),(454,'2019-10-31 09:19:09.449353','PCA6562','PCA6562',3,'',20,1),(455,'2019-10-31 09:19:09.452111','PCA1010','PCA1010',3,'',20,1),(456,'2019-10-31 09:19:09.455541','HCH0005','HCH0005',3,'',20,1),(457,'2019-10-31 09:19:09.459047','HCH0003','HCH0003',3,'',20,1),(458,'2019-10-31 09:19:09.462100','HCH0001','HCH0001',3,'',20,1),(459,'2019-10-31 09:19:09.464380','HCC0000','HCC0000',3,'',20,1),(460,'2019-10-31 09:19:09.466576','ACC1010','ACC1010',3,'',20,1),(461,'2019-10-31 09:19:09.468926','AAC1010','AAC1010',3,'',20,1),(462,'2019-10-31 09:19:09.472146','AAAAAAA','AAAAAAA',3,'',20,1),(463,'2019-10-31 09:20:16.262711','909090','Kenner2 Mendez2',3,'',12,1),(464,'2019-10-31 09:20:16.276549','678957','Obek Escoto Ponce',3,'',12,1),(465,'2019-10-31 09:20:16.279327','678956','Obek Escoto',3,'',12,1),(466,'2019-10-31 09:20:16.281619','51101','Kenssy Medina',3,'',12,1),(467,'2019-10-31 09:20:16.284095','23457','Nicol Giron',3,'',12,1),(468,'2019-10-31 09:20:16.287452','23456','Nicol Giron',3,'',12,1),(469,'2019-10-31 09:20:16.289835','12311','Kevin Escoto',3,'',12,1),(470,'2019-10-31 09:20:16.292321','10101','Oscar Molina',3,'',12,1),(471,'2019-10-31 09:20:16.294431','9089','Hasly Triminio',3,'',12,1),(472,'2019-10-31 09:20:16.297097','8888','Joan Rubio',3,'',12,1),(473,'2019-10-31 09:20:16.301262','5111','Prueba2 Pruebaapellido2',3,'',12,1),(474,'2019-10-31 09:20:16.304475','5110','Prueba Pruebaapellido',3,'',12,1),(475,'2019-10-31 09:20:16.308378','1360','Edgar Ordoñez',3,'',12,1),(476,'2019-10-31 09:20:16.310872','1235','Kevin Escoto',3,'',12,1),(477,'2019-10-31 09:20:16.313070','1234','Nicol escoto',3,'',12,1),(478,'2019-10-31 09:20:16.315421','1233','Kevin Escoto',3,'',12,1),(479,'2019-10-31 09:20:16.324261','1232','Kevin Escoto',3,'',12,1),(480,'2019-10-31 09:20:16.327151','1231','Kevin Escoto',3,'',12,1),(481,'2019-10-31 09:20:16.331594','1109','Prueba09 Vfgo',3,'',12,1),(482,'2019-10-31 09:20:16.334343','1108','Prueba8 Prufkfkfkfk',3,'',12,1),(483,'2019-10-31 09:20:16.337555','1107','Javier Lainez',3,'',12,1),(484,'2019-10-31 09:20:16.340838','1106','Kenssy Medina',3,'',12,1),(485,'2019-10-31 09:20:16.343342','1105','Kenssy Medina',3,'',12,1),(486,'2019-10-31 09:20:16.345628','1104','Kenssy Medina',3,'',12,1),(487,'2019-10-31 09:20:16.348375','1103','Prueba3 Apellido3',3,'',12,1),(488,'2019-10-31 09:20:16.350595','1102','Prueba2 Pellidoprueba2',3,'',12,1),(489,'2019-10-31 09:20:16.353761','1101','Prueba2 Prueba2',3,'',12,1),(490,'2019-10-31 09:20:16.355989','1015','Claudia Morales',3,'',12,1),(491,'2019-10-31 09:20:16.358479','1002','Eva Oliva2',3,'',12,1),(492,'2019-10-31 09:20:16.360786','1000','Kenssy12 Medina',3,'',12,1),(493,'2019-10-31 09:20:16.363940','878','Augusto Guardiola',3,'',12,1),(494,'2019-10-31 09:20:16.367195','812','Josue Alvarez',3,'',12,1),(495,'2019-10-31 09:20:16.370057','199','Andrea Andeouns',3,'',12,1),(496,'2019-10-31 09:20:16.373392','2','Obek escoto',3,'',12,1),(497,'2019-10-31 09:20:57.694263','7','Supervisor de hielo 3',3,'',39,1),(498,'2019-10-31 09:20:57.709151','6','Gerente',3,'',39,1),(499,'2019-10-31 09:20:57.711731','5','secretario',3,'',39,1),(500,'2019-10-31 09:20:57.713937','4','prueba Maziza',3,'',39,1),(501,'2019-10-31 09:20:57.716377','3','Descabezado',3,'',39,1),(502,'2019-10-31 09:20:57.719417','2','Descabezado',3,'',39,1),(503,'2019-10-31 09:22:18.819067','24','admin11',3,'',4,1),(504,'2019-10-31 09:22:18.832665','23','admin12',3,'',4,1),(505,'2019-10-31 09:22:18.834970','31','andrea1',3,'',4,1),(506,'2019-10-31 09:22:18.837259','36','andrea990',3,'',4,1),(507,'2019-10-31 09:22:18.840055','21','cmorales',3,'',4,1),(508,'2019-10-31 09:22:18.842435','19','Edgar_Jair',3,'',4,1),(509,'2019-10-31 09:22:18.846351','40','Eva',3,'',4,1),(510,'2019-10-31 09:22:18.849065','22','guardiola',3,'',4,1),(511,'2019-10-31 09:22:18.851214','28','javier18',3,'',4,1),(512,'2019-10-31 09:22:18.853255','18','kenner',3,'',4,1),(513,'2019-10-31 09:22:18.855370','4','kenssy',3,'',4,1),(514,'2019-10-31 09:22:18.857619','26','kenssy14',3,'',4,1),(515,'2019-10-31 09:22:18.860100','27','kenssy16',3,'',4,1),(516,'2019-10-31 09:22:18.863731','5','kenssy2',3,'',4,1),(517,'2019-10-31 09:22:18.865971','6','kevin',3,'',4,1),(518,'2019-10-31 09:22:18.868123','7','kevin2',3,'',4,1),(519,'2019-10-31 09:22:18.870349','8','kevin3',3,'',4,1),(520,'2019-10-31 09:22:18.872735','9','kevin4',3,'',4,1),(521,'2019-10-31 09:22:18.874852','13','kevin5',3,'',4,1),(522,'2019-10-31 09:22:18.876892','16','MArtyu',3,'',4,1),(523,'2019-10-31 09:22:18.879078','17','MArtyuu',3,'',4,1),(524,'2019-10-31 09:22:18.884574','3','nicol',3,'',4,1),(525,'2019-10-31 09:22:18.888584','14','NicolGiron',3,'',4,1),(526,'2019-10-31 09:22:18.891472','15','NicolGiron1',3,'',4,1),(527,'2019-10-31 09:22:18.893744','2','obek',3,'',4,1),(528,'2019-10-31 09:22:18.897065','30','prueba09',3,'',4,1),(529,'2019-10-31 09:22:18.899327','37','prueba100',3,'',4,1),(530,'2019-10-31 09:22:18.901423','38','prueba101',3,'',4,1),(531,'2019-10-31 09:22:18.903851','39','prueba103',3,'',4,1),(532,'2019-10-31 09:22:18.907419','33','prueba109',3,'',4,1),(533,'2019-10-31 09:22:18.910232','32','prueba111',3,'',4,1),(534,'2019-10-31 09:22:18.912844','25','prueba2',3,'',4,1),(535,'2019-10-31 09:22:18.915767','29','Prueba8',3,'',4,1),(536,'2019-10-31 09:22:18.918164','34','xlr8',3,'',4,1),(537,'2019-10-31 09:22:18.920601','35','xlr9',3,'',4,1),(538,'2019-10-31 09:25:42.647256','37','2019-10-29',3,'',31,1),(539,'2019-10-31 09:25:42.664703','36','2019-10-28',3,'',31,1),(540,'2019-10-31 09:25:42.667404','35','2019-10-27',3,'',31,1),(541,'2019-10-31 09:25:42.669690','34','2019-10-04',3,'',31,1),(542,'2019-10-31 09:25:42.672003','33','2019-10-03',3,'',31,1),(543,'2019-10-31 09:25:42.674170','32','2019-10-02',3,'',31,1),(544,'2019-10-31 09:25:42.676588','31','2019-08-01',3,'',31,1),(545,'2019-10-31 09:25:42.679255','27','2019-07-04',3,'',31,1),(546,'2019-10-31 09:25:42.682427','26','2019-07-05',3,'',31,1),(547,'2019-10-31 09:25:42.684699','12','2019-06-28',3,'',31,1),(548,'2019-10-31 09:25:42.687317','11','2019-06-30',3,'',31,1),(549,'2019-10-31 09:25:42.690185','10','2019-06-29',3,'',31,1),(550,'2019-10-31 09:27:03.646214','16','200',3,'',17,1),(551,'2019-10-31 09:27:03.651035','15','118',3,'',17,1),(552,'2019-10-31 09:27:03.653494','14','13',3,'',17,1),(553,'2019-10-31 09:27:03.655657','13','10',3,'',17,1),(554,'2019-10-31 09:27:03.657781','12','100',3,'',17,1),(555,'2019-10-31 09:27:03.660065','11','100',3,'',17,1),(556,'2019-10-31 09:27:03.662480','10','101',3,'',17,1),(557,'2019-10-31 09:27:03.664968','9','15',3,'',17,1),(558,'2019-10-31 09:27:03.667781','8','12',3,'',17,1),(559,'2019-10-31 09:27:03.669984','7','7',3,'',17,1),(560,'2019-10-31 09:27:03.673421','6','5',3,'',17,1),(561,'2019-10-31 09:27:03.677270','5','4',3,'',17,1),(562,'2019-10-31 09:27:03.679908','4','3',3,'',17,1),(563,'2019-10-31 09:27:03.683242','3','2',3,'',17,1),(564,'2019-10-31 09:27:03.685901','2','1',3,'',17,1),(565,'2019-10-31 09:27:03.688293','1','11',3,'',17,1),(566,'2019-10-31 09:29:01.353177','4','Cafe',1,'[{\"added\": {}}]',15,1),(567,'2019-10-31 09:29:14.062719','5','Amarillo',1,'[{\"added\": {}}]',15,1),(568,'2019-10-31 09:29:22.719731','6','Rosa',1,'[{\"added\": {}}]',15,1),(569,'2019-10-31 09:29:36.365564','7','Verde',1,'[{\"added\": {}}]',15,1),(570,'2019-10-31 09:29:55.815124','8','Gris',1,'[{\"added\": {}}]',15,1),(571,'2019-10-31 09:30:05.464889','6','Rojo',2,'[{\"changed\": {\"fields\": [\"color\"]}}]',15,1),(572,'2019-10-31 09:30:25.138181','9','Naranja',1,'[{\"added\": {}}]',15,1),(573,'2019-10-31 09:30:38.908452','10','Morado',1,'[{\"added\": {}}]',15,1),(574,'2019-10-31 09:31:10.806398','1','Asignado',2,'[]',18,1),(575,'2019-10-31 09:33:21.441933','2','Libra',1,'[{\"added\": {}}]',26,1),(576,'2019-10-31 09:35:49.694194','1','Auditor',3,'',3,1),(577,'2019-10-31 09:35:49.698496','7','Gerente',3,'',3,1),(578,'2019-10-31 09:35:49.703730','5','prueba Maziza',3,'',3,1),(579,'2019-10-31 09:35:49.706413','6','secretario',3,'',3,1),(580,'2019-10-31 09:35:49.712941','4','supervisor',3,'',3,1),(581,'2019-10-31 09:35:49.716700','8','Supervisor de hielo 3',3,'',3,1),(582,'2019-10-31 09:35:49.723391','3','Vice Gerente',3,'',3,1),(583,'2019-10-31 09:36:28.447395','26','Andrea',3,'',9,1),(584,'2019-10-31 09:36:28.452588','25','Empresa De Prueba Vehiculo 3',3,'',9,1),(585,'2019-10-31 09:36:28.455634','24','Empresa De Prueba Vehiculo 2',3,'',9,1),(586,'2019-10-31 09:36:28.457835','23','Empresa De Prueba Vehiculo',3,'',9,1),(587,'2019-10-31 09:36:28.460228','22','Empresa De Prueba 2',3,'',9,1),(588,'2019-10-31 09:36:28.462723','21','Empresa De Prueba',3,'',9,1),(589,'2019-10-31 09:36:28.465028','20','San Juan',3,'',9,1),(590,'2019-10-31 09:36:28.467499','19','San Jorge',3,'',9,1),(591,'2019-10-31 09:36:28.472724','18','Langostinos del Pacifico',3,'',9,1),(592,'2019-10-31 09:36:28.477508','5','Cooperativa Cafetalera Sanmarqueñas',3,'',9,1),(593,'2019-10-31 09:36:28.480394','4','Obek Escoto',3,'',9,1),(594,'2019-10-31 09:36:28.483581','3','Cultivos Marinos',3,'',9,1),(595,'2019-10-31 09:36:28.488947','2','CARGIL S.A',3,'',9,1),(596,'2019-10-31 09:36:28.494597','1','Cultivos Marinos Del Sur',3,'',9,1),(597,'2019-10-31 09:37:23.580600','2020-1111-11103','Agustino Joya',3,'',14,1),(598,'2019-10-31 09:37:23.595429','2020-1111-11101','Gerson Giron',3,'',14,1),(599,'2019-10-31 09:37:23.597739','1111-1111-11111','Jorge Escoto',3,'',14,1),(600,'2019-10-31 09:37:23.600748','1111-1111-11101','David Colindres',3,'',14,1),(601,'2019-10-31 09:37:23.603203','0908-1999-17105','Kevin Solorzano',3,'',14,1),(602,'2019-10-31 09:37:23.605902','0803-1997-16105','Abelino Padilla',3,'',14,1),(603,'2019-10-31 09:37:23.607982','0801-1997-17105','Jorge Escoto',3,'',14,1),(604,'2019-10-31 09:37:23.610488','0801-1997-16108','Sergio Ramirez',3,'',14,1),(605,'2019-10-31 09:37:23.613016','0801-1997-16105','Javier Mendoza',3,'',14,1),(606,'2019-10-31 09:37:23.615156','0801-1997-16100','Paola Amador',3,'',14,1),(607,'2019-10-31 09:37:23.617607','0615-1999-00410','Jhosep Ordoñez',3,'',14,1),(608,'2019-10-31 09:37:23.619984','0000-0000-00001','Juan Molina',3,'',14,1),(609,'2019-10-31 09:38:38.186240','2','Carreton',2,'[{\"changed\": {\"fields\": [\"nombre\"]}}]',19,1),(610,'2019-10-31 09:40:19.050047','2','VENTA',2,'[{\"changed\": {\"fields\": [\"movimiento\"]}}]',28,1),(611,'2019-10-31 09:40:31.930894','1','MAQUILA',2,'[{\"changed\": {\"fields\": [\"movimiento\"]}}]',28,1),(612,'2019-10-31 09:40:46.846782','3','OTRO',1,'[{\"added\": {}}]',28,1),(613,'2019-10-31 10:41:15.817805','41','kevin',2,'[{\"changed\": {\"fields\": [\"is_staff\", \"is_superuser\"]}}]',4,1),(614,'2019-10-31 13:29:31.745414','38','2019-10-31',3,'',31,1),(615,'2019-10-31 14:38:39.582224','39','2019-10-31',3,'',31,1),(616,'2019-10-31 15:01:36.142343','SVC6240','SVC6240',2,'[{\"changed\": {\"fields\": [\"disponible\"]}}]',20,1),(617,'2019-10-31 15:02:18.483263','KPL2345','KPL2345',2,'[{\"changed\": {\"fields\": [\"disponible\"]}}]',20,1),(618,'2019-10-31 15:02:25.581343','FCS3348','FCS3348',2,'[{\"changed\": {\"fields\": [\"disponible\"]}}]',20,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(37,'camaron','cosecha'),(38,'camaron','detallecosecha'),(36,'camaron','detalleentradacamaron'),(35,'camaron','entradacamaron'),(9,'compania','compania'),(8,'compania','finca'),(7,'compania','laguna'),(10,'compania','tipocompania'),(14,'conductor','conductor'),(5,'contenttypes','contenttype'),(39,'empleado','cargo'),(12,'empleado','empleado'),(11,'empleado','permiso'),(13,'empleado','tipoempleado'),(19,'equipo','baseequipo'),(15,'equipo','color'),(17,'equipo','equipo'),(18,'equipo','estado'),(16,'equipo','tamano'),(32,'hielo_proceso','departamentoproceso'),(34,'hielo_proceso','detallehieloproceso'),(31,'hielo_proceso','hieloproceso'),(30,'hielo_proceso','recipiente'),(33,'hielo_proceso','recipientedetallehieloproceso'),(21,'prestamos','detalleprestamoequipo'),(22,'prestamos','estadoprestamo'),(23,'prestamos','prestamoequipo'),(25,'remision','detalleremision'),(29,'remision','estadoremision'),(24,'remision','hielo'),(26,'remision','medida'),(27,'remision','remision'),(28,'remision','tiporemision'),(6,'sessions','session'),(20,'vehiculo','vehiculo');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-04-05 17:42:17.305087'),(2,'auth','0001_initial','2019-04-05 17:42:17.424403'),(3,'admin','0001_initial','2019-04-05 17:42:17.672020'),(4,'admin','0002_logentry_remove_auto_add','2019-04-05 17:42:17.770391'),(5,'admin','0003_logentry_add_action_flag_choices','2019-04-05 17:42:17.783402'),(6,'contenttypes','0002_remove_content_type_name','2019-04-05 17:42:17.865402'),(7,'auth','0002_alter_permission_name_max_length','2019-04-05 17:42:17.903898'),(8,'auth','0003_alter_user_email_max_length','2019-04-05 17:42:17.955370'),(9,'auth','0004_alter_user_username_opts','2019-04-05 17:42:17.967311'),(10,'auth','0005_alter_user_last_login_null','2019-04-05 17:42:18.009201'),(11,'auth','0006_require_contenttypes_0002','2019-04-05 17:42:18.012970'),(12,'auth','0007_alter_validators_add_error_messages','2019-04-05 17:42:18.026304'),(13,'auth','0008_alter_user_username_max_length','2019-04-05 17:42:18.083646'),(14,'auth','0009_alter_user_last_name_max_length','2019-04-05 17:42:18.134955'),(15,'auth','0010_alter_group_name_max_length','2019-04-05 17:42:18.178569'),(16,'auth','0011_update_proxy_permissions','2019-04-05 17:42:18.189336'),(17,'sessions','0001_initial','2019-04-05 17:42:18.204885'),(18,'compania','0001_initial','2019-04-08 15:26:00.092366'),(19,'compania','0002_auto_20190408_1544','2019-04-08 15:46:18.889868'),(20,'empleado','0001_initial','2019-04-08 16:02:58.458175'),(21,'conductor','0001_initial','2019-04-08 16:38:32.896449'),(22,'equipo','0001_initial','2019-04-08 17:03:05.032451'),(23,'vehiculo','0001_initial','2019-04-08 17:17:06.847022'),(24,'prestamos','0001_initial','2019-04-08 17:48:59.029906'),(25,'remision','0001_initial','2019-04-08 19:56:48.699282'),(26,'equipo','0002_auto_20190409_0846','2019-04-09 14:46:54.291102'),(27,'remision','0002_auto_20190409_0846','2019-04-09 14:46:54.589305'),(28,'equipo','0003_auto_20190409_1026','2019-04-09 16:26:31.881201'),(29,'compania','0003_compania_estado','2019-05-02 18:39:41.714956'),(30,'equipo','0004_auto_20190502_1239','2019-05-02 18:39:41.876284'),(31,'compania','0004_auto_20190507_1402','2019-05-07 20:02:36.378894'),(32,'prestamos','0002_auto_20190508_1520','2019-05-08 21:20:43.856406'),(33,'remision','0003_auto_20190523_1118','2019-05-23 17:18:43.096851'),(34,'remision','0004_auto_20190529_1611','2019-05-29 22:32:04.235763'),(35,'remision','0005_auto_20190529_1613','2019-05-29 22:32:04.242155'),(36,'remision','0006_auto_20190529_1614','2019-05-29 22:32:04.245836'),(37,'remision','0007_remision_estado','2019-05-29 22:32:04.249993'),(38,'remision','0008_auto_20190529_1628','2019-05-29 22:32:04.255669'),(39,'remision','0009_auto_20190529_1633','2019-05-29 22:33:46.888754'),(40,'remision','0010_auto_20190529_1643','2019-05-29 22:43:13.887524'),(41,'prestamos','0003_auto_20190612_1452','2019-06-12 20:53:05.734444'),(42,'remision','0011_remision_observacion','2019-06-26 23:49:43.409549'),(43,'hielo_proceso','0001_initial','2019-06-27 20:04:52.039735'),(44,'hielo_proceso','0002_auto_20190627_1415','2019-06-27 20:15:11.025288'),(45,'hielo_proceso','0003_auto_20190627_1415','2019-06-27 20:15:54.627041'),(46,'hielo_proceso','0004_auto_20190627_1435','2019-06-27 20:35:40.645758'),(47,'hielo_proceso','0005_auto_20190627_1451','2019-06-27 20:51:29.238294'),(48,'hielo_proceso','0006_auto_20190628_1932','2019-06-29 01:32:27.366919'),(49,'hielo_proceso','0007_auto_20190628_2007','2019-06-29 02:07:51.746894'),(50,'hielo_proceso','0008_auto_20190628_2030','2019-06-29 02:30:55.433742'),(51,'hielo_proceso','0009_auto_20190629_0923','2019-06-29 15:24:00.015915'),(52,'hielo_proceso','0010_detallehieloproceso_carreton_blanco','2019-06-29 15:29:27.368425'),(53,'hielo_proceso','0011_auto_20190629_1129','2019-06-29 17:29:21.372590'),(54,'hielo_proceso','0012_auto_20190702_1045','2019-07-02 16:46:04.584195'),(55,'hielo_proceso','0013_auto_20190702_1101','2019-07-02 17:02:10.721477'),(56,'hielo_proceso','0014_auto_20190706_1919','2019-07-07 01:19:23.158161'),(57,'camaron','0001_initial','2019-07-07 05:22:18.180229'),(58,'camaron','0002_auto_20190707_0045','2019-07-07 06:59:12.221402'),(59,'camaron','0003_remove_cosecha_finca','2019-07-07 07:02:20.921102'),(60,'camaron','0004_auto_20190708_1000','2019-07-08 16:00:28.461913'),(61,'remision','0012_auto_20190712_0030','2019-07-12 06:30:33.006314'),(62,'remision','0013_auto_20190712_0032','2019-07-12 06:32:41.821062'),(63,'empleado','0002_auto_20190712_0115','2019-07-12 07:35:57.424232'),(64,'empleado','0003_auto_20190712_0135','2019-07-12 07:35:57.558543'),(65,'empleado','0004_auto_20190712_1338','2019-07-12 23:20:52.072215'),(66,'empleado','0005_auto_20190712_1707','2019-07-12 23:20:52.431783'),(67,'empleado','0006_auto_20190712_2203','2019-07-13 04:20:51.356229'),(68,'empleado','0007_auto_20190712_2225','2019-07-13 04:26:16.142674'),(69,'empleado','0008_auto_20190713_2200','2019-07-14 04:00:24.953915'),(70,'empleado','0009_auto_20190714_0023','2019-07-14 06:23:21.847662'),(71,'empleado','0010_auto_20190714_1130','2019-07-14 17:31:13.649985'),(72,'empleado','0011_auto_20190714_1552','2019-07-14 21:52:44.462135'),(73,'empleado','0012_auto_20190715_1115','2019-07-15 17:16:05.946329'),(74,'vehiculo','0002_auto_20190717_0022','2019-07-17 06:22:38.188315'),(75,'vehiculo','0003_auto_20190717_0628','2019-07-17 12:29:04.768515'),(76,'vehiculo','0004_auto_20190717_0648','2019-07-17 12:48:55.707290'),(77,'conductor','0002_auto_20190717_1136','2019-07-17 17:36:22.049841'),(78,'remision','0014_auto_20190723_2219','2019-07-24 04:22:58.736416'),(79,'prestamos','0004_auto_20190724_1407','2019-07-24 20:07:30.108856'),(80,'camaron','0005_auto_20190725_2217','2019-07-26 04:17:24.950162'),(81,'hielo_proceso','0015_auto_20190728_1316','2019-07-28 19:16:27.623092'),(82,'hielo_proceso','0016_auto_20190728_1753','2019-07-28 23:54:09.208374'),(83,'equipo','0005_auto_20190731_1514','2019-07-31 21:14:36.116750'),(84,'equipo','0006_auto_20190731_2104','2019-08-01 03:04:34.751256'),(85,'compania','0005_auto_20190801_1649','2019-08-01 22:49:58.136365'),(86,'compania','0006_auto_20190805_0249','2019-08-05 08:50:11.653169'),(87,'conductor','0003_auto_20190805_1455','2019-08-05 20:55:26.807761'),(88,'empleado','0013_auto_20190806_2112','2019-08-07 03:12:23.100534'),(89,'vehiculo','0005_auto_20190809_1314','2019-08-09 19:16:21.030791'),(90,'vehiculo','0006_auto_20190809_1315','2019-08-09 19:16:21.057397'),(91,'prestamos','0005_detalleprestamoequipo_devuelto','2019-09-09 21:22:28.317053'),(92,'prestamos','0006_auto_20190909_1525','2019-09-09 21:25:46.385559'),(93,'compania','0007_auto_20190914_1923','2019-09-15 01:25:57.849287'),(94,'prestamos','0007_detalleprestamoequipo_tapa','2019-10-09 23:06:44.404657'),(95,'prestamos','0008_remove_detalleprestamoequipo_tapa','2019-10-09 23:09:35.352543'),(96,'prestamos','0009_auto_20191009_1724','2019-10-09 23:50:36.563409'),(97,'prestamos','0010_remove_detalleprestamoequipo_tapadera','2019-10-09 23:50:36.796180'),(98,'prestamos','0011_detalleprestamoequipo_tapadera','2019-10-10 00:04:23.736841'),(99,'conductor','0004_conductor_disponible','2019-10-11 16:59:22.207382'),(100,'vehiculo','0007_vehiculo_disponible','2019-10-12 22:02:51.187607'),(101,'prestamos','0012_detalleprestamoequipo_devueltot','2019-10-15 03:31:21.658497'),(102,'remision','0015_auto_20191019_1309','2019-10-19 19:10:15.124744'),(103,'camaron','0006_auto_20191021_2100','2019-10-22 03:02:19.156662'),(104,'equipo','0007_auto_20191030_2030','2019-10-30 20:30:53.304469');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `session_data` longtext COLLATE utf8_spanish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('06ssdfq088s27vo02riwovs9inrx1h02','ODdlODc0NzlkMmRmNGE4ZDljOWU5NWEwNGEyMWUwMTk0MTdkOTVmMjp7fQ==','2019-04-22 15:46:37.395092'),('08jrs18v7mcqptv47uzir1921e3ct3bg','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-08-12 17:04:00.913711'),('0w5w42t9h114hmib6kio3gmdahz6qsl8','ODdlODc0NzlkMmRmNGE4ZDljOWU5NWEwNGEyMWUwMTk0MTdkOTVmMjp7fQ==','2019-04-19 23:00:21.338089'),('2f9yrnptxv0gznk4e5gz39gqfw7as188','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-08-14 22:26:27.708714'),('2ybdb99qhf437l89ozrn9t7h4qsojybi','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-16 20:36:17.405795'),('33hrwzuw15q4cto9z3d19ls5hz4d3xhw','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-04-22 21:42:04.141628'),('3ibpa8judhylsn0wkj60r5qsm4tfox7q','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-06-05 17:58:42.018536'),('47zv58v28jt6jqyywrr66utcpsric4cp','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-11-14 10:38:09.630406'),('4byahamaapaa3omntre4hqi9s8i3swg0','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-04-26 22:34:06.283642'),('68zq7vpf6df4vygr49d4jfcz5mqpv3uf','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-07-09 04:38:52.946389'),('6fbc8huo1decy7rny8ok5qiu0zkcwr45','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-07-29 21:17:03.583615'),('6greq08jjs015rsu10qxqd88637xm2gm','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-16 20:01:30.484273'),('6ymceqccldyl5gl0c0l07ssw0l71x216','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-04-26 16:01:25.073893'),('74ywvztb8znq95w9ieat36xdvnxjhko1','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-09-12 17:42:56.669111'),('789z4ryuucinh0jv9mle0xuxoqe5ef2a','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-07-31 06:25:43.045410'),('7m2nx1ig2cjc57yaaj1ixqs9dv2r3479','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-16 19:27:15.797903'),('8x4gv1r66i5e3wbp07oegyf05guoav50','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-08-07 04:41:05.392972'),('9ecxvb3v55mrslgypm8kofhj2s6yop3e','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-06-07 15:47:36.065767'),('9ljlxetn1oosj58meee7xaaeykdtu4yo','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-08-16 21:25:28.917026'),('ag2c0p7y2w9d19m0lfu5j5fnmfglj7q9','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-08-13 04:09:31.991356'),('ajql356vlnzp23vb5nm8b5g88k12kz3c','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-08-13 15:53:09.638237'),('aqq2428t2wd4jvxde3obnn0h8zp0j9t8','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-10-21 21:54:34.838146'),('b6sjkyzxhu644c1z52tzfdhsn4danb8k','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-04-22 23:05:22.910769'),('bn77mru6x5klfk5g830uvohlsgr7pd5y','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-07-11 02:42:49.735848'),('ctawb612fupdls1ch0agv0xee293n1sx','ZDVhM2RlODc5ZmMwZjJmMjFlYmExMWQxOTM1NDkzYWQ4MjAyYTc5Nzp7Il9hdXRoX3VzZXJfaWQiOiIxOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2VkODk1MDA5NzUyYmQxOTA1MzFiODRmZmM4Y2IzZjQ4MGZiY2VkZiJ9','2019-08-12 19:18:41.973798'),('einyfl1u77y6tm8dgbov4itybet01t8j','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-06-18 14:18:17.549503'),('eztexg0hp0k7pbhcu85wk7gtaa3yjipe','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-07-31 15:20:31.714642'),('f5kmiacund7ktjjcxmxuc9npwr9iwim9','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-16 20:06:18.256831'),('f7z9kuxfirq9ylw34eiyrk6f7gd23vrx','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-08-12 15:03:13.279749'),('f9wm99imayo5g6y7yz83wgcl1vs7ri12','ODdlODc0NzlkMmRmNGE4ZDljOWU5NWEwNGEyMWUwMTk0MTdkOTVmMjp7fQ==','2019-07-27 04:35:14.221393'),('fhxjudt1vms442gd1h1wz0fd5ocbv60k','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-07-02 17:12:52.379613'),('frjwee19nnehog08zvmdj1sasi7fhr9m','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-10-01 20:49:18.191066'),('g1oj5wgagxshxdjp25ogam0cgnoq5kak','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-07-09 01:07:15.752621'),('gi0cyst6ogxoso1820o1s8hptj25ne2n','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-07-06 21:42:17.120995'),('gif9oi7wvzeou0cnvpgjk8awna7h9uz9','ODdlODc0NzlkMmRmNGE4ZDljOWU5NWEwNGEyMWUwMTk0MTdkOTVmMjp7fQ==','2019-04-19 23:03:57.185561'),('gu8lew4qybsktp03556k6hravejnlxm8','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-08-21 08:21:29.106682'),('gxo8efnzqr26th02sis893lkioo3nqau','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-16 20:27:06.799473'),('h19ej8nppugnmigk4mldb52suf597l7z','ZDA5YzU2YTE4NDg5NWNkY2Y2MzUzZTE0MDEyYTc0Zjc4MzIyYTY2NDp7Il9hdXRoX3VzZXJfaWQiOiI0MSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODYwMzZjNzhiNTUzYzEwZmQzYTNiMTllYzhhODRkNThmMGIxMjdlMSJ9','2019-11-14 11:08:59.075871'),('i3echng64g1aus9l3wbrxu9qlzp3tn1c','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-04-26 15:10:31.104050'),('is4urifqnkk9avrmeaed5509ipdqye2a','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-08-13 02:33:22.309507'),('j2oscpf341chetyb0owvzyy5aket9tzz','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-30 20:37:49.397835'),('jsobic3ek794rkpqq7ugc3020njwbyg8','ODdlODc0NzlkMmRmNGE4ZDljOWU5NWEwNGEyMWUwMTk0MTdkOTVmMjp7fQ==','2019-04-22 16:25:02.524026'),('kfl1luzhi1yoyd729tfd7f8m6v8od3y6','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-13 20:11:19.446415'),('l1e31i1itbnepyqibkm5978o3bnz5yu0','ZDVhM2RlODc5ZmMwZjJmMjFlYmExMWQxOTM1NDkzYWQ4MjAyYTc5Nzp7Il9hdXRoX3VzZXJfaWQiOiIxOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2VkODk1MDA5NzUyYmQxOTA1MzFiODRmZmM4Y2IzZjQ4MGZiY2VkZiJ9','2019-08-12 14:35:26.619891'),('l1vc4de57mkdngws5frlovgacu0ujs1g','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-09-04 20:12:46.998764'),('l601dsa6k0aei9nrs7uzzf1i71g72txk','ODdlODc0NzlkMmRmNGE4ZDljOWU5NWEwNGEyMWUwMTk0MTdkOTVmMjp7fQ==','2019-04-22 16:23:49.355573'),('lv6bu413ttk92tv3ruokexcmb07ugvmh','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-14 21:00:03.926279'),('lv90tcxmy3858c24aid3lt3h0cp003cz','YTBkOTgyODk5ZTkzNDc4MmMwZWY5OGE3Y2U2NGY0ODllZDcxMTY3Zjp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmQ2MWMyOTk0YzhkY2M3MDNmY2U5MWU2ZWRlNjY2Nzg2OTU4MWE3YSJ9','2019-08-12 19:22:51.540375'),('m6ev7ufjwej0w94ajsuh98f7mgof3abb','ODdlODc0NzlkMmRmNGE4ZDljOWU5NWEwNGEyMWUwMTk0MTdkOTVmMjp7fQ==','2019-07-30 00:35:45.633242'),('mmd0yeycohirvxmnhhc9ojl7mu6kv7au','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-16 18:40:11.747889'),('ms6ubp54n1stqk3983626l24o1isy6co','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-09-17 20:43:11.217978'),('muzb4ctht03ft51lhr2dqtm6s09hzrre','ZDVhM2RlODc5ZmMwZjJmMjFlYmExMWQxOTM1NDkzYWQ4MjAyYTc5Nzp7Il9hdXRoX3VzZXJfaWQiOiIxOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2VkODk1MDA5NzUyYmQxOTA1MzFiODRmZmM4Y2IzZjQ4MGZiY2VkZiJ9','2019-08-21 05:22:12.866366'),('n9po8u5e57s590oqq6yp63yj0vzrf9qm','ZDVhM2RlODc5ZmMwZjJmMjFlYmExMWQxOTM1NDkzYWQ4MjAyYTc5Nzp7Il9hdXRoX3VzZXJfaWQiOiIxOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2VkODk1MDA5NzUyYmQxOTA1MzFiODRmZmM4Y2IzZjQ4MGZiY2VkZiJ9','2019-08-23 18:15:32.223586'),('o05esfmxg1m6h717f2x8q6ivx7mm7u42','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-16 20:25:35.083867'),('o5872boufe0op90zlcglwqx2saqes6gg','ODdlODc0NzlkMmRmNGE4ZDljOWU5NWEwNGEyMWUwMTk0MTdkOTVmMjp7fQ==','2019-04-22 16:19:04.680416'),('op3dzzmqmjjdr41pfgrk8wux0bkk36g4','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-06-05 03:08:10.044374'),('pn3hchaf4ipmcpp585wk3mfyh2xnec4d','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-04-23 22:59:13.013927'),('ppjkd00jnnpo8j3v5hs9ayezlv2wlw09','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-04-23 20:01:18.324370'),('qchbkx99n4gcv6mppm371wmcq040wlqd','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-08-13 15:58:12.015049'),('r9pbpozqq6x0h71ai4852p8i8xgwbq1z','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-10-23 23:45:28.643495'),('rlp6hmke26lqs7r3k5pdqs8c28a5vd0w','ODdlODc0NzlkMmRmNGE4ZDljOWU5NWEwNGEyMWUwMTk0MTdkOTVmMjp7fQ==','2019-07-29 20:21:01.398816'),('rnmwdnot22j3om0uxq5kdiek416gx6cx','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-04-26 15:25:07.117015'),('rsg1vi9qqy67g2w5d8rn5bofzjmfpk7u','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-13 19:15:44.742057'),('rz507unqw70g7ngkyggjoqg91n0jppus','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-20 18:20:08.838659'),('s5gf3uxi1659b9fped4gb24tt2o6hi7i','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-09-18 19:07:37.469110'),('s6taralgki21b2g0sh0p3r6f83vxj2n6','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-06-07 17:42:11.236741'),('sxdcj702jbkpt21zc8595j7imvble0pr','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-07-09 16:27:44.600584'),('u7q233rwo903fwg3sv751vac6y2dx4q6','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-07-09 21:59:17.923338'),('ug5ef1s2unn0aixkd8a566trx57rczhh','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-04-23 17:24:55.537986'),('veihdletw5qswukr5nfr70tytqed7sw2','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-07-26 06:55:01.915330'),('vmn64dw44md9j7q59a6j1qpzsq4lyys4','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-09-05 18:56:21.643265'),('vtdmjbe4zkpfcukh4nkcn5xt03qvwfgd','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-13 15:24:25.317252'),('vuhnxjyjoo5pebsbre9h2yub6fj62f6r','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-06-08 16:13:23.009510'),('vuuxeg119seavgyg490oaqmsa3vmjoip','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-06-06 22:51:37.300716'),('w3d6qtk6fuk6xqxhsqcu3vxi0mhy5eah','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-07-06 22:38:34.619500'),('wmaxbtmxmzyg8uvf7kpo6u23e6br2f36','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-08-15 21:45:01.324989'),('ye7xmna6ph8lqb4u6afzmfzdgi21p8bi','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-16 20:34:50.993505'),('yzwv894fen7xnvhonoo59igm3cm75yo6','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-06-05 20:54:10.595529'),('zi3q7r46dkzr8538i16pk6qbmttjfjlz','NTdlOGQzMjQxNDZlNTEyMGNiMDBlZTAzODAyNmNmZDU0MDg1YTk0Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmYTBhNGIxNDc1ZTI2MzMzMGZlY2Q2NTcyMWFkMTEyNmZjYmU2ZjVmIn0=','2019-05-14 22:12:33.889679');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado_cargo`
--

DROP TABLE IF EXISTS `empleado_cargo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `empleado_cargo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cargo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `grupo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `empleado_cargo_grupo_id_a2ff8bf6_fk_auth_group_id` (`grupo_id`),
  CONSTRAINT `empleado_cargo_grupo_id_a2ff8bf6_fk_auth_group_id` FOREIGN KEY (`grupo_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado_cargo`
--

LOCK TABLES `empleado_cargo` WRITE;
/*!40000 ALTER TABLE `empleado_cargo` DISABLE KEYS */;
INSERT INTO `empleado_cargo` VALUES (1,'Supervisor de hielo',2),(8,'Gerente de operaciones',9);
/*!40000 ALTER TABLE `empleado_cargo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado_empleado`
--

DROP TABLE IF EXISTS `empleado_empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `empleado_empleado` (
  `codEmpleado` int(11) NOT NULL,
  `identidad` varchar(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `nombre` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(9) COLLATE utf8_spanish_ci NOT NULL,
  `actualizoContrasena` tinyint(1) NOT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `cargo_id` int(11) NOT NULL,
  `apellido` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `segundoApellido` varchar(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `segundoNombre` varchar(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`codEmpleado`),
  UNIQUE KEY `usuario_id` (`usuario_id`),
  KEY `empleado_empleado_cargo_id_bb586569_fk_empleado_cargo_id` (`cargo_id`),
  CONSTRAINT `empleado_empleado_cargo_id_bb586569_fk_empleado_cargo_id` FOREIGN KEY (`cargo_id`) REFERENCES `empleado_cargo` (`id`),
  CONSTRAINT `empleado_empleado_usuario_id_f52cee6d_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado_empleado`
--

LOCK TABLES `empleado_empleado` WRITE;
/*!40000 ALTER TABLE `empleado_empleado` DISABLE KEYS */;
INSERT INTO `empleado_empleado` VALUES (1,'0801-1997-17105','Jorge','94763554',1,1,1,'escoto',NULL,NULL),(118,'0611198900693','Maryori','',1,20,1,'Burke','Ortiz','yanini'),(801,'0801-1999-16298','Kevin','9596-7567',1,41,1,'Escoto','Ponce','Abel');
/*!40000 ALTER TABLE `empleado_empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipo_baseequipo`
--

DROP TABLE IF EXISTS `equipo_baseequipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `equipo_baseequipo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipo_baseequipo`
--

LOCK TABLES `equipo_baseequipo` WRITE;
/*!40000 ALTER TABLE `equipo_baseequipo` DISABLE KEYS */;
INSERT INTO `equipo_baseequipo` VALUES (1,'Bin'),(2,'Carretón'),(3,'Canasta'),(4,'Tapadera');
/*!40000 ALTER TABLE `equipo_baseequipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipo_color`
--

DROP TABLE IF EXISTS `equipo_color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `equipo_color` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `color` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipo_color`
--

LOCK TABLES `equipo_color` WRITE;
/*!40000 ALTER TABLE `equipo_color` DISABLE KEYS */;
INSERT INTO `equipo_color` VALUES (1,'Blanco'),(2,'Negro'),(3,'Azul'),(4,'Cafe'),(5,'Amarillo'),(6,'Rojo'),(7,'Verde'),(8,'Gris'),(9,'Naranja'),(10,'Morado');
/*!40000 ALTER TABLE `equipo_color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipo_equipo`
--

DROP TABLE IF EXISTS `equipo_equipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `equipo_equipo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero` int(10) unsigned NOT NULL,
  `codigo_barras` varchar(160) COLLATE utf8_spanish_ci DEFAULT NULL,
  `informacion` longtext COLLATE utf8_spanish_ci,
  `estado_id` int(11) NOT NULL,
  `color_id` int(11) NOT NULL,
  `nombre_id` int(11) NOT NULL,
  `tamano_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo_barras` (`codigo_barras`),
  KEY `equipo_equipo_color_id_8895e078_fk_equipo_color_id` (`color_id`),
  KEY `equipo_equipo_nombre_id_06f31cb7_fk_equipo_baseequipo_id` (`nombre_id`),
  KEY `equipo_equipo_estado_id_c677b784_fk_equipo_estado_id` (`estado_id`),
  KEY `equipo_equipo_tamano_id_6783c29f_fk_equipo_tamano_id` (`tamano_id`),
  CONSTRAINT `equipo_equipo_color_id_8895e078_fk_equipo_color_id` FOREIGN KEY (`color_id`) REFERENCES `equipo_color` (`id`),
  CONSTRAINT `equipo_equipo_estado_id_c677b784_fk_equipo_estado_id` FOREIGN KEY (`estado_id`) REFERENCES `equipo_estado` (`id`),
  CONSTRAINT `equipo_equipo_nombre_id_06f31cb7_fk_equipo_baseequipo_id` FOREIGN KEY (`nombre_id`) REFERENCES `equipo_baseequipo` (`id`),
  CONSTRAINT `equipo_equipo_tamano_id_6783c29f_fk_equipo_tamano_id` FOREIGN KEY (`tamano_id`) REFERENCES `equipo_tamano` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipo_equipo`
--

LOCK TABLES `equipo_equipo` WRITE;
/*!40000 ALTER TABLE `equipo_equipo` DISABLE KEYS */;
INSERT INTO `equipo_equipo` VALUES (17,1,'EQEL-1-01-1-3-1','',1,3,1,1),(18,2,'EQEL-1-02-1-5-1','',1,5,1,1),(19,3,'EQEL-1-3-1-3-1','',1,3,1,1),(20,4,'EQEL-1-4-1-3-1','',1,3,1,1),(21,6,'EQEL-1-6-1-3-1','',1,3,1,1),(22,5,'EQEL-1-5-2-5-1','',1,5,1,2),(23,7,'EQEL-1-7-3-3-1','',1,3,1,3),(24,8,'EQEL-1-8-1-3-1','',1,3,1,1),(25,9,'EQEL-1-9-3-5-1','',1,5,1,3),(26,10,'EQEL-1-10-2-3-1','',1,3,1,2),(27,11,'EQEL-1-11-1-3-1','',1,3,1,1),(28,12,'EQEL-1-12-3-5-1','',1,5,1,3),(29,13,'EQEL-1-13-3-5-1','',1,5,1,3),(30,14,'EQEL-1-14-3-3-1','',1,3,1,3),(31,15,'EQEL-1-15-3-3-1','',1,3,1,3),(32,16,'EQEL-1-16-1-5-1','',2,5,1,1),(33,17,'EQEL-1-17-2-5-1','',2,5,1,2),(34,18,'EQEL-1-18-2-5-1','',2,5,1,2),(35,19,'EQEL-1-19-3-3-1','',2,3,1,3),(36,20,'EQEL-1-20-1-3-1','',2,3,1,1),(40,21,'EQEL-1-21-2-3-1','',2,3,1,2),(41,22,'EQEL-1-22-3-5-1','',2,5,1,3),(42,23,'EQEL-1-23-1-5-1','',2,5,1,1),(43,24,'EQEL-1-24-2-3-1','',2,3,1,2),(44,25,'EQEL-1-25-1-3-1','',2,3,1,1),(45,26,'EQEL-1-26-2-5-1','',2,5,1,2),(46,27,'EQEL-1-27-3-3-1','',2,3,1,3),(47,28,'EQEL-1-28-1-5-1','',2,5,1,1),(48,29,'EQEL-1-29-1-5-1','',2,5,1,1),(49,30,'EQEL-1-30-3-3-1','',2,3,1,3),(50,31,'EQEL-1-31-1-3-1','',2,3,1,1),(51,32,'EQEL-1-32-1-5-1','',2,5,1,1),(52,33,'EQEL-1-33-3-5-1','',2,5,1,3),(53,34,'EQEL-1-34-1-5-1','',2,5,1,1),(54,35,'EQEL-1-35-3-3-1','',2,3,1,3),(55,36,'EQEL-1-36-1-3-1','',2,3,1,1),(56,37,'EQEL-1-37-1-5-1','',2,5,1,1),(57,38,'EQEL-1-38-1-3-1','',2,3,1,1),(58,39,'EQEL-1-39-3-3-1','',2,3,1,3),(59,40,'EQEL-1-40-1-3-1','',2,3,1,1),(60,41,'EQEL-1-41-3-3-1','',2,3,1,3),(61,42,'EQEL-1-42-1-3-1','',2,3,1,1),(62,43,'EQEL-1-43-3-5-1','',2,5,1,3),(63,44,'EQEL-1-44-1-3-1','',2,3,1,1),(64,45,'EQEL-1-45-1-3-1','',2,3,1,1),(65,46,'EQEL-1-46-3-5-1','',2,5,1,3),(66,47,'EQEL-1-47-3-3-1','',2,3,1,3),(67,48,'EQEL-1-48-1-3-1','',2,3,1,1),(68,49,'EQEL-1-49-1-3-1','',2,3,1,1),(69,50,'EQEL-1-50-1-5-1','',2,5,1,1),(70,50,'EQEL-4-50-1-3-1','',2,3,4,1),(71,1,'EQEL-4-1-1-3-1','',1,3,4,1),(72,2,'EQEL-4-2-1-3-1','',1,3,4,1),(73,3,'EQEL-4-3-1-5-1','',1,5,4,1),(74,4,'EQEL-4-4-2-5-1','',1,5,4,2),(75,5,'EQEL-4-5-3-3-1','',1,3,4,3),(76,6,'EQEL-4-6-2-5-1','',1,5,4,2),(77,7,'EQEL-4-7-1-5-1','',1,5,4,1),(78,8,'EQEL-4-8-2-5-1','',1,5,4,2),(79,9,'EQEL-4-9-3-3-1','',1,3,4,3),(80,10,'EQEL-4-10-1-3-1','',1,3,4,1),(81,11,'EQEL-4-11-3-5-1','',1,5,4,3),(82,12,'EQEL-4-12-1-3-1','',1,3,4,1),(83,13,'EQEL-4-13-2-3-1','',1,3,4,2),(85,14,'EQEL-4-14-2-3-1','',1,3,4,2),(86,15,'EQEL-4-15-3-5-1','',1,5,4,3),(87,16,'EQEL-4-16-1-3-1','',2,3,4,1),(88,17,'EQEL-4-17-1-3-1','',2,3,4,1),(89,18,'EQEL-4-18-3-3-1','',2,3,4,3),(90,19,'EQEL-4-19-3-3-1','',2,3,4,3),(91,20,'EQEL-4-20-1-5-1','',2,5,4,1),(92,21,'EQEL-4-21-1-5-1','',2,5,4,1),(93,22,'EQEL-4-22-3-3-1','',2,3,4,3),(94,23,'EQEL-4-23-1-3-1','',2,3,4,1),(95,24,'EQEL-4-24-3-3-1','',2,3,4,3),(96,25,'EQEL-4-25-1-5-1','',2,5,4,1),(97,26,'EQEL-4-26-1-5-1','',2,5,4,1),(98,27,'EQEL-4-27-3-5-1','',2,5,4,3),(99,28,'EQEL-4-28-2-5-1','',2,5,4,2),(100,29,'EQEL-4-29-1-5-1','',2,5,4,1),(102,30,'EQEL-4-30-1-5-1','',2,5,4,1),(103,31,'EQEL-4-31-1-3-1','',2,3,4,1),(104,32,'EQEL-4-32-3-5-1','',2,5,4,3),(105,33,'EQEL-4-33-1-3-1','',2,3,4,1),(106,34,'EQEL-4-34-2-5-1','',2,5,4,2),(108,35,'EQEL-4-35-2-5-1','',2,5,4,2),(109,36,'EQEL-4-36-2-3-1','',2,3,4,2),(110,37,'EQEL-4-37-1-5-1','',2,5,4,1),(111,38,'EQEL-4-38-1-3-1','',2,3,4,1),(112,39,'EQEL-4-39-1-5-1','',2,5,4,1),(113,40,'EQEL-4-40-3-5-1','',2,5,4,3),(114,41,'EQEL-4-41-2-5-1','',2,5,4,2),(115,42,'EQEL-4-42-3-5-1','',2,5,4,3),(116,43,'EQEL-4-43-1-5-1','',2,5,4,1),(118,44,'EQEL-4-44-1-5-1','',2,5,4,1),(119,45,'EQEL-4-45-3-3-1','',2,3,4,3),(120,46,'EQEL-4-46-3-3-1','',2,3,4,3),(122,47,'EQEL-4-47-3-3-1','',2,3,4,3),(123,48,'EQEL-4-48-2-3-1','',2,3,4,2),(125,49,'EQEL-4-49-2-5-1','',2,5,4,2);
/*!40000 ALTER TABLE `equipo_equipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipo_estado`
--

DROP TABLE IF EXISTS `equipo_estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `equipo_estado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipo_estado`
--

LOCK TABLES `equipo_estado` WRITE;
/*!40000 ALTER TABLE `equipo_estado` DISABLE KEYS */;
INSERT INTO `equipo_estado` VALUES (1,'Asignado'),(2,'Disponible'),(3,'Fuera de Servicio');
/*!40000 ALTER TABLE `equipo_estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipo_tamano`
--

DROP TABLE IF EXISTS `equipo_tamano`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `equipo_tamano` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tamano` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipo_tamano`
--

LOCK TABLES `equipo_tamano` WRITE;
/*!40000 ALTER TABLE `equipo_tamano` DISABLE KEYS */;
INSERT INTO `equipo_tamano` VALUES (1,'Grande'),(2,'Pequeño'),(3,'Normal');
/*!40000 ALTER TABLE `equipo_tamano` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hielo_proceso_departamentoproceso`
--

DROP TABLE IF EXISTS `hielo_proceso_departamentoproceso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `hielo_proceso_departamentoproceso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `departamento` varchar(25) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hielo_proceso_departamentoproceso`
--

LOCK TABLES `hielo_proceso_departamentoproceso` WRITE;
/*!40000 ALTER TABLE `hielo_proceso_departamentoproceso` DISABLE KEYS */;
INSERT INTO `hielo_proceso_departamentoproceso` VALUES (2,'Maquina 1'),(3,'Maquina 2'),(4,'Maquina 3'),(5,'Maquina 4'),(6,'Empaque fresco'),(7,'Descabezado'),(8,'Reenhielado'),(9,'Clasificado'),(10,'Reproceso'),(11,'Langosta'),(12,'Pelado'),(13,'Descongelado');
/*!40000 ALTER TABLE `hielo_proceso_departamentoproceso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hielo_proceso_detallehieloproceso`
--

DROP TABLE IF EXISTS `hielo_proceso_detallehieloproceso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `hielo_proceso_detallehieloproceso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hieloProceso_id` int(11) DEFAULT NULL,
  `departamento_id` int(11) NOT NULL,
  `binGrande` int(10) unsigned NOT NULL,
  `binPequeno` int(10) unsigned NOT NULL,
  `canastaA` int(10) unsigned NOT NULL,
  `canastapAzul` int(10) unsigned NOT NULL,
  `canastapRoja` int(10) unsigned NOT NULL,
  `carretonBlanco` int(10) unsigned NOT NULL,
  `glaseo` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hielo_proceso_detall_hieloProceso_id_225a9404_fk_hielo_pro` (`hieloProceso_id`),
  KEY `hielo_proceso_detall_departamento_id_7ec3a715_fk_hielo_pro` (`departamento_id`),
  CONSTRAINT `hielo_proceso_detall_departamento_id_7ec3a715_fk_hielo_pro` FOREIGN KEY (`departamento_id`) REFERENCES `hielo_proceso_departamentoproceso` (`id`),
  CONSTRAINT `hielo_proceso_detall_hieloProceso_id_225a9404_fk_hielo_pro` FOREIGN KEY (`hieloProceso_id`) REFERENCES `hielo_proceso_hieloproceso` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hielo_proceso_detallehieloproceso`
--

LOCK TABLES `hielo_proceso_detallehieloproceso` WRITE;
/*!40000 ALTER TABLE `hielo_proceso_detallehieloproceso` DISABLE KEYS */;
INSERT INTO `hielo_proceso_detallehieloproceso` VALUES (74,40,2,4,7,2,6,5,2,1),(75,40,3,5,6,2,4,4,3,2),(76,41,2,5,7,6,6,7,5,4),(77,41,3,4,6,5,5,6,6,4),(78,42,2,5,8,2,7,6,4,4),(79,42,3,5,7,2,5,6,5,5),(80,42,4,4,9,2,5,5,4,4),(81,43,2,4,6,5,5,6,5,4),(82,43,3,4,7,5,6,6,5,4),(83,44,2,6,8,7,8,6,6,5),(84,44,3,5,8,6,8,6,5,4),(85,45,2,5,7,6,7,8,8,4),(86,45,3,5,8,6,5,6,5,4),(87,46,2,4,9,7,6,9,7,4),(88,46,3,4,7,6,5,5,7,4),(89,47,2,4,9,6,8,5,7,4),(90,47,3,5,6,7,6,5,8,3),(91,48,2,4,8,6,6,6,8,5),(92,48,3,5,6,7,9,5,9,4),(93,49,2,5,8,9,7,10,7,4),(94,49,3,5,9,8,6,7,9,5),(95,50,2,4,8,7,6,8,6,4),(96,50,3,5,9,6,5,8,6,4),(105,51,2,4,8,7,6,9,6,4),(106,51,3,5,9,6,5,7,6,4),(107,52,2,5,6,6,5,7,5,4),(108,52,3,4,7,5,5,8,6,4),(109,53,2,5,7,8,7,6,6,4),(110,53,3,4,8,9,6,6,5,4),(111,54,2,6,8,6,5,7,7,5),(112,54,3,5,8,5,4,6,6,5),(113,55,2,5,8,5,4,8,7,4),(114,55,3,5,6,6,5,6,6,4),(115,56,2,5,7,6,4,7,8,4),(116,56,3,4,6,5,4,6,9,4),(117,57,2,5,9,7,5,8,8,6),(118,57,3,6,9,6,4,9,7,5),(119,58,2,5,6,6,4,7,7,4),(120,58,3,4,6,5,4,6,6,4),(121,59,2,5,9,5,5,9,6,3),(122,59,3,6,5,6,5,7,4,4),(123,60,2,5,5,6,5,8,8,5),(124,60,3,5,6,4,4,9,8,5),(125,61,2,4,6,6,6,6,6,5),(126,61,3,5,9,7,5,8,7,4);
/*!40000 ALTER TABLE `hielo_proceso_detallehieloproceso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hielo_proceso_hieloproceso`
--

DROP TABLE IF EXISTS `hielo_proceso_hieloproceso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `hielo_proceso_hieloproceso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `registrado_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hielo_proceso_hieloproceso_fecha_98b5df34_uniq` (`fecha`),
  KEY `hielo_proceso_hielop_registrado_id_4af33447_fk_empleado_` (`registrado_id`),
  CONSTRAINT `hielo_proceso_hielop_registrado_id_4af33447_fk_empleado_` FOREIGN KEY (`registrado_id`) REFERENCES `empleado_empleado` (`codEmpleado`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hielo_proceso_hieloproceso`
--

LOCK TABLES `hielo_proceso_hieloproceso` WRITE;
/*!40000 ALTER TABLE `hielo_proceso_hieloproceso` DISABLE KEYS */;
INSERT INTO `hielo_proceso_hieloproceso` VALUES (40,'2019-08-01',801),(41,'2019-08-02',801),(42,'2019-08-03',801),(43,'2019-08-04',801),(44,'2019-08-05',801),(45,'2019-08-06',801),(46,'2019-08-07',801),(47,'2019-08-08',801),(48,'2019-08-09',801),(49,'2019-08-10',801),(50,'2019-09-01',801),(51,'2019-03-09',801),(52,'2019-09-02',801),(53,'2019-09-03',801),(54,'2019-09-04',801),(55,'2019-09-05',801),(56,'2019-09-06',801),(57,'2019-09-07',801),(58,'2019-09-08',801),(59,'2019-09-09',801),(60,'2019-09-10',801),(61,'2019-10-01',801);
/*!40000 ALTER TABLE `hielo_proceso_hieloproceso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestamos_detalleprestamoequipo`
--

DROP TABLE IF EXISTS `prestamos_detalleprestamoequipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `prestamos_detalleprestamoequipo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `equipo_id` int(11) NOT NULL,
  `prestamoEquipo_id` varchar(6) COLLATE utf8_spanish_ci DEFAULT NULL,
  `devuelto` tinyint(1),
  `tapadera_id` int(11) DEFAULT NULL,
  `devueltoT` tinyint(1),
  PRIMARY KEY (`id`),
  KEY `prestamos_detallepre_equipo_id_9ee8a488_fk_equipo_eq` (`equipo_id`),
  KEY `prestamos_detallepre_prestamoEquipo_id_4074fcbc_fk_prestamos` (`prestamoEquipo_id`),
  KEY `prestamos_detallepre_tapadera_id_90e57269_fk_equipo_eq` (`tapadera_id`),
  CONSTRAINT `prestamos_detallepre_equipo_id_9ee8a488_fk_equipo_eq` FOREIGN KEY (`equipo_id`) REFERENCES `equipo_equipo` (`id`),
  CONSTRAINT `prestamos_detallepre_prestamoEquipo_id_4074fcbc_fk_prestamos` FOREIGN KEY (`prestamoEquipo_id`) REFERENCES `prestamos_prestamoequipo` (`numPrestamo`),
  CONSTRAINT `prestamos_detallepre_tapadera_id_90e57269_fk_equipo_eq` FOREIGN KEY (`tapadera_id`) REFERENCES `equipo_equipo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestamos_detalleprestamoequipo`
--

LOCK TABLES `prestamos_detalleprestamoequipo` WRITE;
/*!40000 ALTER TABLE `prestamos_detalleprestamoequipo` DISABLE KEYS */;
INSERT INTO `prestamos_detalleprestamoequipo` VALUES (84,NULL,17,'100001',0,71,0),(85,NULL,18,'100001',0,72,0),(86,NULL,19,'100001',0,73,0),(87,NULL,20,'100001',0,74,0),(88,NULL,21,'100002',0,76,0),(89,NULL,23,'100002',0,77,0),(90,NULL,22,'100003',0,75,0),(91,NULL,24,'100003',0,78,0),(92,NULL,25,'100003',0,79,0),(93,NULL,26,'100004',0,80,0),(94,NULL,27,'100004',0,81,0),(95,NULL,28,'100004',0,82,0),(96,NULL,29,'100005',0,83,0),(97,NULL,30,'100005',0,85,0),(98,NULL,31,'100005',0,86,0);
/*!40000 ALTER TABLE `prestamos_detalleprestamoequipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestamos_estadoprestamo`
--

DROP TABLE IF EXISTS `prestamos_estadoprestamo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `prestamos_estadoprestamo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestamos_estadoprestamo`
--

LOCK TABLES `prestamos_estadoprestamo` WRITE;
/*!40000 ALTER TABLE `prestamos_estadoprestamo` DISABLE KEYS */;
INSERT INTO `prestamos_estadoprestamo` VALUES (1,'Activo'),(2,'Anulado'),(3,'Asignado'),(4,'Terminado');
/*!40000 ALTER TABLE `prestamos_estadoprestamo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestamos_prestamoequipo`
--

DROP TABLE IF EXISTS `prestamos_prestamoequipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `prestamos_prestamoequipo` (
  `numPrestamo` varchar(6) COLLATE utf8_spanish_ci NOT NULL,
  `horaSalida` time(6) NOT NULL,
  `fechaSalida` date NOT NULL,
  `fechaEntrada` date DEFAULT NULL,
  `observaciones` longtext COLLATE utf8_spanish_ci,
  `compania_id` int(11) NOT NULL,
  `conductor_id` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `empleado_id` int(11) NOT NULL,
  `estadoPrestamo_id` int(11) NOT NULL,
  `placa_id` varchar(7) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`numPrestamo`),
  KEY `prestamos_prestamoeq_compania_id_6b75f608_fk_compania_` (`compania_id`),
  KEY `prestamos_prestamoeq_conductor_id_f392e338_fk_conductor` (`conductor_id`),
  KEY `prestamos_prestamoeq_empleado_id_8e5fd1ff_fk_empleado_` (`empleado_id`),
  KEY `prestamos_prestamoeq_estadoPrestamo_id_40fa0176_fk_prestamos` (`estadoPrestamo_id`),
  KEY `prestamos_prestamoeq_placa_id_c8be6980_fk_vehiculo_` (`placa_id`),
  CONSTRAINT `prestamos_prestamoeq_compania_id_6b75f608_fk_compania_` FOREIGN KEY (`compania_id`) REFERENCES `compania_compania` (`id`),
  CONSTRAINT `prestamos_prestamoeq_conductor_id_f392e338_fk_conductor` FOREIGN KEY (`conductor_id`) REFERENCES `conductor_conductor` (`numIdentidad`),
  CONSTRAINT `prestamos_prestamoeq_empleado_id_8e5fd1ff_fk_empleado_` FOREIGN KEY (`empleado_id`) REFERENCES `empleado_empleado` (`codEmpleado`),
  CONSTRAINT `prestamos_prestamoeq_estadoPrestamo_id_40fa0176_fk_prestamos` FOREIGN KEY (`estadoPrestamo_id`) REFERENCES `prestamos_estadoprestamo` (`id`),
  CONSTRAINT `prestamos_prestamoeq_placa_id_c8be6980_fk_vehiculo_` FOREIGN KEY (`placa_id`) REFERENCES `vehiculo_vehiculo` (`placa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestamos_prestamoequipo`
--

LOCK TABLES `prestamos_prestamoequipo` WRITE;
/*!40000 ALTER TABLE `prestamos_prestamoequipo` DISABLE KEYS */;
INSERT INTO `prestamos_prestamoequipo` VALUES ('100001','07:00:00.000000','2019-08-09',NULL,'',31,'0601-1975-16144',1,1,'PEJ1001'),('100002','07:00:00.000000','2019-08-12',NULL,'',31,'0615-1990-00415',1,1,'FCS3348'),('100003','07:00:00.000000','2019-08-18',NULL,'',32,'0601-1974-12245',1,1,'KJY6213'),('100004','07:00:00.000000','2019-10-31',NULL,'',32,'0601-1975-14223',1,1,'KPL2345'),('100005','14:01:00.000000','2019-08-22',NULL,'',33,'0601-1982-16012',1,1,'LPD3561');
/*!40000 ALTER TABLE `prestamos_prestamoequipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remision_detalleremision`
--

DROP TABLE IF EXISTS `remision_detalleremision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `remision_detalleremision` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `salida` int(11) NOT NULL,
  `devolucion` int(11) NOT NULL,
  `hielo_id` int(11) NOT NULL,
  `remision_id` varchar(6) COLLATE utf8_spanish_ci DEFAULT NULL,
  `unidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `remision_detalleremision_hielo_id_89b3047b_fk_remision_hielo_id` (`hielo_id`),
  KEY `remision_detalleremi_unidad_id_0e308672_fk_remision_` (`unidad_id`),
  KEY `remision_detalleremi_remision_id_c3192fdb_fk_remision_` (`remision_id`),
  CONSTRAINT `remision_detalleremi_remision_id_c3192fdb_fk_remision_` FOREIGN KEY (`remision_id`) REFERENCES `remision_remision` (`numRemision`),
  CONSTRAINT `remision_detalleremi_unidad_id_0e308672_fk_remision_` FOREIGN KEY (`unidad_id`) REFERENCES `remision_medida` (`id`),
  CONSTRAINT `remision_detalleremision_hielo_id_89b3047b_fk_remision_hielo_id` FOREIGN KEY (`hielo_id`) REFERENCES `remision_hielo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=186 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remision_detalleremision`
--

LOCK TABLES `remision_detalleremision` WRITE;
/*!40000 ALTER TABLE `remision_detalleremision` DISABLE KEYS */;
/*!40000 ALTER TABLE `remision_detalleremision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remision_estadoremision`
--

DROP TABLE IF EXISTS `remision_estadoremision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `remision_estadoremision` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remision_estadoremision`
--

LOCK TABLES `remision_estadoremision` WRITE;
/*!40000 ALTER TABLE `remision_estadoremision` DISABLE KEYS */;
INSERT INTO `remision_estadoremision` VALUES (1,'Activo'),(2,'Terminado'),(3,'Anulado');
/*!40000 ALTER TABLE `remision_estadoremision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remision_hielo`
--

DROP TABLE IF EXISTS `remision_hielo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `remision_hielo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estadoHielo` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `precioQuintal` decimal(6,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remision_hielo`
--

LOCK TABLES `remision_hielo` WRITE;
/*!40000 ALTER TABLE `remision_hielo` DISABLE KEYS */;
INSERT INTO `remision_hielo` VALUES (1,'Limpio',60.00),(2,'Sucio',10.00);
/*!40000 ALTER TABLE `remision_hielo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remision_medida`
--

DROP TABLE IF EXISTS `remision_medida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `remision_medida` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `magnitud` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `unidad` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `abreviatura` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remision_medida`
--

LOCK TABLES `remision_medida` WRITE;
/*!40000 ALTER TABLE `remision_medida` DISABLE KEYS */;
INSERT INTO `remision_medida` VALUES (1,'Masa','Quintal','Q'),(2,'Masa','Libra','lb');
/*!40000 ALTER TABLE `remision_medida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remision_remision`
--

DROP TABLE IF EXISTS `remision_remision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `remision_remision` (
  `numRemision` varchar(6) COLLATE utf8_spanish_ci NOT NULL,
  `guia` varchar(6) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fecha` date NOT NULL,
  `estado_id` int(11) DEFAULT NULL,
  `compania_id` int(11) NOT NULL,
  `conductor_id` varchar(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `entrego_id` int(11) NOT NULL,
  `placa_id` varchar(7) COLLATE utf8_spanish_ci DEFAULT NULL,
  `prestamoEquipo_id` varchar(6) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipoRemision_id` int(11) NOT NULL,
  `observacion` longtext COLLATE utf8_spanish_ci,
  PRIMARY KEY (`numRemision`),
  UNIQUE KEY `prestamoEquipo_id` (`prestamoEquipo_id`),
  KEY `remision_remision_compania_id_fa2fa9ac_fk_compania_compania_id` (`compania_id`),
  KEY `remision_remision_conductor_id_c476febe_fk_conductor` (`conductor_id`),
  KEY `remision_remision_placa_id_60eb933e_fk_vehiculo_vehiculo_placa` (`placa_id`),
  KEY `remision_remision_tipoRemision_id_ede822ae_fk_remision_` (`tipoRemision_id`),
  KEY `remision_remision_entrego_id_fc9fdc38_fk_empleado_` (`entrego_id`),
  KEY `remision_remision_estado_id_315928ef` (`estado_id`),
  CONSTRAINT `remision_remision_compania_id_fa2fa9ac_fk_compania_compania_id` FOREIGN KEY (`compania_id`) REFERENCES `compania_compania` (`id`),
  CONSTRAINT `remision_remision_conductor_id_c476febe_fk_conductor` FOREIGN KEY (`conductor_id`) REFERENCES `conductor_conductor` (`numIdentidad`),
  CONSTRAINT `remision_remision_entrego_id_fc9fdc38_fk_empleado_` FOREIGN KEY (`entrego_id`) REFERENCES `empleado_empleado` (`codEmpleado`),
  CONSTRAINT `remision_remision_placa_id_60eb933e_fk_vehiculo_vehiculo_placa` FOREIGN KEY (`placa_id`) REFERENCES `vehiculo_vehiculo` (`placa`),
  CONSTRAINT `remision_remision_prestamoEquipo_id_9b6f9286_fk_prestamos` FOREIGN KEY (`prestamoEquipo_id`) REFERENCES `prestamos_prestamoequipo` (`numPrestamo`),
  CONSTRAINT `remision_remision_tipoRemision_id_ede822ae_fk_remision_` FOREIGN KEY (`tipoRemision_id`) REFERENCES `remision_tiporemision` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remision_remision`
--

LOCK TABLES `remision_remision` WRITE;
/*!40000 ALTER TABLE `remision_remision` DISABLE KEYS */;
/*!40000 ALTER TABLE `remision_remision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remision_tiporemision`
--

DROP TABLE IF EXISTS `remision_tiporemision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `remision_tiporemision` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movimiento` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remision_tiporemision`
--

LOCK TABLES `remision_tiporemision` WRITE;
/*!40000 ALTER TABLE `remision_tiporemision` DISABLE KEYS */;
INSERT INTO `remision_tiporemision` VALUES (1,'MAQUILA'),(2,'VENTA'),(3,'OTRO');
/*!40000 ALTER TABLE `remision_tiporemision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehiculo_vehiculo`
--

DROP TABLE IF EXISTS `vehiculo_vehiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `vehiculo_vehiculo` (
  `placa` varchar(7) COLLATE utf8_spanish_ci NOT NULL,
  `marca` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `modelo` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `anio` int(10) unsigned NOT NULL,
  `color_id` int(11) NOT NULL,
  `empresaFlete_id` int(11) DEFAULT NULL,
  `disponible` tinyint(1) NOT NULL,
  PRIMARY KEY (`placa`),
  KEY `vehiculo_vehiculo_color_id_80a97ffb_fk_equipo_color_id` (`color_id`),
  KEY `vehiculo_vehiculo_empresaFlete_id_5b66f4f6_fk_compania_` (`empresaFlete_id`),
  CONSTRAINT `vehiculo_vehiculo_color_id_80a97ffb_fk_equipo_color_id` FOREIGN KEY (`color_id`) REFERENCES `equipo_color` (`id`),
  CONSTRAINT `vehiculo_vehiculo_empresaFlete_id_5b66f4f6_fk_compania_` FOREIGN KEY (`empresaFlete_id`) REFERENCES `compania_compania` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiculo_vehiculo`
--

LOCK TABLES `vehiculo_vehiculo` WRITE;
/*!40000 ALTER TABLE `vehiculo_vehiculo` DISABLE KEYS */;
INSERT INTO `vehiculo_vehiculo` VALUES ('FCS3348','ISUZU','2.3',2004,2,28,0),('KJY6213','KIA','2.3',2001,1,30,0),('KPL2345','ISUZU','2.3',2003,1,27,0),('LPD3561','HYUNDAI','2.4',2008,3,30,0),('PEJ1001','Honda','RINO',1980,2,29,0),('PLD3248','MITSUBISCHI','2.0',2006,1,29,1),('PSA3281','MITSUBISCHI','2.0',2006,2,28,1),('SVC6240','KIA','2.4',1998,3,27,1);
/*!40000 ALTER TABLE `vehiculo_vehiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'empacadoralitoral'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-31 17:10:26
