from operasi.operasi_pembagian import OperasiPembagian
from operasi.operasi_pengurangan import OperasiPengurangan
from operasi.operasi_perkalian import OperasiPerkalian
from operasi.operasi_penjumlahan import OperasiPenjumlahan
from kalkulator import Kalkulator

def main():
    status = True

    while status :
        kalkulator = Kalkulator()

        operasi = {
            '1': OperasiPenjumlahan(),
            '2': OperasiPengurangan(),
            '3': OperasiPerkalian(),
            '4': OperasiPembagian(),
            '5': None,
        }

        print("=== Kalkulator Sederhana ===")
        print("Pilih Operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        pilihan = input("Masukkan No sesuai Pilihan Operasi yang ingin dilakukan: ")

        if pilihan not in operasi:
            print("Pilihan Anda Tidak Valid, Masukan Nomor yang Sesuai 1-5")
            break
        elif pilihan == "5":
            print("Terimakasih telah menggunakan Program ini :)")
            status = False
            break
        else:
            a = int(input("Masukkan Bilangan Pertama: "))
            b = int(input("Masukkan Bilangan Kedua: "))
            strategy = operasi[pilihan]
            kalkulator.pilih_strategi(strategy)
            result = kalkulator.hitung(a, b)

            print("Hasil : ", result)

if __name__ == '__main__' :
    main()