number_list = [2, 5, 2, 10, 1, 14]
print(number_list)

number_list.append(20)
print(number_list)

number_list.insert(1, 7)
print(number_list)

number_list.remove(1)
print(number_list)

number_list.sort()
print(number_list)

number_list.reverse()
print(number_list)

print(1 in number_list)
print(9 in number_list)

print(number_list.count(2))

print(number_list.index(14))

number_list.pop()
print(number_list)

number_list_2 = number_list.copy()
number_list_2.clear()
print(number_list_2)