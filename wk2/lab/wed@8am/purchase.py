"""
Code Follow-Along: purchase.py:
    product name
    product price
    payment_type
        cash or credit
    payment_given
        exact if credit
        can be more or less if cash
Output summary of purchase to console or error message

"""
import sys
import os
if len(sys.argv) != 5:
    print("Incorrect usage!", end=" ")
    print(os.path.basename(__file__) + " <product> <price> <payment_type> <payment_given>")
    exit()

product_name = sys.argv[1]
product_price = sys.argv[2]
payment_type = sys.argv[3]
payment_given = sys.argv[4]


class Product:
    def __init__(self, name, price, payment_type, payment_given):
        self.name = name
        self.price = price
        self.payment_type = payment_type
        self.payment_given = payment_given

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value if len(value) > 3 else "default product name"

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        try:
            number = float(value)
            if number < 0:
                raise ValueError("Price cannot be zero")

            self.__price = number
        except Exception as e:
            print(e, file=sys.stderr)
    """
    Your turn. Create validation for payment_type. only accept debit, credit or cash
    """
    @property
    def payment_type(self):
        return self.__payment_type
    @payment_type.setter
    def payment_type(self, value):
        self.__payment_type = value if value in ["debit", "credit", "cash"] else "cash"

    @property
    def payment_given(self):
        return self.__payment_given

    @payment_given.setter
    def payment_given(self, value):
        self.__payment_given = 0
        try:
            number = float(value)
            if (self.__payment_type == "credit" or self.__payment_type == "debit") and number != self.__price:
                raise ValueError("Payment should be exact")
            elif self.__payment_type == "cash" and number < self.__price:
                raise ValueError("You are short on cash")

            self.__payment_given = number

        except ValueError as e:
            print(e, file=sys.stderr)

    def __str__(self):
        return (f'Name={self.name}, Price={self.price}, '
                f'Payment Type={self.payment_type}, '
                f'Payment Given={self.payment_given}')

product = Product(product_name, product_price, payment_type, payment_given)
print(product)
