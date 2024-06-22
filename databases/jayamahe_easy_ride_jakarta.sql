-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 22, 2024 at 08:07 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jayamahe_easy_ride_jakarta`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL,
  `tanggal_mulai` varchar(10) NOT NULL,
  `tanggal_selesai` varchar(10) NOT NULL,
  `with_driver` tinyint(1) NOT NULL,
  `total_harga` int(11) NOT NULL,
  `car_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`booking_id`, `tanggal_mulai`, `tanggal_selesai`, `with_driver`, `total_harga`, `car_id`) VALUES
(1, '2024-07-01', '2024-07-05', 1, 1280000, 1),
(2, '2024-07-10', '2024-07-12', 0, 520000, 2),
(3, '2024-07-15', '2024-07-18', 1, 1480000, 3),
(4, '2024-07-20', '2024-07-22', 0, 580000, 4),
(5, '2024-07-25', '2024-07-30', 1, 3060000, 5);

-- --------------------------------------------------------

--
-- Table structure for table `car`
--

CREATE TABLE `car` (
  `car_id` int(11) NOT NULL,
  `car_brand` varchar(50) NOT NULL,
  `car_name` varchar(50) NOT NULL,
  `car_type` varchar(50) NOT NULL,
  `car_transmission` varchar(10) NOT NULL,
  `car_year` int(11) NOT NULL,
  `car_seats` int(11) NOT NULL,
  `car_luggages` int(11) NOT NULL,
  `car_price` int(11) NOT NULL,
  `driver_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `car`
--

INSERT INTO `car` (`car_id`, `car_brand`, `car_name`, `car_type`, `car_transmission`, `car_year`, `car_seats`, `car_luggages`, `car_price`, `driver_id`) VALUES
(1, 'Nissan', 'Grand Livina', 'MPV', 'Automatic', 2020, 7, 2, 320000, 1),
(2, 'Toyota', 'Yaris', 'Hatchback', 'Manual', 2019, 5, 1, 260000, 2),
(3, 'Mitsubishi', 'Xpander', 'MPV', 'Automatic', 2021, 7, 3, 370000, 3),
(4, 'Daihatsu', 'Terios', 'SUV', 'Manual', 2018, 7, 2, 290000, 4),
(5, 'Ford', 'Everest', 'SUV', 'Automatic', 2022, 7, 3, 510000, 5),
(6, 'Toyota', 'Corolla', 'Sedan', 'Automatic', 2022, 5, 2, 25000, 1),
(7, 'Toyota', 'Corolla', 'Sedan', 'Automatic', 2022, 5, 2, 25000, 1),
(8, 'Toyota', 'Corollas', 'Sedan', 'Automatic', 2022, 5, 2, 25000, 1);

-- --------------------------------------------------------

--
-- Table structure for table `driver`
--

CREATE TABLE `driver` (
  `driver_id` int(11) NOT NULL,
  `driver_name` varchar(100) NOT NULL,
  `driver_gender` char(1) NOT NULL,
  `driver_age` int(11) NOT NULL,
  `driver_phone` varchar(15) NOT NULL,
  `car_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `driver`
--

INSERT INTO `driver` (`driver_id`, `driver_name`, `driver_gender`, `driver_age`, `driver_phone`, `car_id`) VALUES
(1, 'Andi Wijaya', 'M', 40, '081234567895', 1),
(2, 'Nurul Huda', 'F', 35, '081234567896', 2),
(3, 'Rudi Hartono', 'M', 32, '081234567897', 3),
(4, 'Siti Nurhaliza', 'F', 29, '081234567898', 4),
(5, 'Yusuf Ibrahim', 'M', 48, '081234567899', 5);

-- --------------------------------------------------------

--
-- Table structure for table `provider`
--

CREATE TABLE `provider` (
  `provider_name` varchar(50) NOT NULL,
  `provider_address` varchar(50) NOT NULL,
  `provider_city` varchar(50) NOT NULL,
  `provider_num` varchar(15) NOT NULL,
  `policy` text NOT NULL,
  `information` text NOT NULL,
  `map` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `provider`
--

INSERT INTO `provider` (`provider_name`, `provider_address`, `provider_city`, `provider_num`, `policy`, `information`, `map`) VALUES
('Jayamahe Easy Ride', 'Jl. Kebon Sirih No.45', 'Jakarta', '085112233475', 'Kami menawarkan opsi deposit fleksibel, mulai dari Rp 50.000, tergantung pada jenis mobil yang disewa. Pengemudi diharapkan mengisi ulang bahan bakar sebelum pengembalian. Setiap kerusakan atau kehilangan akan dievaluasi berdasarkan kondisi mobil saat disewa.', 'Dapatkan pengalaman menyewa mobil yang nyaman dengan kami. Kami menyediakan mobil dari berbagai merek terkemuka dengan harga yang kompetitif. Layanan pelanggan kami siap membantu Anda dengan segala kebutuhan selama masa penyewaan.', '<div class=\"mapouter\"><div class=\"gmap_canvas\"><iframe width=\"820\" height=\"560\" id=\"gmap_canvas\" src=\"https://maps.google.com/maps?q=Jl.+Kebon+Sirih+No.45&t=&z=13&ie=UTF8&iwloc=&output=embed\" frameborder=\"0\" scrolling=\"no\" marginheight=\"0\" marginwidth=\"0\"></iframe><a href=\"https://online.stopwatch-timer.net/\">timer for kids</a><br><a href=\"https://textcaseconvert.com/\"></a><br><style>.mapouter{position: relative;text-align: right;height: 560px;width: 820px;}</style><a href=\"https://www.mapembed.net\">custom google maps embed</a><style>.gmap_canvas{overflow: hidden;background: none !important;height: 560px;width: 820px;}</style></div></div>');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`booking_id`),
  ADD KEY `car_id` (`car_id`);

--
-- Indexes for table `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`car_id`),
  ADD KEY `fk_driver` (`driver_id`);

--
-- Indexes for table `driver`
--
ALTER TABLE `driver`
  ADD PRIMARY KEY (`driver_id`),
  ADD KEY `fk_car` (`car_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `car`
--
ALTER TABLE `car`
  MODIFY `car_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `driver`
--
ALTER TABLE `driver`
  MODIFY `driver_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`car_id`) REFERENCES `car` (`car_id`);

--
-- Constraints for table `car`
--
ALTER TABLE `car`
  ADD CONSTRAINT `fk_driver` FOREIGN KEY (`driver_id`) REFERENCES `driver` (`driver_id`);

--
-- Constraints for table `driver`
--
ALTER TABLE `driver`
  ADD CONSTRAINT `fk_car` FOREIGN KEY (`car_id`) REFERENCES `car` (`car_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
