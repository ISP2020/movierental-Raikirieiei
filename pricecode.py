from enum import Enum
from movie import Movie
from datetime import datetime
class PriceCode(Enum):

    # The types of movies (price_code). 
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2

    """An enumeration for different kinds of movies and their behavior"""
    new_release = { "price": lambda days: 3.0*days, 
                    "frp": lambda days: days,
                    "code": 1

                  }
    normal = { "price": lambda days : 2+1.5*(days-2) if (days > 2) else 2,
               "frp": lambda days: 1,
               "code": 0
             }
    childrens = { "price": lambda days: 1.5+1.5*(days-3) if (days > 3) else 1.5,
               "frp": lambda days: 1,
               "code": 2
             }
    
    @classmethod
    def set_price_code(cls, movie: Movie):
        """set price code for each type of movie"""
        now = datetime.now().year
        if int(movie.get_year()) == now:
            return PriceCode.new_release
        elif movie.is_genre("Children"):
            return PriceCode.childrens
        else: return PriceCode.normal

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days"""
        pricing = self.value["price"]    # the enum member's price formula
        return pricing(days)
    
    def frequent(self, days: int):
        """Return the frequent point for rental."""
        point = self.value["frp"]
        return point(days)