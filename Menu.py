import Jawaban1
import Jawaban2
import inputValidasi


while True :
    while True :
        print("===========================================================")
        print("1. Program mencetak Pola 1")
        print("2. Program mencetak Pola 2")
        print("===========================================================")
        pilih = int(input("Masukkan pilihan anda (1/2) :"))
        ValidasiAwal = inputValidasi.inputValidasi()
        n = ValidasiAwal.inputNilaiN()
        validasi = ValidasiAwal.validasiInputN()
        if validasi :
            if pilih == 1 :
                jawaban1 = Jawaban1.Jawaban1(n)
                jawaban1.cetakPola()
                break
            elif pilih == 2 :
                jawaban2 = Jawaban2.Jawaban2(n)
                jawaban2.cetakPola()
                break
        else :
            print("Inputan anda salah, Masukkan Bilangan Ganjil ")
    lagi = input("Apakah anda mau menjalankan program lagi (y/n) :")
    lagi = lagi.upper()
        
    if lagi == 'N':
        break

