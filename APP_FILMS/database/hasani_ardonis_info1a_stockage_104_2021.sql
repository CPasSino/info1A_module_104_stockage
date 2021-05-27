DROP DATABASE IF EXISTS hasani_ardonis_info1a_stockage ;
CREATE DATABASE IF NOT EXISTS hasani_ardonis_info1a_stockage ;
USE hasani_ardonis_info1a_stockage ;
-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Jeu 27 Mai 2021 à 07:26
-- Version du serveur :  5.7.11
-- Version de PHP :  5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `hasani_ardonis_info1a_stockage`
--

-- --------------------------------------------------------

--
-- Structure de la table `t_customer`
--

CREATE TABLE `t_customer` (
  `id_customer` int(11) NOT NULL,
  `first_name_customer` varchar(30) NOT NULL,
  `last_name_customer` varchar(30) NOT NULL,
  `fk_sector` int(11) NOT NULL,
  `phone_customer` varchar(12) NOT NULL,
  `personal_number_customer` varchar(8) NOT NULL,
  `location_customer` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_device`
--

CREATE TABLE `t_device` (
  `id_device` int(11) NOT NULL,
  `fk_model` int(11) NOT NULL,
  `serial_number_device` varchar(50) NOT NULL,
  `fk_status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_model`
--

CREATE TABLE `t_model` (
  `id_model` int(11) NOT NULL,
  `name_model` varchar(20) NOT NULL,
  `fk_sector` int(11) NOT NULL,
  `bought_date_model` date NOT NULL,
  `guarantee_date_model` date NOT NULL,
  `description_model` varchar(100) NOT NULL,
  `quantite_model` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_sector`
--

CREATE TABLE `t_sector` (
  `id_sector` int(11) NOT NULL,
  `name_sector` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_status`
--

CREATE TABLE `t_status` (
  `id_status` int(11) NOT NULL,
  `name_status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_use`
--

CREATE TABLE `t_use` (
  `id_start_use` int(11) NOT NULL,
  `fk_device` int(11) NOT NULL,
  `fk_customer` int(11) NOT NULL,
  `date_start_use` date NOT NULL,
  `date_end_use` date NOT NULL,
  `reason_end_use` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Index pour les tables exportées
--

--
-- Index pour la table `t_customer`
--
ALTER TABLE `t_customer`
  ADD PRIMARY KEY (`id_customer`);

--
-- Index pour la table `t_device`
--
ALTER TABLE `t_device`
  ADD PRIMARY KEY (`id_device`),
  ADD UNIQUE KEY `serial_number_device` (`serial_number_device`);

--
-- Index pour la table `t_model`
--
ALTER TABLE `t_model`
  ADD PRIMARY KEY (`id_model`),
  ADD UNIQUE KEY `UNIQUE` (`name_model`);

--
-- Index pour la table `t_sector`
--
ALTER TABLE `t_sector`
  ADD PRIMARY KEY (`id_sector`),
  ADD UNIQUE KEY `UNIQUE` (`name_sector`);

--
-- Index pour la table `t_status`
--
ALTER TABLE `t_status`
  ADD PRIMARY KEY (`id_status`),
  ADD UNIQUE KEY `UNIQUE` (`name_status`);

--
-- Index pour la table `t_use`
--
ALTER TABLE `t_use`
  ADD PRIMARY KEY (`id_start_use`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `t_customer`
--
ALTER TABLE `t_customer`
  MODIFY `id_customer` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT pour la table `t_device`
--
ALTER TABLE `t_device`
  MODIFY `id_device` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT pour la table `t_model`
--
ALTER TABLE `t_model`
  MODIFY `id_model` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT pour la table `t_sector`
--
ALTER TABLE `t_sector`
  MODIFY `id_sector` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT pour la table `t_status`
--
ALTER TABLE `t_status`
  MODIFY `id_status` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT pour la table `t_use`
--
ALTER TABLE `t_use`
  MODIFY `id_start_use` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
