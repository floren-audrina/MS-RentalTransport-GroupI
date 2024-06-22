-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 22, 2024 at 08:08 AM
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
-- Database: `puri_bali`
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
(1, '2024-06-06', '2024-06-07', 1, 1000000, 1),
(2, '2024-06-12', '2024-06-14', 0, 1500000, 2),
(3, '2024-06-18', '2024-06-21', 1, 2400000, 3),
(4, '2024-06-24', '2024-06-28', 0, 2650000, 4),
(5, '2024-06-30', '2024-07-05', 1, 4800000, 5),
(6, '2024-07-07', '2024-07-08', 0, 2200000, 6),
(7, '2024-07-14', '2024-07-16', 1, 1500000, 7);

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
(1, 'Honda', 'Brio', 'Hatchback', 'Automatic', 2018, 4, 2, 500000, 1),
(2, 'Toyota', 'Avanza', 'MPV', 'Automatic', 2018, 6, 2, 500000, 2),
(3, 'Mitsubishi', 'Xpander', 'MPV', 'Automatic', 2017, 6, 3, 600000, 3),
(4, 'Honda', 'Mobilio RS', 'MPV', 'Automatic', 2022, 6, 2, 550000, 4),
(5, 'Toyota', 'Innova Reborn', 'MPV', 'Automatic', 2019, 7, 4, 800000, 5),
(6, 'Toyota', 'Innova Zenix', 'MPV', 'Automatic', 2024, 7, 4, 1100000, 6),
(7, 'Toyota', 'Agya', 'Hatchback', 'Automatic', 2020, 4, 2, 500000, 7);

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
(1, 'Wempi Sugianto', 'M', 31, '081000000001', 1),
(2, 'Elly Moenawaroh', 'F', 32, '081000000002', 2),
(3, 'Riyanto Riyan', 'M', 33, '081000000003', 3),
(4, 'Rifki Bakri', 'M', 34, '081000000004', 4),
(5, 'Ong Didi', 'M', 35, '081000000005', 5),
(6, 'Ribkah Kristiani', 'F', 36, '081000000006', 6),
(7, 'Vivin Dwi Fitri Dika', 'F', 37, '081000000007', 7);

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
('Puri', 'Jl. Raya Seminyak No.18', 'Bali', '088351289777', 'Setiap mobil yang disewa harus kembali dalam kondisi baik seperti saat diserahkan. Deposit akan ditentukan berdasarkan jenis dan lama penyewaan mobil. Pengemudi diharapkan mengisi bahan bakar sebelum mengembalikan kendaraan. Kami bertanggung jawab atas perawatan dan kondisi mobil selama disewa.', 'Jelajahi kemudahan dan keamanan dalam menyewa mobil bersama kami. Kami menyediakan armada mobil terbaru dengan berbagai pilihan, mulai dari sedan hingga mobil keluarga. Layanan pelanggan kami siap membantu Anda 24/7 untuk memastikan pengalaman rental yang mulus dan tak terlupakan.', '<div class=\"mapouter\"><div class=\"gmap_canvas\"><iframe width=\"820\" height=\"560\" id=\"gmap_canvas\" src=\"https://maps.google.com/maps?q=Jl.+Raya+Seminyak+No.18&t=&z=13&ie=UTF8&iwloc=&output=embed\" frameborder=\"0\" scrolling=\"no\" marginheight=\"0\" marginwidth=\"0\"></iframe><a href=\"https://online.stopwatch-timer.net/\">timer for kids</a><br><a href=\"https://textcaseconvert.com/\"></a><br><style>.mapouter{position: relative;text-align: right;height: 560px;width: 820px;}</style><a href=\"https://www.mapembed.net\">google map for my website</a><style>.gmap_canvas{overflow: hidden;background: none !important;height: 560px;width: 820px;}</style></div></div>');

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
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `car`
--
ALTER TABLE `car`
  MODIFY `car_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `driver`
--
ALTER TABLE `driver`
  MODIFY `driver_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

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
