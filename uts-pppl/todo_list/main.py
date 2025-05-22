from todo_list import TodoList 
from manage_perintah import ManagePerintah
from perintah.perintah_tambah_tugas import PerintahTambahTugas
from perintah.perintah_hapus_tugas import PerintahHapusTugas
from perintah.perintah_tandai_selesai import PerintahTandaiSelesai

def main():
    todo = TodoList()
    manager = ManagePerintah()

    while True:

        print("\n===== TODO LIST =====")
        todo.tampilkan_tugas()
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Tandai Selesai")
        print("4. Undo")
        print("5. Redo")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tugas = input("Masukkan Tugas Baru : ")
            perintah_tambah = PerintahTambahTugas(todo, tugas)
            manager.eksekusi(perintah_tambah)
        elif pilihan == "2":
            if not todo.tugas:
                print("Belum ada tugas yang bisa dihapus.")
                continue
            index = int(input("Masukkan Nomor Tugas yang ingin dihapus : ")) -1
            perintah_hapus = PerintahHapusTugas(todo, index)
            manager.eksekusi(perintah_hapus)
        elif pilihan == "3":
            if not todo.tugas:
                print("Belum ada tugas yang bisa ditandai selesai.")
                continue
            index = int(input("Masukkan Nomor Tugas yang sudah selesai: ")) -1
            perintah_tandai_selesai = PerintahTandaiSelesai(todo, index)
            manager.eksekusi(perintah_tandai_selesai)
        elif pilihan == "4":
            manager.kembalikan()
        elif pilihan == "5":
            manager.redo()
        elif pilihan == "6":
            print("Terimakasih telah menggunakan Program ini :)")
            break
        else:
            print("Pilihan tidak Valid, masukkan angka 1-6")

if __name__ == "__main__" :
    main()
