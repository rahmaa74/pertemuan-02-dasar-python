# Pertemuan 02 Dasar Python

## Identitas

- Nama : rahma muhrohmah jalianty
- NIM : 2225250169
- Kelas : 3f

---

## Tujuan Repository

Repository ini dibuat untuk memenuhi tugas Pertemuan 02 mata kuliah Algoritma dan Pemrograman.

Materi yang dipelajari pada pertemuan ini meliputi:

- Variabel dan konstanta
- Tipe data dasar Python
- Input dan output
- Operator aritmetika
- Konversi tipe data
- Penggunaan Git dan GitHub

---

## Struktur Project

```text
pertemuan-02-dasar-python/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_biodata.py
│   ├── 02_persegi_panjang.py
│   ├── 03_konversi_suhu.py
│   └── 04_nilai_akhir.py
├── tugas/
│   └── kalkulator_koordinat.py
└── kuis.docx
```

---

## Deskripsi Program

### latihan/01_biodata.py

Program untuk menerima input nama, NIM, kelas, dan tahun lahir, kemudian menghitung perkiraan umur berdasarkan tahun sekarang.

### latihan/02_persegi_panjang.py

Program untuk menghitung luas dan keliling persegi panjang berdasarkan input panjang dan lebar.

### latihan/03_konversi_suhu.py

Program untuk mengonversi suhu dari Celsius ke Fahrenheit dan Kelvin.

### latihan/04_nilai_akhir.py

Program untuk menghitung nilai akhir mahasiswa berdasarkan bobot nilai Tugas, UTS, dan UAS.

### tugas/kalkulator_koordinat.py

Program untuk:

- Menghitung perubahan koordinat (dx dan dy)
- Menghitung jarak Euclidean dua titik
- Menghitung titik tengah dua koordinat
- Menampilkan hasil dengan format dua angka desimal

---

## Cara Menjalankan Program

### Latihan 1 - Biodata

```bash
python latihan/01_biodata.py
```

### Latihan 2 - Persegi Panjang

```bash
python latihan/02_persegi_panjang.py
```

### Latihan 3 - Konversi Suhu

```bash
python latihan/03_konversi_suhu.py
```

### Latihan 4 - Nilai Akhir

```bash
python latihan/04_nilai_akhir.py
```

### Tugas Utama - Kalkulator Koordinat

```bash
python tugas/kalkulator_koordinat.py
```

Pada sistem Linux atau macOS dapat menggunakan:

```bash
python3 nama_file.py
```

---

# Hasil Pengujian

## Latihan 1 - Biodata

### Input

```text
Nama : rahma muhrohmah jalianty
NIM : 2225250169
Kelas : 3f
Tahun lahir : 2007
```

### Output

```text
KARTU BIODATA

Nama  : rahma muhrohmah jalianty
NIM   : 2225250169
Kelas : 3f
Umur  : sekitar 19 tahun
```

---

## Latihan 2 - Persegi Panjang

| Panjang | Lebar | Luas | Keliling |
|----------|----------|----------|----------|
| 15 | 28 | 420.00 | 86.00 |

---

## Latihan 3 - Konversi Suhu

| Celsius | Fahrenheit | Kelvin |
|----------|----------|----------|
| 0 | 32.00 °F | 273.15 K |
| 100 | 212.00 °F | 373.15 K |

---

## Latihan 4 - Nilai Akhir

| Nilai Tugas | Nilai UTS | Nilai UAS | Nilai Akhir |
|------------|------------|-----------|------------|
| 90 | 85 | 95 | 90.00 |

---

## Tugas Utama - Kalkulator Koordinat

| Kasus | Titik A | Titik B | Jarak | Titik Tengah |
|--------|----------|----------|----------|----------|
| 1 | (0,0) | (3,4) | 5.00 | (1.50, 2.00) |
| 2 | (-2,1) | (4,1) | 6.00 | (1.00, 1.00) |
| 3 | (2.5,-1) | (2.5,3) | 4.00 | (2.50, 1.00) |

### Kesimpulan Pengujian

Seluruh program berhasil dijalankan dengan baik dan menghasilkan output yang sesuai dengan perhitungan manual maupun test case yang diberikan pada modul praktikum.

---

## Refleksi

Pada pertemuan ini saya mempelajari dasar-dasar pemrograman Python, seperti penggunaan variabel, konstanta, tipe data, input-output, operator aritmetika, dan format output menggunakan f-string.

Saya juga mempelajari penggunaan Git dan GitHub untuk mengelola versi program, membuat commit, serta mengunggah tugas ke repository secara online.

Kesalahan yang saya temukan selama pengerjaan adalah kurang teliti dalam penggunaan tipe data dan format tampilan output. Kesalahan tersebut dapat diperbaiki dengan melakukan pengujian menggunakan test case yang telah disediakan pada modul.

Pada pertemuan berikutnya saya ingin lebih memahami materi mengenai percabangan (if), logika program, serta penyelesaian masalah menggunakan algoritma yang lebih kompleks.

---

## Sumber

- Modul Algoritma dan Pemrograman Pertemuan 02.
- Python Software Foundation – Python Documentation.
- Visual Studio Code Documentation.
- GitHub Documentation.