from src.interface.observer import Observer
from src.subject.temperatur_sensor import TemperatureSensor

class CurrentConditionsDisplay(Observer):
    """
    Observer yang menampilkan suhu saat ini.
    """
    def __init__(self, sensor: TemperatureSensor):
        self._current_temperature: float = 0.0
        self._sensor: TemperatureSensor = sensor
        self._sensor.register_observer(self)  # Mendaftarkan diri sebagai observer
        print("CurrentConditionsDisplay: Siap menampilkan suhu saat ini.")

    def update(self, temperature: float):
        """
        Method yang dipanggil saat ada pembaruan suhu.

        Args:
            temperature (float): Suhu terbaru.
        """
        self._current_temperature = temperature
        print(f"CurrentConditionsDisplay: Suhu saat ini: {self._current_temperature}°C")

    def __str__(self):
        return "CurrentConditionsDisplay"