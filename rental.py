
import logging
from pricecode import PriceCode
class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented
	field is used.
	"""
	

	def __init__(self, movie, days_rented): 
		"""Initialize a new movie rental object for
		   a movie with known rental period (daysRented).
		"""
		self.price_code = PriceCode.set_price_code(movie)
		self.__movie = movie
		self.days_rented = days_rented

	def get_days_rented(self):
		"""get renteds day"""
		return self.days_rented

	def get_frequent_point(self, day_rent):
		"""get the frequent point """
		return self.price_code.frequent(day_rent)
	
	def get_price(self, day_rent):
		"""get the price"""
		return self.price_code.price(day_rent)
	
	def get_title(self):
		return self.__movie.get_title()
	
	