"""A set of classes used to represent gas and electric cars."""

class Car:
	"""Define a simple Car class to represent a car"""
	
	def __init__(self, make, model, year):
		"""Initialize attributes"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		"""Return a nicely formatted descriptive name"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	
	def read_odometer(self):
		"""Print the car's mileage"""
		print(f"Current Mileage: {self.odometer_reading} miles")
		
	def update_odometer(self, mileage):
		"""
		Update odometer_reading
		Reject update if it attempts to roll back
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
			
	def increment_odometer(self, miles):
		"""Add new miles to odometer_reading"""
		if miles >= 0:
			self.odometer_reading += miles
		else:
			print("You can't add negative miles!")  
			

class Battery:
	"""Model an EV battery"""
	
	def __init__(self, size=40):
		"""Initialize the battery's attributes"""
		self.battery_size = size
	
	def describe_battery(self):
		"""Describe the size of battery"""
		print(f"Battery Size: {self.battery_size}-kWh")	
	
	# Exercise 9.9 Upgrade the battery size
	def upgrade_battery(self):
		"""Upgrade battery size"""
		if self.battery_size < 65:
			self.battery_size = 65
		
	def get_range(self):
		"""Print the range of the included battery"""
		if self.battery_size == 40:
			range = 150
		elif self.battery_size == 65:
			range = 225
		print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles"""
	
	def __init__(self, make, model, year):
		"""Initialize attributes"""
		super().__init__(make, model, year)
		self.battery = Battery()	