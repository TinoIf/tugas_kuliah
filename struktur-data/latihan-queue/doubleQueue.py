class doubleQueue:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.doubleQueue = [None] * kapasitas
        self.awal = 0
        self.rearAwal = -1
        self.akhir = kapasitas - 1
        self.rearAkhir = kapasitas

    def is_empty(self):
        return self.awal > self.rearAwal and self.akhir < self.rearAkhir

    def appendAwal(self, item):
        if self.rearAwal + 1 >= self.rearAkhir:
            print("Queue penuh di sisi kiri!")
            return None
        self.rearAwal += 1
        self.doubleQueue[self.rearAwal] = item
        return item

    def appendAkhir(self, item):
        if self.rearAkhir - 1 <= self.rearAwal:
            print("Queue penuh di sisi kanan!")
            return None
        self.rearAkhir -= 1
        self.doubleQueue[self.rearAkhir] = item
        return item

    def hapusAwal(self):
        # if self.doubleQueue[self.awal] == None:
        #     print("Antrian Kosong, tidak ada yang bisa dihapus")
        #     return None
        # else:
        #     item = self.doubleQueue[self.awal]
        #     self.doubleQueue[self.awal]= None
        #     self.awal +=1
        #     return item

        if self.rearAwal < 0:
            print("Antrian Kosong di sisi kiri, tidak ada yang bisa dihapus")
            return None
        item = self.doubleQueue[self.awal]
        # Geser elemen ke kiri
        for i in range(1, self.rearAwal + 1):
            self.doubleQueue[i - 1] = self.doubleQueue[i]
        self.doubleQueue[self.rearAwal] = None
        self.rearAwal -= 1
        return item

    def hapusAkhir(self):
        # if self.doubleQueue[self.akhir] == None:
        #     print("Antrian Kosong, tidak ada yang bisa dihapus")
        #     return None
        # else:
        #     item = self.doubleQueue[self.akhir]
        #     self.doubleQueue[self.akhir]= None
        #     self.akhir -=1
        #     return item

        if self.rearAkhir >= self.kapasitas:
            print("Antrian Kosong di sisi kanan, tidak ada yang bisa dihapus")
            return None
        item = self.doubleQueue[self.akhir]
        # Geser elemen ke kanan
        for i in range(self.kapasitas - 2, self.rearAkhir - 1, -1):
            self.doubleQueue[i + 1] = self.doubleQueue[i]
        self.doubleQueue[self.rearAkhir] = None
        self.rearAkhir += 1
        return item

    def tampilkan(self):
        print("Double Queue:", self.doubleQueue)


def main():
    dq = doubleQueue(6)

    while True:
        print("\n===== MENU DOUBLE QUEUE =====")
        print("1. Enqueue Queue 1 (Dari kiri)")
        print("2. Enqueue Queue 2 (Dari kanan)")
        print("3. Dequeue Queue 1")
        print("4. Dequeue Queue 2")
        print("5. Tampilkan isi array")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            item = input("Masukkan item ke Queue 1: ")
            dq.appendAwal(item)
            dq.tampilkan()

        elif pilihan == '2':
            item = input("Masukkan item ke Queue 2: ")
            dq.appendAkhir(item)
            dq.tampilkan()

        elif pilihan == '3':
            removed = dq.hapusAwal()
            if removed is not None:
                print(f"Item '{removed}' dihapus dari Queue 1.")
            dq.tampilkan()

        elif pilihan == '4':
            removed = dq.hapusAkhir()
            if removed is not None:
                print(f"Item '{removed}' dihapus dari Queue 2.")
            dq.tampilkan()

        elif pilihan == '5':
            dq.tampilkan()

        elif pilihan == '6':
            print("Terima kasih, program selesai.")
            break

        else:
            print("Pilihan tidak valid, silakan pilih antara 1-6.")

if __name__ == "__main__":
    main()
