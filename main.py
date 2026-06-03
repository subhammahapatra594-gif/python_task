from sensor import read_sensor
from movement import decide_movement

sensors, active_sensors = read_sensor()

action = decide_movement(sensors)

print("Sensor Values:", sensors)
print("Active Sensors:", active_sensors)
print("Robot Action:", action)