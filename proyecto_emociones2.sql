/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-12.3.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: Proyecto_Emociones2
-- ------------------------------------------------------
-- Server version	12.3.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Current Database: `Proyecto_Emociones2`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `Proyecto_Emociones2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_uca1400_ai_ci */;

USE `Proyecto_Emociones2`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',3,'add_permission'),
(6,'Can change permission',3,'change_permission'),
(7,'Can delete permission',3,'delete_permission'),
(8,'Can view permission',3,'view_permission'),
(9,'Can add group',2,'add_group'),
(10,'Can change group',2,'change_group'),
(11,'Can delete group',2,'delete_group'),
(12,'Can view group',2,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add alumno',7,'add_alumno'),
(26,'Can change alumno',7,'change_alumno'),
(27,'Can delete alumno',7,'delete_alumno'),
(28,'Can view alumno',7,'view_alumno'),
(29,'Can add estilos aprendizaje',8,'add_estilosaprendizaje'),
(30,'Can change estilos aprendizaje',8,'change_estilosaprendizaje'),
(31,'Can delete estilos aprendizaje',8,'delete_estilosaprendizaje'),
(32,'Can view estilos aprendizaje',8,'view_estilosaprendizaje'),
(33,'Can add estilos_aprendizaje',8,'add_estilos_aprendizaje'),
(34,'Can change estilos_aprendizaje',8,'change_estilos_aprendizaje'),
(35,'Can delete estilos_aprendizaje',8,'delete_estilos_aprendizaje'),
(36,'Can view estilos_aprendizaje',8,'view_estilos_aprendizaje');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `catalog_alumno`
--

DROP TABLE IF EXISTS `catalog_alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `catalog_alumno` (
  `id_alumno` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `apellido_paterno` varchar(20) NOT NULL,
  `apellido_materno` varchar(20) NOT NULL,
  `edad` int(10) unsigned NOT NULL CHECK (`edad` >= 0),
  `licenciatura` varchar(40) NOT NULL,
  `tipo_aprendizaje` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_alumno`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalog_alumno`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `catalog_alumno` WRITE;
/*!40000 ALTER TABLE `catalog_alumno` DISABLE KEYS */;
INSERT INTO `catalog_alumno` VALUES
(1,'Samantha','Hernandez','Aguilar',19,'Derecho','kinestésico'),
(2,'Samantha','Hernandez','Aguilar',19,'Derecho',NULL),
(3,'jose','perez','lopez',19,'psicologia','auditivo'),
(4,'jose','perez','lopez',19,'psicologia',NULL),
(5,'jose','perez','lopez',19,'psicologia','auditivo'),
(6,'jose','perez','lopez',19,'psicologia',NULL),
(7,'jose','perez','lopez',19,'psicologia','auditivo'),
(8,'Juan','Carlo','Maria',21,'Ciencias','auditivo'),
(9,'Juan','Carlo','Maria',21,'Ciencias','auditivo'),
(10,'Samuel','Fuentes','Hernandez',18,'Ciencias','visual'),
(11,'sujeto','Prueba','final',19,'Derecho','kinestésico'),
(12,'Juan','Lopez','Perez',19,'Psicología','kinestésico');
/*!40000 ALTER TABLE `catalog_alumno` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `catalog_estilos_aprendizaje`
--

DROP TABLE IF EXISTS `catalog_estilos_aprendizaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `catalog_estilos_aprendizaje` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `p1` varchar(1) NOT NULL,
  `p2` varchar(1) NOT NULL,
  `p3` varchar(1) NOT NULL,
  `p4` varchar(1) NOT NULL,
  `p5` varchar(1) NOT NULL,
  `p6` varchar(1) NOT NULL,
  `p7` varchar(1) NOT NULL,
  `p8` varchar(1) NOT NULL,
  `p9` varchar(1) NOT NULL,
  `p10` varchar(1) NOT NULL,
  `resultado` varchar(50) NOT NULL,
  `alumno_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `catalog_estilosapren_alumno_id_c8ad6bdd_fk_catalog_a` (`alumno_id`),
  CONSTRAINT `catalog_estilosapren_alumno_id_c8ad6bdd_fk_catalog_a` FOREIGN KEY (`alumno_id`) REFERENCES `catalog_alumno` (`id_alumno`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalog_estilos_aprendizaje`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `catalog_estilos_aprendizaje` WRITE;
/*!40000 ALTER TABLE `catalog_estilos_aprendizaje` DISABLE KEYS */;
INSERT INTO `catalog_estilos_aprendizaje` VALUES
(1,'A','B','B','B','B','B','B','B','B','C','Auditivo',3),
(2,'B','B','B','B','C','B','B','B','C','C','Auditivo',5),
(3,'B','B','B','B','C','B','B','B','C','C','Auditivo',5),
(4,'B','B','B','B','C','B','B','B','C','C','Auditivo',5),
(5,'B','B','B','B','C','B','B','B','C','C','Auditivo',5),
(6,'B','B','B','B','C','B','B','B','C','C','Auditivo',5),
(7,'B','B','B','B','C','B','B','B','C','C','Auditivo',5),
(8,'B','B','B','B','C','B','B','B','C','C','Auditivo',5),
(9,'B','B','B','B','C','B','B','B','C','C','Auditivo',5),
(10,'B','B','B','B','C','B','B','B','C','C','Auditivo',5),
(11,'B','B','B','B','B','B','B','B','B','C','Auditivo',7),
(12,'B','B','B','B','B','B','B','B','B','C','Auditivo',7),
(13,'B','B','B','B','B','B','B','B','B','C','Auditivo',7),
(14,'B','B','B','B','B','B','B','B','B','C','Auditivo',7),
(15,'B','B','B','B','B','B','B','B','B','C','Auditivo',7),
(16,'B','B','B','B','B','B','B','B','B','C','Auditivo',7),
(17,'B','B','B','B','B','B','B','B','B','C','Auditivo',7),
(18,'B','B','B','B','B','B','B','B','B','C','Auditivo',7),
(19,'B','B','B','B','B','B','B','B','B','B','Auditivo',1),
(20,'B','B','B','B','B','B','B','B','B','B','Auditivo',1),
(21,'B','B','B','B','B','B','B','B','B','B','Auditivo',1),
(22,'B','B','B','B','B','B','B','B','B','B','Auditivo',8),
(23,'B','B','B','B','B','B','B','B','B','B','Auditivo',8),
(24,'B','B','B','B','B','B','B','B','B','C','Auditivo',9),
(25,'B','B','B','B','B','B','B','B','B','C','Auditivo',9),
(26,'A','B','B','B','A','B','A','A','A','A','Visual',1),
(27,'C','C','C','C','C','C','C','C','C','C','Kinestésico',1),
(28,'A','A','A','A','A','A','A','A','A','A','Visual',10),
(29,'C','C','C','B','B','A','C','C','C','C','Kinestésico',11),
(30,'C','C','B','C','B','C','C','C','A','C','Kinestésico',12);
/*!40000 ALTER TABLE `catalog_estilos_aprendizaje` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES
(1,'admin','logentry'),
(2,'auth','group'),
(3,'auth','permission'),
(4,'auth','user'),
(7,'catalog','alumno'),
(8,'catalog','estilos_aprendizaje'),
(5,'contenttypes','contenttype'),
(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2026-01-25 19:47:52.758932'),
(2,'auth','0001_initial','2026-01-25 19:47:53.113170'),
(3,'admin','0001_initial','2026-01-25 19:47:53.206325'),
(4,'admin','0002_logentry_remove_auto_add','2026-01-25 19:47:53.228419'),
(5,'admin','0003_logentry_add_action_flag_choices','2026-01-25 19:47:53.251002'),
(6,'contenttypes','0002_remove_content_type_name','2026-01-25 19:47:53.336658'),
(7,'auth','0002_alter_permission_name_max_length','2026-01-25 19:47:53.384745'),
(8,'auth','0003_alter_user_email_max_length','2026-01-25 19:47:53.420400'),
(9,'auth','0004_alter_user_username_opts','2026-01-25 19:47:53.441783'),
(10,'auth','0005_alter_user_last_login_null','2026-01-25 19:47:53.491269'),
(11,'auth','0006_require_contenttypes_0002','2026-01-25 19:47:53.508316'),
(12,'auth','0007_alter_validators_add_error_messages','2026-01-25 19:47:53.531033'),
(13,'auth','0008_alter_user_username_max_length','2026-01-25 19:47:53.567844'),
(14,'auth','0009_alter_user_last_name_max_length','2026-01-25 19:47:53.602446'),
(15,'auth','0010_alter_group_name_max_length','2026-01-25 19:47:53.636632'),
(16,'auth','0011_update_proxy_permissions','2026-01-25 19:47:53.656237'),
(17,'auth','0012_alter_user_first_name_max_length','2026-01-25 19:47:53.691320'),
(18,'catalog','0001_initial','2026-01-25 19:47:53.708366'),
(19,'sessions','0001_initial','2026-01-25 19:47:53.741585'),
(20,'catalog','0002_estilosaprendizaje','2026-01-25 20:08:09.838420'),
(21,'catalog','0003_rename_estilosaprendizaje_estilos_aprendizaje','2026-01-25 20:52:55.475086'),
(22,'catalog','0004_alter_estilos_aprendizaje_p1_and_more','2026-01-25 20:56:21.396754'),
(23,'catalog','0005_alter_estilos_aprendizaje_p1_and_more','2026-01-25 22:21:47.805259');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES
('81g91j9b94ojz1iqnm98tbsna3dy2dg4','.eJxFyTsOgCAQRdG9vJpCK-N0rsRMZIpRBCOfQsLepTGW956KW2J2iW1Y-brFW314F1D9AYQlW01aAgyKxswONBjwd2k2ONRLTBJ16z12dPn0YVULmlp7AccGJNM:1vk851:Ps6QU-Lg_9e3qwJa_mv5MptXar0-GrooJ_xettLS5qA','2026-02-08 21:55:35.737432');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2026-06-10 20:23:59
