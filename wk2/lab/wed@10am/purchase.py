"""
Code Follow-Along: purchase.py:
    product name
    product price
    payment_type
        cash or credit
    payment_given
        exact if credit
        can be more or less if cash
            not going to do
Output summary of purchase to console or error message

"""
import csv
import sys, os

if len(sys.argv) != 5:
    print("Incorrect! Usage:", end=" ")
    print(os.path.basename(__file__),
          "<product name> <product price> "
          "<payment_type> <payment_given>")
    exit()


class Product:
    def __init__(self, product_name, product_price,
                 payment_type, payment_given):

        self.name = product_name if isinstance(product_name, str) \
                                    and len(product_name) >= 3 else "Default Name"
        # validate price: needs to be a float and value is greater than 0
        # validate payment_type, needs to be either cash, credit, debit
        self.price = product_price if isinstance(product_price, float) and product_price > 0 else 0.1
        self.payment_type = payment_type if isinstance(payment_type, str) \
                                            and payment_type.lower() in "cash credit debit".split(" ") \
                                            else "cash"
        # only accept payment if payment is greater or equal to price
        self.payment_given = payment_given if isinstance(payment_given, int) and payment_given >= self.price else 0

        self.save_sale()

    def save_sale(self):
        """
        Write to a csv file, the product name, price, payment type, payment given AND Change
        :return: None
        """
        headers = "name,price,type,given,change".split(",")
        data = dict.fromkeys(headers)
        data[headers[0]] = self.name
        data[headers[1]] = self.price
        data[headers[2]] = self.payment_type
        data[headers[3]] = self.payment_given
        data[headers[4]] = self.payment_given - self.price

        with open("sales.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=headers, lineterminator='\n')
            writer.writerow(data)

    #summarize the Product object
    def __str__(self):
        return (f"Name = {self.name}, Price = {self.price}, Payment Type = {self.payment_type}, "
                f"Payment Given = {self.payment_given}")

product_name = sys.argv[1]
product_price = float(sys.argv[2])
payment_type = sys.argv[3]
payment_given = int(sys.argv[4])

product = Product(product_name=product_name, product_price=product_price,
                  payment_type=payment_type, payment_given=payment_given)

print(product)
