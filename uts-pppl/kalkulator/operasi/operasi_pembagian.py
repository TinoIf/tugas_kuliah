from strategi_operasi import StartegiOperasi

class OperasiPembagian(StartegiOperasi):
    def eksekusi(self, a: int, b: int) -> float:
        if b == 0:
            return print("Tidak Bisa Membagi sebuah angka dengan 0")
        return a / b 