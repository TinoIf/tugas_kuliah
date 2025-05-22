# Penjelasan Implementasi Membuat Kalkulator dengan Strategy Pattern

Proyek ini adalah implementasi kalkulator sederhana menggunakan **Strategy Design Pattern** dengan bahasa Python. Program dijalankan melalui CLI (Command Line Interface) dan mendukung operasi penjumlahan, pengurangan, perkalian, dan pembagian.

---

## Langkah-langkah Implementasi

### Langkah 1: Membuat Kelas Abstrak

- File: `strategi_operasi.py`
- Gunakan modul `ABC` dari Python untuk membuat kelas abstrak `StrategiOperasi`.
- Di dalam kelas ini dibuat method abstrak `eksekusi(a, b)` yang nantinya harus diisi (diimplementasikan) oleh setiap strategi operasi.

### Langkah 2: Membuat Kelas Operasi Matematika

- Folder: `operasi`
- Buat 4 file:
  - `operasi_penjumlahan.py`
  - `operasi_pengurangan.py`
  - `operasi_perkalian.py`
  - `operasi_pembagian.py`
- Masing-masing file berisi kelas yang mengimplementasikan `StrategiOperasi` dan mengisi fungsi `eksekusi(a, b)` sesuai jenis operasinya contoh dalam file `operasi_penjumlahan.py` ini akan mengembalikan nilai a + b dalam fungsi eksekusi nya.

### Langkah 3: Membuat Kelas Kalkulator

- File: `kalkulator.py`
- Di dalam kelas `Kalkulator`, dibuat method `pilih_strategi()` untuk menyimpan strategi yang dipilih, dan method `hitung(a, b)` untuk mengeksekusi strategi tersebut.

### Langkah 4: Membuat Program Utama (main.py)

Di file `main.py`, dibuat antarmuka pengguna berbasis teks (CLI) untuk menjalankan kalkulator. Berikut adalah penjelasan alur program:

1. **Perulangan Program**:

   - Program berjalan dalam loop `while status` agar dapat terus menerima input dari pengguna sampai memilih untuk keluar.

2. **Inisialisasi Kalkulator**:

   - Di dalam loop, dibuat objek `Kalkulator` setiap kali perulangan dimulai.

3. **Membuat Objek Strategi Operasi**:

   - Sebuah dictionary `operasi` dibuat, yang berisi objek dari masing-masing operasi (`OperasiPenjumlahan`, `OperasiPengurangan`, `OperasiPerkalian`, `OperasiPembagian`).
   - Masing-masing objek sudah mengimplementasikan strategi yang berbeda dari kelas abstrak `StrategiOperasi`.

4. **Menampilkan Menu CLI**:

   - Pengguna diberikan pilihan 1–5 untuk memilih operasi matematika atau keluar dari program.

5. **Memproses Pilihan Pengguna**:

   - Program memeriksa apakah input valid (`1` hingga `5`).
   - Jika pengguna memilih `5`, program menampilkan pesan terima kasih dan menghentikan perulangan.

6. **Meminta Input Angka**:

   - Jika pengguna memilih operasi (1–4), maka diminta untuk memasukkan dua bilangan (a dan b) sebagai input operasi.

7. **Memilih Strategi dan Menjalankan Operasi**:

   - Objek strategi dari dictionary `operasi` diambil berdasarkan input pengguna.
   - Objek strategi ini kemudian dikirim ke objek `Kalkulator` menggunakan `pilih_strategi()`.
   - Kemudian, kalkulator menjalankan perhitungan menggunakan `hitung(a, b)` yang secara internal akan memanggil method `eksekusi()` dari strategi yang telah dipilih.

8. **Menampilkan Hasil**:
   - Hasil operasi ditampilkan ke layar.

---

## Cara Menjalankan Program

1. Jalankan terminal atau command prompt.
2. Pastikan berada di direktori utama proyek.
3. Jalankan perintah:

```bash
python main.py
```
