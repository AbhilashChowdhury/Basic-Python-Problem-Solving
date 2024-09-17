def greetings(first_name, last_name):
    print(f"Good morning {first_name} {last_name}")

greetings("Chowdhury", "Abhilash")
greetings(last_name="Chowdhury", first_name="Abhilash")

print('*' *40)

def total_cost_of_the_prodect(price, shipping, discount):
    print(f"total_cost_of_the_prodect: {price + shipping - discount} Taka")

total_cost_of_the_prodect( 1100, 50,100 )
total_cost_of_the_prodect( price=1100, shipping=50, discount=100 )
total_cost_of_the_prodect( shipping=50, price=1000,  discount=70 )
total_cost_of_the_prodect( discount=100, shipping=120, price=10000 )