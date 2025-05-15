class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.tail = 0

    def enqueue(self, item):
        if self.is_full():
            print("Antrian penuh, tidak bisa menambahkan item.")
            return
        i = self.tail - 1
        while i >= 0 and self.queue[i] > item:
            self.queue[i + 1] = self.queue[i]
            i -= 1
        self.queue[i + 1] = item
        self.tail += 1

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada item untuk dihapus.")
            return None
        removed_item = self.queue[0]
        for i in range(1, self.tail):
            self.queue[i - 1] = self.queue[i]
        self.queue[self.tail - 1] = None
        self.tail -= 1
        return removed_item

    def is_empty(self):
        return self.tail == 0

    def is_full(self):
        return self.tail >= self.capacity

    def cetak(self):
        print("Isi antrian saat ini:", self.queue)


def main():
    q = Queue(capacity=5)

    while True:
        print("\n====== MENU QUEUE ======")
        print("1. Tambah Antrian")
        print("2. Hapus data (dequeue)")
        print("3. Keluar")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            try:
                item = int(input("Masukkan angka untuk ditambahkan (Wajib Angka): "))
                q.enqueue(item)
                q.cetak()
            except ValueError:
                print("Input tidak valid. Masukkan angka.")

        elif pilihan == '2':
            removed_item = q.dequeue()
            if removed_item is not None:
                print(f"{removed_item} berhasil dihapus.")
                q.cetak()

        elif pilihan == '3':
            print("Terima kasih. Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 3.")

if __name__ == "__main__":
    main()
