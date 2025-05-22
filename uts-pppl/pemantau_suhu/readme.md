# Sistem Pemantau Suhu Sederhana dengan Observer Pattern

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Design Pattern](https://img.shields.io/badge/Design_Pattern-Observer-orange.svg)](https://refactoring.guru/design-patterns/observer)

Sistem ini mendemonstrasikan implementasi **Observer Design Pattern** untuk memantau perubahan suhu dari sebuah sensor dan memperbarui berbagai tampilan secara otomatis.

---

## Daftar Isi

- [Apa itu Observer Pattern?](#apa-itu-observer-pattern)
- [Struktur Proyek](#struktur-proyek)
- [Konsep Observer Pattern dalam Kode](#konsep-observer-pattern-dalam-kode)
  - [Subject (Penerbit)](#subject-penerbit)
  - [Observer (Pelanggan)](#observer-pelanggan)
  - [Orkestrasi Utama (`main.py`)](#orkestrasi-utama-mainpy)
- [Cara Menjalankan Program](#cara-menjalankan-program)

---

## Apa itu Observer Pattern?

**Observer Pattern** adalah _behavioral design pattern_ yang mendefinisikan ketergantungan _one-to-many_ antara objek. Ini berarti ketika satu objek (disebut **Subject** atau **Publisher**) berubah status, semua objek yang bergantung padanya (disebut **Observer** atau **Subscriber**) akan diberitahu dan diperbarui secara otomatis.

**Manfaat Utama:**

- **Loose Coupling:** Subject tidak perlu mengetahui detail konkret dari Observer. Ia hanya berinteraksi melalui antarmuka Observer. Ini membuat sistem lebih fleksibel dan mudah diubah.
- **Notifikasi Otomatis:** Observer tidak perlu secara terus-menerus "memeriksa" perubahan pada Subject. Mereka akan secara otomatis diberitahu saat ada perubahan.

---

## Struktur Proyek

Struktur folder proyek diorganisir secara modular untuk kejelasan dan pemisahan tanggung jawab.
temperature_monitor/
├── src/
│ ├── interfaces/
│ │ └── observer.py # Antarmuka untuk semua Observer
│ ├── observers/
│ │ ├── current_conditions_display.py # Observer untuk tampilan suhu saat ini
│ │ └── statistics_display.py # Observer untuk tampilan statistik suhu
│ └── subject/
│ └── temperature_sensor.py # Subject yang mengelola suhu dan notifikasi
└── main.py # Program utama untuk demonstrasi

---

## Konsep Observer Pattern dalam Kode

Mari kita lihat bagaimana peran Subject dan Observer diimplementasikan dalam kode kita:

### Subject (Penerbit)

**File:** `src/subject/temperature_sensor.py`

**Peran:** `TemperatureSensor` adalah **Subject** dalam pola ini. Ia bertanggung jawab untuk menyimpan data suhu (`_temperature`) dan mengelola daftar **Observer** yang tertarik pada perubahan suhu tersebut.

**Implementasi Kunci:**

- **`_observers: List[Observer]`**: Ini adalah daftar semua objek `Observer` yang telah mendaftar (berlangganan) ke `TemperatureSensor`. Ini merupakan inti dari hubungan _one-to-many_.
- **`register_observer(self, observer: Observer)`**: Metode ini memungkinkan sebuah objek `Observer` untuk **mendaftarkan diri** ke `TemperatureSensor`. Setelah terdaftar, `Observer` ini akan menerima notifikasi.
- **`remove_observer(self, observer: Observer)`**: Metode ini memungkinkan sebuah objek `Observer` untuk **berhenti berlangganan** dari `TemperatureSensor`. Setelah dihapus, Observer ini tidak akan lagi menerima notifikasi.
- **`_notify_observers(self)`**: Ini adalah metode **penting** yang menjadi pemicu notifikasi. Ketika dipanggil, ia akan **melakukan iterasi** melalui semua `Observer` yang terdaftar dalam `_observers` dan memanggil metode `update()` mereka masing-masing, meneruskan suhu terbaru (`_temperature`).
- **`set_temperature(self, new_temperature: float)`**: Ini adalah metode utama untuk **mengubah status** `TemperatureSensor`. Jika suhu baru berbeda dari suhu sebelumnya, `_notify_observers()` akan dipanggil.

### Observer (Pelanggan)

**File:** `src/interfaces/observer.py` (Antarmuka)
**File:** `src/observers/current_conditions_display.py` (Implementasi Konkret)
**File:** `src/observers/statistics_display.py` (Implementasi Konkret)

**Peran:**

1.  **`Observer` (Antarmuka):** Mendefinisikan kontrak yang harus dipatuhi oleh semua kelas Observer konkret. Ini memastikan bahwa setiap Observer memiliki metode `update()` yang akan dipanggil oleh Subject.
2.  **`CurrentConditionsDisplay` & `StatisticsDisplay` (Observer Konkret):** Ini adalah dua implementasi spesifik dari `Observer`. Mereka "berlangganan" ke `TemperatureSensor` dan akan bereaksi serta memperbarui tampilan mereka setiap kali suhu berubah.

**Implementasi Kunci:**

- **Mewarisi `Observer`**: Kedua kelas tampilan (`CurrentConditionsDisplay`, `StatisticsDisplay`) mewarisi dari `Observer` (`class CurrentConditionsDisplay(Observer):`), memastikan mereka mengimplementasikan metode `update()`.
- **Pendaftaran Diri saat Inisialisasi**: Dalam konstruktor (`__init__`), setiap Observer menerima instance `TemperatureSensor` sebagai argumen dan segera memanggil `self._sensor.register_observer(self)`. Ini adalah langkah di mana Observer "berlangganan" ke Subject.
- **`update(self, temperature: float)`**: Metode ini adalah **titik reaksi** bagi Observer. Ketika `TemperatureSensor` memanggil `_notify_observers()`, metode `update()` pada setiap Observer terdaftar akan dipanggil dengan suhu terbaru. Setiap Observer kemudian akan menjalankan logikanya sendiri untuk memproses dan menampilkan data tersebut (misalnya, `CurrentConditionsDisplay` menampilkan suhu saat ini, sedangkan `StatisticsDisplay` menghitung rata-rata, min, dan maks).

### Orkestrasi Utama (`main.py`)

**File:** `main.py`

**Peran:** File ini adalah titik masuk program yang menginisialisasi Subject (`TemperatureSensor`) dan Observer (`CurrentConditionsDisplay`, `StatisticsDisplay`), serta mengorkestrasi interaksi antara pengguna dan sistem.

**Implementasi Kunci:**

- **Inisialisasi Subject:** Sebuah instance `TemperatureSensor` dibuat.
- **Inisialisasi & Pendaftaran Observer:** Dua instance Observer dibuat, dan **saat inisialisasi, mereka otomatis mendaftarkan diri** ke `temperature_sensor`.
- **Loop Interaktif:** Program berjalan dalam loop `while True`, terus meminta pengguna untuk memasukkan suhu baru.
- **Pemicu Perubahan Status:** Ketika pengguna memasukkan suhu baru, `temperature_sensor.set_temperature(new_temperature)` dipanggil. Ini adalah momen di mana Subject mengubah statusnya, dan secara otomatis **memicu mekanisme notifikasi** ke semua Observer yang terdaftar.

---

## Cara Menjalankan Program

Untuk menjalankan program ini, ikuti langkah-langkah di bawah:

1.  **Buat Struktur Folder:**
    Pastikan Anda memiliki struktur folder seperti yang ditunjukkan di bagian [Struktur Proyek](#struktur-proyek) di atas, dengan semua file `.py` berada di lokasi yang benar.

2.  **Navigasi ke Direktori Utama Proyek:**
    Buka terminal atau command prompt Anda dan navigasikan ke direktori `temperature_monitor`:

    ```bash
    cd /path/to/your/temperature_monitor
    ```

3.  **Jalankan Program:**
    Eksekusi file `main.py` menggunakan Python:

    ```bash
    python main.py
    ```

4.  **Interaksi:**
    - Program akan meminta Anda untuk "Masukkan suhu baru (°C):".
    - Masukkan nilai suhu (misalnya, `25.5`, `27`, `22.1`).
    - Setelah Anda menekan Enter, Anda akan melihat `CurrentConditionsDisplay` dan `StatisticsDisplay` secara otomatis memperbarui output mereka.
    - Untuk mengakhiri program, ketik `keluar` dan tekan Enter.

Ini adalah demonstrasi langsung bagaimana Observer Pattern bekerja: perubahan pada satu objek (sensor suhu) secara otomatis memicu pembaruan pada banyak objek lain (tampilan), tanpa Subject perlu mengetahui detail implementasi setiap Observer.
