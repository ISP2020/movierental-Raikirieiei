from movie import Movie
import logging
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
		self.movie = movie
		self.days_rented = days_rented

	def get_movie(self):
		"""get the rented movie"""
		return self.movie

	def get_days_rented(self):
		"""get renteds day"""
		return self.days_rented

	def get_frequent_point(self):
		"""get the frequent point """
		return self.get_movie().get_frequent_point(self.get_days_rented())
	
	def get_price(self):
		"""get the price"""
		return self.get_movie().get_price(self.get_days_rented())