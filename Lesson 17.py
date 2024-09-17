grocery_list = ['Milk', 'Rice', 'Tea', 'Sugar']

print(grocery_list[0])
print(grocery_list[-1])
print(grocery_list[2])
print(grocery_list[2:])
print(grocery_list[:2])
print(grocery_list[1:2])

grocery_list[1] = 'Oil'

print(grocery_list)
print('*' *40)

price = [10, 50, 25, 99, 65, 80]
max = price[0]
for value in price:
    if value > max:
        max = value
print(f'Max price is : {max} taka')

