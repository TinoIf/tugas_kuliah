size = 3
dataset = []
top = -1
status = True

def push(data):
    global top, dataset, size
    if top == size - 1:
        print('Stack penuh')
    else:
        top += 1
        dataset[top] = data

def pop():
    global top, dataset
    if top == -1:
        print('Stack kosong')
    else:
        del dataset[top]
        top -= 1

def clear():
    global dataset, top
    dataset = []
    top = -1

def peek():
    global top, dataset
    if top == -1:
        print('Stack kosong')
    else:
        return dataset[top]

while status == True:
    print('Dataset: ' + str(dataset))
    pilihan = int(input('Pilih: 1.Push | 2. Pop | 3. Clear | 4. Peek | 5. Keluar : '))
    if pilihan == 1:
        a = input('Input data:')
        push(a)
    elif pilihan == 2:
        pop()
    elif pilihan == 3:
        clear()
    elif pilihan == 4:
        print(peek())
    elif pilihan == 5:
        status = False
    else:
        print("Masukan Angka Range 1 - 5")