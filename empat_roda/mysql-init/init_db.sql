-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 15, 2024 at 04:17 PM
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
-- Database: `empat_roda_jogja`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL,
  `tanggal_mulai` date NOT NULL,
  `tanggal_selesai` date NOT NULL,
  `with_driver` tinyint(1) NOT NULL,
  `total_harga` int(11) NOT NULL,
  `car_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`booking_id`, `tanggal_mulai`, `tanggal_selesai`, `with_driver`, `total_harga`, `car_id`) VALUES
(1, '2024-06-02', '2024-06-09', 1, 1300000, 1),
(2, '2024-06-03', '2024-06-08', 1, 1100000, 2),
(3, '2024-06-03', '2024-06-10', 0, 800000, 3),
(4, '2024-06-13', '2024-06-18', 1, 1100000, 1),
(5, '2024-06-16', '2024-06-25', 0, 900000, 4),
(6, '2024-06-23', '2024-06-29', 0, 750000, 3),
(7, '2024-07-01', '2024-07-03', 1, 500000, 1),
(8, '2024-07-05', '2024-07-09', 1, 700000, 5),
(9, '2024-08-05', '2024-08-09', 0, 560000, 3);

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
  `car_image` varchar(255) NOT NULL,
  `driver_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `car`
--

INSERT INTO `car` (`car_id`, `car_brand`, `car_name`, `car_type`, `car_transmission`, `car_year`, `car_seats`, `car_luggages`, `car_price`, `car_image`, `driver_id`) VALUES
(1, 'Toyota', 'Avanza', 'MPV', 'Automatic', 2020, 7, 2, 350000, 'https://www.toyota.astra.co.id//sites/default/files/2023-09/1-avanza-purplish-silver.png', 1),
(2, 'Honda', 'Jazz', 'Hatchback', 'Manual', 2019, 5, 1, 275000, 'https://asset.honda-indonesia.com/2020/04/27/exterior_2l_1__1588046929826.jpg', 2),
(3, 'Suzuki', 'Ertiga', 'MPV', 'Automatic', 2021, 7, 3, 360000, 'https://www.suzukicdn.com/assets/static/img/variant/Brave_khaki.webp', 3),
(4, 'Daihatsu', 'Xenia', 'MPV', 'Manual', 2018, 7, 2, 285000, 'https://salesdaihatsusoloraya.com/app/uploads/2022/06/all-new-xenia.jpg', 4),
(5, 'Mitsubishi', 'Pajero', 'SUV', 'Automatic', 2022, 7, 3, 600000, 'https://assets.mitsubishi-motors.co.id/compress/products/colors/1627574998-pajero-4x2-greypng.webp', 5);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `driver`
--

INSERT INTO `driver` (`driver_id`, `driver_name`, `driver_gender`, `driver_age`, `driver_phone`, `car_id`) VALUES
(1, 'Roni Waluyo', 'M', 48, '088987654321', 1),
(2, 'Adi Janudi', 'M', 37, '081123459876', 2),
(3, 'Ezra Datu', 'M', 42, '081678954321', 3),
(4, 'Melina Subandi', 'F', 39, '088678912345', 4),
(5, 'Denis Sutejo', 'M', 50, '085543216789', 5);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `provider`
--

INSERT INTO `provider` (`provider_name`, `provider_address`, `provider_city`, `provider_num`, `policy`, `information`, `map`) VALUES
('Empat Roda', 'Jl. Karya Utama RT 06/RW 34 Sedan', 'Yogyakarta', '081123456789', 'Layanan Pelanggan 24/7, Asuransi Termasuk, Dapat Dikembalikan, Penggunaan dari pukul 00:00 hingga 23:59, Kembalikan bahan bakar sesuai dengan kondisi saat diterima', 'Sebelum Anda memesan: Pastikan untuk membaca persyaratan sewa. Setelah Anda memesan: Penyedia sewa akan menghubungi pengemudi melalui WhatsApp untuk meminta foto dokumen yang diperlukan. Saat penjemputan: Bawa KTP, SIM, dan dokumen lain yang diperlukan oleh penyedia sewa. Ketika Anda bertemu dengan staf penyewaan, periksa kondisi mobil bersama staf tersebut. Setelah itu, baca dan tanda tangani perjanjian sewa.', '<div class=\"mapouter\"><div class=\"gmap_canvas\"><iframe width=\"820\" height=\"560\" id=\"gmap_canvas\" src=\"https://maps.google.com/maps?q=Jogja+Empat+Roda+-+Car+Rental+Jogja&t=&z=13&ie=UTF8&iwloc=&output=embed\" frameborder=\"0\" scrolling=\"no\" marginheight=\"0\" marginwidth=\"0\"></iframe><a href=\"https://textcaseconvert.com/\"></a><br><a href=\"https://timenowin.net/\"></a><br><style>.mapouter{position: relative;text-align: right;height: 560px;width: 820px;}</style><a href=\"https://www.mapembed.net\">embedding maps in website</a><style>.gmap_canvas{overflow: hidden;background: none !important;height: 560px;width: 820px;}</style></div></div>');

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
  ADD KEY `car_id` (`car_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `car`
--
ALTER TABLE `car`
  MODIFY `car_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `driver`
--
ALTER TABLE `driver`
  MODIFY `driver_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

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
  ADD CONSTRAINT `driver_ibfk_1` FOREIGN KEY (`car_id`) REFERENCES `car` (`car_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
