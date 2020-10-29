
class Movie:
	"""
	A movie available for rent.
	"""
	
	def __init__(self, title, year, genre ):
		# Initialize a new movie. 
		self.__title = title
		self.__year = year
		self.__genre = genre
	
	def get_title(self):
		"""get the title"""
		return self.__title
	
	def get_year(self):
		return self.__year

	def get_genre(self):
		return self.__genre
	
	def is_genre(self, genre):
		if genre in self.__genre:
			return True
		else:	return False

	def __str__(self):
		return self.__title

