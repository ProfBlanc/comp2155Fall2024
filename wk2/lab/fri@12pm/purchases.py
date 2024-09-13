"""
allow he user to use the command-line to
purchase a product

python||py||python3 purchase.py <product_name> <product_price> <payment_type> <payment_given>


"""
import sys, os

class Product:
    # condensed if statment
    # value if condtion else default value
    # name = name if isinstance(name, str) and len(name) >= 3 else "Ben"
    def __init__(self, name, price, payment_type, payment_given):
        self.name = name if isinstance(name, str) and len(name) >= 3 else "Default Product Name"
        self.price = price if isinstance(price, float) and price > 0 else 1.0
        self.payment_type = payment_type \
            if isinstance(payment_type, str) \
               and payment_type in "debit,credit,cash".split(',') else "cash"
        self.payment_given = payment_given if isinstance(payment_given, float) \
                                                  and payment_given >= self.price else 0.0
    def give_change_back(self):
        return self.payment_given - self.price

    def create_receipt(self):
        # create a file with the name {product name}.txt.
        # write the summary of the product purchase
        file_name = os.path.join(
            os.path.dirname(__file__)
            ,
            f"{self.name}.txt"
        )
        open(file_name, "w").write(self.__str__())

    # summarize the object
    def __str__(self):
        return (f"Name={self.name}, Price={self.price}, "
                f"Payment Type={self.payment_type}, "
                f"Payment Given={self.payment_given}")

try:
    if len(sys.argv) != 5:
        print(f"Usage: {os.path.basename(__file__)} <product_name> "
              f"<product_price> "
              f"<payment_type> <payment_given>")
        exit()

    name = sys.argv[1]
    price = float(sys.argv[2])
    payment_type = sys.argv[3]
    payment_given = float(sys.argv[4])

    product = Product(name, price, payment_type, payment_given)
    print(product)
    print("Change Back=",product.give_change_back())
    product.create_receipt()
except Exception as e:
    print(e, file=sys.stderr)
