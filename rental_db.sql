-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 29, 2024 at 05:19 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rental_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `car`
--

CREATE TABLE `car` (
  `car_id` int(11) NOT NULL,
  `car_brand` text NOT NULL,
  `car_name` text NOT NULL,
  `car_type` text NOT NULL,
  `car_trans` text NOT NULL,
  `car_year` int(11) NOT NULL,
  `car_seats` int(11) NOT NULL,
  `car_lugg` int(11) NOT NULL,
  `car_price` int(11) NOT NULL,
  `provider_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car`
--

INSERT INTO `car` (`car_id`, `car_brand`, `car_name`, `car_type`, `car_trans`, `car_year`, `car_seats`, `car_lugg`, `car_price`, `provider_id`) VALUES
(1, 'Toyota', 'Avanza', 'MPV', 'Manual', 2020, 7, 2, 500000, 1),
(2, 'Honda', 'Brio', 'Hatchback', 'Automatic', 2019, 5, 1, 300000, 1),
(3, 'Ford', 'Fiesta', 'Hatchback', 'Automatic', 2018, 5, 2, 400000, 2),
(4, 'Chevrolet', 'Spark', 'Hatchback', 'Manual', 2017, 5, 1, 350000, 2),
(5, 'Nissan', 'X-Trail', 'SUV', 'Automatic', 2021, 7, 3, 600000, 3),
(6, 'BMW', 'X5', 'SUV', 'Automatic', 2019, 5, 4, 900000, 3),
(7, 'Mercedes-Benz', 'C-Class', 'Sedan', 'Automatic', 2022, 5, 3, 1000000, 4),
(8, 'Toyota', 'Rush', 'SUV', 'Manual', 2022, 6, 3, 500000, 4);

-- --------------------------------------------------------

--
-- Table structure for table `driver`
--

CREATE TABLE `driver` (
  `driver_id` int(11) NOT NULL,
  `driver_name` text NOT NULL,
  `driver_gender` text NOT NULL,
  `driver_age` int(11) NOT NULL,
  `driver_phone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `driver`
--

INSERT INTO `driver` (`driver_id`, `driver_name`, `driver_gender`, `driver_age`, `driver_phone`) VALUES
(1, 'Budi', 'Male', 35, 2147483647),
(2, 'Siti', 'Female', 28, 2147483647),
(3, 'Siti', 'Female', 32, 2147483647),
(4, 'Tono', 'Male', 45, 2147483647),
(5, 'Rina', 'Female', 29, 2147483647),
(6, 'Dedi', 'Male', 38, 2147483647),
(7, 'Andi', 'Male', 40, 2147483647);

-- --------------------------------------------------------

--
-- Table structure for table `provider`
--

CREATE TABLE `provider` (
  `provider_id` int(11) NOT NULL,
  `provider_name` text NOT NULL,
  `provider_loc` text NOT NULL,
  `provider_phone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `provider`
--

INSERT INTO `provider` (`provider_id`, `provider_name`, `provider_loc`, `provider_phone`) VALUES
(1, 'ABC Rentals', 'Jakarta', 2147483647),
(2, 'XYZ Rentals', 'Bandung', 2147483647),
(3, 'PQR Car Rentals', 'Surabaya', 2147483647),
(4, 'JKL Car Services', 'Medan', 2147483647),
(5, 'DEF Auto Rentals', 'Bali', 2147483647),
(6, 'GHI Car Hire', 'Yogyakarta', 2147483647),
(7, 'JKL Car Rentals', 'Bandung', 2147483647);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`car_id`),
  ADD KEY `provider_id` (`provider_id`);

--
-- Indexes for table `driver`
--
ALTER TABLE `driver`
  ADD PRIMARY KEY (`driver_id`);

--
-- Indexes for table `provider`
--
ALTER TABLE `provider`
  ADD PRIMARY KEY (`provider_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `car`
--
ALTER TABLE `car`
  MODIFY `car_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `driver`
--
ALTER TABLE `driver`
  MODIFY `driver_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `provider`
--
ALTER TABLE `provider`
  MODIFY `provider_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `car`
--
ALTER TABLE `car`
  ADD CONSTRAINT `car_ibfk_1` FOREIGN KEY (`provider_id`) REFERENCES `provider` (`provider_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
