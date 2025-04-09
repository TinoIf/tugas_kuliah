size = 6
dataset = [None] * size
top1 = -1
top2 = size
status = True

def push1(data):
    global top1, top2, dataset
    if top2 - top1 > 1:
        dataset[top1+1] = data
        top1 += 1
    else:
        print("Stack Sudah Penuh")

def push2(data):
    global top1, top2, dataset
    if top2 - top1 > 1:
        dataset[top2-1] = data
        top2 -= 1
    else:
        print("Stack 2 Sudah Penuh")

def pop1():
    global top1, top2, dataset, data
    if top1 > -1:
        dataset[top1]= None
        top1 += 1
    else:
        print("Stack Sudah Kosong")

def pop2():
    global top1, top2, dataset
    if top2 <= size-1:
        dataset[top2] = None
        top2 -= 1
    else:
        print("Stack Sudah Kosong")

def clearAll():
    global top1, top2, dataset
    dataset = [None] * size
    top1 = -1
    top2 = size
    print(dataset)

def clear1():
    global top1, dataset
    for i in range(top1, -1, -1):
        dataset[i] = None
    top1 -= -1
    print(dataset)

def clear2():
    global top2, dataset
    for i in range(top2, size, 1):
        dataset[i] = None
    top2 = size-1
    print(dataset)

def peek1():
    global top1,top2,dataset
    data = dataset[top1]
    print(data)

def peek2():
    global top1, top2, dataset
    data = dataset[top2]
    print(data)

while(status):
    print("Selamat Datang di Program")
    print("Pilih Menu yang diingikan")
    print("1. Push1 || 2. Push2  || 3. Pop1  || 4. Pop2 || 5. ClearAll || 6. Clear1 || 7. Clear2 || 8. Peek1 || 9. Peek2 || 10. Break")
    pilihan = int(input("Masukkan Angka sesuai menu yang dipilih : "))
    if(pilihan == 1):
        data = input("Masukkan Data yang ingin di Push : ")
        push1(data)
        print(dataset)
    elif(pilihan == 2):
        data = input("Masukkan data yang ingin di Push: ")
        push2(data)
        print(dataset)
    elif(pilihan == 3):
        pop1()
        print(dataset)
    elif(pilihan == 4):
        pop2()
        print(dataset)
    elif(pilihan == 5):
        clearAll()
    elif(pilihan == 6):
        clear1()
    elif(pilihan == 7):
        clear2()
    elif(pilihan == 8):
        peek1()
    elif(pilihan == 9):
        peek2()
    elif(pilihan == 10):
        break






