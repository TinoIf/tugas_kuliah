from perintah.perintah import Perintah

class PerintahTambahTugas(Perintah):
    def __init__(self, todo_list, tugas):
        self.todo_list = todo_list
        self.tugas = tugas

    def eksekusi(self):
        self.todo_list.tambahkan_tugas(self.tugas)

    def kembalikan(self):
        self.todo_list.hapus_tugas(len(self.todo_list.tugas)-1)


        