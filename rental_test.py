import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
	"""Class for testing Rental class"""
	
	def setUp(self):
		self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
		self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", Movie.REGULAR)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(Movie.REGULAR, m.get_price_code())

	def test_rental_price(self):
		"""test case for testing rental price for each movies type"""
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)

		rental = Rental(self.childrens_movie, 1)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.get_price(), 4.5)

		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_price(), 6.5)
	

	def test_rental_points(self):
		"""test case for testing frequent point for each movies type"""
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_frequent_point(), 1)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_frequent_point(), 5)

		rental = Rental(self.childrens_movie, 1)
		self.assertEqual(rental.get_frequent_point(), 1)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.get_frequent_point(), 1)

		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_frequent_point(), 1)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_frequent_point(), 1)
		

if __name__ == "__main__":
	unittest.main()