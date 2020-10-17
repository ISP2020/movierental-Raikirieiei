from enum import Enum

class PriceCode(Enum):
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

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days"""
        pricing = self.value["price"]    # the enum member's price formula
        return pricing(days)
    
    def frequent(self, days: int):
        """Return the frequent point for rental."""
        point = self.value["frp"]
        return point(days)