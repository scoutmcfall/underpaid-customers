"""melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00"""

#for loop that takes in a string of customer order, separates it by | into a list of 4 elements
#then generates the expected cost
#then the if statement and print statement
melon_cost = 1.00
#def melon_payment_report():
"""Iterate over report and compare expected to actual payments to find under and overpayment"""
the_file = open("customer-orders.txt")
for line in the_file:
    order = line.split("|")
    #print(order)
    #print(order[2])
    customer_name = order[1]
    customer_paid = float(order[3])
    expected_cost = float(order[2]) * melon_cost
    if expected_cost != order[3]:
        print(f"{customer_name} paid ${customer_paid:.2f},",
        f"expected ${expected_cost:.2f}"
        )
    if float(expected_cost) > customer_paid:
        print("Customer underpaid."
        )
    if float(expected_cost) < customer_paid:
        print("Customer overpaid."
        )
the_file.close()
#melon_payment_report("customer-orders.txt")
"""customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print(f"{customer1_name} paid ${customer1_paid:.2f},",
          f"expected ${customer1_expected:.2f}"
          )

customer2_expected = customer2_melons * melon_cost
if customer2_expected != customer2_paid:
    print(f"{customer2_name} paid ${customer2_paid:.2f},",
          f"expected ${customer2_expected:.2f}"
          )

customer3_expected = customer3_melons * melon_cost
if customer3_expected != customer3_paid:
    print(f"{customer3_name} paid ${customer3_paid:.2f},",
          f"expected ${customer3_expected:.2f}"
          )

customer4_expected = customer4_melons * melon_cost
if customer4_expected != customer4_paid:
    print(f"{customer4_name} paid ${customer4_paid:.2f},",
          f"expected ${customer4_expected:.2f}"
          )

customer5_expected = customer5_melons * melon_cost
if customer5_expected != customer5_paid:
    print(f"{customer5_name} paid ${customer5_paid:.2f},",
          f"expected ${customer5_expected:.2f}"
          )

customer6_expected = customer6_melons * melon_cost
if customer6_expected != customer6_paid:
    print(f"{customer6_name} paid ${customer6_paid:.2f},",
          f"expected ${customer6_expected:.2f}"
          )"""
