print("Welcome to Caesar Cipher Game!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,key):
    cipher_text = ''
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + key)%26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f'Your Encrypted Text is:\n{cipher_text}')

def decrypt(text,key):
    cipher_text = ''
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - key)%26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f'Your Decrypted Text is:\n{cipher_text}')

end_cipher = False

while not end_cipher:
    direction = input("Do you want to encode or decode your msg?\n")
    if direction.lower() == 'encode':
        text_msg = input("Enter your message\n")
        shift = int(input("Enter the shift number\n"))
        encrypt(text_msg, shift)
    elif direction.lower() == 'decode':
        text_msg = input("Enter your message\n")
        shift = int(input("Enter the shift number\n"))
        decrypt(text_msg, shift)
    cont_cipher = input("Do you want to continue with caesar cipher? 'y' or 'n' \n")
    if cont_cipher.lower() == 'n':
        end_cipher = True
        print("Thank you for using Caesar Cipher Game!\nHave a nice day!")
