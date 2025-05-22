# UTS PPPL (Prinsip Pengembangan Perangkat Lunak)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Design Patterns](https://img.shields.io/badge/Design_Patterns-Implemented-brightgreen.svg)](https://refactoring.guru/design-patterns)

Repositori ini berisi implementasi dari berbagai **Design Pattern** dalam program-program sederhana berbasis Command Line Interface (CLI). Setiap program dikembangkan untuk menunjukkan cara kerja dan manfaat dari pola desain tertentu.

---

## 📂 Struktur Repositori

uts-pppl/
├── kalkulator/
│   ├── ... (File-file proyek Kalkulator)
│   └── README.md
├── pemantau_suhu/
│   ├── ... (File-file proyek Pemantau Suhu)
│   └── README.md
├── todo_list/
│   ├── ... (File-file proyek Todo List)
│   └── README.md
└── README.md                   # README utama repositori ini


---

## 🚀 Proyek dan Design Pattern yang Digunakan

Repositori ini mencakup tiga proyek utama, masing-masing dengan implementasi Design Pattern yang berbeda:

### 1. Kalkulator Sederhana

* **Design Pattern:** **Strategy Pattern**
* **Deskripsi:** Program kalkulator CLI yang memungkinkan pemilihan strategi operasi matematika (penjumlahan, pengurangan, perkalian, pembagian) secara dinamis.
* **Detail Lebih Lanjut:** Untuk penjelasan mendalam mengenai implementasi Strategy Pattern pada kalkulator ini, silakan lihat [README.md di folder `kalkulator`](./kalkulator/README.md).

### 2. Sistem Pemantau Suhu

* **Design Pattern:** **Observer Pattern**
* **Deskripsi:** Aplikasi pemantau suhu sederhana yang secara otomatis memperbarui berbagai tampilan (display) saat suhu dari sensor berubah.
* **Detail Lebih Lanjut:** Untuk penjelasan mendalam mengenai implementasi Observer Pattern pada sistem pemantau suhu ini, silakan lihat [README.md di folder `pemantau_suhu`](./pemantau_suhu/README.md).

### 3. Aplikasi Todo List

* **Design Pattern:** **Command Pattern**
* **Deskripsi:** Aplikasi Todo List berbasis CLI yang mendukung penambahan, penghapusan, penandaan tugas selesai, serta fitur **Undo** dan **Redo** menggunakan Command Pattern.
* **Detail Lebih Lanjut:** Untuk penjelasan mendalam mengenai implementasi Command Pattern pada aplikasi Todo List ini, silakan lihat [README.md di folder `todo_list`](./todo_list/README.md).

---

## 📚 Cara Menjalankan

Untuk menjalankan masing-masing program:

1.  **Kloning repositori ini:**
    ```bash
    git clone [https://github.com/TinoIf/tugas_kuliah.git](https://github.com/TinoIf/tugas_kuliah.git)
    cd tugas_kuliah/uts-pppl
    ```
2.  **Navigasi ke direktori proyek yang ingin Anda jalankan:**
    * Untuk Kalkulator: `cd kalkulator`
    * Untuk Pemantau Suhu: `cd pemantau_suhu`
    * Untuk Todo List: `cd todo_list`
3.  **Jalankan program utama dari direktori tersebut:**
    ```bash
    python main.py
    ```
    (Pastikan Anda berada di direktori proyek yang benar)

---

## 🤝 Kontribusi

Jika Anda memiliki saran atau perbaikan, jangan ragu untuk membuka *issue* atau mengirim *pull request*.

---
