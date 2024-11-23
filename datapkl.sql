-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 23, 2024 at 09:10 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `datapkl`
--
CREATE DATABASE IF NOT EXISTS `datapkl` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `datapkl`;

-- --------------------------------------------------------

--
-- Table structure for table `tb_elektronika`
--

DROP TABLE IF EXISTS `tb_elektronika`;
CREATE TABLE `tb_elektronika` (
  `letak_buku_pkl` varchar(20) DEFAULT NULL,
  `arsip_laporan_pkl` varchar(10) DEFAULT NULL,
  `tahun_pelaksanaan` int(11) DEFAULT NULL,
  `nim` varchar(20) NOT NULL,
  `nama_mahasiswa` varchar(50) DEFAULT NULL,
  `judul_laporan_pkl` varchar(200) DEFAULT NULL,
  `nama_dosen_pembimbing` varchar(50) DEFAULT NULL,
  `nama_tempat_pelaksanaan` varchar(200) DEFAULT NULL,
  `kabupaten_kota` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_elektronika`
--

INSERT INTO `tb_elektronika` (`letak_buku_pkl`, `arsip_laporan_pkl`, `tahun_pelaksanaan`, `nim`, `nama_mahasiswa`, `judul_laporan_pkl`, `nama_dosen_pembimbing`, `nama_tempat_pelaksanaan`, `kabupaten_kota`) VALUES
('TA ARSITEKTUR 2016', '621.38', 2020, '3201711014', 'Sindy', 'MONITORING FREKUENSI SELULER(UNIT PELAKSANAAN TEKNISI) LINGKUNGAN DIREKTORIAT JENDRAL POS DAN TELEKOMUNIKASI', 'Medi Yuwono Tharam,ST.,MT', 'INSTALASI UPT(UNIT PELAKSANAAN TEKNIS) LINGKUNGAN DIREKTORIAT JENDRAL POS DAN TELEKOMUNIKASI', 'KOTA PONTIANAK'),
('TA ARSITEKTUR 2016', '621.81', 2020, '3201711020', 'Andre', 'PEMBONGKARAN DAN PERBAIKAN POMPA SENTRIFUGAL', 'Widdo Arifin,ST.,MT', 'PDAM TIRTHA KHATULISTIWA PONTIANAK', 'KOTA PONTIANAK'),
('TA ARSITEKTUR 2016', '629.7', 2020, '3201711041', 'Dwi Siswanto', 'PENGENALAN PEMOGRAMAN HOLLYSYS DISTRIBUTED CONTROL SYSTEM MACS V5.2.4', 'Eko Mardianto,SST.,MT', 'PT INDONESIA CHEMICAL ALUMINA', 'KABUPATEN SANGGAU'),
('TA ARSITEKTUR 2016', '621.88', 2020, '3201711073', 'Yufli Adria Yugis', 'PEMELIHARAAN PREVENTIF, PERIODIK DAN KOREKTIF PADA MOTOR LISTRIK DI ULPTP/G SIANTAN', 'Agus Riyanto,ST.,MT', 'ULPTP/G SIANTAN', 'PONTIANAK'),
('TA ARSITEKTUR 2016', '629.8', 2020, '3201713028', 'Khalis Rasis', 'SISTEM WWTP(WASTEWATER TREATMENT PLANT)', 'Hasan,ST.,MT', 'PT INDOFOOD CBP SUKSES MAKMUR Tbk', 'KOTA PONTIANAK UTARA'),
('PKL INFORMATIKA D.II', '620.82', 2021, '3201811002', 'Ajiu', 'MONITORING FREKUENSI SELULER PADA BADWITH 900 MHZ DIBALAI MONITOR SPEKTRUM FREKUNSI RADIO KELAS II PONTIANAK', 'Wiwit Indah Rahayu,ST.,MT.', 'BALAI MONITOR KELAS II PONTIANAK', 'JAKARTA TIMUR'),
('PKL INFORMATIKA D.II', '697.9', 2021, '3201811014', 'Abdul Aziz', 'INSTANSI DAN KEPERAWATAN DAN PERBAIKAN PADA AC SPLIT WALL', 'Medi Yuwono Tharam,ST.,MT', 'PT. GOBEL DHARMA NUSANTARA', 'JAKARTA TIMUR'),
('PKL INFORMATIKA D.II', '621.83', 2021, '3201811024', 'Muhammad Reza Pahlawan Pulungan', 'PERAWATAN DAN PENGOPERASIAN MESIN DIESEL DIPEMBANGKIT LISTRIK TENAGA DIESEL(PLTD) MENYURAI', 'Agus Riyanto,ST.,MT', 'PT PLN(PERSERO)', 'KABUPATEN SANGGAU'),
('PKL INFORMATIKA D.II', '621.4', 2021, '3201811025', 'Muhammad Irfan', 'PEMASANGAN DAN MAINTANCE CAMERA CCTV DAHUA IP CAM PADA PROGRAM SMART CITY', 'Eko Mardianto,SST.,MT', 'DINAS KOMUNIKASI DAN INFORMATIKA', 'KOTA PONTIANAK'),
('PKL INFORMATIKA D.II', '621.37', 2021, '3201811031', 'Jemi Julyan', 'PERBAIKAN SISTEM JARINGAN KOMPUTER', 'Ir.Rusman,MT', 'PT WILMAR CAHAYA INDONESIA.Tbk', 'KOTA PONTIANAK');

-- --------------------------------------------------------

--
-- Table structure for table `tb_informatika`
--

DROP TABLE IF EXISTS `tb_informatika`;
CREATE TABLE `tb_informatika` (
  `letak_buku_pkl` varchar(20) DEFAULT NULL,
  `arsip_laporan_pkl` varchar(10) DEFAULT NULL,
  `tahun_pelaksanaan` int(11) DEFAULT NULL,
  `nim` varchar(20) NOT NULL,
  `nama_mahasiswa` varchar(50) DEFAULT NULL,
  `judul_laporan_pkl` varchar(200) DEFAULT NULL,
  `nama_dosen_pembimbing` varchar(50) DEFAULT NULL,
  `nama_tempat_pelaksanaan` varchar(200) DEFAULT NULL,
  `kabupaten_kota` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_informatika`
--

INSERT INTO `tb_informatika` (`letak_buku_pkl`, `arsip_laporan_pkl`, `tahun_pelaksanaan`, `nim`, `nama_mahasiswa`, `judul_laporan_pkl`, `nama_dosen_pembimbing`, `nama_tempat_pelaksanaan`, `kabupaten_kota`) VALUES
('PKL TPHP 1027', '005.3', 2021, '3201816014', 'Gusti Damara', 'PENGGUNAAN APLIKASI KOMPUTERISASI KEGIATAN PERTAHANAN (KPP)', 'Yasir Arafat,S.ST.,MT', 'KANTOR PERTAHANAN', 'KABUPATEN KUBU RAYA'),
('PKL TPHP 1027', '005.4', 2021, '3201816029', 'Yanti Novitasari', 'PENGGUNAAN APLIKASI SIBEJI', 'Irwan Suharto,S.T.,MT', 'DINAS KOMUNIKASI DAN INFORMASI', 'KABUPATEN SINTANG'),
('PKL TPHP 1027', '005.36', 2021, '3201816066', 'Rizky Pratama Syahrul Ramadhan', 'RANCANG BANGUN SISTEM INFORMATIKA PENGARSIPAN SURAT BERBASIS WEB', 'Budianingsih,S.T.,M.T', 'UMUM DAN APARATUR DINAS PENDIDIKAN DAN KEBUDAYAAN', 'KOTA PONTIANAK'),
('PKL TPHP 1027', '006.7', 2021, '3201816067', 'Ryan Maghribie', 'PENGOLAHAN GAMBAR DAN VIDEO DI DISKOMINFO', 'Tri Bowo Atmojo,S.T.,M.Cs', 'DINAS KOMUNIKASI DAN INFORMASI KOTA PONTIANAK', 'KOTA PONTIANAK'),
('PKL TPHP 1027', '006.5', 2021, '3201816084', 'Ahmad Tuflihun', 'PENGGUNAAN AMAZON WEB SERVICES DAN FRAMEWORK-FRAME UNTUK MEMBUAT WEBSITE VIRTUAL TOUR NU SKIN', 'Wawan Heryawan,ST,.MT', 'CV.ULMITA SOLUSI DIGITAL', 'KOTA PONTIANAK');

-- --------------------------------------------------------

--
-- Table structure for table `tb_listrik`
--

DROP TABLE IF EXISTS `tb_listrik`;
CREATE TABLE `tb_listrik` (
  `letak_buku_pkl` varchar(20) DEFAULT NULL,
  `arsip_laporan_pkl` varchar(10) DEFAULT NULL,
  `tahun_pelaksanaan` int(11) DEFAULT NULL,
  `nim` varchar(20) NOT NULL,
  `nama_mahasiswa` varchar(50) DEFAULT NULL,
  `judul_laporan_pkl` varchar(200) DEFAULT NULL,
  `nama_dosen_pembimbing` varchar(50) DEFAULT NULL,
  `nama_tempat_pelaksanaan` varchar(200) DEFAULT NULL,
  `kabupaten_kota` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_listrik`
--

INSERT INTO `tb_listrik` (`letak_buku_pkl`, `arsip_laporan_pkl`, `tahun_pelaksanaan`, `nim`, `nama_mahasiswa`, `judul_laporan_pkl`, `nama_dosen_pembimbing`, `nama_tempat_pelaksanaan`, `kabupaten_kota`) VALUES
('TA ARSITEKTUR 2016', '621.319', 2020, '3201703038', 'Arif Setiawan', 'PEMASANGAN LAMPU JALAN UMUM(PJU)', 'Ir.H.Syarif Agus Salim,MT', 'PT.PRIMA ELECTRIK KHATULISTIWA', 'JL.KOMYOS SUDARSO GANG TIMUN 1 NO.27 KEL. SUNGAI JAWI LUAR KEC.PONTIANAK BARAT'),
('PKL TPHP 1027', '621.46', 2020, '3201703045', 'Dimas Aditya Pratama', 'PERAWATAN MOTOR INDUKSI 3 PHASA DENGAN MENGGUNAKAN ALAT KHUSUS', 'Ir.Abu Bakar,MT', 'CHEMICAL ALUMINA DUSUN PIASAK, DESA PEDALAMAN', 'KEC TAYAN HILIR'),
('PKL TPHP 1027', '621.3', 2020, '3201703051', 'Destu Aji', 'ELECTROSTATIC PRECIPITATOR(ESP) UNTUK SISTEM PENGATURAN', 'Wawan Heryawan,ST,MT', 'PLTU-3 PARIT BARU SITE BENGKAYANG', 'BENGKAYANG'),
('PKL TPHP 1027', '621.34', 2020, '3201703065', 'Dimas Aditya Pratama', 'INDUKSI MOTOR 3 PHASA', 'Ir.Abu Bakar,MT', 'PT.PLN(PERSERO) AREA SINGKAWANG', 'SINGKAWANG'),
('TA ARSITEKTUR 2016', '621.83', 2021, '3201803009', 'Khairul Abidin', 'PENGGANTIAN BEARING MOTOR PERUMDA AIR MINUM GUNUNG POTENG', 'Ir.Rusman,MT', 'PERUMDA', 'KOTA SINGKAWANG'),
('TA ARSITEKTUR 2016', '621.31', 2021, '3201803032', 'Wahyudi Apriandi', 'PEMASANGAN PANEL ATS(AUTOMATIC TRANSFER SWITCH) DIRUMAH SAKIT TEMUNGGUNG GERGAJI', 'Ir.Suharto.MT', 'RUMAH SAKIT TEMUNGGUNG GERGAJI', 'KECAMATAN SEKAYAM, BALAI KARANGAN'),
('TA ARSITEKTUR 2016', '621.39', 2021, '3201803033', 'Febri Maharani Putra', 'PENGUKURUAN PHASA RST PADA GARDU, PEMASANGAN KWH METER DAN PENGGALIAN LOBANG UNTUK TIANG', 'Ir.Rusman,MT', 'KANTOR PLN UP3 PONTIANAK', 'KOTA PONTIANAK'),
('TA ARSITEKTUR 2016', '621.86', 2021, '3201803066', 'Beno Kristanio', 'PERAWATAN DAN PERBAIKAN POMPA SENTRIFUGAL DI PDAM TIRTA PANCUR AJI KOTA SANGGAU', 'Dr.Halasan Sihombing', 'PDAM TIRTA PANCUR AJI', 'KOTA SANGGAU'),
('TA ARSITEKTUR 2016', '620.004', 2021, '3201803069', 'Randa Apriandi', 'PERBAIKAN DAN PERAWATAN PANEL HUBUNG BAGI MESIN PRESSING', 'Ir.Suharto.MT', 'PT PUNDI LAHAN KHATULISTIWA', 'KABUPATEN KUBURAYA');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_elektronika`
--
ALTER TABLE `tb_elektronika`
  ADD PRIMARY KEY (`nim`);

--
-- Indexes for table `tb_informatika`
--
ALTER TABLE `tb_informatika`
  ADD PRIMARY KEY (`nim`);

--
-- Indexes for table `tb_listrik`
--
ALTER TABLE `tb_listrik`
  ADD PRIMARY KEY (`nim`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
