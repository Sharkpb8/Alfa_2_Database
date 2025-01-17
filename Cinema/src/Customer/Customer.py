from src.Inputs_check import *
from src.Error import *

class Customer:
    """
    Represents a customer in the system, with details including personal information, loyalty program status, and registry date.

    Attributes
    ----------
    id : int
        A unique identifier for the customer, defaulting to 0.
    Name : str
        The first name of the customer.
    Last_name : str
        The last name of the customer.
    Loyalty_program : int
        Indicates if the customer is a member of the loyalty program (1 for Yes, 0 for No).
    Loyalty_points : float
        The number of loyalty points the customer has.
    Registry_date : str
        The date the customer was registered in the system.

    Methods
    -------
    __str__()
        Returns a formatted string with the customer's details.
    """

    def __init__(self,Name,Last_name,loyalty_program,loyalty_points,Registry_date,id = 0):
        """
        Initialises a new instance of the `Customer` class with the provided attributes.

        Parameters
        ----------
        Name : str
            The first name of the customer, maximum length of 30 characters.
        Last_name : str
            The last name of the customer, maximum length of 30 characters.
        loyalty_program : int
            Indicates if the customer is a member of the loyalty program (1 for Yes, 0 for No).
        loyalty_points : float
            The number of loyalty points the customer has, must be non-negative.
        Registry_date : str
            The date the customer was registered in the system, formatted as "YYYY-MM-DD".
        id : int, optional
            A unique identifier for the customer, defaulting to 0.

        Raises
        ------
        IDValueError
            If the `id` is not a valid positive integer.
        NameValueError
            If the `Name` exceeds 30 characters or is invalid.
        LastNameValueError
            If the `Last_name` exceeds 30 characters or is invalid.
        LoyaltyProgramValueError
            If the `loyalty_program` is not 0 or 1.
        LoyaltyPointsValueError
            If the `loyalty_points` is negative or exceeds 10 digits.
        RegistryDateValueError
            If the `Registry_date` is not a valid date format with '-' as a delimiter.
        """

        if not NumberCheck(str(id),decimal=False ,negative=False):
            raise IDValueError
        self.id = int(id)

        if not StringCheck(Name, 30):
            raise NameValueError
        self.Name = Name

        if not StringCheck(Last_name, 30):
            raise LastNameValueError
        self.Last_name = Last_name

        if not BoolCheck(int(loyalty_program), 1, 0):
            raise LoyaltyProgramValueError
        self.Loyalty_program = int(loyalty_program)

        if not NumberCheck(str(loyalty_points), 10, negative=False):
            raise LoyaltyPointsValueError
        self.Loyalty_points = float(loyalty_points)

        if not DateCheck(str(Registry_date), specialchar="-"):
            raise RegistryDateValueError
        self.Registry_date = Registry_date
    
    def __str__(self):
        """
        Returns a formatted string with the customer's details.

        Returns
        -------
        str
            A string representation of the customer's details.

        Examples
        --------
        >>> customer = Customer("John", "Doe", 1, 150.5, "2023-01-01")
        >>> print(customer)
        ID: 0, Jméno: John, Příjmení: Doe, Člen věrnostního programu: Ano, Body: 150.5, Registrace: 2023-01-01
        """
        return (f"ID: {self.id}, Jméno: {self.Name}, Příjmení: {self.Last_name}, Člen věrnostního programu: {'Ano' if self.Loyalty_program else 'Ne'}, Body: {self.Loyalty_points}, Registrace: {self.Registry_date}")