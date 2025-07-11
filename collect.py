from smbus2 import SMBus
from bme280 import BME280
import time
from ltr559 import LTR559
import time
from enviroplus import gas
import time
from pms5003 import PMS5003

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

print("Temperature: ")
print(bme280.get_temperature())
print("Pressure: ")
print(bme280.get_pressure())
print("Humidity: ")
print(bme280.get_humidity())

ltr = LTR559()
print("Light: ")
print(ltr.get_lux())
print("Proximity: ")
print(ltr.get_proximity())

readings = gas.read_all()
print(readings)

pms5003 = PMS5003()
readings = pms5003.read()
print(readings)