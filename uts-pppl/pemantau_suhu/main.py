from src.subject.temperatur_sensor import TemperatureSensor
from src.observers.current_condition_display import CurrentConditionsDisplay
from src.observers.statistic_display import StatisticsDisplay

def main():
    print("--- Memulai Sistem Pemantau Suhu Sederhana ---")

    temperature_sensor = TemperatureSensor()
    current_display = CurrentConditionsDisplay(temperature_sensor)
    statistics_display = StatisticsDisplay(temperature_sensor)

    print("\nMasukkan suhu baru atau ketik 'keluar' untuk mengakhiri program.")
    while True:
        try:
            user_input = input("\nMasukkan suhu baru (°C): ")
            
            if user_input.lower() == 'keluar':
                print("Terima kasih telah menggunakan Sistem Pemantau Suhu :)")
                break
            
            new_temperature = float(user_input)
            temperature_sensor.set_temperature(new_temperature)
            
        except ValueError:
            print("Input tidak valid. Harap masukkan angka untuk suhu atau 'keluar'.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()