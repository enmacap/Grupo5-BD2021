-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 31-05-2021 a las 13:09:03
-- Versión del servidor: 10.3.27-MariaDB-0+deb10u1
-- Versión de PHP: 7.3.27-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdfuncionario`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `id_departamento` int(11) NOT NULL,
  `dpnombre` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`id_departamento`, `dpnombre`) VALUES
(1, 'RRHH'),
(2, 'hgvhgvg'),
(3, 'caja'),
(4, 'caja2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `funcionario`
--

CREATE TABLE `funcionario` (
  `id_funcionario` int(11) NOT NULL,
  `ci` varchar(150) DEFAULT NULL,
  `nombre` varchar(150) DEFAULT NULL,
  `apellido` varchar(150) DEFAULT NULL,
  `correo` varchar(150) DEFAULT NULL,
  `infectado` varchar(20) DEFAULT NULL,
  `departamento_id` int(11) DEFAULT NULL,
  `tarjeta_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `funcionario`
--

INSERT INTO `funcionario` (`id_funcionario`, `ci`, `nombre`, `apellido`, `correo`, `infectado`, `departamento_id`, `tarjeta_id`) VALUES
(1, '555', 'Manu', 'Cap', 'sdfd@blabla.com', '1', 1, 1),
(2, '5343', 'hola', 'cha', 'sdfsd', '1', 1, 1),
(3, '5343', 'dfg', 'dsfsa', 'dsf', '1', 1, 1),
(4, '65665', 'SDFS', 'DSF', 'FSDF', '1', 1, 1),
(5, '55', 'BN', 'G', 'HGH', '1', 2, 2),
(6, '552sa', 'f', 'f', 'f', '1', 1, 1),
(7, '11111', 'mnkjnb', 'n b', ' mn', '1', 1, 1),
(8, '1111', 'hola', 'chau', 'sss@', '1', 1, 1),
(9, '555', 'df', 'dsf', 'df', 'df', 1, 1),
(10, '56', 'dasd', 'asda', 'sd', '1', 2, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tarjeta`
--

CREATE TABLE `tarjeta` (
  `id_tarjeta` int(11) NOT NULL,
  `codigo_rfid` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tarjeta`
--

INSERT INTO `tarjeta` (`id_tarjeta`, `codigo_rfid`) VALUES
(1, 'fdgzxdfg333'),
(2, '2516541'),
(3, '544646'),
(4, '56566'),
(5, '26526'),
(6, '56555561'),
(7, '45345');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`id_departamento`);

--
-- Indices de la tabla `funcionario`
--
ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`id_funcionario`),
  ADD KEY `departamento_id` (`departamento_id`),
  ADD KEY `tarjeta_id` (`tarjeta_id`);

--
-- Indices de la tabla `tarjeta`
--
ALTER TABLE `tarjeta`
  ADD PRIMARY KEY (`id_tarjeta`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `departamento`
--
ALTER TABLE `departamento`
  MODIFY `id_departamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de la tabla `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `id_funcionario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT de la tabla `tarjeta`
--
ALTER TABLE `tarjeta`
  MODIFY `id_tarjeta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `funcionario`
--
ALTER TABLE `funcionario`
  ADD CONSTRAINT `funcionario_ibfk_1` FOREIGN KEY (`departamento_id`) REFERENCES `departamento` (`id_departamento`),
  ADD CONSTRAINT `funcionario_ibfk_2` FOREIGN KEY (`tarjeta_id`) REFERENCES `tarjeta` (`id_tarjeta`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
