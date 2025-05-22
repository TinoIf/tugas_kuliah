class Kalkulator:
    def __init__(self):
        self.strategi = None

    def pilih_strategi(self, strategi):
        self.strategi = strategi

    def hitung(self, a:int, b:int) -> float:
        return self.strategi.eksekusi(a,b)