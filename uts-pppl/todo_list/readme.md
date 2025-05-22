# ✅ Todo List App dengan Command Pattern

Aplikasi **Todo List** berbasis terminal menggunakan **Command Pattern**. Mendukung fitur `Undo` dan `Redo` dengan implementasi modular dan OOP.

---

## 📌 Fitur

- Tambah tugas
- Hapus tugas
- Tandai tugas sebagai selesai
- Undo & Redo beberapa langkah
- Struktur kode bersih dan terorganisir

---

### 💬 Analisis:

- **Pemicu perintah** berada di `main.py`, yaitu saat pengguna memilih aksi dari menu (input).
- **Pelaksana aksi** dibungkus sebagai objek command (`PerintahTambahTugas`, `PerintahHapusTugas`, `PerintahTandaiSelesai`) yang semuanya **mengimplementasikan interface `Perintah`**.
- **Pemrosesan command** dipisahkan ke `ManagePerintah`, yang bertanggung jawab untuk menyimpan histori dan menangani eksekusi, undo, dan redo.

---

## 🛠️ Langkah-langkah Implementasi

### 1. Buat Interface `Perintah` (Command Interface)

📁 `perintah/command_interface.py`

Ini adalah **kontrak** utama dalam Command Pattern. Setiap aksi yang ingin Anda jadikan "perintah" harus mematuhi kontrak ini.
Berisi metode abstrak:

- `eksekusi()`: Metode ini mendefinisikan apa yang harus dilakukan oleh perintah.
- `undo()`: Metode ini mendefinisikan bagaimana membatalkan efek dari perintah yang telah dieksekusi. Keberadaan metode `undo()` inilah yang memungkinkan fitur _undo_ dan _redo_.

### 2. Buat Kelas `TodoList` (Receiver)

📄 `todo_list.py`

`TodoList` adalah **Receiver** dalam pola Command. Receiver adalah objek yang tahu bagaimana melakukan operasi atau aksi sebenarnya. Dalam kasus ini, `TodoList` adalah objek yang **benar-benar melakukan** penambahan, penghapusan, atau penandaan tugas.
Berfungsi menyimpan dan memanipulasi daftar tugas dengan metode seperti:

- `tambah_tugas()`
- `hapus_tugas()`
- `tandai_selesai()`
- `tampilkan_tugas()`

### 3. Implementasikan Command Classes (Concrete Commands)

📁 `perintah/`

Ini adalah **perintah-perintah konkret** yang membungkus (encapsulate) permintaan tertentu. Setiap kelas command ini adalah representasi dari sebuah aksi spesifik yang bisa dilakukan.

- `perintah_tambah_tugas.py`: Perintah untuk menambah tugas. Ketika `eksekusi()` dipanggil, ia akan memanggil `todo.tambah_tugas()`. Ketika `undo()` dipanggil, ia akan memanggil `todo.hapus_tugas()` pada tugas yang baru ditambahkan.
- `perintah_hapus_tugas.py`: Perintah untuk menghapus tugas. Metode `eksekusi()` akan memanggil `todo.hapus_tugas()`, dan `undo()` akan memanggil `todo.tambah_tugas()` untuk mengembalikan tugas yang terhapus.
- `perintah_tandai_selesai.py`: Perintah untuk menandai tugas selesai. Metode `eksekusi()` akan memanggil `todo.tandai_selesai()`, dan `undo()` akan membatalkan status selesai.

Semua class ini **mengimplementasikan interface `Perintah`**, sehingga mereka memiliki metode `eksekusi()` dan `undo()`. Mereka membawa referensi ke objek `TodoList` (Receiver) yang akan mereka operasikan.

### 4. Buat `ManagePerintah` (Invoker/Command Processor)

📄 `manage_perintah.py`

`ManagePerintah` adalah **Invoker**. Perannya adalah **menerima dan mengelola perintah**, tanpa perlu tahu detail bagaimana perintah itu bekerja. Ia adalah "juru masak" yang tahu bagaimana mengambil "resep" (Command) dan memberikannya kepada "koki" (Receiver) untuk dijalankan. Ini juga menyimpan riwayat perintah untuk fitur `undo` dan `redo`.
Menyediakan fungsi-fungsi:

- **`eksekusi(command)`**: Metode ini menerima objek `command` (yang merupakan turunan dari `Perintah`). Ia kemudian memanggil `command.eksekusi()`. Setelah eksekusi, `command` ini disimpan dalam tumpukan `undo_stack` untuk kemungkinan pembatalan di kemudian hari.
- **`kembalikan()` (undo)**: Mengambil perintah terakhir dari `undo_stack`, memanggil metode `undo()` pada perintah tersebut, dan memindahkannya ke `redo_stack`.
- **`redo()`**: Mengambil perintah terakhir dari `redo_stack`, memanggil metode `eksekusi()` pada perintah tersebut, dan memindahkannya kembali ke `undo_stack`.

### 5. Buat Program Utama (`main.py`)

📄 `main.py`

`main.py` adalah **Client**. Ia adalah antarmuka interaktif yang **membuat** objek `Perintah` (command) berdasarkan pilihan pengguna dan **memberikan** perintah tersebut kepada `ManagePerintah` (Invoker) untuk dieksekusi. `main.py` tidak secara langsung memanggil metode `TodoList` untuk mengubah tugas; ia mendelegasikannya kepada objek `Perintah` dan `ManagePerintah`.
Menangani interaksi CLI dengan user, menampilkan menu, dan mengeksekusi perintah berdasarkan input.

---

### Ilustrasi Alur Kerja (Contoh: Tambah Tugas)

1.  Pengguna memilih "Tambah Tugas" di `main.py` (Client).
2.  `main.py` **membuat** objek `PerintahTambahTugas` dan memberikannya ke `manager` (`ManagePerintah`).
3.  `manager.eksekusi(perintah_tambah_tugas)` dipanggil.
4.  Di dalam `ManagePerintah`, `perintah_tambah_tugas.eksekusi()` dipanggil.
5.  Di dalam `PerintahTambahTugas.eksekusi()`, metode `todo.tambah_tugas()` (pada objek `TodoList` yang merupakan Receiver) **benar-benar menambahkan** tugas ke daftar.
6.  `ManagePerintah` menyimpan `perintah_tambah_tugas` ke `undo_stack`-nya.

Ini adalah inti dari Command Pattern: permintaan (misalnya, "tambah tugas") dibungkus menjadi objek, yang kemudian dapat dioperasikan (dieksekusi, di-undo, di-redo) oleh Invoker, memisahkan peminta dari pelaksana sebenarnya.

---

### 6. Jalankan Program

```bash
python main.py
```
