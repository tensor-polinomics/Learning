""" Restaurant and IceCreamStand classes"""

class Restaurant:
	"""A simple restaurant class"""
	
	def __init__(self, name, cuisine):
		"""Initialize name and cuisine attributes"""
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0
	
	def describe_restaurant(self):
		"""Method to describe the type of restaurant"""
		print(f"Restaurant {self.name} serves {self.cuisine} foods.")
	
	def open_restaurant(self):
		"""Simulate the opening of a restaurant"""
		print(f"{self.cuisine} Restaurant {self.name} is now open!")
		
	def describe_customers(self):
		"""Describe the number of customers served"""
		print(f"# of customers served: {self.number_served}")
		
	def set_number_served(self, num):
		"""Set the number of customers served"""
		self.number_served = num
		
	def increment_number_served(self, new):
		"""Increment the number of customers served"""
		self.number_served += new
		
class IceCreamStand(Restaurant):
	"""A subclass of Restaurant class"""
	
	def __init__(self, name, cuisine, flavors):
		"""Initialize the subclass"""
		super().__init__(name, cuisine)
		self.flavors = flavors
		
	def display_flavors(self):
		"""Display available flavors"""
		print(f"Available Flavors: {', '.join(self.flavors)}")