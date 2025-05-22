from perintah.perintah import Perintah

class PerintahTandaiSelesai(Perintah):
    def __init__(self, todo_list, index):
        self.todo_list = todo_list
        self.index = index
        self.status_sebelumnya = False

    def eksekusi(self):
        if 0 <= self.index < len(self.todo_list.tugas):
            self.status_sebelumnya = self.todo_list.tugas[self.index]["done"]
            self.todo_list.tandai_selesai(self.index)

    def kembalikan(self):
        self.todo_list.tugas[self.index]["done"] = self.status_sebelumnya