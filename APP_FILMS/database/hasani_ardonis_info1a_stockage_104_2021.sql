DROP DATABASE IF EXISTS hasani_ardonis_info1a_stockage ;
CREATE DATABASE IF NOT EXISTS hasani_ardonis_info1a_stockage ;
USE hasani_ardonis_info1a_stockage ;

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

--
-- Contenu de la table `t_customer`
--

INSERT INTO `t_customer` (`id_customer`, `first_name_customer`, `last_name_customer`, `fk_sector`, `phone_customer`, `personal_number_customer`, `location_customer`) VALUES
(2, 'olive', 'zuc', 4, '65', '3423', '1'),
(4, 'yannock', 'widper', 3, '4', '45345345', '122311'),
(6, 'ardoise', 'hasano', 14, '7', '123123', '3104');

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

--
-- Contenu de la table `t_device`
--

INSERT INTO `t_device` (`id_device`, `fk_model`, `serial_number_device`, `fk_status`) VALUES
(1, 2, 'JHS98E456H498', 'Marche bien'),
(2, 1, 'KHD8745NBIWEZ', '0'),
(7, 2, 'JKDSHZ985ZE', '0'),
(8, 1, 'DJFSHDFSF74', '0'),
(12, 1, 'odjpjd887dj', '1');

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
  `description_model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_model`
--

INSERT INTO `t_model` (`id_model`, `name_model`, `fk_sector`, `bought_date_model`, `guarantee_date_model`, `description_model`) VALUES
(2, 'un_g_2LOQ', 0, '0000-00-00', '0000-00-00', ''),
(3, 'dasd', 0, '0000-00-00', '0000-00-00', '');

-- --------------------------------------------------------

--
-- Structure de la table `t_sector`
--

CREATE TABLE `t_sector` (
  `id_sector` int(11) NOT NULL,
  `name_sector` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_sector`
--

INSERT INTO `t_sector` (`id_sector`, `name_sector`) VALUES
(2, 'prof');

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
  `date_start_use` datetime NOT NULL,
  `date_end_use` datetime NOT NULL,
  `reason_end_use` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_use`
--

INSERT INTO `t_use` (`id_start_use`, `fk_device`, `fk_customer`, `Date_start_use`, `date_end_use`, `reason_end_use`) VALUES
(1, 1, 2, '2021-03-03 00:00:00', '0000-00-00 00:00:00', ''),
(2, 2, 1, '2021-03-26 00:00:00', '0000-00-00 00:00:00', '');

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
  MODIFY `id_customer` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT pour la table `t_device`
--
ALTER TABLE `t_device`
  MODIFY `id_device` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT pour la table `t_model`
--
ALTER TABLE `t_model`
  MODIFY `id_model` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_sector`
--
ALTER TABLE `t_sector`
  MODIFY `id_sector` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT pour la table `t_status`
--
ALTER TABLE `t_status`
  MODIFY `id_status` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_use`
--
ALTER TABLE `t_use`
  MODIFY `id_start_use` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
