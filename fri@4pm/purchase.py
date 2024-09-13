"""
create a command-line script that allows user to purchase
    product_name
    product_price
    payment_type
    payment_given

purchase.py <product_name> <product_price> <payment_type> <payment_given>

purchase.py jeans 50 credit 50
"""
import sys, os

class Product:
    def __init__(self, product_name, product_price,
                 payment_type, payment_given):

        # condensed if statement
        # value if <condition> else <default value>

        self.product_name = product_name if isinstance(product_name, str) and len(product_name) >= 3 else "Default Name"
        self.product_price = product_price if isinstance(product_price, float) and product_price > 0 else 0.5
        self.payment_type = payment_type if isinstance(payment_type, str) and payment_type in "cash,credit,debit".split(",") else "cash"
        self.payment_given = payment_given if isinstance(payment_given, float) and payment_given >= self.product_price else 0

    # create a function that returns the change someone is owed
    # cost = 15. payment is 20. owed is 5
    def change_due(self):
        return self.payment_given - self.product_price
    # summarize the Product object
    # output name=name, price=price, etc
    def __str__(self):
        return (f"Product Name: {self.product_name}, Price: {self.product_price}, "
                f"Payment Type: {self.payment_type}, Payment Given: {self.payment_given}")
    # create a method that is named record_purchase
    # create a file named {product_name}.txt. Content = name, price, payment type and given
    def record_purchase(self):
        file_name = os.path.join(
            os.path.dirname(__file__)
            ,
            f"{self.product_name}.txt"
        )

        open(file_name, "w").write(self.__str__())


try:
    if len(sys.argv) != 5:
        print(f"Usage: {os.path.basename(__file__)} <product_name> <product_price> "
              f"<payment_type> <payment_given>")
        exit()

    product_name = sys.argv[1]
    product_price = float(sys.argv[2])
    payment_type = sys.argv[3]
    payment_given = float(sys.argv[4])

    new_purchase = Product(product_name=product_name, product_price=product_price,
                           payment_type=payment_type, payment_given=payment_given
                           )
    print(new_purchase)
    if new_purchase.change_due() > 0:
        print("Here is your change", new_purchase.change_due())
    if new_purchase.payment_given > 0:
        new_purchase.record_purchase()

except ValueError as e:
    print(e, file=sys.stderr)
