from typing import List
from src.interface.observer import Observer
from src.subject.temperatur_sensor import TemperatureSensor

class StatisticsDisplay(Observer):
    """
    Observer yang menampilkan suhu rata-rata, minimum, dan maksimum.
    """
    def __init__(self, sensor: TemperatureSensor):
        self._temperatures: List[float] = []
        self._sensor: TemperatureSensor = sensor
        self._sensor.register_observer(self) # Mendaftarkan diri sebagai observer
        print("StatisticsDisplay: Siap menghitung statistik suhu.")

    def update(self, temperature: float):
        """
        Method yang dipanggil saat ada pembaruan suhu.

        Args:
            temperature (float): Suhu terbaru.
        """
        self._temperatures.append(temperature)
        if len(self._temperatures) > 0:
            avg_temp = sum(self._temperatures) / len(self._temperatures)
            min_temp = min(self._temperatures)
            max_temp = max(self._temperatures)
            print(f"StatisticsDisplay: Rata-rata: {avg_temp:.2f}°C, Min: {min_temp}°C, Max: {max_temp}°C")
        else:
            print("StatisticsDisplay: Belum ada data suhu untuk dihitung.")

    def __str__(self):
        return "StatisticsDisplay"