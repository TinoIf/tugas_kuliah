import random

class CircularStack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.front = -1
        self.rear = -1
        self.locked = False

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def push(self, item):
        if self.is_full():
            print("Stack penuh! Tidak bisa menambahkan.")
            return

        if not self.locked:
            index = random.randint(0, self.size - 1)
            self.front = self.rear = index
            self.stack[index] = item
            self.locked = True
            print(f"Data {item} berhasil ditambahkan di index acak {index}.")
        else:
            self.rear = (self.rear + 1) % self.size
            if self.stack[self.rear] is not None:
                print("Stack penuh di bagian tersebut! Tidak bisa menambahkan.")
                self.rear = (self.rear - 1 + self.size) % self.size 
                return
            self.stack[self.rear] = item
            print(f"Data {item} berhasil ditambahkan di index {self.rear}.")

    def pop(self):
        if self.is_empty():
            print("Stack kosong! Tidak bisa menghapus.")
            return
        item = self.stack[self.front]
        self.stack[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
            self.locked = False
        else:
            self.front = (self.front + 1) % self.size
        print(f"Data {item} berhasil dihapus dari stack.")

    def peek(self):
        if self.is_empty():
            print("Stack kosong!")
        else:
            print(f"Data paling depan adalah: {self.stack[self.front]}")

    def display(self):
        print("Isi seluruh array stack:")
        for i in range(self.size):
            tanda = ""
            if i == self.front:
                tanda += " <- front"
            if i == self.rear:
                tanda += " <- rear"
            print(f"[{i}] {self.stack[i]}{tanda}")

def main():
    ukuran = int(input("Masukkan ukuran stack: "))
    cs = CircularStack(ukuran)

    while True:
        print("\n====== MENU CIRCULAR STACK ======")
        print("1. Tambah data")
        print("2. Hapus data (pop)")
        print("3. Lihat data teratas (peek)")
        print("4. Tampilkan semua isi stack")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            data = input("Masukkan data yang ingin ditambahkan: ")
            cs.push(data)

        elif pilihan == '2':
            cs.pop()

        elif pilihan == '3':
            cs.peek()

        elif pilihan == '4':
            cs.display()

        elif pilihan == '5':
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
