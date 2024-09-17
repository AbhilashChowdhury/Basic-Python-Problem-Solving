class Keyboard:
  def definition(self):
    print("Keyboard is an input device")
    
  def number_of_keys(self):
    print('There are 101 keys')

  def price_of_keyboard(self):
    print('Price of the Keyboard : 2000')


my_keyboard = Keyboard()
my_keyboard.definition()
my_keyboard.number_of_keys()
my_keyboard.brand = "Corsair"
print(my_keyboard.brand)
my_keyboard.price_of_keyboard()

print('*' *40)

new_keyboard = Keyboard()
new_keyboard.definition()

new_keyboard.brand = "HP"
print(new_keyboard.brand)
new_keyboard.price_of_keyboard = "1000"
print(new_keyboard.price_of_keyboard)
new_keyboard.warrenty = "1 Year"
print(new_keyboard.warrenty)