good_condition = False
reasonable_price = False
poor_condition = True

if good_condition and reasonable_price and not poor_condition:
    print("We will buy the house")

if good_condition or reasonable_price or not poor_condition:
    print("We are interested")

if not good_condition or not reasonable_price or poor_condition:
     print("We are not interested")