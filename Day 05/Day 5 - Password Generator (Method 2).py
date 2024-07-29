import random
print('Welcome to PyPassword Generator')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

let_len = int(input('How many letters would you like in your password:\n'))
sym_len = int(input('How many symbols would you like in your password:\n'))
num_len = int(input('How many numbers would you like in your password:\n'))

pass_string = ''
for char in range(1,let_len+1):
    random_char = random.choice(letters)
    pass_string += random_char
for sym in range(1,sym_len+1):
    random_sym = random.choice(symbols)
    pass_string +=random_sym
for num in range(1,num_len+1):
    random_num = random.choice(numbers)
    pass_string +=random_num
print(pass_string)