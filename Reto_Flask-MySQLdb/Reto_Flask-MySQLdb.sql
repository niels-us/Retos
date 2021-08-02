-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.33 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para db_sistemapos
CREATE DATABASE IF NOT EXISTS `db_sistemapos` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `db_sistemapos`;

-- Volcando estructura para tabla db_sistemapos.categorias
CREATE TABLE IF NOT EXISTS `categorias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `categoria` varchar(255) DEFAULT '0',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COMMENT='Mostrar Categorias';

-- Volcando datos para la tabla db_sistemapos.categorias: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` (`id`, `categoria`) VALUES
	(4, 'Deporte'),
	(5, 'Tecnologia'),
	(6, 'Dormitorio'),
	(7, 'Mascotas'),
	(8, 'Oficina'),
	(9, 'Juguetes');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_doc_ide_id` int(11) NOT NULL DEFAULT '0' COMMENT 'Tipo Documento - referencia a la tabla tipo_doc_ide',
  `nro_doc` varchar(20) NOT NULL DEFAULT '0' COMMENT 'Numero Documento',
  `nombre` varchar(255) DEFAULT '0',
  `telefono` varchar(20) DEFAULT '0',
  `email` varchar(20) DEFAULT '0',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `u_documento_identidad` (`tipo_doc_ide_id`,`nro_doc`) USING BTREE,
  CONSTRAINT `FK_clientes_tipo_doc_ide` FOREIGN KEY (`tipo_doc_ide_id`) REFERENCES `tipo_doc_ide` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COMMENT='Registrar los clientes de sistema';

-- Volcando datos para la tabla db_sistemapos.clientes: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` (`id`, `tipo_doc_ide_id`, `nro_doc`, `nombre`, `telefono`, `email`) VALUES
	(1, 1, '44622152', 'niels', '980400440', 'niels_us@outlook.com'),
	(2, 1, '23433452', 'juan', '98989898', 'juan_dr@gmail.com');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL DEFAULT '',
  `precio` double NOT NULL DEFAULT '0',
  `stock` bigint(20) DEFAULT '0',
  `id_categorias` int(5) NOT NULL COMMENT 'Lista de categorias',
  PRIMARY KEY (`id`),
  KEY `categorias` (`id_categorias`),
  CONSTRAINT `categorias` FOREIGN KEY (`id_categorias`) REFERENCES `categorias` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla db_sistemapos.productos: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`id`, `nombre`, `precio`, `stock`, `id_categorias`) VALUES
	(1, 'USB', 25, 1000, 5),
	(2, 'Canilleras', 50, 500, 4),
	(3, 'Cuaderno', 2, 200, 8),
	(4, 'Mouse', 35, 1500, 5),
	(5, 'Notebook', 3500, 2500, 5),
	(6, 'Pelota', 50, 2050, 4),
	(7, 'Teclado', 55, 1000, 5),
	(8, 'PortaMina', 35, 1233, 8),
	(9, 'Borrardor', 1, 1000, 8);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.tipo_doc_ide
CREATE TABLE IF NOT EXISTS `tipo_doc_ide` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla db_sistemapos.tipo_doc_ide: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `tipo_doc_ide` DISABLE KEYS */;
INSERT INTO `tipo_doc_ide` (`id`, `nombre`) VALUES
	(1, 'DNI'),
	(2, 'RUC'),
	(3, 'CARNET EXTRANJERIA');
/*!40000 ALTER TABLE `tipo_doc_ide` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
