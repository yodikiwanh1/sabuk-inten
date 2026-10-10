# Chunk RAG – ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf

Total chunk: 62. Nomor halaman mengacu pada halaman fisik PDF (bukan nomor cetak di footer; nomor cetak = halaman PDF − 6 untuk isi utama). Isi teks ditulis dalam bahasa Indonesia (terjemahan dari dokumen asli berbahasa Inggris); istilah teknis, nama antarmuka, label tabel/gambar, dan nilai angka dipertahankan seperti aslinya. Deskripsi gambar ditulis dalam blok kutipan (>). Halaman daftar isi, daftar gambar, dan daftar tabel tidak dimasukkan.

---

## Chunk 001
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 1
- **Tipe:** teks
- **Heading:** Cover / Informasi Dokumen

ZXEPS E6N1 DC Power System – Quick Installation Guide. Version: R01M201.
Penerbit: ZTE CORPORATION, ZTE Plaza, Keji Road South, Hi-Tech Industrial Park, Nanshan District, Shenzhen, P.R.China. Postcode: 518057.
Tel: +86-755-26771900. URL: https://support.zte.com.cn. E-mail: support@zte.com.cn.

---

## Chunk 002
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 2
- **Tipe:** tabel
- **Heading:** Legal Information & Revision History

Copyright 2025 ZTE CORPORATION. Dokumen ini dilindungi hak cipta; reproduksi atau distribusi tanpa izin tertulis ZTE dilarang. Dokumen disediakan "as is" tanpa jaminan apa pun. ZTE berhak melakukan perubahan teknis tanpa pemberitahuan. Informasi dukungan teknis: https://support.zte.com.cn. (Teks disclaimer hukum lengkap diringkas.)

**Revision History**

| Revision No. | Revision Date | Revision Reason |
|---|---|---|
| R1.0 | 2025-06-30 | First edition. |

Serial Number: SJ-20250722111610-002. Publishing Date: 2025-06-30 (R1.0).

---

## Chunk 003
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 5
- **Tipe:** teks+tabel
- **Heading:** About This Manual – Purpose, Audience, Chapter Overview

**Purpose:** manual ini berlaku untuk instalasi sistem catu daya DC ZXEPS E6N1 R01M201 (disingkat "ZXEPS E6N1 system").

**Intended audience:** equipment installation engineers dan maintenance engineers.

**Isi manual:**

| Chapter | Judul | Deskripsi |
|---|---|---|
| 1 | Safety Instructions | Menjelaskan tindakan pencegahan keselamatan umum. |
| 2 | Tool Preparations | Alat dan instrumen yang harus disiapkan sebelum instalasi. |
| 3 | Product Architecture | Struktur keseluruhan dan komponen. |
| 4 | Connecting Cables | Penyambungan kabel. |
| 5 | Checks After Installation | Pemeriksaan yang harus dilakukan setelah instalasi. |
| 6 | Checking Electrical Connections | Cara memeriksa sambungan listrik. |
| 7 | System Power-On | Prosedur menyalakan sistem. |
| 8 | Replacing Parts | Cara mengganti komponen. |
| 9 | Related Operations and Precautions | Operasi lain dan tindakan pencegahan. |

**Related documentation:** ZXEPS E6N1 R01M201 DC Power System Product Description; ZXDT CSU603A Centralized System Management Unit User Guide; ZXDU V6.0 Series Telecom DC Power System Maintenance Guide.

---

## Chunk 004
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 6
- **Tipe:** tabel
- **Heading:** About This Manual – Conventions (Format Teks & Tingkat Peringatan)

| Konvensi | Arti |
|---|---|
| Italics | Variabel dalam perintah; dapat juga merujuk ke manual/dokumen terkait. |
| Bold | Menu, opsi menu, nama fungsi, kolom input, nama tombol opsi, check box, drop-down list, nama dialog, nama jendela, parameter, dan perintah. |
| Constant width | Teks yang diketik, kode program, nama file, nama direktori, dan nama fungsi. |
| [] | Parameter opsional. |
| {} | Parameter wajib. |
| \| | Pemisah antar parameter dalam rangkaian parameter. |

**Tingkat peringatan:**

| Simbol | Arti |
|---|---|
| Danger | Situasi berbahaya yang akan segera terjadi; jika diabaikan mengakibatkan kematian atau cedera serius. |
| Warning | Situasi yang berpotensi berbahaya; jika diabaikan dapat mengakibatkan kematian atau cedera serius. |
| Caution | Situasi berpotensi berbahaya; jika diabaikan dapat mengakibatkan cedera ringan atau sedang. |
| Notice | Informasi keselamatan peralatan/lingkungan; jika diabaikan dapat menyebabkan kerusakan peralatan, kehilangan data, penurunan kinerja, pencemaran lingkungan, atau hasil tak terduga lain. |
| Note | Informasi tambahan tentang suatu topik. |

---

## Chunk 005
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 7
- **Tipe:** teks
- **Heading:** Chapter 1 Safety Instructions – Installation Environment

Untuk menjamin keselamatan personel dan peralatan, baca dan patuhi aturan berikut sebelum instalasi.

**Installation Environment**
- Dilarang memasang peralatan di lingkungan asam dan korosif, atau lingkungan dengan banyak debu konduktif.
- Air, logam, dan serpihan lain dilarang jatuh ke dalam peralatan; jika tidak, peralatan dapat rusak karena korsleting.
- Sediakan ruang 90 mm di depan peralatan dan 50 mm di belakang peralatan; tidak boleh ada barang di ruang tersebut.
- Pelanggan bertanggung jawab atas kerusakan peralatan akibat terendam air serta akibat modifikasi atau pengangkutan yang dilakukan pelanggan sendiri.
- Kapasitas circuit breaker, fuse, atau komponen proteksi lain yang dipasang untuk peralatan harus lebih besar daripada kapasitas AC input circuit breaker peralatan.

---

## Chunk 006
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 7
- **Tipe:** teks
- **Heading:** Chapter 1 Safety Instructions – Personnel Requirements & Electrical Connection Safety

**Personnel Requirements**
Installation engineer harus terlatih secara ketat, mengetahui cara pengoperasian yang benar, dan memahami tindakan pencegahan keselamatan.

**Electrical Connection Safety Specifications**
- Jangan pernah memasang atau melepas kabel saat peralatan menyala. Battery pack tidak boleh dihubungsingkatkan dengan cara apa pun selama pengoperasian.
- Live wire dan neutral wire tidak boleh tertukar. Neutral wire harus tersambung dengan benar tanpa putus dalam kondisi apa pun.
- Baterai harus dipasang sesuai kutub positif dan negatifnya.
- Gunakan sarung tangan keselamatan dan alat berinsulasi untuk sambungan listrik.
- Terminal sekrup dan bagian telanjang yang tidak perlu harus diinsulasi dengan baik.
- Kabel harus tersambung dengan benar agar tidak terjadi korsleting atau rangkaian terbuka.

---

## Chunk 007
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 8
- **Tipe:** teks
- **Heading:** Chapter 1 Safety Instructions – Cables Connection Requirements

- Lapisan insulasi kabel tidak boleh rusak.
- Luas penampang kabel harus memenuhi kebutuhan beban maksimum perangkat.
- Jika dipakai kabel dengan warna non-standar, pilih kabel hitam dan gunakan heat shrink tube atau isolasi dengan warna yang sesuai agar mudah diidentifikasi. Jika regulasi lokal tentang warna kabel berbeda dari manual ini, patuhi regulasi lokal.

---

## Chunk 008
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 9-10
- **Tipe:** tabel+gambar
- **Heading:** Chapter 2 Tool Preparations – Table 2-1 Tools and Instruments

Alat dan instrumen yang harus disiapkan sebelum instalasi tertera pada Table 2-1.

> **Note:** Alat dan instrumen mengikuti standar lokal. Gambar di tabel hanya sebagai referensi. Semua instrumen harus dikalibrasi secara ketat dan terbukti memenuhi syarat sebelum digunakan.

**Table 2-1 Tools and Instruments**

| Name | Function |
|---|---|
| Crosshead screwdriver | Mengencangkan sekrup crosshead. |
| Flat head screwdriver | Mengencangkan sekrup flat-head, serta memasang dan melepas floating nut. |
| Tape measure | Mengukur panjang. |
| Spirit level | Memeriksa kerataan adjustable base dan kabinet. |
| Marker pen | Menandai posisi lubang bor di lantai. |
| Multimeter | Memeriksa sambungan listrik. |
| Crimping pliers for tubular terminals | Meng-crimp tubular terminal. |
| Insulating gloves | Digunakan selama instalasi. |
| Cable tie | Mengikat kabel. |
| Adjustable wrench | Mengencangkan baut. |
| Socket spanner | Mengencangkan baut. |
| Hammer drill | Digunakan untuk mengebor. |
| Vacuum cleaner | Membersihkan lubang instalasi dan lantai. |
| Ladder | Digunakan saat bekerja di ketinggian. |
| Water pump pliers | Melepas dan memasang circuit breaker. |

> **[Deskripsi gambar – Table 2-1: kolom Image]** Kolom gambar pada tabel berisi foto/ilustrasi kecil dari masing-masing alat di atas (obeng, meteran, multimeter, tang crimping, sarung tangan isolasi, kabel tie, kunci pas, bor, penyedot debu, tangga, tang water pump) sebagai referensi visual bentuk alat.

---

## Chunk 009
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 11
- **Tipe:** teks+gambar
- **Heading:** Chapter 3 Product Architecture – External Dimensions

Figure 3-1 menunjukkan dimensi eksternal sistem catu daya ZXEPS E6N1. Flange termasuk dalam lebar, tetapi bagian yang menonjol (bulges) umumnya tidak dihitung. 1U = 44.45 mm.

> **[Deskripsi gambar – Figure 3-1: External Dimensions of the ZXEPS E6N1 Power System]** Tampilan 3D miring dari unit rack berwarna abu-abu/hitam yang memperlihatkan panel depan (CSU dengan layar dan terminal hijau, modul rectifier berkipas, breaker). Anak panah dimensi menunjukkan tinggi 5U (5 × 44.45 mm = 222.25 mm), lebar 482.6 mm, dan kedalaman 360 mm.

---

## Chunk 010
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 12
- **Tipe:** teks+gambar
- **Heading:** Chapter 3 Product Architecture – Components

Figure 3-2 menunjukkan komponen sistem catu daya ZXEPS E6N1:
1. DC PDU
2. CSU603A
3. ZXEPS R4850 rectifier
4. AC PDU
5. Main grounding point

> **Note:** Main grounding point adalah M8, dengan torsi pengencangan (10.0 ± 1.0) N·m. Gambar hanya sebagai referensi; konfigurasi yang ditetapkan dalam kontrak yang berlaku. Sebelum pengiriman, label tata letak komponen digantung pada flange kanan sistem catu daya.

> **[Deskripsi gambar – Figure 3-2: Components of the ZXEPS E6N1 Power System]** Tampak depan rack. Bagian atas kiri (kotak merah, nomor 1) adalah DC PDU berisi dua baris circuit breaker. Di sebelah kanannya (kotak merah, nomor 2) adalah CSU603A dengan layar LCD, tombol, dan terminal hijau. Di bawahnya (nomor 3) ada dua baris modul rectifier ZXEPS R4850 yang ditandai kipas bulat. Di bagian paling bawah (kotak merah, nomor 4) adalah AC PDU. Titik grounding utama (nomor 5) berada di flange sisi kiri.

---

## Chunk 011
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 12
- **Tipe:** teks+gambar
- **Heading:** Chapter 3 Product Architecture – AC PDU

Figure 3-3 menunjukkan komponen AC PDU.

> **[Deskripsi gambar – Figure 3-3: AC PDU]** Tampak depan AC PDU berupa panel horizontal. Di sisi kiri ada empat circuit breaker berlabel N, L1, L2, L3 yang membentuk grup AC input. Di sisi kanan ada grup AC output (optional) dengan tiga kolom terminal; label N di atas tiap kolom dan L1, L2, L3 di bawahnya.

---

## Chunk 012
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 12-13
- **Tipe:** teks+gambar
- **Heading:** Chapter 3 Product Architecture – DC PDU

Figure 3-4 menunjukkan komponen DC PDU.

> **[Deskripsi gambar – Figure 3-4: DC PDU]** Dua baris circuit breaker. Baris atas: grup LLVD1 di sisi kiri (beberapa breaker beban) dan grup BLVD di sisi kanan. Baris bawah: di kiri empat breaker berlabel Battery circuit breaker 1–4, di sebelahnya slot BLVD, dan di ujung kanan modul DC SPD (surge protective device).

---

## Chunk 013
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 14
- **Tipe:** teks
- **Heading:** 4.1 CSU603A – Functions

CSU603A adalah unit manajemen front-end sistem catu daya DC komunikasi. Fungsinya melacak dan mengelola status operasional sistem, serta mendukung akses Web.

**Management**
- Battery management: mendukung charging management, discharging management, dan test management untuk battery set.
- Rectifier management: mengontrol sleep otomatis rectifier untuk menghemat energi.
- Tenant management: mengatur korespondensi antara PDU dan tenant serta mengelola pemutusan daya tenant.
- PU management: mengontrol PU secara cerdas untuk menghemat energi.
- Alarm management: mengatur level alarm dan relay serta mengaktifkan/menonaktifkan alarm.
- Maintenance management: mengumpulkan statistik informasi perangkat, menghapus alarm, upgrade software, dan ekspor data.

**Web access**
Setelah CSU terhubung ke jaringan, CSU dapat diakses menggunakan Chrome untuk membaca data CSU secara real time dan mengonfigurasi CSU.

---

## Chunk 014
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 15
- **Tipe:** teks+gambar
- **Heading:** 4.1 CSU603A – External View (Panel CSU)

Figure 4-1 menunjukkan panel CSU603A:
1. Indicators
2. LCD screen
3. Buttons
4. USB interface
5. FE interface
6. SPB

> **[Deskripsi gambar – Figure 4-1: Panel of the CSU]** Panel depan CSU603A berlogo ZTE. Dari kiri ke kanan: tiga LED indikator (1), layar LCD persegi (2), empat tombol bulat (3), port USB (4) dan port Ethernet RJ45/FE (5), lalu blok terminal hijau SPB (6) di sisi kanan dengan label pin kecil di bawahnya.

---

## Chunk 015
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 15-17
- **Tipe:** teks+gambar
- **Heading:** 4.1 CSU603A – SPB (Interface Layout)

SPB menyediakan input relay, output relay, antarmuka komunikasi, dan antarmuka deteksi lingkungan. Tata letak antarmuka ditunjukkan pada Figure 4-2, Figure 4-3, dan Figure 4-4; deskripsi antarmuka ada di Table 4-1.

> **Note:** Hanya antarmuka sinyal yang tersedia untuk pengguna yang dijelaskan di bagian ini. Antarmuka sinyal yang dipakai sistem tidak dicantumkan.

> **[Deskripsi gambar – Figure 4-2: SPB Interface Layout]** Papan SPB hijau tampak 3D dengan anak panah biru melengkung yang menunjukkan papan ini terpasang ke dalam CSU. Konektor J16 (pin 6 sampai 1) disorot di bagian atas; tampilan SPB top view dan SPB front view ditunjukkan di sisi kanan dan bawah dengan blok terminal hijau disorot.

> **[Deskripsi gambar – Figure 4-3: SPB Interfaces (Front View)]** Tampak depan SPB: konektor J2 berisi 16 pin dalam dua baris, baris atas A1–A8 dan baris bawah B1–B8. Di sebelah kanannya ada J3, J4, dan J5, masing-masing 4 pin (atas: 1 dan 3; bawah: 2 dan 4).

> **[Deskripsi gambar – Figure 4-4: SPB Interfaces (Top View)]** Tampak atas SPB. Konektor X9 berada di bagian atas. J7 berupa deretan vertikal pin 1–8. Konektor lain dengan label dan jumlah pin: J11 (2 pin), J9 (2 pin), J10 (2 pin), J6 (3 pin), J8 (2 pin), J15 (3 pin), J14 (4 pin), J13 (2 pin), J12 (2 pin).

---

## Chunk 016
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 17-18
- **Tipe:** tabel
- **Heading:** 4.1 CSU603A – Table 4-1 SPB Interface Descriptions: J2 (Output Relay & Input Relay)

**Table 4-1 SPB Interface Descriptions (bagian 1: J2)**

| Interface | Interface definition | Pin | Signal | Signal description |
|---|---|---|---|---|

| J2 | Output relay | A1 | DO1 | Normally open terminal of output relay 1. |
| J2 | Output relay | A2 | CO1 | Common terminal of output relay 1. |
| J2 | Output relay | A3 | DO2 | Normally open terminal of output relay 2. |
| J2 | Output relay | A4 | CO2 | Common terminal of output relay 2. |
| J2 | Output relay | A5 | DO3 | Normally open terminal of output relay 3. |
| J2 | Output relay | A6 | CO3 | Common terminal of output relay 3. |
| J2 | Output relay | A7 | DO4 | Normally open terminal of output relay 4. |
| J2 | Output relay | A8 | CO4 | Common terminal of output relay 4. |
| J2 | Input relay | B1 | DI1 | Input relay 1. |
| J2 | Input relay | B2 | 5V | Input relay for 5 V power supply. |
| J2 | Input relay | B3 | DI2 | Input relay 2. |
| J2 | Input relay | B4 | 5V | Input relay for 5 V power supply. |
| J2 | Input relay | B5 | DI3 | Input relay 3. |
| J2 | Input relay | B6 | 5V | Input relay for 5 V power supply. |
| J2 | Input relay | B7 | DI4 | Input relay 4. |
| J2 | Input relay | B8 | 5V | Input relay for 5 V power supply. |

---

## Chunk 017
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 18
- **Tipe:** tabel
- **Heading:** 4.1 CSU603A – Table 4-1 SPB Interface Descriptions: J3, J4, J5 (Door, Smoke, Temperature, RS485)

**Table 4-1 SPB Interface Descriptions (bagian 2: J3, J4, J5)**

| Interface | Interface definition | Pin | Signal | Signal description |
|---|---|---|---|---|

| J3 | Door | 1 | DR | Magnetic door switch signal. |
| J3 | Door | 3 | VD | 5 V power supply interface for the magnetic door sensor. |
| J3 | Smoke | 2 | SMK | Smoke signal. |
| J3 | Smoke | 4 | VS | 5 V power supply interface for the smoke sensor. |
| J4 | Temp1 | 1 | T1 | Battery temperature signal 1. |
| J4 | Temp1 | 3 | VCC | 5 V power supply interface for the temperature sensor. |
| J4 | ENV Temp | 2 | ENT | Ambient temperature signal. |
| J4 | ENV Temp | 4 | VCC | 5 V power supply interface for the temperature sensor. |
| J5 | RS485N | 1 | B | Independent northbound RS485 signal line B. |
| J5 | RS485N | 3 | A | Independent northbound RS485 signal line A. |
| J5 | 485S1-1 | 2 | B | The first RS485 signal line B for transmitting the first southbound signal. |
| J5 | 485S1-1 | 4 | A | The first RS485 signal line A for transmitting the first southbound signal. |

---

## Chunk 018
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 19
- **Tipe:** tabel
- **Heading:** 4.1 CSU603A – Table 4-1 SPB Interface Descriptions: J6 – J12 (RS232, Output Relay 5–8, RS485, CAN, Temp2)

**Table 4-1 SPB Interface Descriptions (bagian 3: J6 sampai J12)**

| Interface | Interface definition | Pin | Signal | Signal description |
|---|---|---|---|---|

| J6 | RS232 | 1 | RXD | Independent northbound RS232 received signal. |
| J6 | RS232 | 2 | TXD | Independent northbound RS232 transmitted signal. |
| J6 | RS232 | 3 | G | GND for independent northbound RS232 signal. |
| J7 | Output relay | 1 | DO5 | Normally open terminal of output relay 5. |
| J7 | Output relay | 2 | CO5 | Common terminal of output relay 5. |
| J7 | Output relay | 3 | DO6 | Normally open terminal of output relay 6. |
| J7 | Output relay | 4 | CO6 | Common terminal of output relay 6. |
| J7 | Output relay | 5 | DO7 | Normally open terminal of output relay 7. |
| J7 | Output relay | 6 | CO7 | Common terminal of output relay 7. |
| J7 | Output relay | 7 | DO8 | Normally open terminal of output relay 8. |
| J7 | Output relay | 8 | CO8 | Common terminal of output relay 8. |
| J8 | 485S1-2 | 1 | B | The second RS485 signal line B for transmitting the first southbound signal. |
| J8 | 485S1-2 | 2 | A | The second RS485 signal line A for transmitting the first southbound signal. |
| J9 | 485S2-1 | 1 | B | The first RS485 signal line B for transmitting the second southbound signal. |
| J9 | 485S2-1 | 2 | A | The first RS485 signal line A for transmitting the second southbound signal. |
| J10 | 485S2-2 | 1 | B | The second RS485 signal line B for transmitting the second southbound signal. |
| J10 | 485S2-2 | 2 | A | The second RS485 signal line A for transmitting the second southbound signal. |
| J11 | Southbound CAN signal CAN | 1 | H | Southbound CAN_H signal. |
| J11 | Southbound CAN signal CAN | 2 | L | Southbound CAN_L signal. |
| J12 | Battery temperature signal 2 (Temp2) | 1 | T2 | Battery temperature signal 2. |
| J12 | Battery temperature signal 2 (Temp2) | 2 | VCC | 5 V power supply interface for the temperature sensor. |

---

## Chunk 019
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 20
- **Tipe:** tabel+teks
- **Heading:** 4.1 CSU603A – Table 4-1 SPB Interface Descriptions: J13 – J16, X9 & Catatan RS485

**Table 4-1 SPB Interface Descriptions (bagian 4: J13 sampai J16 dan X9)**

| Interface | Interface definition | Pin | Signal | Signal description |
|---|---|---|---|---|

| J13 | Battery temperature signal 3 (Temp3) | 1 | T3 | Battery temperature signal 3. |
| J13 | Battery temperature signal 3 (Temp3) | 2 | VCC | 5 V power supply interface for the temperature sensor. |
| J14 | Waterlogging (Flood) | 1 | VF | Internal power supply for the waterlogging sensor. |
| J14 | Waterlogging (Flood) | 2 | VD | 5 V power supply interface for the waterlogging sensor. |
| J14 | Waterlogging (Flood) | 3 | G | GND for the waterlogging sensor. |
| J14 | Waterlogging (Flood) | 4 | WAT | Waterlogging alarm signal. |
| J15 | Humidity | 1 | VD | 5 V power supply interface for the humidity sensor. |
| J15 | Humidity | 2 | HUM | Humidity alarm signal. |
| J15 | Humidity | 3 | G | GND for the humidity sensor. |
| J16 | Input relay | 1 | DI5 | Input relay 5. |
| J16 | Input relay | 2 | DI6 | Input relay 6. |
| J16 | Input relay | 3 | DI7 | Input relay 7. |
| J16 | Input relay | 4 | DI8 | Input relay 8. |
| J16 | Input relay | 5 | 5V | Input relay for 5 V power supply. |
| J16 | Input relay | 6 | 5V | Input relay for 5 V power supply. |
| X9 | Wireless communication module SWCU | Internal standard wires | – | Wireless communication module interface. |

**Catatan:**
- J5-2&4 dan J8 adalah antarmuka RS485 southbound yang sama; konfigurasi antarmuka memakai set parameter yang sama (misalnya baud rate).
- J9 dan J10 adalah antarmuka RS485 southbound yang sama; konfigurasi antarmuka memakai set parameter yang sama (misalnya baud rate).

---

## Chunk 020
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 20-21
- **Tipe:** teks
- **Heading:** 4.1 CSU603A – Interfaces (USB & FE)

**USB interface**
- Mendukung USB flash drive, tetapi tidak mendukung SD card atau perangkat penyimpanan portabel lain seperti portable hard disk, MP3, atau MP4.
- Format sistem file USB adalah FAT.
- Mendukung USB flash drive hingga 32 GB.

**FE interface**
- Kecepatan antarmuka FE adalah 10 M/100 M (adaptif).
- Antarmuka Ethernet RJ45 mendukung beberapa mode jaringan monitoring melalui HTTPS, SNMP, protokol YD/T 1363, dan protokol YD/T 1104.

---

## Chunk 021
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 21
- **Tipe:** tabel
- **Heading:** 4.1 CSU603A – Indicators (Table 4-2 Indicator Status)

Indikator menunjukkan status operasional CSU.

**Table 4-2 Indicator Status**

| Power Indicator | Operating Indicator | Alarm Indicator | Operational Status of the CSU |
|---|---|---|---|
| On | Flashing | Off | Operating normally |
| On | Flashing | Flashing | Alarm |
| On | On or off | - | Faulty |
| Off | Off | Off | Not operating |

"-" berarti status indikator tidak tetap.

---

## Chunk 022
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 21-22
- **Tipe:** tabel+teks
- **Heading:** 4.1 CSU603A – Buttons (Table 4-3) & LCD Screen

Informasi dapat dilihat dan parameter dapat diatur melalui tombol menu.

**Table 4-3 Buttons**

| Button | Button Name | Function |
|---|---|---|
| ▲ | Up/Direction button | Pindah ke item sebelumnya. Menaikkan nilai numerik. |
| ▼ | Down/Direction button | Pindah ke item berikutnya. Menggeser kursor. |
| Esc | Return button | Kembali ke layar tingkat atas. Membatalkan modifikasi. |
| Ent | Confirmation button | Mengonfirmasi operasi. Menyimpan modifikasi. |
| ▲ + ▼ | Combination button | Tekan kedua tombol bersamaan untuk masuk ke shortcut menu dan melihat alarm internal serta informasi debugging dengan cepat. |

Urutan karakter yang dimasukkan dengan tombol atas: 1. Digit angka 0–9; 2. Huruf kapital A–Z; 3. Huruf kecil a–z; 4. Simbol khusus "`" – ".". Jika perlu memasukkan banyak huruf atau simbol, disarankan login ke Web portal.

**LCD Screen**
Layar LCD dipakai untuk interaksi manusia-mesin. Dengan menekan tombol menu, data sistem dapat dilihat dan parameter dapat diatur untuk mengontrol sistem melalui layar LCD.

---

## Chunk 023
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 22
- **Tipe:** teks
- **Heading:** 4.2.1 Connecting Input Relay Cables

**Abstract:** prosedur ini menjelaskan cara menyambungkan kabel input relay.

**Steps**
1. Sambungkan kabel ke input relay pada antarmuka J2/J16 CSU sesuai kebutuhan alarm, dengan mengacu pada deskripsi antarmuka di Table 4-1.
2. (Optional) Untuk mengubah hubungan antara input relay dan alarm, lihat ZXDT CSU603A Centralized System Management Unit User Guide saat provisioning sistem untuk mengatur properti input relay.

> **Note:** Status alarm input relay adalah "closed" dan level alarm adalah "masked". Ini adalah kondisi default; status dan level alarm dapat didefinisikan.

---

## Chunk 024
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 22-23
- **Tipe:** teks
- **Heading:** 4.2.2 Connecting Output Relay Cables

**Abstract:** prosedur ini menjelaskan cara menyambungkan kabel output relay.

**Steps**
1. Sambungkan kabel ke output relay pada antarmuka J2/J7 CSU dengan mengacu pada deskripsi antarmuka di Table 4-1.
2. (Optional) Jika perlu mengubah sinyal terkait dan status output default output relay, lihat bagian "Configuring Input and Output Relays" pada ZXDT CSU603A Centralized System Management Unit User Guide saat sistem dinyalakan.

---

## Chunk 025
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 23
- **Tipe:** teks+tabel
- **Heading:** 4.2.3 Connecting Communication Cables

**Abstract:** prosedur ini menjelaskan cara menyambungkan kabel komunikasi untuk membangun jaringan antar perangkat.

**Steps**
1. Sambungkan kabel komunikasi yang diperlukan arsitektur jaringan ke antarmuka yang sesuai. Mode komunikasi dan antarmuka terkait ada pada Table 4-4.

**Table 4-4 Communication Modes and Corresponding Interfaces**

| Communication Mode | Communication Interface | Communication Port Position |
|---|---|---|
| Ethernet | RJ45 (Ethernet interface) | Front panel of the CSU |
| Serial port | Southbound RS485 serial port | Interface J5-2&4/J8/J9/J10 of the SPB |
| Serial port | Northbound RS232 serial port | Interface J6 of the SPB |
| Serial port | Northbound RS485 serial port | Interface J5-1&3 of the SPB |

---

## Chunk 026
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 23-24
- **Tipe:** teks+tabel
- **Heading:** 4.2.4 Connecting the Cables of the Battery Temperature Sensor and Ambient Temperature Sensor

**Abstract:** prosedur ini menjelaskan cara menyambungkan kabel sensor suhu baterai dan sensor suhu ruangan agar suhu ruangan dan baterai dapat diperiksa melalui CSU dan alarm muncul saat suhu terlalu tinggi.

**Context:** secara default, sistem catu daya ini tidak dikonfigurasi dengan sensor suhu baterai. Sensor perlu dikonfigurasi sesuai kebutuhan.

**Steps**
1. Sambungkan kabel sensor suhu baterai ke antarmuka J4-Temp1/J12/J13 pada SPB sesuai kebutuhan.
2. Sambungkan kabel sensor suhu ruangan ke antarmuka J4-ENV Temp pada SPB sesuai kebutuhan.
3. (Optional) Atur kanal sampling suhu. Sistem mendukung empat kanal sampling suhu. Korespondensi antara kanal sampling suhu dan battery pack dapat diatur melalui CSU. Deskripsi kanal ada pada Table 4-5.

**Table 4-5 Temperature Sampling Channel Descriptions**

| Interface Name | Description |
|---|---|
| Temperature sampling channels 1–4 | Sebuah kanal sampling suhu dapat mendeteksi suhu baterai atau suhu ruangan, yang dapat ditentukan melalui CSU. Detail lihat ZXDT CSU603A Centralized System Management Unit User Guide. |

---

## Chunk 027
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 24-25
- **Tipe:** teks+gambar
- **Heading:** 4.3.1 Connecting Cables to a 125 A-Case Circuit Breaker – Abstract & Context

**Abstract:** kabel harus dibuat dan circuit breaker harus disambungkan dengan benar agar operasi circuit breaker tidak terganggu. Prosedur ini menjelaskan cara menyambungkan kabel ke circuit breaker 125 A case.

**Context:** Figure 4-5 menunjukkan tampak luar circuit breaker 125 A case:
1. Screw hole for the negative terminal
2. Negative hole
3. Screw hole for the positive terminal
4. Positive hole
5. Circuit breaker position indicator

> **[Deskripsi gambar – Figure 4-5: 125 A-Case Circuit Breaker]** Dua tampilan modul breaker hitam: tampilan 3D (Three-dimensional view) dengan lima titik bernomor 1–5 dan tampilan depan (Front view) yang menandai Negative pole di sebelah kiri dan Positive pole di sebelah kanan. Indikator posisi breaker (5) berupa kotak hijau kecil di bagian bawah depan.

---

## Chunk 028
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 25-26
- **Tipe:** teks+gambar
- **Heading:** 4.3.1 Connecting Cables to a 125 A-Case Circuit Breaker – Steps 1–2 (Strip & Crimp Cable)

**Steps**
1. Kupas sheath kabel sepanjang 20 mm (Figure 4-6). Luas penampang kabel adalah 35 mm². Kabel dapat dimasukkan ke pre-insulated tubular terminal dengan tabung tembaga sepanjang 16 mm (Figure 4-7).

> **Note:** Disarankan memakai pre-insulated tubular terminal yang disediakan produsen perangkat.

> **Notice:** Jika pre-insulated tubular terminal yang kabelnya tidak di-crimp dipasang ke circuit breaker, sambungan kabel dapat tidak andal, resistansi kontak dapat meningkat, atau titik kontak dapat memanas hingga membakar perangkat.

2. Masukkan bagian kabel yang terbuka ke pre-insulated tubular terminal (panjang bagian logam 16 mm), lalu crimp terminal dengan kencang menggunakan crimping pliers. Penampang terminal setelah di-crimp berbentuk trapesium (Figure 4-8).

> **[Deskripsi gambar – Figure 4-6: Strip off the Cable]** Foto kabel merah dan biru yang sheath-nya dikupas 20 mm, di dekat modul breaker dan sebuah terminal hijau; penanda dimensi 20 mm ditunjukkan di bawah ujung kabel.

> **[Deskripsi gambar – Figure 4-7: Pre-Insulated Tubular Terminal]** Diagram samping terminal tubular pre-insulated 35 mm² (selubung hijau) dengan bagian tabung tembaga abu-abu sepanjang 16 mm.

> **[Deskripsi gambar – Figure 4-8: Crimping the Pre-Insulated Tubular Terminal]** Foto close-up terminal hijau yang sudah di-crimp pada kabel merah dan biru. Ditandai indented surface (permukaan bekas crimp) pada terminal, dan inset menunjukkan cross section berbentuk trapesium.

---

## Chunk 029
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 26-27
- **Tipe:** teks+gambar
- **Heading:** 4.3.1 Connecting Cables to a 125 A-Case Circuit Breaker – Steps 3–6 (Insert Cables)

**Steps (lanjutan)**
3. Tarik keluar switch untuk memutuskan circuit breaker (Figure 4-9).
4. Longgarkan dua sekrup berlawanan arah jarum jam untuk membuka slot kabel (Figure 4-10).

> **Notice:** Torsi harus berada di antara 1.5 N·m dan 2 N·m; jika tidak, kabel mungkin tidak dapat dimasukkan ke slot.

5. Masukkan kabel positif dan negatif ke slot kabel yang sesuai (Figure 4-11).

> **Notice:**
> - Indented surface kabel harus menghadap ke lubang sekrupnya. Pastikan kabel terpasang dengan benar.
> - Jangan menyambungkan kabel saat circuit breaker "ON" agar circuit breaker tidak rusak.

6. Kencangkan dua sekrup searah jarum jam dan pastikan kabel terpasang kuat.

> **[Deskripsi gambar – Figure 4-9: Pulling Out the Switch]** Breaker hitam dengan tuas/switch bagian bawah yang ditarik keluar; label "Pull out the switch".

> **[Deskripsi gambar – Figure 4-10: Loosening the Screws]** Breaker dengan dua sekrup di bagian depan disorot merah; label "Loosen the two screws".

> **[Deskripsi gambar – Figure 4-11: Inserting the Cables]** Kabel positif (hitam) dan negatif (biru) masuk ke slot breaker. Keterangan: indented surface kabel positif menghadap ke bawah dan indented surface kabel negatif menghadap ke atas.

---

## Chunk 030
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 27-28
- **Tipe:** teks+tabel+gambar
- **Heading:** 4.3.2 Connecting Cables to a 63 A-Case Circuit Breaker – Abstract, Context & Table 4-6

**Abstract:** prosedur ini memakai kabel dengan luas penampang 10 mm² sampai 16 mm² sebagai contoh untuk menjelaskan cara menyambungkan kabel ke circuit breaker 63 A case.

**Context:** luas penampang (CSA) kabel yang dapat dipakai circuit breaker 63 A case ada pada Table 4-6.

**Table 4-6 CSAs of Cables Used by 63 A-Case Circuit Breakers**

| CSA (mm²) | Length of the Copper Tube of the Pre-Insulated Tubular Terminal (mm) | Stripped Length (mm) |
|---|---|---|
| 1–6 | 12 | 16 |
| 10–16 | 16 | 24 |

Figure 4-12 menunjukkan tampak luar circuit breaker 63 A case:
1. Negative spring
2. Negative hole
3. Positive spring
4. Positive hole
5. Circuit breaker position indicator

> **[Deskripsi gambar – Figure 4-12: 63 A Case Circuit Breaker]** Tampilan 3D dan tampilan depan breaker hitam, dengan label Negative pole dan Positive pole di tampilan depan. Lima titik bernomor menunjukkan negative spring, negative hole, positive spring, positive hole, dan indikator posisi (kotak hijau).

---

## Chunk 031
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 28-29
- **Tipe:** teks+gambar
- **Heading:** 4.3.2 Connecting Cables to a 63 A-Case Circuit Breaker – Steps 1–2 (Strip & Crimp Cable)

**Steps**
1. Kupas sheath kabel sepanjang 24 mm (Figure 4-13). Figure 4-14 menunjukkan korespondensi antara tipe pre-insulated tubular terminal dan kabel dengan CSA tertentu.

> **Note:** Disarankan memakai pre-insulated tubular terminal yang disediakan produsen perangkat.

> **Notice:** Jika pre-insulated tubular terminal yang kabelnya tidak di-crimp dipasang ke circuit breaker, sambungan kabel dapat tidak andal, resistansi kontak dapat meningkat, atau titik kontak dapat memanas hingga membakar perangkat.

2. Masukkan bagian kabel yang terbuka ke pre-insulated tubular terminal (panjang bagian logam 16 mm), lalu crimp dengan kencang menggunakan crimping pliers. Penampang terminal setelah di-crimp berbentuk trapesium (Figure 4-15).

> **[Deskripsi gambar – Figure 4-13: Strip off the Cable]** Foto kabel merah dan biru dengan sheath dikupas 24 mm; penanda dimensi 24 mm di bawah ujung kabel, dengan terminal hijau/putih di dekatnya.

> **[Deskripsi gambar – Figure 4-14: Pre-Insulated Tubular Terminal]** Dua terminal berdampingan: terminal 10 mm² (selubung putih) dan terminal 16 mm² (selubung hijau); keduanya dengan tabung tembaga 16 mm.

> **[Deskripsi gambar – Figure 4-15: Crimping the Pre-Insulated Tubular Terminal]** Foto terminal hijau yang sudah di-crimp pada kabel merah dan biru, dengan penanda indented surface dan inset cross section trapesium.

---

## Chunk 032
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 29-30
- **Tipe:** teks+gambar
- **Heading:** 4.3.2 Connecting Cables to a 63 A-Case Circuit Breaker – Steps 3–6 (Insert Cables)

**Steps (lanjutan)**
3. Tarik keluar switch untuk memutuskan circuit breaker.
4. Masukkan obeng flat-head ke removal hole dan installation hole circuit breaker 63 A case (Figure 4-16).
5. Masukkan kabel positif dan negatif ke slot kabel yang sesuai (Figure 4-17).

> **Notice:**
> - Indented surface kabel harus menghadap ke lubang sekrupnya. Pastikan kabel terpasang dengan benar.
> - Jangan menyambungkan kabel saat circuit breaker "ON" agar circuit breaker tidak rusak.

6. Lepaskan obeng flat-head dan pastikan kabel terpasang kuat.

> **[Deskripsi gambar – Figure 4-16: Inserting a Flat-Head Screwdriver]** Breaker hitam dengan dua obeng flat-head (gagang merah) dimasukkan ke dua lubang di bagian depan atas; label "Flat-head screwdriver".

> **[Deskripsi gambar – Figure 4-17: Inserting the Cables]** Kabel positif (hitam) dan negatif (biru) dimasukkan ke breaker sementara dua obeng flat-head tetap terpasang. Keterangan: indented surface kabel negatif menghadap ke bawah dan indented surface kabel positif menghadap ke atas.

---

## Chunk 033
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 30-31
- **Tipe:** teks+gambar
- **Heading:** 4.4 Connecting the PE Cable

**Abstract:** prosedur ini menjelaskan cara menyambungkan kabel PE untuk mengalirkan muatan listrik dari casing logam yang bertegangan ke tanah, sehingga mencegah sengatan listrik saat seseorang menyentuh casing logam.

**Steps**
1. Sambungkan kabel PE sistem catu daya. Satu ujung kabel PE disambungkan ke grounding busbar site, ujung lainnya ke main grounding point di sisi kiri sistem catu daya (Figure 4-18).

> **Note:**
> - Sistem catu daya dilengkapi kabel PE 10 mm².
> - Main grounding point adalah M8, dengan torsi pengencangan (10.0 ± 1.0) N·m.

> **[Deskripsi gambar – Figure 4-18: Connecting the PE Cable]** Tampak depan rack dengan garis kabel kuning dari main grounding point di flange kiri turun ke grounding busbar site (panel abu-abu berlubang dengan label kuning "Grounding busbar of a site") di bagian bawah.

---

## Chunk 034
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 31-32
- **Tipe:** teks
- **Heading:** 4.5 Connecting AC Input Cables – Abstract, Caution & Notice

**Abstract:** prosedur ini menjelaskan cara menyambungkan kabel AC input untuk memasukkan pasokan daya AC.

> **CAUTION:** Jangan menyambung atau melepas kabel saat daya menyala.

> **Notice:**
> - Sambungan live wire dan neutral wire tidak boleh tertukar.
> - Kapasitas AC circuit breaker eksternal harus lebih besar daripada kapasitas AC input circuit breaker perangkat ini agar beban tidak terputus akibat circuit breaker trip.
> - Disarankan memakai kabel tembaga 10 mm² atau 16 mm². Untuk memilih kabel dengan luas penampang berbeda, lihat rumus perhitungan pada Table 4-7.
> - Saat menutup (close) AC input circuit breaker, operasikan dengan kedua tangan. Letakkan ibu jari pada handle di antara L1 dan L2 serta L3 dan N (bagian handle yang berlubang). Tekan handle untuk menutup circuit breaker. Setelah circuit breaker tertutup, pastikan handle sejajar dengan panel depan circuit breaker.

---

## Chunk 035
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 32-33
- **Tipe:** teks+gambar
- **Heading:** 4.5 Connecting AC Input Cables – Steps

**Steps**
1. (Optional) Sambungkan aluminum/copper concentric cable. Jika kabel AC input adalah kabel aluminium, kabel tidak dapat langsung disambungkan ke AC input circuit breaker; kabel harus disambungkan melalui aluminum/copper concentric cable (Figure 4-19).
2. Atur external power switch sistem catu daya (di AC power distribution cabinet) ke posisi OFF.
3. Atur AC input circuit breaker perangkat ke posisi OFF.
4. Sambungkan kabel AC input (Figure 4-20).

> **Note:**
> - Cara menyiapkan kabel AC input: lihat "4.3.1 Connecting Cables to a 125 A-Case Circuit Breaker".
> - Disarankan mengupas sheath kabel 24 mm dan memakai terminal khusus dari produsen perangkat. Indented surface pre-insulated tubular terminal untuk live dan neutral wire harus sama-sama menghadap ke atas (yaitu menghadap lubang persegi).

5. Tutup AC input circuit breaker. Letakkan ibu jari pada handle di antara N dan L1 serta L2 dan L3 (bagian handle yang berlubang). Tekan handle untuk menutup circuit breaker. Jendela posisi circuit breaker berubah dari hijau menjadi merah (Figure 4-21). Setelah tertutup, pastikan handle sejajar dengan panel depan circuit breaker.

> **[Deskripsi gambar – Figure 4-19: External View of an Aluminum/Copper Concentric Cable]** Kabel panjang abu-abu dengan ujung aluminium (25 mm²) di kiri dan ujung tembaga (16 mm²) di kanan; ujung tembaga memakai pre-insulated tubular terminal hijau 16 mm².

> **[Deskripsi gambar – Figure 4-20: Connecting the AC Input Cables]** Empat breaker AC input berlabel N, L1, L2, L3 dengan kabel biru (N), cokelat (L1), hitam (L2), dan abu-abu (L3). Inset foto menunjukkan indented surface terminal; keterangan: indented surface kabel menghadap ke atas.

> **[Deskripsi gambar – Figure 4-21: Closing an AC Input Circuit Breaker]** Perbandingan dua gambar dengan anak panah biru: kiri, empat jendela posisi breaker berwarna hijau (terbuka) dengan penunjuk "Press here" pada handle; kanan, keempat jendela berwarna merah (tertutup).

---

## Chunk 036
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 33-34
- **Tipe:** teks+gambar
- **Heading:** 4.6 (Optional) Connecting AC Output Cables

**Abstract:** prosedur ini menjelaskan cara menyambungkan kabel AC output untuk memasok daya ke beban AC saat diperlukan switchover.

**Context:** AC output circuit breaker memakai circuit breaker 16 A (63 A case). Cara menyiapkan kabel: lihat 4.3.2 Connecting Cables to a 63 A-Case Circuit Breaker.

**Steps**
1. Atur AC output circuit breaker perangkat ke posisi OFF.
2. Sambungkan kabel AC output (Figure 4-22).

> **Note:** Indented surface live wire atau neutral wire harus menghadap ke lubang sekrupnya.

> **[Deskripsi gambar – Figure 4-22: Connecting the AC Output Cables]** Tiga kolom terminal AC output (optional): kabel biru N di bagian atas dan kabel L1 (cokelat), L2 (hitam), L3 (abu-abu) di bagian bawah. Inset foto menunjukkan indented surface; keterangan: indented surface kabel menghadap ke bawah.

---

## Chunk 037
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 34-35
- **Tipe:** teks+tabel
- **Heading:** 4.7 Connecting DC Output Cables – Abstract, Caution, Notice & Table 4-7

**Abstract:** prosedur ini menjelaskan cara menyambungkan kabel DC output untuk memasok daya ke beban DC.

> **CAUTION:**
> - Kabel DC output harus terpasang kuat pada DC output circuit breaker. Tarik kabel dengan wajar untuk memastikan kabel terpasang kuat.
> - Jangan melepas atau memasang kabel saat daya menyala.

> **Notice:**
> - Kapasitas beban yang disambungkan tidak boleh melebihi batas kapasitas circuit breaker terkait. Sisakan margin keselamatan antara kapasitas aktual dan batas kapasitas.
> - Sambungan kabel DC output positif dan negatif tidak boleh tertukar.
> - Jangan menyambungkan kabel aluminium secara langsung.

**Context:** DC PDU dikonfigurasi dengan load circuit breaker dan battery circuit breaker berkapasitas berbeda. Kapasitas circuit breaker menentukan rentang luas penampang kabel yang dapat disambungkan. Hubungan antara kapasitas circuit breaker dan luas penampang kabel yang disarankan ada pada Table 4-7.

**Table 4-7 Relationships Between Circuit Breaker Capacities and Cross-Sectional Areas of Cables**

| Circuit Breaker Capacity (A) | Cross-Sectional Area of Adaptive Cables (mm²) |
|---|---|
| 10 | 1–16 |
| 16 | 1.5–16 |
| 32 | 4–16 |
| 63 | 10–16 |
| 100 | 25–35 |
| 125 | 35 |

**Remarks (berlaku untuk tabel di atas):**
- Selain berada dalam rentang yang disarankan, luas penampang kabel yang dipilih juga harus lebih besar atau sama dengan hasil rumus: Arus kerja maksimum (A) × Panjang total kabel (m) / (Penurunan tegangan yang diizinkan pada kabel (V) × Konduktivitas kabel tembaga). Konduktivitas kabel tembaga dapat dianggap sekitar 50.
- Contoh: jika arus kerja maksimum perangkat 20 A, panjang total kabel positif dan negatif 20 m, dan penurunan tegangan yang diizinkan pada kabel 2 V, maka luas penampang kabel yang dipilih harus ≥ 4 mm². Jika disambungkan ke circuit breaker 32 A, kabel dengan luas penampang 4 mm² dapat dipakai.
- Jika copper-aluminum connecting terminal dipakai, kemungkinan terminal tidak memenuhi persyaratan luas penampang circuit breaker sehingga mengganggu switching circuit breaker. Dalam kasus ini, gunakan terminal atau kabel dengan luas penampang lebih kecil.

---

## Chunk 038
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 35
- **Tipe:** teks+gambar
- **Heading:** 4.7 Connecting DC Output Cables – Steps

**Steps**
1. Atur DC output circuit breaker ke posisi OFF.
2. Sambungkan kabel DC output (Figure 4-23).

> **Note:** Kapasitas DC output circuit breaker dapat berkisar 10 A sampai 63 A atau 100 A sampai 125 A. Untuk circuit breaker 100 A–125 A, lihat 4.3.1 Connecting Cables to a 125 A-Case Circuit Breaker. Untuk circuit breaker 10 A–63 A, lihat 4.3.2 Connecting Cables to a 63 A-Case Circuit Breaker.

> **[Deskripsi gambar – Figure 4-23: Connecting the DC Output Cables]** Dua beban di atas DC PDU: "Minor load" dengan kabel biru (−) dan hitam (+) disambungkan ke salah satu breaker pada grup LLVD1, dan "Major load" disambungkan ke breaker pada grup BLVD. Di bawah terlihat Battery circuit breaker 1–4, BLVD, dan DC SPD.

---

## Chunk 039
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 35-36
- **Tipe:** teks+gambar
- **Heading:** 4.8 Connecting Cables for Lithium-Ion Batteries – Abstract & Grounding Cables

**Abstract:** prosedur ini memakai baterai lithium-ion pintar ZXESM R321 (V1.0) sebagai contoh. Untuk model baterai lithium-ion lain, lihat user guide terkait. Sambungan terdiri dari:
- Communication cable connection: komunikasi antar baterai yang dikaskade dan antara baterai dengan CSU.
- Power cable connection: menyalurkan daya DC ke sistem catu daya.

> **Notice:**
> - Untuk mencegah kerusakan perangkat, kabel positif dan negatif tidak boleh terbalik.
> - Untuk luas penampang kabel, lihat Table 4-7.

**Steps**
1. Atur battery circuit breaker sistem catu daya ke posisi OFF.
2. Sambungkan kabel grounding baterai lithium-ion. Satu ujung kabel grounding disambungkan ke sekrup grounding M6 baterai lithium-ion dengan torsi pengencangan 5 N·m; ujung lainnya ke grounding busbar site (Figure 4-24).

> **[Deskripsi gambar – Figure 4-24: Installing the Grounding Cables for the Lithium-Ion Batteries]** Empat battery pack ditumpuk vertikal (Battery pack 4 paling atas sampai Battery pack 1 paling bawah). Kabel grounding kuning-hijau dari tiap pack turun ke grounding busbar site di bagian bawah.

---

## Chunk 040
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 36-37
- **Tipe:** teks+gambar
- **Heading:** 4.8 Connecting Cables for Lithium-Ion Batteries – Step 3 (Communication Cables)

**Steps (lanjutan)**
3. Figure 4-25 menunjukkan sambungan kabel komunikasi untuk baterai lithium-ion pintar.
   a. Sambungkan kabel komunikasi antar baterai secara seri: satu ujung kabel komunikasi ke antarmuka COM IN baterai paling atas (Battery pack 4) dan ujung lainnya ke antarmuka COM OUT baterai berikutnya (Battery pack 3). Ulangi langkah ini sampai baterai paling bawah tersambung.
   b. Sambungkan kabel "RJ45-resistor-terminating-plug-to-two-core-3.81-mm-connector" ke CSU. Masukkan RJ45 resistor terminating plug kabel ke antarmuka COM OUT baterai paling atas, dan masukkan konektor dua-inti 3.81 mm kabel ke antarmuka J5-2&4 pada papan SPB base unit.
   c. Masukkan RJ45 termination resistor ke antarmuka COM IN Battery pack 1.

> **[Deskripsi gambar – Figure 4-25: Installing the Communication Cables for the Lithium-Ion Batteries]** Empat battery pack ditumpuk (Battery pack 4 atas sampai Battery pack 1 bawah) dengan kabel komunikasi hitam yang dirangkai antar port RJ45 di sisi kiri tiap pack. Dari baterai paling atas, kabel "RJ45-resistor-terminating-plug-to-2-pin-3.81-mm-pitch connector cable" menuju antarmuka J5 pada SPB (pin 1–4) di kanan atas. Di Battery pack 1 paling bawah dipasang RJ45 termination resistor.

---

## Chunk 041
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 37-38
- **Tipe:** teks+gambar
- **Heading:** 4.8 Connecting Cables for Lithium-Ion Batteries – Step 4 (Power Cables)

**Steps (lanjutan)**
4. Sambungkan kabel daya baterai lithium-ion seperti pada Figure 4-26.

> **Note:** Terminal positif dan negatif baterai sama-sama berupa sekrup M6, dengan torsi pengencangan 5 N·m.

> **[Deskripsi gambar – Figure 4-26: Installing the Power Cables for the Lithium-Ion Batteries]** Empat Battery circuit breaker (1–4) di bagian atas. Tiap breaker tersambung ke satu battery pack (Battery pack 1–4, bertumpuk di bawah) dengan sepasang kabel: kabel hitam ke terminal positif (+) dan kabel biru ke terminal negatif (−) pada sisi kanan pack tersebut.

---

## Chunk 042
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 39
- **Tipe:** teks
- **Heading:** Chapter 5 Checks After Installation – Environment Check & Electrical Connection Check

**Environment Check**
- Tidak ada selotip atau cable tie berlebih pada kabel.
- Tidak ada selotip, cable tie, serpihan kertas, atau kantong kemasan di sekitar perangkat.

**Electrical Connection Check**
- Semua kabel PE buatan sendiri harus kabel inti tembaga dengan diameter yang benar. Pada setiap bagian sambungan tidak boleh ada komponen yang dapat diputus seperti switch atau fuse, dan tidak boleh ada korsleting.
- Pastikan kabel grounding, kabel AC input, dan kabel internal tersambung dengan benar dan sekrup terkencang kuat. Pastikan input dan output tidak terhubung singkat.
- Potong sisa kabel daya dan kabel PE yang berlebih; jangan digulung.
- Terminal kabel daya dan kabel PE harus disolder atau di-crimp dengan kuat.
- Kabel yang terbuka dan gagang terminal pada terminal block harus dilindungi dengan heat-shrink tube dan tidak boleh terekspos.
- OT terminal harus dipasang dengan flat washer dan spring washer agar terpasang kuat; permukaan kontaknya harus dalam kondisi baik tanpa deformasi.
- Setelah kabel daya atau busbar penghubung tersambung, personel instalasi harus mengencangkan sekrup dengan alat torsi sesuai persyaratan torsi; personel instalasi dan personel inspeksi memakai penandaan garis merah dan biru untuk pemeriksaan ganda (double inspection):
  1. Setelah personel instalasi memeriksa dan memastikan sekrup terkencang, mereka melukis garis penanda **biru** pada sekrup. Garis harus melewati tepi sekrup (Figure 5-1).
  2. Setelah personel inspeksi memeriksa dan memastikan sekrup terkencang, mereka melukis garis penanda **merah** pada sekrup. Garis harus melewati tepi sekrup (Figure 5-1).

---

## Chunk 043
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 40
- **Tipe:** teks+gambar
- **Heading:** Chapter 5 Checks After Installation – Red and Blue Screw Markings & Cable Connection Check

Penandaan garis merah dan biru pada sekrup ditunjukkan pada Figure 5-1.

> **[Deskripsi gambar – Figure 5-1: Red and Blue Markings on a Screw]** Gambar sebuah sekrup/baut dari atas dengan dua garis penanda: garis biru di satu sisi dan garis merah di sisi lain, masing-masing melewati tepi sekrup ke permukaan di bawahnya.

**Cable Connection Check**
- Semua sambungan kabel harus kuat. Perhatikan khusus kekuatan dan konektivitas kabel sinyal.
- Kabel harus diikat rapi tanpa terpilin atau tertekuk berlebihan. Cable tie harus berjarak merata dan dikencangkan dengan benar, dan semua kepala cable tie menghadap arah yang sama.
- Ikat kabel daya, kabel PE, dan kabel sinyal secara terpisah.
- Kabel harus dirutekan dengan baik untuk memudahkan perawatan dan perluasan di masa depan.
- Semua cable tie di dalam ruangan harus dipotong rapi tanpa sisa panjang atau tepi tajam. Untuk cable tie di luar ruangan, sisakan 3 mm sampai 5 mm setelah dipotong.
- Ambil tindakan perlindungan untuk antarmuka yang tidak tersambung kabel.
- Pastikan label kabel benar dan menghadap arah yang sama agar mudah diperiksa di masa depan.

---

## Chunk 044
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 41
- **Tipe:** teks
- **Heading:** Chapter 6 Checking Electrical Connections – Overview

Uji sambungan listrik wajib dilakukan setelah menyambungkan kabel, untuk menghindari kerusakan perangkat akibat sambungan yang salah. Bagian dalam bab ini: 6.1 Detecting a Short Circuit on the AC Input Circuit; 6.2 Detecting a Short Circuit on the DC Output Circuit; 6.3 Measuring the AC Input Voltage; 6.4 Measuring the Terminal Voltage of a Battery Pack.

---

## Chunk 045
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 41-42
- **Tipe:** teks+tabel+gambar
- **Heading:** 6.1 Detecting a Short Circuit on the AC Input Circuit

**Abstract:** prosedur ini menjelaskan cara mendeteksi korsleting pada rangkaian AC input dan memeriksa apakah kabel AC input tersambung dengan benar.

> **Notice:** Untuk menghindari kerusakan multimeter, jangan melakukan uji korsleting saat daya menyala.

**Steps**
1. Atur external power switch perangkat (di AC power distribution unit) ke posisi OFF.
2. Atur AC input circuit breaker perangkat ke posisi ON.
3. Ubah multimeter ke mode buzzer.
4. Deteksi korsleting antar terminal rangkaian AC input perangkat. Titik dan kriteria deteksi ada pada Table 6-1. Figure 6-1 menunjukkan cara mendeteksi korsleting antara terminal AC input L1 dan N.
5. Setelah deteksi selesai, atur AC input circuit breaker perangkat ke posisi OFF.

**Table 6-1 Detection Points and Detection Criteria**

| Detection Points | Detection Criteria |
|---|---|
| L1-L2, L2-L3, dan L3-L1 | Jika buzzer tidak berbunyi, tidak ada korsleting. Jika buzzer berbunyi, ada korsleting; cari dan perbaiki titik gangguan, lalu sambung ulang kabel. |
| L1-N, L2-N, dan L3-N | (kriteria sama dengan baris di atas) |
| L1-PE, L2-PE, dan L3-PE | (kriteria sama dengan baris di atas) |
| N-PE | (kriteria sama dengan baris di atas) |

> **[Deskripsi gambar – Figure 6-1: Detecting a Short Circuit on the AC Input Circuit]** Empat breaker AC input berlabel N, L1, L2, L3. Sebuah tangan menempelkan black test lead (−) pada terminal N dan tangan lain menempelkan red test lead (+) pada terminal L1. Di sebelah kanan, ikon multimeter dengan keterangan "Buzzer mode".

---

## Chunk 046
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 42-43
- **Tipe:** teks+tabel
- **Heading:** 6.2 Detecting a Short Circuit on the DC Output Circuit – Abstract & Resistance Mode (dengan Rectifier)

**Abstract:** prosedur ini menjelaskan cara mendeteksi korsleting pada rangkaian DC output dan memeriksa apakah kabel DC output tersambung dengan benar.

> **Notice:** Untuk menghindari kerusakan multimeter, jangan melakukan uji korsleting saat daya menyala.

**Steps**
1. Pastikan DC output circuit breaker perangkat berada di posisi OFF.
2. Lakukan deteksi sesuai dua situasi berikut:
   - **Ada rectifier di sistem catu daya:** ubah multimeter ke mode resistance (hambatan) dan deteksi korsleting pada rangkaian DC output. Kriteria deteksi ada pada Table 6-2 (lihat Figure 6-2).

**Table 6-2 Detection Points and Detection Criteria (Resistance Mode)**

| Detection Points | Detection Criteria |
|---|---|
| Black test lead: negative terminal of the DC output circuit breaker. Red test lead: positive terminal of the DC output circuit breaker. | Jika nilai resistansi naik bertahap, tidak ada korsleting. Jika nilai resistansi 0 atau tidak berubah, ada korsleting; cari dan perbaiki titik gangguan lalu sambung ulang kabel. |

> **[Deskripsi gambar – Figure 6-2: Detecting a Short Circuit on a DC Output Circuit (Resistance Mode)]** DC PDU (grup LLVD1, BLVD, Battery circuit breaker 1–4, DC SPD). Sebuah tangan menempelkan red test lead (+) pada terminal positif breaker DC output dan tangan lain menempelkan black test lead (−) pada terminal negatifnya. Multimeter di kiri berlabel "Resistance mode".

---

## Chunk 047
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 43-44
- **Tipe:** teks+tabel
- **Heading:** 6.2 Detecting a Short Circuit on the DC Output Circuit – Buzzer Mode (tanpa Rectifier)

- **Tidak ada rectifier di sistem catu daya:** ubah multimeter ke mode buzzer dan deteksi korsleting pada rangkaian DC output. Kriteria deteksi ada pada Table 6-3 (lihat Figure 6-3).

**Table 6-3 Detection Points and Detection Criteria (Buzzer Mode)**

| Detection Points | Detection Criteria |
|---|---|
| Black test lead: negative terminal of the DC output circuit breaker. Red test lead: positive terminal of the DC output circuit breaker. | Jika buzzer tidak berbunyi, tidak ada korsleting. Jika buzzer berbunyi, ada korsleting; cari dan perbaiki titik gangguan lalu sambung ulang kabel. |

3. Setelah deteksi selesai, atur DC output circuit breaker di perangkat ke posisi OFF.

> **[Deskripsi gambar – Figure 6-3: Detecting a Short Circuit on a DC Output Circuit (Buzzer Mode)]** Sama seperti Figure 6-2: tangan memegang red test lead (+) pada terminal positif dan black test lead (−) pada terminal negatif breaker DC output pada DC PDU; multimeter berlabel "Buzzer mode".

---

## Chunk 048
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 44-45
- **Tipe:** teks+tabel+gambar
- **Heading:** 6.3 Measuring the AC Input Voltage

**Abstract:** prosedur ini menjelaskan cara mengukur tegangan AC input dan memeriksa apakah tegangan AC input memenuhi persyaratan operasional sistem catu daya.

**Steps**
1. Pastikan AC input circuit breaker perangkat berada di posisi OFF.
2. Atur external power switch sistem catu daya (di AC power distribution cabinet) ke posisi ON.
3. Ubah multimeter ke mode AC voltage.
4. Ukur tegangan AC input antar terminal AC input perangkat. Titik dan kriteria deteksi ada pada Table 6-4. Figure 6-4 menunjukkan cara mengukur tegangan AC input antara terminal L1 dan N.
5. Setelah pemeriksaan selesai, atur external power switch perangkat ke posisi OFF.

**Table 6-4 Detection Points and Detection Criteria**

| Detection Points | Detection Criteria |
|---|---|
| L1-N, L2-N, dan L3-N; N-PE | Tegangan neutral-to-ground harus lebih rendah dari 5 V. Jika tidak terpenuhi, jaringan listrik perlu diperbaiki untuk mengurangi selisih tegangan neutral-to-ground. Tegangan phase-to-neutral berada pada rentang 176 V sampai 295 V. Jika tidak terpenuhi, disarankan memakai diesel generator untuk memasok daya. |

> **[Deskripsi gambar – Figure 6-4: Measuring the AC Input Voltage]** Empat breaker AC input N, L1, L2, L3; black test lead (−) pada N dan red test lead (+) pada L1. Multimeter di kanan berlabel "AC voltage mode".

---

## Chunk 049
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 45-46
- **Tipe:** teks+tabel+gambar
- **Heading:** 6.4 Measuring the Terminal Voltage of a Battery Pack

**Abstract:** prosedur ini menjelaskan cara mengukur tegangan terminal battery pack dan memeriksa apakah kabel baterai tersambung dengan benar.

> **Notice:** Jika elektroda baterai tersambung salah, perangkat dapat rusak. Jika sambungan kabel baterai terbalik, lepas satu konektor baterai dari battery pack, lalu sambungkan kembali kabel baterai dengan benar.

**Steps**
1. Atur battery circuit breaker perangkat ke posisi OFF.
2. Ubah multimeter ke mode DC voltage.
3. Periksa tegangan terminal setiap battery pack. Titik dan kriteria deteksi ada pada Table 6-5. Figure 6-5 menunjukkan contoh pengukuran tegangan terminal battery pack 1.

**Table 6-5 Detection Points and Detection Criteria**

| Object | Detection Points | Detection Criteria |
|---|---|---|
| Battery pack 1/2/3/4 | Black test lead: negative terminal blocks of battery pack 1/2/3/4. Red test lead: positive terminal blocks of battery pack 1/2/3/4. | Jika nilainya positif, kabel baterai tersambung dengan benar. Jika nilainya negatif, sambungan kabel baterai terbalik; kabel harus disambung ulang dengan benar. |

> **[Deskripsi gambar – Figure 6-5: Measuring the Terminal Voltage of a Battery Pack]** Empat Battery circuit breaker (1–4) dalam satu baris. Satu tangan menempelkan black test lead (−) dan tangan lain red test lead (+) pada terminal breaker. Multimeter di kanan berlabel "DC voltage mode".

---

## Chunk 050
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 47
- **Tipe:** teks
- **Heading:** Chapter 7 System Power-On

Power-on hanya dapat dilakukan setelah uji sambungan listrik selesai. Prosedur power-on:
1. Pastikan baterai terpasang dengan benar, AC input circuit breaker dalam keadaan terputus (disconnected), dan DC output circuit breaker dalam keadaan terputus.
2. Masukkan (insert) rectifier.
3. Aktifkan AC input dan tutup AC input circuit breaker.
4. Tutup battery circuit breaker satu per satu.
5. Setelah tegangan sistem stabil, tutup DC output circuit breaker.

---

## Chunk 051
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 48
- **Tipe:** teks
- **Heading:** 8.1 Replacing a CSU – Abstract & Notice

**Abstract:** CSU dipakai untuk mengumpulkan informasi, mendeteksi alarm, dan mengelola operasi sistem catu daya DC. Jika CSU rusak, segera ganti. CSU mendukung hot swapping, yaitu pasokan daya ke perangkat tidak perlu diputus saat penggantian.

> **Notice:**
> - Untuk perangkat pintar yang memiliki data akumulasi, jika perangkat tidak di-reset sebelum diganti, data akumulasi dapat berubah secara abnormal. Karena itu, sebelum mengganti perangkat pintar, hapus data akumulasi dan catatan historis terkait.
> - Jika CSU sistem catu daya rusak, segera ganti.
> - Saat hot swapping CSU, lakukan perlahan agar tidak timbul percikan.
> - Saat mendorong CSU ke slot, jangan menekan layar LCD, tombol, atau indikator agar tidak rusak.
> - Setelah memasang CSU baru, parameter site CSU baru harus dikonfigurasi (impor parameter backup) dan harus sama dengan parameter site asli. Jika tidak, operasi sistem catu daya dapat sangat terpengaruh, mengakibatkan umur baterai lebih pendek atau gangguan layanan yang signifikan.

> **Note:** Agar personel perawatan di lokasi mudah memperoleh konfigurasi model yang kompatibel dan menghindari kunjungan ulang, disarankan membuat backup konfigurasi model dan parameter setiap site sebelum site acceptance test, lalu menyerahkannya kepada tim O&M klien.

---

## Chunk 052
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 48-49
- **Tipe:** teks+gambar
- **Heading:** 8.1 Replacing a CSU – Steps

**Steps**
1. Melepas CSU.
   a. Lepas baut dan tarik keluar CSU (Figure 8-1).
   b. Lepas kabel daya dan kabel sinyal dari CSU.
2. Memasang CSU.
   a. Sambungkan kabel daya dan kabel sinyal ke CSU.
      > **Notice:** Kabel harus disambungkan ke antarmuka yang sesuai pada papan SPB.
   b. Masukkan CSU ke slot dan kencangkan baut (Figure 8-2).

> **[Deskripsi gambar – Figure 8-1: Removing a CSU]** Dua panel dengan anak panah biru di tengah. Kiri: baut di sisi CSU dilepas (anak panah melengkung) dan CSU mulai ditarik keluar. Kanan: CSU sudah tertarik keluar sebagian sehingga papan hijau dengan terminal hijau terlihat.

> **[Deskripsi gambar – Figure 8-2: Installing a CSU]** Kebalikan Figure 8-1. Kiri: CSU didorong masuk ke slot. Kanan: CSU terpasang dan baut dikencangkan (anak panah melengkung) di kedua sisi.

---

## Chunk 053
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 49-50
- **Tipe:** teks
- **Heading:** 8.2 Replacing a Rectifier – Abstract, Notice & Note

**Abstract:** prosedur ini menjelaskan cara mengganti rectifier. Rectifier mendukung hot swap; dapat dipasang atau dilepas secara online saat sistem catu daya beroperasi. Jika rectifier rusak, segera ganti.

> **Notice:**
> - Jika CSU sedang beroperasi, jalankan fungsi CAN device statistics sebelum melepas rectifier.
> - Sebelum memasang rectifier baru, lepas film pada ventilasi atau benda lain yang menghalangi pendinginan rectifier, agar rectifier tidak rusak akibat pembuangan panas yang buruk.
> - Saat hot swapping rectifier, lakukan perlahan agar tidak timbul percikan.
> - Setelah rectifier menyala, sambungan rectifier yang longgar dapat merusak perangkat itu sendiri dan bahkan menyebabkan kebakaran akibat panas berlebih. Karena itu rectifier harus terpasang kuat.
> - Saat mendorong rectifier ke slot, jangan menekan ventilasi, tombol, atau indikator; jika tidak, rectifier dapat rusak.

> **Note:** Pengangkutan jarak jauh dapat membuat komponen di dalam perangkat longgar. Jika terdengar suara aneh di dalam rectifier saat instalasi, hubungi supplier untuk perbaikan atau penggantian.

---

## Chunk 054
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 50-52
- **Tipe:** teks+gambar
- **Heading:** 8.2 Replacing a Rectifier – Steps (Remove & Install)

**Steps**
1. Melepas rectifier.
   a. Geser unlocking slider ke atas ke posisi unlocking (Figure 8-3).
   b. Tarik turun ejector lever rectifier (Figure 8-4).
   c. Pegang wrench (tuas) dan tarik rectifier keluar dari subrack (Figure 8-5).
   d. Saat rectifier hampir keluar sepenuhnya, angkat dengan satu tangan dan tarik keluar.
2. Memasang rectifier.
   a. Geser unlocking slider ke atas ke posisi unlocking, dan tarik turun wrench rectifier.
   b. Dorong perlahan rectifier ke subrack rectifier mengikuti guide rail (Figure 8-6).
   c. Setelah rectifier terdorong masuk sepenuhnya, putar (turn on) ejector lever untuk mengunci rectifier di slot instalasi (Figure 8-7).
   d. Geser unlocking slider ke bawah ke posisi lock (Figure 8-8).

> **[Deskripsi gambar – Figure 8-3: Move the Unlocking Slider Upward to the Unlocking Position]** Close-up panel depan rectifier ZTE R4850 (kipas bulat di kiri) dengan anak panah biru ke atas pada slider di sisi kanan.

> **[Deskripsi gambar – Figure 8-4: Pull Down the Ejector Lever of the Rectifier]** Close-up rectifier dengan anak panah biru melengkung ke bawah pada ejector lever.

> **[Deskripsi gambar – Figure 8-5: Removing a Rectifier]** Rectifier abu-abu ditarik keluar horizontal dari subrack; anak panah biru menunjuk ke kiri (arah keluar).

> **[Deskripsi gambar – Figure 8-6: Installing a Rectifier]** Kebalikan Figure 8-5: rectifier didorong masuk ke subrack mengikuti guide rail; anak panah biru menunjuk ke kanan (arah masuk).

> **[Deskripsi gambar – Figure 8-7: Turn On the Rectifier's Ejector Lever]** Close-up rectifier dengan anak panah biru melengkung ke atas pada ejector lever.

> **[Deskripsi gambar – Figure 8-8: Pull Down the Unlocking Slider to the Lock Position]** Close-up rectifier dengan anak panah biru ke bawah pada unlocking slider.

---

## Chunk 055
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 52-53
- **Tipe:** teks+gambar
- **Heading:** 8.3 Replacing a Circuit Breaker

**Abstract:** smart circuit breaker dipakai untuk menyambungkan beban atau baterai. Jika smart circuit breaker rusak, segera ganti agar beban atau baterai dapat berjalan dengan baik.

> **Notice:**
> - Jangan atur circuit breaker ke posisi ON sebelum terpasang dengan benar.
> - Circuit breaker harus dipasang dengan slot koneksi kabel berada di atas switch.
> - Terminal kabel daya harus di-crimp sesuai panduan di 4.3.1 Connecting Cables to a 125 A-Case Circuit Breaker atau 4.3.2 Connecting Cables to a 63 A-Case Circuit Breaker. Kabel telanjang tidak boleh disambungkan langsung ke circuit breaker.
> - Circuit breaker harus dipasang sebelum kabel daya disambungkan.
> - Jangan menarik protection pole saat memasang atau melepas circuit breaker agar protection pole tidak rusak.

**Prerequisite:** pastikan circuit breaker yang akan dipasang tidak rusak.

**Steps**
1. Atur circuit breaker yang akan diganti ke posisi OFF.
2. Catat informasi sambungan kabel dan lepas kabel.
3. Tarik keluar circuit breaker:
   a. Tarik keluar switch circuit breaker.
   b. Gunakan water pump pliers untuk menarik keluar circuit breaker (Figure 8-9).
4. Pasang circuit breaker baru.
5. Sambungkan kabel ke circuit breaker sesuai informasi sambungan kabel yang dicatat.
6. Atur circuit breaker ke posisi ON.

> **[Deskripsi gambar – Figure 8-9: Replacing a Circuit Breaker]** Modul breaker hitam dengan tangan menarik switch di bagian bawah depan; anak panah merah menunjukkan arah tarikan.

---

## Chunk 056
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 53-54
- **Tipe:** teks+gambar
- **Heading:** 8.4 Replacing a DC SPD

**Abstract:** DC SPD memberikan perlindungan terhadap surge pada rangkaian DC. Prosedur ini menjelaskan cara mengganti DC SPD.

**Steps**
1. Tarik keluar DC SPD yang rusak (Figure 8-10).
2. Pasang DC SPD baru dengan spesifikasi yang sama ke slot asal (Figure 8-11).

> **[Deskripsi gambar – Figure 8-10: Pulling out the DC SPD]** Tangan menarik modul DC SPD hitam keluar dari slot DC PDU; anak panah biru menunjuk keluar. Indikator hijau breaker terlihat di sekitarnya.

> **[Deskripsi gambar – Figure 8-11: Installing a New DC SPD]** Tangan mendorong modul DC SPD baru masuk ke slot asalnya di DC PDU; anak panah biru menunjuk ke dalam.

---

## Chunk 057
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 55-56
- **Tipe:** teks+gambar
- **Heading:** 9.1 Exporting the Parameter File

**Abstract:** agar personel perawatan di lokasi mudah memperoleh konfigurasi model yang kompatibel dan menghindari kunjungan ulang, disarankan membuat backup konfigurasi model dan parameter setiap site sebelum site acceptance test, lalu menyerahkannya kepada tim O&M klien. Prosedur ini menjelaskan cara mengekspor file parameter dari CSU.

**Steps**
- **Web Operations**
  1. Di halaman utama, pilih **System Maintain > Devices Maintain > Parameter Maintain**; halaman **Parameter Maintain** ditampilkan (Figure 9-1).
  2. Klik **Export Parameter File** untuk mengekspor file parameter.
- **GUI Operations**
  1. Di layar utama, pilih ikon menu (ikon disket/simpan) **> Para. Maintain > Export Para. File** untuk mengekspor file parameter.

> **[Deskripsi gambar – Figure 9-1: Parameter Maintain Page]** Tangkapan layar web CSU "ZTE Energy Management". Menu kiri berisi Site Overview, Real Alarm, Real Data, Parameter Set, Device Control, Parameter Config, System Maintain (aktif), System Information, Devices Maintain, Historical Record, Users Management, Device Information. Tab Parameter Maintain aktif di bagian atas. Panel utama memiliki bagian Parameter Export (checkbox export file encryption password dan tombol Export Parameter File), bagian Parameter Import (checkbox encryption password, kolom pilih file dengan tombol Choose dan Upload Parameter File), dan bagian Parameter Backup & Recover dengan beberapa tombol backup/restore.

---

## Chunk 058
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 56-57
- **Tipe:** teks+gambar
- **Heading:** 9.2 Importing the Parameter File

**Abstract:** setelah memasang CSU baru, parameter site CSU baru harus dikonfigurasi (impor parameter backup) dan harus sama dengan parameter site asli. Prosedur ini menjelaskan cara mengimpor file parameter ke CSU.

**Steps**
- **Web Operations**
  1. Di halaman utama, pilih **System Maintain > Devices Maintain > Parameter Maintain**; halaman **Parameter Maintain** ditampilkan (Figure 9-2).
  2. Klik tombol **Choose** untuk memilih file parameter.
  3. Klik tombol **Upload Parameter File** untuk mengunggah.
- **GUI Operations**
  1. Di layar utama, pilih ikon menu (ikon disket/simpan) **> Para. Maintain > Import Para. File** untuk mengimpor file parameter.

> **[Deskripsi gambar – Figure 9-2: Parameter Maintain Page]** Tangkapan layar yang sama dengan Figure 9-1: halaman web CSU "ZTE Energy Management" dengan tab Parameter Maintain aktif. Bagian Parameter Import berisi kolom pemilihan file dengan tombol Choose dan Upload Parameter File.

---

## Chunk 059
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 57-58
- **Tipe:** tabel
- **Heading:** 9.3 Setting Parameters – Table 9-1 Parameter List

**Abstract:** sebelum meninggalkan pabrik, berbagai parameter sistem catu daya sudah diatur sebelumnya. Karena kondisi lokasi dan kebutuhan pengguna berbeda, sebagian parameter perlu diatur dan dikalibrasi sesuai kondisi aktual saat perangkat dinyalakan. Jika ragu terhadap pengaturan parameter tertentu, hubungi technical support.

**Steps**
1. Dengan konfigurasi baterai ZXESM R321 pada sistem catu daya sebagai contoh, atur parameter berikut melalui CSU sesuai kondisi aktual, mengacu pada Table 9-1.

**Table 9-1 Parameter List** (nilai parameter pada tabel hanyalah contoh)

| No. | Parameter | Default Value | Access method |
|---|---|---|---|
| 1 | AC Input Scenario | Mains | ⚙ > System > Parameter Set |
| 2 | Battery Config | Smart Li Batt | ⚙ > System > Parameter Set |
| 3 | Li Battery Charge Current Coefficient | 0.10 C3 | > Battery > Parameter Set |
| 4 | Battery Capacity[1] | 81 Ah | > Battery > Parameter Set |
| 5 | Battery Capacity[2] | 0 Ah | > Battery > Parameter Set |
| 6 | Battery Capacity[3] | 0 Ah | > Battery > Parameter Set |
| 7 | Battery Capacity[4] | 0 Ah | > Battery > Parameter Set |
| 8 | Battery Capacity[5] | 0 Ah | > Battery > Parameter Set |
| 9 | Battery Capacity[6] | 0 Ah | > Battery > Parameter Set |
| 10 | Battery Capacity[7] | 0 Ah | > Battery > Parameter Set |
| 11 | Battery Capacity[8] | 0 Ah | > Battery > Parameter Set |
| 12 | LLVD1 Voltage | 47.0 V | > Battery > Parameter Set |
| 13 | BLVD Voltage | 46.0 V | > Battery > Parameter Set |

---

## Chunk 060
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 58
- **Tipe:** tabel
- **Heading:** 9.4 Torques for Connecting Cables to Circuit Breakers (Table 9-2)

Torsi untuk menyambungkan kabel ke berbagai tipe circuit breaker ada pada Table 9-2.

**Table 9-2 Torques for Connecting Cables to Circuit Breakers**

| Type | Torque (N·m) |
|---|---|
| 100 A/4P AC input circuit breaker | 2.0 |
| 16 A/1P AC output circuit breaker | 1.2 |
| 125 A/1P battery circuit breaker | 2.0 |
| 63 A/1P DC output circuit breaker | 1.2 |
| 125 A/1P DC output circuit breaker | 2.0 |

---

## Chunk 061
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 58-60
- **Tipe:** teks+gambar
- **Heading:** 9.5 Precautions for Installing a Circuit Breaker

- Saat memasang circuit breaker, masukkan secara horizontal mengikuti guide rail subrack. Jangan miringkan ke kiri atau kanan. Setelah circuit breaker terpasang di subrack, circuit breaker masih dapat bergoyang karena celah pada guide rail.
- Saat memasang circuit breaker, jangan memaksa mendorong atau memukul dengan palu ketika terasa ada hambatan atau circuit breaker tidak dapat masuk sepenuhnya dan masih tersisa margin 1 sampai 2 cm. Hambatan terjadi karena circuit breaker tidak dimasukkan secara horizontal. Jika terasa ada hambatan, tarik circuit breaker keluar dan masukkan kembali secara horizontal.
- Figure 9-3 dan Figure 9-4 menunjukkan pemasangan yang salah. Figure 9-5 menunjukkan pemasangan yang benar.

> **[Deskripsi gambar – Figure 9-3: Incorrect Insertion 1]** Foto breaker yang dimasukkan miring ke kiri pada subrack; anak panah merah miring, teks "Tilts left." dan tanda silang (X) merah besar menandakan pemasangan salah.

> **[Deskripsi gambar – Figure 9-4: Incorrect Insertion 2]** Foto breaker yang dimasukkan miring ke kanan; anak panah merah miring, teks "Tilts right." dan tanda silang (X) merah besar menandakan pemasangan salah.

> **[Deskripsi gambar – Figure 9-5: Correct Insertion]** Foto breaker yang dimasukkan lurus mengikuti guide rail; anak panah merah vertikal lurus, teks "Insert horizontally." dan tanda centang (✓) merah menandakan pemasangan benar.

---

## Chunk 062
- **Dokumen:** ZXEPS_E6N1_DC_Power_System_Quick_Installation_Guide_R01M201.pdf
- **Halaman:** 65-66
- **Tipe:** tabel
- **Heading:** Glossary (Daftar Singkatan)

| Singkatan | Kepanjangan |
|---|---|
| CSU | Centralized System Management Unit |
| DI | Digital Input |
| DO | Digital Output |
| FAT | File Allocation Table |
| FE | Fast Ethernet |
| HTTPS | Hypertext Transfer Protocol Secure |
| LCD | Liquid Crystal Display |
| O&M | Operation & Maintenance |
| PDU | Power Distribution Unit |
| PU | Power Unit |
| SD | Secure Digital memory card |
| SNMP | Simple Network Management Protocol |
| USB | Universal Serial Bus |

---
