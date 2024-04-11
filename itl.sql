-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-04-2024 a las 20:19:48
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `itl`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carreras`
--

CREATE TABLE `carreras` (
  `IDCarrera` varchar(4) NOT NULL,
  `Nombre` varchar(90) NOT NULL,
  `Semestres` smallint(1) NOT NULL DEFAULT 9
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Almacena los datos de la carrera';

--
-- Volcado de datos para la tabla `carreras`
--

INSERT INTO `carreras` (`IDCarrera`, `Nombre`, `Semestres`) VALUES
('CBS', 'CIENCIAS BASICAS', 0),
('IELC', 'Ingeniería Electrónica', 9),
('IEME', 'Ingeniería ELECTROMECANICA', 10),
('IGEM', 'Ingeniería en Gestión Empresarial', 9),
('IIND', 'Ingeniería Industrial', 9),
('ILOG', 'Ingeniería en Logística', 9),
('IMCT', 'Ingeniería Mecatrónica', 9),
('ISIC', 'Ingeniería en Sistemas Computacionales', 9),
('ITIC', 'Ingeniería en Tecnologías de la Información y Comunicaciones', 9);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidades`
--

CREATE TABLE `especialidades` (
  `IDEspecialidad` varchar(3) NOT NULL,
  `IDCarrera` varchar(4) NOT NULL,
  `Nombre` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Almacena los datos de las especialidades';

--
-- Volcado de datos para la tabla `especialidades`
--

INSERT INTO `especialidades` (`IDEspecialidad`, `IDCarrera`, `Nombre`) VALUES
('CBS', 'CBS', 'Ciencias Básicas2'),
('CIP', 'IGEM', 'Gestión de la calidad e innovación de procesos 2024'),
('DAE', 'ISIC', 'Desarrollo de aplicaciones empresariales'),
('EIN', 'ISIC', 'Entornos Inteligentes'),
('GST', 'ITIC', 'Gestión de Servicios de T.I. en Ambientes Empresariales'),
('IMC', 'IIND', 'Ingeniería en manufactura y calidad'),
('MAP', 'IIND', 'Manufactura en artículos de piel'),
('PRA', 'IIND', 'Producción de acero'),
('RAE', 'ISIC', 'Redes Convergentes de Alta Disponibilidad');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `IDMateria` varchar(8) NOT NULL,
  `IDCarrera` varchar(4) NOT NULL,
  `Nombre` varchar(90) NOT NULL,
  `IDEspecialidad` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Almacena los datos de las materias';

--
-- Volcado de datos para la tabla `materias`
--

INSERT INTO `materias` (`IDMateria`, `IDCarrera`, `Nombre`, `IDEspecialidad`) VALUES
('ACA-0907', 'ILOG', 'Taller de ética', 'CBS'),
('LOC-0919', 'ILOG', 'Introducción a la ingeniería en logística', 'CBS'),
('LOC-0927', 'ILOG', 'Química', 'CBS');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carreras`
--
ALTER TABLE `carreras`
  ADD PRIMARY KEY (`IDCarrera`);

--
-- Indices de la tabla `especialidades`
--
ALTER TABLE `especialidades`
  ADD PRIMARY KEY (`IDEspecialidad`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`IDMateria`,`IDCarrera`) USING BTREE;

--
-- Restricciones para tablas volcadas
--


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
