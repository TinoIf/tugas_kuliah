class inputValidasi:
    def validasiInputN(self) -> bool:
        if (self.n >= 5 and self.n <= 89 and self.n % 2 != 0):
            return True
        else :
            return False
        
    def inputNilaiN(self) -> int:
        self.n = int(input("Masukkan nilai n = "))
        return self.n