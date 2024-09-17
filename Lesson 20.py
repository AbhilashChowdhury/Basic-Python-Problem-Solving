number_list = [ 1, 2, 1, 6, 5, 10, 1, 10]
unique = []

for number in number_list:
    if number not in unique:
        unique.append(number)
        print(unique)