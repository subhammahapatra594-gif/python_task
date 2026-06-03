# sensor.py

def read_sensor():

    sensor_input = input("Enter 6 sensor values: (e.g., 001100)")

    # Convert string into list of integers
    sensors = list(map(int, sensor_input))

    # Count active sensors
    active_sensors = len(list(filter(lambda x: x == 1, sensors)))

    return sensors, active_sensors