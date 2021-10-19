from service import  ds18b20 as ds

class Controller():
	def __init__(self):
		print("Controller Sensor!")

	def read_DS18B20():
		# ds.read_temp()
		return ds.read_temp()