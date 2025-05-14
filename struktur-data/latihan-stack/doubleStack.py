class DoubleStack:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.top1 = -1
        self.top2 = size

    def is_empty1(self):
        return self.top1 == -1

    def is_empty2(self):
        return self.top2 == self.size

    def is_full(self):
        return self.top1 + 1 == self.top2

    def push1(self, item):
        if self.is_full():
            print("Double Stack Penuh!")
            return
        self.top1 += 1
        self.array[self.top1] = item
        print(f"Data '{item}' berhasil di-push ke Stack 1.")

    def push2(self, item):
        if self.is_full():
            print("Double Stack Penuh!")
            return
        self.top2 -= 1
        self.array[self.top2] = item
        print(f"Data '{item}' berhasil di-push ke Stack 2.")

    def pop1(self):
        if self.is_empty1():
            print("Stack 1 Kosong!")
            return None
        item = self.array[self.top1]
        self.array[self.top1] = None 
        self.top1 -= 1
        print(f"Data '{item}' berhasil di-pop dari Stack 1.")
        return item

    def pop2(self):
        if self.is_empty2():
            print("Stack 2 Kosong!")
            return None
        item = self.array[self.top2]
        self.array[self.top2] = None  # optional: bersihkan bekas data
        self.top2 += 1
        print(f"Data '{item}' berhasil di-pop dari Stack 2.")
        return item

    def peek1(self):
        if self.is_empty1():
            print("Stack 1 Kosong!")
            return None
        print(f"Top Stack 1: {self.array[self.top1]}")
        return self.array[self.top1]

    def peek2(self):
        if self.is_empty2():
            print("Stack 2 Kosong!")
            return None
        print(f"Top Stack 2: {self.array[self.top2]}")
        return self.array[self.top2]

    def clear1(self):
        while not self.is_empty1():
            self.pop1()
        print("Stack 1 berhasil dikosongkan.")

    def clear2(self):
        while not self.is_empty2():
            self.pop2()
        print("Stack 2 berhasil dikosongkan.")


# Bagian interaksi
while True:
    try:
        size = int(input("Masukkan ukuran Double Stack: "))
        if size <= 0:
            print("Ukuran harus lebih dari 0!")
        else:
            break
    except ValueError:
        print("Input tidak valid! Masukkan angka bulat positif.")

double_stack = DoubleStack(size)
status = True

while status:
    print("\n--- Menu Double Stack ---")
    print("Array:", double_stack.array)
    print("Top Stack 1:", double_stack.top1)
    print("Top Stack 2:", double_stack.top2)
    print("1. Push ke Stack 1")
    print("2. Pop dari Stack 1")
    print("3. Peek Stack 1")
    print("4. Clear Stack 1")
    print("5. Push ke Stack 2")
    print("6. Pop dari Stack 2")
    print("7. Peek Stack 2")
    print("8. Clear Stack 2")
    print("9. Keluar")

    pilihan = input("Pilih operasi (1-9): ")

    if pilihan == '1':
        data = input("Input data untuk Stack 1: ")
        double_stack.push1(data)
    elif pilihan == '2':
        double_stack.pop1()
    elif pilihan == '3':
        double_stack.peek1()
    elif pilihan == '4':
        double_stack.clear1()
    elif pilihan == '5':
        data = input("Input data untuk Stack 2: ")
        double_stack.push2(data)
    elif pilihan == '6':
        double_stack.pop2()
    elif pilihan == '7':
        double_stack.peek2()
    elif pilihan == '8':
        double_stack.clear2()
    elif pilihan == '9':
        status = False
        print("Keluar dari program.")
    else:
        print("Pilihan tidak valid. Silakan masukkan angka antara 1 dan 9.")
