from perintah.perintah import Perintah

class PerintahHapusTugas(Perintah):
    def __init__(self, todo_list, index):
        self.todo_list = todo_list
        self.index = index
        self.tugas_terhapus = None

    def eksekusi(self):
        self.tugas_terhapus = self.todo_list.hapus_tugas(self.index)

    def kembalikan(self):
        if self.tugas_terhapus:
            self.todo_list.tugas.insert(self.index, self.tugas_terhapus)
        
