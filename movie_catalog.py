from movie import Movie
from rental import Rental
import csv
from datetime import datetime

class MovieCatalog:
            
    def get_movie(self,title: str):  
        for line in self.load_file('movies.csv'):
            if(line[0].startswith("#") == False):
                if(line[1] == title):
                    temp_title = line[1]
                    return Movie(temp_title, line[2], line[3].split('|') )
                   
    
    def load_file(self,csv_file):
        moviecatalog = open(csv_file, 'r', newline='')
        file_reader = csv.reader(moviecatalog, delimiter =',')  
        return file_reader


