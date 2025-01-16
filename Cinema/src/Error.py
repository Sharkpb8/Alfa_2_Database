#global errors
class IDValueError(Exception):
    pass

#errors for Customer
class NameValueError(Exception):
    pass
class LastNameValueError(Exception):
    pass
class LoyaltyProgramValueError(Exception):
    pass
class LoyaltyPointsValueError(Exception):
    pass
class RegistryDateValueError(Exception):
    pass
class GenreNameValueError(Exception):
    pass

#errors for Genre
class GenreNameValueError(Exception):
    pass

#errors for Movie
class GenreIDValueError(Exception):
    pass
class MovieNameValueError(Exception):
    pass
class MovieLengthValueError(Exception):
    pass
class MoviePriceValueError(Exception):
    pass
class MoviePremiereDateValueError(Exception):
    pass