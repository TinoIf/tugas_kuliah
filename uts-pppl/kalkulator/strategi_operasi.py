from abc import ABC, abstractmethod

class StartegiOperasi(ABC):
    @abstractmethod
    def eksekusi(self, a: int, b:int) -> float:
        pass

