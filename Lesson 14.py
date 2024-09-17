actual_price = 50

guess_count = 1
guess_limit = 5

while guess_count <= guess_limit:
    guess = int(input('Guess the price: '))
    guess_count += 1
    if guess == actual_price:
        print("Congratulation, You've won.")
        break

print('You Failed.')

