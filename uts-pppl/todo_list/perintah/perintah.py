from abc import ABC,abstractmethod

class Perintah(ABC):
    @abstractmethod
    def eksekusi(self):
        pass

    @abstractmethod
    def kembalikan(self):
        pass