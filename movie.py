from pricecode import PriceCode
class Movie:
	"""
	A movie available for rent.
	"""
	# The types of movies (price_code). 
	REGULAR = 0
	NEW_RELEASE = 1
	CHILDRENS = 2
	
	def __init__(self, price_code, title, year, genre ):
		# Initialize a new movie. 
		self.title = title
		self.price_code = PriceCode.normal
		self.set_price_code(price_code)
		self.year = year
		self.genre = genre
		# self.price_code_name = self.set_price_code_name(self.price_code)
		

	def get_price_code(self):
		# get the price code
		return self.price_code.value["code"]

	# def set_price_code_name(self, price_code):
	# 	# get the price code name
	# 	if price_code == PriceCode.normal:
	# 		self.price_code_name = "Regular"
	# 	elif price_code == PriceCode.new_release:
	# 		self.price_code_name = "New Release"
	# 	elif price_code == PriceCode.childrens:
	# 		self.price_code_name = "Childrens"

	# def get_price_code_name(self):
	# 	return self.price_code_name
		
	
	def get_title(self):
		"""get the title"""
		return self.title

	def get_year(self):
		return self.year

	def get_genre(self):
		return self.genre

	def set_price_code(self, code):
		"""set price code for each type of movie"""
		if code == Movie.REGULAR:
			self.price_code = PriceCode.normal
		elif code == Movie.CHILDRENS:
			self.price_code = PriceCode.childrens
		elif code == Movie.NEW_RELEASE:
			self.price_code = PriceCode.new_release
			
	def get_price(self, day_rent):
		"""get the price"""
		return self.price_code.price(day_rent)

	def get_frequent_point(self, day_rent):
		""" get the frequent point"""
		return self.price_code.frequent(day_rent)
		
	def __str__(self):
		return self.title
