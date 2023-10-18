-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: mylcc
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add my news',7,'add_mynews'),(26,'Can change my news',7,'change_mynews'),(27,'Can delete my news',7,'delete_mynews'),(28,'Can view my news',7,'view_mynews'),(29,'Can add goods',8,'add_goods'),(30,'Can change goods',8,'change_goods'),(31,'Can delete goods',8,'delete_goods'),(32,'Can view goods',8,'view_goods');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$hbbn1IZqegj4mvn1nB6y3H$7fvyeQ9i0dUTCIOXtWXhhBHGE0GWWInEVcA6xWQ9ONs=','2023-10-03 19:50:59.636960',1,'lcc','','','lcc@gmail.com',1,1,'2023-09-19 19:50:53.264266');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-09-19 20:42:16.367869','1','myNews object (1)',1,'[{\"added\": {}}]',7,1),(2,'2023-09-19 21:05:57.023273','2','myNews object (2)',1,'[{\"added\": {}}]',7,1),(3,'2023-09-26 21:30:35.654601','3','myNews object (3)',1,'[{\"added\": {}}]',7,1),(4,'2023-09-26 21:31:29.682661','4','myNews object (4)',1,'[{\"added\": {}}]',7,1),(5,'2023-10-03 19:56:53.497577','1','Goods object (1)',1,'[{\"added\": {}}]',8,1),(6,'2023-10-03 19:56:57.770196','1','Goods object (1)',2,'[]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'news','mynews'),(8,'product','goods'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-09-19 19:31:12.291212'),(2,'auth','0001_initial','2023-09-19 19:31:13.208266'),(3,'admin','0001_initial','2023-09-19 19:31:13.436136'),(4,'admin','0002_logentry_remove_auto_add','2023-09-19 19:31:13.448143'),(5,'admin','0003_logentry_add_action_flag_choices','2023-09-19 19:31:13.459123'),(6,'contenttypes','0002_remove_content_type_name','2023-09-19 19:31:13.643017'),(7,'auth','0002_alter_permission_name_max_length','2023-09-19 19:31:13.771944'),(8,'auth','0003_alter_user_email_max_length','2023-09-19 19:31:13.941847'),(9,'auth','0004_alter_user_username_opts','2023-09-19 19:31:13.956839'),(10,'auth','0005_alter_user_last_login_null','2023-09-19 19:31:14.067777'),(11,'auth','0006_require_contenttypes_0002','2023-09-19 19:31:14.076771'),(12,'auth','0007_alter_validators_add_error_messages','2023-09-19 19:31:14.102756'),(13,'auth','0008_alter_user_username_max_length','2023-09-19 19:31:14.235680'),(14,'auth','0009_alter_user_last_name_max_length','2023-09-19 19:31:14.363607'),(15,'auth','0010_alter_group_name_max_length','2023-09-19 19:31:14.491533'),(16,'auth','0011_update_proxy_permissions','2023-09-19 19:31:14.506528'),(17,'auth','0012_alter_user_first_name_max_length','2023-09-19 19:31:14.628457'),(18,'sessions','0001_initial','2023-09-19 19:31:14.677441'),(19,'news','0001_initial','2023-09-19 20:38:40.375233'),(20,'product','0001_initial','2023-10-03 19:49:16.181169'),(21,'product','0002_rename_c_date_date_goods_c_date','2023-10-03 19:58:37.459153');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('c0ozgl5pia3u2nckpddti2ivj8o59fpq','.eJxVjDsOg0AMBe-ydbTCmPUuKdNzBmTsdSCJQOJTRbl7QKJI2pl57-1a3ta-3ZY8t4O6qwN3-WUdyzOPh9AHj_fJyzSu89D5I_GnXXwzaX7dzvbvoOel39cBTS0woVmOpSIZCYBYgFQZdFBgTDutqKgpMaqWlAWIMWMtEpP7fAHrgDfe:1qia2T:b2a-oDxxtwXRX2w7K8sJYDviJ3DTYNDAHW4CZsA8_eY','2023-10-03 20:41:13.443125'),('h2lmybnlvwuymh413kgd6c98du7fd66f','.eJxVjDsOg0AMBe-ydbTCmPUuKdNzBmTsdSCJQOJTRbl7QKJI2pl57-1a3ta-3ZY8t4O6qwN3-WUdyzOPh9AHj_fJyzSu89D5I_GnXXwzaX7dzvbvoOel39cBTS0woVmOpSIZCYBYgFQZdFBgTDutqKgpMaqWlAWIMWMtEpP7fAHrgDfe:1ql81l:QwaiN1jVWkPcFGamyuX4ppJby8XhTxzxJhj5B9JE2qk','2023-10-10 21:23:01.480635'),('nbsllvnxo5k4738yias30v5oxqe71svr','.eJxVjDsOg0AMBe-ydbTCmPUuKdNzBmTsdSCJQOJTRbl7QKJI2pl57-1a3ta-3ZY8t4O6qwN3-WUdyzOPh9AHj_fJyzSu89D5I_GnXXwzaX7dzvbvoOel39cBTS0woVmOpSIZCYBYgFQZdFBgTDutqKgpMaqWlAWIMWMtEpP7fAHrgDfe:1qndvX:FIB4Z5gMXpvLvo33xY6OFXPukCkgogxQvFNY1U1DwuM','2023-10-17 19:50:59.641477');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `news` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `content` longtext NOT NULL,
  `photo_url` varchar(200) NOT NULL,
  `c_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (1,'太魯閣事故車廂「驚見遺骸」　花檢鑑定：37件與10罹難者相符','花蓮台鐵太魯閣號事故傷亡慘重，消息震驚國際社會；時隔2年多，今年9月還在事故車廂發現罹難者遺物以及遺骸，再次引起譁然。花蓮地檢今（19）日表示，經統計事故車廂內發現疑似被害人骨骸共計44件，其中37件檢出被害人身分，比對後共計與10名罹難者相符，將儘速聯繫被害人家屬協調骨骸發還等事宜。','https://cc.tvbs.com.tw/img/upload/2023/09/04/20230904172850-564888e0.jpg','2023-09-19 20:42:16.361872'),(2,'縣市長滿意度調查曝！高虹安墊底　藍營這2位則要再加油','《天下雜誌》縣市首長施政滿意度調查，今（19日）出爐。身兼新北市長的國民黨總統參選人侯友宜在去年選舉時雖大勝對手46萬票，但名次從去年第9名，今年滑落到排名倒數第4，專家評價也不如人意。去年風光登場的新秀首長，包含台北市長蔣萬安、基隆市長謝國樑、高虹安分居末三位，其中，高虹安的施政滿意度更是墊底，引發關注。','https://cc.tvbs.com.tw/img/upload/2023/09/13/20230913125150-144d2b37.jpg','2023-09-19 21:05:57.021275'),(3,'郭台銘確定出局！侯友宜民調糾纏「力保新北不能出事」恐成罩門','「侯友宜現在民調已逐步站上老二，若能和賴清德再拉近距離，在非綠的整合上會更有底氣。」一位力挺國民黨總統參選人侯友宜的藍營要角向本刊表示，綜觀藍營目前最大的障礙，就是藍白合尚未水到渠成，由於侯的民調與民眾黨總統參選人柯文哲呈現糾纏，至少要領先柯超出誤差範圍，談合作才會更有空間。至於鴻海集團創辦人郭台銘的問題，該人士不諱言：「目前已沒有在整合的討論範圍。」\r\n\r\n \r\n該名藍營要角指出，中選會在11月20日至24日受理總統、副總統候選人登記，不論是藍白合或非綠整合，都不可能到最後一刻才談，這不只是2黨候選人跟程序的問題而已，像是雙方都已各自召開全代會通過提名總統人選要如何解套？另也要考量藍白支持者的情緒消化時間，「時程上真的很緊迫，再加上柯文哲10月初還要訪美，如果10月中旬藍白還沒有初步共識，那恐怕就沒戲了！」因此關鍵時間恐怕就落在這1個月內，必須談妥。','https://cc.tvbs.com.tw/img/upload/2023/09/26/20230926080002-0b23a796.jpg','2023-09-26 21:30:35.646602'),(4,'快訊／萊爾富發票「爽中1000萬」！獎落這縣市　1秒爽離職','不要懷疑，就是你，快兌獎！財政部今（25）日公布7、8月期統一發票中獎號碼，幸運兒僅在超商萊爾富購買飲料，就爽中1000萬！\r\n財政部公布7、8月期統一發票中獎號碼，千萬特別獎為「21981893」；獎金200萬元的特獎號碼為「39597522」；頭獎（20萬元）3組分別為「09505831」、「54219897」、「17469638」。\r\n此次千萬大獎中，超商可說是最大贏家，其中萊爾富開出1000萬大獎，幸運兒在於新竹縣的湖口好客店，僅花費44元購買2瓶飲料，就爽中1000萬元特別獎，中獎門市地址位在：新竹縣湖口鄉中平路一段368、370號。','https://cc.tvbs.com.tw/img/upload/2022/04/13/20220413073326-bb3c86e3.jpg','2023-09-26 21:31:29.670694');
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `price` int(11) NOT NULL,
  `photo_url` varchar(200) NOT NULL,
  `link_url` varchar(200) NOT NULL,
  `c_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'滿意寶寶 極上呵護輕巧褲 箱購 (L-XL)',1439,'https://img.pchome.com.tw/cs/items/DAAO95A900GCX24/000001_1696239434.jpg','https://24h.pchome.com.tw/prod/DAAO95-A900GCX24','2023-10-03'),(2,'Lenovo 15.6吋文書',12990,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002094036_1-1-B-1000x1000.jpg','https://24h.pchome.com.tw/DHBF75-1900GIOTT','2023-10-03'),(3,'ASUS 27型 FHD 護眼螢幕',3588,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002100400_1-2-B-1000x1000.jpg','https://24h.pchome.com.tw/DSABE8','2023-10-03'),(4,'Razer Orochi V2 八岐大蛇靈刃 V2 無線電競滑鼠(水銀白) RZ01-03730400-R3A1',999,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928120606_1-3-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DCBF45','2023-10-03'),(5,'iPhone 15 256G',33400,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230926143031_1-4-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DYAJKL','2023-10-03'),(6,'DJI MINI 4 Pro 長續航暢飛套裝(DJI RC2)',33640,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002141436_1-5-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DGCS3L','2023-10-03'),(7,'Acer  i3 SSD W11電腦',13990,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927103203_1-6-B-1000x1000.jpg','https://24h.pchome.com.tw/DSAA2P-1900GO8T5','2023-10-03'),(8,'Acer Predator GM3500 2TB PCIe SSD',2599,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927142641_1-7-B-1000x1000.jpg','https://24h.pchome.com.tw/DRAHB9-A900GC66R','2023-10-03'),(9,'羅技Logitech SPOTLIGHT 簡報遙控器-香檳金',2700,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002104730_1-8-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DSAR26','2023-10-03'),(10,'ESR億色 iPhone 15 Pro 鏡頭支架磁吸殼',1599,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927192131_1-9-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DYARFS','2023-10-03'),(11,'EPSON L3210 高速三合一 連續供墨複合機',4288,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928181553_1-10-B-1000x1000.jpg','https://24h.pchome.com.tw/DCAE86-A900GARPN','2023-10-03'),(12,'ASUS 15.6吋效能筆電',29999,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927153351_1-11-B-1000x1000.jpg','https://24h.pchome.com.tw/DHAFON-1900GG4XV','2023-10-03'),(13,'ASUS TUF Gaming RTX 4070 12GB 顯示卡	',21090,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927142750_1-12-B-1000x1000.jpg','https://24h.pchome.com.tw/prod/DRADOG-1900GOBDO','2023-10-03'),(14,'羅技MX Mechanical 鍵盤 Mini ',3990,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002113823_1-13-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DSAR82','2023-10-03'),(15,'【2入組】UKKO PD 100W 數字顯示充電+傳輸線',299,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928140711_1-14-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DYAPGI','2023-10-03'),(16,'NS《薩爾達傳說 王國之淚》中文版 ',1490,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002133245_1-15-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DGBJMQ','2023-10-03'),(17,'Acer Swift Go 14吋OLED效能筆電',31900,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002095711_1-16-B-1000x1000.jpg','https://24h.pchome.com.tw/DHAEII-A900GHVBJ','2023-10-03'),(18,'WD 金標 8TB 企業級硬碟',7970,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927143128_1-17-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DRAB4M','2023-10-03'),(19,'【KINYO】1開3插三USB延長線',399,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928120740_1-18-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DSAO1F','2023-10-03'),(20,'SONY Xperia 10V (8G/128G)',10590,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928154846_1-19-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DYAWA0','2023-10-03'),(21,'酷碼Cooler Master CALIBER E1 電競椅(黑)',4588,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002095803_1-20-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DCBT0E','2023-10-03'),(22,'HP Probook 17.3吋商務筆電',29999,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927161507_1-21-B-1000x1000.jpg','https://24h.pchome.com.tw/DHAG7M-A900GDDDX','2023-10-03'),(23,'Toshiba A5 2TB 2.5吋行動硬碟',2190,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231003100658_1-22-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DRAA1U','2023-10-03'),(24,'Kdan PDF Windows買斷版',1290,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928145427_1-23-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DSAE2D','2023-10-03'),(25,'realme 11 Pro+ 5G (12G/512G) -綠野之城',13790,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928154432_1-24-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DYAA72','2023-10-03'),(26,'PHILIPS 智能錄音筆 VTR5102Pro',4590,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002135133_1-25-B-1000x1000.jpg','https://24h.pchome.com.tw/DGAF1D-A900FZ6LV','2023-10-03'),(27,'Apple 第六代 iPad mini 8.3 吋 256G WiFi 星光色 (MK7V3TA/A)	',20580,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002095935_1-26-B-1000x1000.jpg','https://24h.pchome.com.tw/DYAJK6-1900FYTKF','2023-10-03'),(28,'TP-Link Tapo C220 網路攝影機 ',1099,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230926185855_1-27-B-1000x1000.jpg','https://24h.pchome.com.tw/DRAN3B-A900GK7JI','2023-10-03'),(29,'免安裝電子螢光板(可升降款)/廣告牌/廣告板/發光板/LED手寫',990,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928185242_1-28-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DECD39','2023-10-03'),(30,'SAMSUNG Galaxy S22 (8G/128G)',15180,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928153222_1-29-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DYALI9','2023-10-03'),(31,'Yamaha TW-E3B 真無線藍牙耳機',1499,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927194656_1-30-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DYAQ0Z','2023-10-03'),(32,'Dyson Supersonic 吹風機 HD08 托帕石橙紅(附精美禮盒)',9999,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002093126_2-1-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DMBP01','2023-10-03'),(33,'Dyson 三合一涼暖空氣清淨機HP07(黑鋼)',16900,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002143743_2-2-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DMBF0B','2023-10-03'),(34,'irocks T07 Plus 人體工學椅',12500,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230923122710_2-3-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DQBJ4C','2023-10-03'),(35,'藏野匠【一鳥】雙鍋組28cm',699,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928155241_2-4-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DEAWUW','2023-10-03'),(36,'【GARMIN導航吸塵組】',5490,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928160108_2-5-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DXAO2V','2023-10-03'),(37,'BenQ 50型 Android 11 液晶顯示器',12900,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002091529_2-6-B-1000x1000.jpg','https://24h.pchome.com.tw/DPAD0O-A900FX3R3','2023-10-03'),(38,'LG 17公斤WiFi直立式變頻洗衣機',18810,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230925121715_2-7-B-1000x1000.jpg','https://24h.pchome.com.tw/DPAI1L-A900EVM89','2023-10-03'),(39,'BOSCH 18V 鋰電免碳刷震動電鑽配件套裝',5990,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928160637_2-8-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DQBA63','2023-10-03'),(40,'【EverClean 藍鑽】粗顆粒清香結塊貓砂22.5lb/10.2kg*2盒',1099,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928180830_2-9-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DEAKO2','2023-10-03'),(41,'【法國皇家】室內成貓IN27 10KG',2599,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928163816_2-10-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DEBVDV','2023-10-03'),(42,'美國富及第 Frigidaire 20L 美型微波爐 FKM-2022MW 白(香檳金手把)',1990,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230925185838_2-11-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DMBJ00','2023-10-03'),(43,'飛利浦 奈米級抗敏空氣清淨機 AC4558',9999,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927160328_2-12-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DMAC2O','2023-10-03'),(44,'HOPMA 三門二抽衣櫥',2868,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002161453_2-13-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DQCD3G','2023-10-03'),(45,'BRITA MAXTRA Plus 濾芯去水垢專家(10入裝)',2149,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002160514_2-14-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DEAY39','2023-10-03'),(46,'Ta-Da 泰達隨身椅 全新第二系列自動手杖椅',2180,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928184938_2-15-B-1000x1000.jpg','https://24h.pchome.com.tw/DEBQOS-A900DVZMZ','2023-10-03'),(47,'Oral-B-Smart Professional 智能藍芽電動牙刷',3511,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002150135_2-16-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DMBA0K','2023-10-03'),(48,'國際牌 366公升雙門冰箱',19341,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230925092137_2-17-B-1000x1000.jpg','https://24h.pchome.com.tw/DPAC1T-A900FLZQU','2023-10-03'),(49,'美國TCP 10W高亮版節能燈泡-12入',499,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002161000_2-18-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DQBN3H','2023-10-03'),(50,'康寧900ML拉麵4件組',599,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928155415_2-19-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DEBS12','2023-10-03'),(51,'Adidas 運動鞋',1499,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927163808_2-20-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DXAXAL','2023-10-03'),(52,'Mdovia Detruire 智能偵測 全方位廚餘機',3990,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002104802_2-21-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DMAG0K','2023-10-03'),(53,'惠而浦 10.5L節能除濕機',4999,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002094220_2-22-B-1000x1000.jpg','https://24h.pchome.com.tw/DMAU0L-A900AJ8E2','2023-10-03'),(54,'AOTTO 啞光五層抽屜收納櫃',999,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928150900_2-23-B-1000x1000.jpg','https://24h.pchome.com.tw/DEBAFX-A900G8Z67','2023-10-03'),(55,'MUJI無印良品 PP收納盒2入',1298,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002182555_2-24-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DEDK2L','2023-10-03'),(56,'輝葉 miniV美型口袋按摩槍(HY-10599)',1999,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002140917_2-25-B-1000x1000.jpg','https://24h.pchome.com.tw/prod/preview/v1/DMADFG-A900FNYZ6','2023-10-03'),(57,'Roborock 石頭掃地機器人 Q7 Max+',12999,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230926164601_2-26-B-1000x1000.jpg','https://24h.pchome.com.tw/DMBT01-A900GNO6C','2023-10-03'),(58,'樂天Kobo Clara 2E【16GB 深夜藍】6吋電子書閱讀器',4888,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002160526_2-27-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DCBR0E','2023-10-03'),(59,'3M 兒童安全牙線棒超值組-6包',499,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002160330_2-28-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DAAN8I','2023-10-03'),(60,'Muti Living維他命過濾蓮蓬頭_2入組',1299,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927164206_2-29-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DEDW0J','2023-10-03'),(61,'【innogoods】自動感應給皂機',629,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928175419_2-30-B-1000x1000.jpg','https://24h.pchome.com.tw/DEDG00-A900DE2D5','2023-10-03'),(62,'五月花 新柔韌抽取衛生紙 (110抽x12包x6串/箱)_2015升級版',859,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928185254_3-1-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DAAG0U','2023-10-03'),(63,'【OOHA】氣泡飲 水蜜桃烏龍茶 寶特瓶500ml x24入/箱',499,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928195628_3-2-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DBABHA','2023-10-03'),(64,'KIEHLS 金盞花植物精華化妝水250ml',699,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928160236_3-3-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DDAD8M','2023-10-03'),(65,'【老協珍】人蔘精禮盒 (60ml x14入x2盒)',1399,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928103936_3-4-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DBDJ05','2023-10-03'),(66,'Timberland 鞋款/服飾',790,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231001045405_3-5-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DIDD2C','2023-10-03'),(67,'滿意寶寶 極上呵護紙尿褲(M-XL)',1899,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927114907_3-6-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DAAO3W','2023-10-03'),(68,'UCC 職人珈琲-金質炭燒咖啡豆400gx4包',749,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928200132_3-7-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DBATC0','2023-10-03'),(69,'品木宣言 青春無敵健康光潤機能乳液100ml',950,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928160938_3-8-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DDAD0A','2023-10-03'),(70,'Jacky Wu 日安玩美紅藜麥穀物粉 30包/盒',2780,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928174218_3-9-B-1000x1000.jpg','https://24h.pchome.com.tw/DBBB7F-A900GN9C0','2023-10-03'),(71,'GILDAN美國棉 亞規棉柔中性素面圓筒T恤-深麻灰',350,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002183738_3-10-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DICU7B','2023-10-03'),(72,'BOSCH 洗碗機專用洗碗錠180入組 (30x20g/盒x6)',1200,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928160322_3-11-B-1000x1000.jpg-rename.png','https://24h.pchome.com.tw/store/DAAZ44','2023-10-03'),(73,'【卡迪那95℃】北海道風味薯條-原味(18gx5包) x3',199,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928193905_3-12-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DBAC23','2023-10-03'),(74,'理膚寶水 淨痘無瑕極效精華組',1646,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230926171037_3-13-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DDCA10','2023-10-03'),(75,'中衛 雙鋼印醫療口罩(50片/盒)',250,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002163601_3-14-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DABC7Y','2023-10-03'),(76,'LONGCHAMP 再生帆布二用包(海軍藍)',5389,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002180821_3-15-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DICK8E','2023-10-03'),(77,'【好神拖Supamop】輕巧手壓旋轉拖把組(1布)',788,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928183125_3-16-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DAAC4Z','2023-10-03'),(78,'日清食品 中杯麵-海鮮75gx10',699,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928185816_3-17-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DBAY41','2023-10-03'),(79,'艾瑪絲 洗髮精1000mL',880,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231003103712_3-18-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DDBX0U','2023-10-03'),(80,'《天地合補》葉黃素功能飲(60ml*18入)x3盒',2889,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002101323_3-19-B-1000x1000.jpg','https://24h.pchome.com.tw/DBBB0W-1900A9SMH','2023-10-03'),(81,'Injinji 吸排五趾短襪 ',520,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231003102939_3-20-B-1000x1000.jpg','https://24h.pchome.com.tw/DICGDR-A900AW7TR','2023-10-03'),(82,'蘇菲 超熟睡 內褲型衛生棉 M / L / XL (2片 x 12包) 箱購',589,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928185409_3-21-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DAAB22','2023-10-03'),(83,'【義豐】蔥油派(10片1組)3組',820,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002154903_3-22-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DBCX0Q','2023-10-03'),(84,'ITO 抽取式洗臉巾3入組',588,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230922172611_3-23-B-1000x1000.jpg','https://24h.pchome.com.tw/DDBK9P-A900GCVEC','2023-10-03'),(85,'天然所 帝王神力瑪卡 KING POWER - 28包/盒',659,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927114155_3-24-B-1000x1000.jpg','https://24h.pchome.com.tw/DBAW4Z-A9009GJSW','2023-10-03'),(86,'王品集團燒肉餐廳1000元通用券(Oh my!原燒、肉次方、最肉) (一次抵用型)(限內用)',888,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20231002093452_3-25-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DBCRJZ','2023-10-03'),(87,'小獅王辛巴 UDI H1消毒鍋',3599,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928112023_3-26-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DWAC6D','2023-10-03'),(88,'威德in果凍-能量 (白葡萄口味)-180g x6入/盒x4盒',749,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928195741_3-27-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DBABCA','2023-10-03'),(89,'貝利達 全方位抗敏牙膏四入組',700,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230926180029_3-28-B-1000x1000.jpg','https://24h.pchome.com.tw/store/DAAL65','2023-10-03'),(90,'Mass 家用指尖血氧器',339,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230927192448_3-29-B-1000x1000.jpg','https://24h.pchome.com.tw/DAAH7X-A900F4TAX','2023-10-03'),(91,'tokuyo 涼峰按摩車用墊TH-273',1780,'https://fs-c.ecimg.tw/img/h24/v1/layout/onsale/20231003/20230928174129_3-30-B-1000x1000.jpg','https://24h.pchome.com.tw/DEAD0B-A900ET40Q','2023-10-03');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-03 21:44:45
