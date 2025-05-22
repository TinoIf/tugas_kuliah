from strategi_operasi import StartegiOperasi

class OperasiPengurangan(StartegiOperasi):
    def eksekusi(self, a: int, b: int) -> float:
        return a - b 