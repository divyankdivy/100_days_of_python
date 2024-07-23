print("Welcome to Caesar Cipher Game!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(cipher_direction,text,key):
    cipher_text = ''
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if cipher_direction == 'decode':
                new_position = (position - key) % 26
            elif cipher_direction == 'encode':
                new_position = (position + key)%26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f'Your cipher Text is:\n{cipher_text}')


end_cipher = False

while not end_cipher:
    direction = input("Do you want to encode or decode your msg?\n")
    text_msg = input("Enter your message\n")
    shift = int(input("Enter the shift number\n"))
    caesar(direction,text_msg,shift)
    cont_cipher = input("Do you want to continue with caesar cipher? 'y' or 'n' \n")
    if cont_cipher.lower() == 'n':
        end_cipher = True
        print("Thank you for using Caesar Cipher Game!\nHave a nice day!")