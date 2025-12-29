from datetime import datetime

class Receipt:
    def __init__(self,name,  price_per_liter, liter):
        self.__name = name
        self.__price_per_liter = price_per_liter
        self.__liter = liter
        now = datetime.now()
        self.__date = f"{now.day}/{now.month}/{now.year}/{now.hour}/{now.minute}"


    def __str__(self):
        output = f"""
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          fuel:              {self.__name}
          Price per liter:   {self.__price_per_liter}
          Liter Bought:      {self.__liter}
          Price:             {self.__price_per_liter * self.__liter:.2f}
          Date:              {self.__date}
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          """
        return output