matrix = [
    [2, 9, 5],
    [7, 4, 1],
    [6, 0, 3]
]
print(matrix)

print(matrix[1])

print(matrix[1][1])
print(matrix[1][2])

matrix[1][2] = 10
print (matrix)

print('*' *40)

for row in matrix:
    for item in row:
        print(item)