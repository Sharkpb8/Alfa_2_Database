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

#errors for Hall
class HallNameValueError(Exception):
    pass
class HallTypeValueError(Exception):
    pass

#errors for Screening
class ScreeningMovieIDValueError(Exception):
    pass
class ScreeningHallIDValueError(Exception):
    pass
class ScreeningDateValueError(Exception):
    pass

#errors for Rezervation
class RezervationCustomerIDValueError(Exception):
    pass
class RezervationScreeningIDValueError(Exception):
    pass
class RezervationDateValueError(Exception):
    pass
class RezervationTicketAmountValueError(Exception):
    pass
class RezervationTotalPriceValueError(Exception):
    pass