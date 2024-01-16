-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 15, 2024 at 09:56 PM
-- Server version: 8.0.35-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_go_dev`
--

-- --------------------------------------------------------

--
-- Stand-in structure for view `Active_Drivers`
-- (See below for the actual view)
--
CREATE TABLE `Active_Drivers` (
`Driver_ID` int
,`Location_Lat` decimal(8,6)
,`Location_Lon` decimal(9,6)
,`Per_Mile` decimal(10,2)
,`Per_Minute` decimal(10,2)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `Requests_Bids`
-- (See below for the actual view)
--
CREATE TABLE `Requests_Bids` (
`Bid_ID` int
,`Request_ID` int
);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_Auth`
--

CREATE TABLE `tbl_Auth` (
  `_username` int NOT NULL,
  `_password` varchar(50) NOT NULL,
  `_status` int NOT NULL,
  `_type` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_Bids`
--

CREATE TABLE `tbl_Bids` (
  `Bid_ID` int NOT NULL,
  `Bid_Timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Driver_ID` int NOT NULL,
  `Request_ID` int NOT NULL,
  `Per_Mile` decimal(5,2) NOT NULL,
  `Per_Min` decimal(5,2) NOT NULL,
  `Est_Cost` decimal(10,2) NOT NULL,
  `Est_Pickup_Time` decimal(10,2) NOT NULL,
  `Status` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_Dictionary`
--

CREATE TABLE `tbl_Dictionary` (
  `Type` varchar(25) NOT NULL,
  `Name` varchar(25) NOT NULL,
  `Value` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_Drivers`
--

CREATE TABLE `tbl_Drivers` (
  `User_ID` int NOT NULL,
  `First_Name` varchar(50) NOT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Address2` varchar(30) NOT NULL,
  `City` varchar(50) NOT NULL,
  `State` varchar(12) NOT NULL,
  `Zip` varchar(12) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Status` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_Driver_Bid_Profiles`
--

CREATE TABLE `tbl_Driver_Bid_Profiles` (
  `Profile_ID` int NOT NULL,
  `Driver_ID` int NOT NULL,
  `Profile_Name` varchar(50) NOT NULL,
  `Per_Mile` decimal(10,2) NOT NULL,
  `Per_Minute` decimal(10,2) NOT NULL,
  `Active` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_Driver_Sessions`
--

CREATE TABLE `tbl_Driver_Sessions` (
  `Session_ID` int NOT NULL,
  `Driver_ID` int NOT NULL,
  `Location_Lat` decimal(8,6) NOT NULL,
  `Location_Lon` decimal(9,6) NOT NULL,
  `Status` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_Riders`
--

CREATE TABLE `tbl_Riders` (
  `User_ID` int NOT NULL,
  `First_Name` varchar(50) NOT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Address2` varchar(25) NOT NULL,
  `City` varchar(50) NOT NULL,
  `State` varchar(10) NOT NULL,
  `Zip` varchar(12) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_Trips`
--

CREATE TABLE `tbl_Trips` (
  `Trip_ID` int NOT NULL,
  `Trip_Request_ID` int NOT NULL,
  `Bid_ID` int NOT NULL,
  `Trip_Date` date DEFAULT NULL,
  `Start_Time` time DEFAULT NULL,
  `Start_Lat` decimal(8,6) DEFAULT NULL,
  `Start_Lon` decimal(9,6) DEFAULT NULL,
  `End_Time` time DEFAULT NULL,
  `End_Lat` decimal(8,6) DEFAULT NULL,
  `End_Lon` decimal(9,6) DEFAULT NULL,
  `Actual_Distance` decimal(4,2) DEFAULT NULL,
  `Actual_Duration` decimal(6,2) DEFAULT NULL,
  `Toll_Cost` decimal(5,2) DEFAULT NULL,
  `Total_Cost` decimal(5,2) DEFAULT NULL,
  `Status` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_Trip_Request`
--

CREATE TABLE `tbl_Trip_Request` (
  `Request_ID` int NOT NULL,
  `Rider_ID` int NOT NULL,
  `Start_Lat` decimal(8,6) NOT NULL,
  `Start_Lon` decimal(9,6) NOT NULL,
  `End_Lat` decimal(8,6) NOT NULL,
  `End_Lon` decimal(9,6) NOT NULL,
  `Create_Time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `Est_Distance` decimal(10,2) NOT NULL,
  `Est_Duration` time(2) NOT NULL,
  `Status` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure for view `Active_Drivers`
--
DROP TABLE IF EXISTS `Active_Drivers`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `Active_Drivers`  AS SELECT `tbl_Driver_Sessions`.`Driver_ID` AS `Driver_ID`, `tbl_Driver_Sessions`.`Location_Lat` AS `Location_Lat`, `tbl_Driver_Sessions`.`Location_Lon` AS `Location_Lon`, `tbl_Driver_Bid_Profiles`.`Per_Mile` AS `Per_Mile`, `tbl_Driver_Bid_Profiles`.`Per_Minute` AS `Per_Minute` FROM (`tbl_Driver_Sessions` join `tbl_Driver_Bid_Profiles` on((`tbl_Driver_Sessions`.`Driver_ID` = `tbl_Driver_Bid_Profiles`.`Driver_ID`))) WHERE (`tbl_Driver_Bid_Profiles`.`Active` = 1) ;

-- --------------------------------------------------------

--
-- Structure for view `Requests_Bids`
--
DROP TABLE IF EXISTS `Requests_Bids`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `Requests_Bids`  AS SELECT `tbl_Bids`.`Bid_ID` AS `Bid_ID`, `tbl_Trip_Request`.`Request_ID` AS `Request_ID` FROM (`tbl_Bids` join `tbl_Trip_Request` on((`tbl_Bids`.`Request_ID` = `tbl_Trip_Request`.`Request_ID`))) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_Bids`
--
ALTER TABLE `tbl_Bids`
  ADD PRIMARY KEY (`Bid_ID`);

--
-- Indexes for table `tbl_Drivers`
--
ALTER TABLE `tbl_Drivers`
  ADD PRIMARY KEY (`User_ID`);

--
-- Indexes for table `tbl_Driver_Bid_Profiles`
--
ALTER TABLE `tbl_Driver_Bid_Profiles`
  ADD PRIMARY KEY (`Profile_ID`);

--
-- Indexes for table `tbl_Driver_Sessions`
--
ALTER TABLE `tbl_Driver_Sessions`
  ADD PRIMARY KEY (`Session_ID`);

--
-- Indexes for table `tbl_Riders`
--
ALTER TABLE `tbl_Riders`
  ADD PRIMARY KEY (`User_ID`);

--
-- Indexes for table `tbl_Trips`
--
ALTER TABLE `tbl_Trips`
  ADD PRIMARY KEY (`Trip_ID`);

--
-- Indexes for table `tbl_Trip_Request`
--
ALTER TABLE `tbl_Trip_Request`
  ADD PRIMARY KEY (`Request_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_Bids`
--
ALTER TABLE `tbl_Bids`
  MODIFY `Bid_ID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_Drivers`
--
ALTER TABLE `tbl_Drivers`
  MODIFY `User_ID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_Driver_Bid_Profiles`
--
ALTER TABLE `tbl_Driver_Bid_Profiles`
  MODIFY `Profile_ID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_Driver_Sessions`
--
ALTER TABLE `tbl_Driver_Sessions`
  MODIFY `Session_ID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_Riders`
--
ALTER TABLE `tbl_Riders`
  MODIFY `User_ID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_Trips`
--
ALTER TABLE `tbl_Trips`
  MODIFY `Trip_ID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_Trip_Request`
--
ALTER TABLE `tbl_Trip_Request`
  MODIFY `Request_ID` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
