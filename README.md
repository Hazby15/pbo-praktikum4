# Praktikum PBO - Abstraksi Data Bangun Ruang

## Deskripsi
Repository ini berisi implementasi konsep Pemrograman Berorientasi Objek (OOP) berbasis Python 3. Program ini dirancang untuk mendemonstrasikan prinsip **Abstraksi Data**, **Pewarisan (Inheritance)**, dan **Polimorfisme** melalui studi kasus perhitungan geometri (Kubus, Balok, dan Tabung) guna memenuhi tugas Praktikum PBO Minggu ke-4.

## Fitur Utama
* **Abstract Base Class (ABC):** Penggunaan modul bawaan `abc` untuk mendefinisikan kerangka induk bangun ruang yang tidak dapat diinstansiasi secara langsung.
* **Polimorfisme:** Eksekusi method `hitung_volume()`, `hitung_luas_permukaan()`, dan `hitung_keliling()` secara dinamis dari berbagai objek melalui satu struktur perulangan.
* **Subclassing Spesifik:** Setiap subclass konkret meng-override method abstrak dan menambahkan minimal 2 atribut unik (misal: `massa` dan `bahan` pada Kubus, serta `orientasi` dan `fungsi` pada Balok).

## Cara Menjalankan Program
1. Pastikan Python 3 sudah terinstal di sistem Anda.
2. Unduh file program atau kloning repository ini:
   ```bash
   git clone <link-repository-kamu>
