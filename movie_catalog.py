from movie import Movie
import csv
from datetime import datetime

class MovieCatalog:

    def __init__(self):
        pass
        

    def get_movie(self,title: str):
        with open('movies.csv', newline='') as moviecatalog:
            reader = csv.reader(moviecatalog, delimiter =',')    
            for line in reader:
                if(line[0].startswith("#") == False):
                    this_year = datetime.now().year
                    if(line[1] == title):
                        temp_title = line[1]
                    if(int(line[2]) == this_year):
                        temp_price_code = Movie.NEW_RELEASE
                    else:
                        temp_price_code = Movie.REGULAR
            return Movie(temp_price_code, temp_title, line[2], line[3] )
        
mc = MovieCatalog()        
m = mc.get_movie("The Arrival")       
print(m.get_title())
print(m.get_price_code())
print(m.get_genre())
print(m.get_year())
