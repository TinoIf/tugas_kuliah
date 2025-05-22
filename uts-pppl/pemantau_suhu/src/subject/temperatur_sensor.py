from typing import List
from src.interface.observer import Observer

class TemperatureSensor:
    """
    Subject yang bertanggung jawab untuk mengelola suhu dan memberitahu observer.
    """
    def __init__(self):
        self._temperature: float = 0.0
        self._observers: List[Observer] = []
        print("TemperatureSensor: Inisialisasi sensor suhu.")

    def register_observer(self, observer: Observer):
        """
        Mendaftarkan observer ke daftar observer.

        Args:
            observer (Observer): Objek observer yang ingin didaftarkan.
        """
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"TemperatureSensor: Observer '{observer.__class__.__name__}' ditambahkan.")
        else:
            print(f"TemperatureSensor: Observer '{observer.__class__.__name__}' sudah terdaftar.")

    def remove_observer(self, observer: Observer):
        """
        Menghapus observer dari daftar observer.

        Args:
            observer (Observer): Objek observer yang ingin dihapus.
        """
        try:
            self._observers.remove(observer)
            print(f"TemperatureSensor: Observer '{observer.__class__.__name__}' dihapus.")
        except ValueError:
            print(f"TemperatureSensor: Observer '{observer.__class__.__name__}' tidak ditemukan.")

    def _notify_observers(self):
        """
        Memberitahu semua observer yang terdaftar tentang perubahan suhu.
        """
        print("\n--- TemperatureSensor: Memberitahu semua Observer ---")
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, new_temperature: float):
        """
        Mengatur suhu baru dan memicu notifikasi jika suhu berubah.

        Args:
            new_temperature (float): Suhu baru yang akan diatur.
        """
        if self._temperature != new_temperature:
            print(f"\nTemperatureSensor: Suhu diubah dari {self._temperature}°C menjadi {new_temperature}°C")
            self._temperature = new_temperature
            self._notify_observers()
        else:
            print(f"\nTemperatureSensor: Suhu tetap {self._temperature}°C, tidak ada perubahan yang dilaporkan.")

    def get_temperature(self) -> float:
        """
        Mengembalikan suhu saat ini.

        Returns:
            float: Suhu saat ini.
        """
        return self._temperature