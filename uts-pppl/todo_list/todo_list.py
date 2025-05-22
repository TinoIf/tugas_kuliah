class TodoList:
    def __init__(self):
        self.tugas = []

    def tambahkan_tugas(self, tugas):
        self.tugas.append({'tugas': tugas, 'done': False})

    def hapus_tugas(self,index):
        if 0 <= index < len(self.tugas):
            return self.tugas.pop(index)
        return None
    
    def tandai_selesai(self, index):
        if 0 <= index < len(self.tugas):
            self.tugas[index]['done'] = True

    def tampilkan_tugas(self):
        if not self.tugas:
            print("Tidak ada tugas yang dapat ditampilkan")
        else:
            for i, t in enumerate(self.tugas):
                status = "✓" if t['done'] else "X"
                print(f"{i+1}. [{status}] {t['tugas']}")
    
