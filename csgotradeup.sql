-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 18, 2022 at 09:08 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `csgotradeup`
--

-- --------------------------------------------------------

--
-- Table structure for table `classified`
--

CREATE TABLE `classified` (
  `ID` int(11) NOT NULL,
  `SKIN_ID` varchar(60) NOT NULL,
  `QUALITY` varchar(60) NOT NULL,
  `PRICE` varchar(60) NOT NULL,
  `COLLECTION` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `consumer`
--

CREATE TABLE `consumer` (
  `ID` int(60) NOT NULL,
  `SKIN_ID` varchar(60) NOT NULL,
  `QUALITY` varchar(60) NOT NULL,
  `PRICE` varchar(60) NOT NULL,
  `COLLECTION` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `covert`
--

CREATE TABLE `covert` (
  `ID` int(11) NOT NULL,
  `SKIN_ID` varchar(60) NOT NULL,
  `QUALITY` varchar(60) NOT NULL,
  `PRICE` varchar(60) NOT NULL,
  `COLLECTION` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `error`
--

CREATE TABLE `error` (
  `ID` varchar(60) NOT NULL,
  `ERROR` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `industrial`
--

CREATE TABLE `industrial` (
  `ID` int(11) NOT NULL,
  `SKIN_ID` varchar(60) NOT NULL,
  `QUALITY` varchar(60) NOT NULL,
  `PRICE` varchar(60) NOT NULL,
  `COLLECTION` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `milspec`
--

CREATE TABLE `milspec` (
  `ID` int(11) NOT NULL,
  `SKIN_ID` varchar(60) NOT NULL,
  `QUALITY` varchar(60) NOT NULL,
  `PRICE` varchar(60) NOT NULL,
  `COLLECTION` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `restricted`
--

CREATE TABLE `restricted` (
  `ID` int(11) NOT NULL,
  `SKIN_ID` varchar(60) NOT NULL,
  `QUALITY` varchar(60) NOT NULL,
  `PRICE` varchar(60) NOT NULL,
  `COLLECTION` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tradeup`
--

CREATE TABLE `tradeup` (
  `profitability` varchar(60) NOT NULL,
  `cost_ingredient` varchar(60) NOT NULL,
  `cost_resault` varchar(60) NOT NULL,
  `skin_id_1` varchar(60) NOT NULL,
  `skin_cost_1` varchar(60) NOT NULL,
  `skin_id_2` varchar(60) NOT NULL,
  `skin_cost_2` varchar(60) NOT NULL,
  `skin_id_3` varchar(60) NOT NULL,
  `skin_cost_3` varchar(60) NOT NULL,
  `skin_id_4` varchar(60) NOT NULL,
  `skin_cost_4` varchar(60) NOT NULL,
  `skin_id_5` varchar(60) NOT NULL,
  `skin_cost_5` varchar(60) NOT NULL,
  `from_to` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `classified`
--
ALTER TABLE `classified`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `consumer`
--
ALTER TABLE `consumer`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `covert`
--
ALTER TABLE `covert`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `industrial`
--
ALTER TABLE `industrial`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `milspec`
--
ALTER TABLE `milspec`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `restricted`
--
ALTER TABLE `restricted`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `classified`
--
ALTER TABLE `classified`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `consumer`
--
ALTER TABLE `consumer`
  MODIFY `ID` int(60) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `covert`
--
ALTER TABLE `covert`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `industrial`
--
ALTER TABLE `industrial`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `milspec`
--
ALTER TABLE `milspec`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `restricted`
--
ALTER TABLE `restricted`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
