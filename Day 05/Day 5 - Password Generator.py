import random
print("Welcome to Password Generator.")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

let_length = int(input('How many letters would you like in your password?\n'))
sym_length = int(input('How many symbols would you like in your password?\n'))
num_length = int(input('How many numbers would you like in your password?\n'))

pass_list = []
for i in range(let_length):
    pass_list.append(random.choice(letters))
for i in range(sym_length):
    pass_list.append(random.choice(symbols))
for i in range(num_length):
    pass_list.append(random.choice(numbers))

print(pass_list)
random.shuffle(pass_list)
print(pass_list)

pass_string = ''.join(pass_list)
# We can also convert list to string using other methods

print(f'Here is your Final Password:\n{pass_string}')