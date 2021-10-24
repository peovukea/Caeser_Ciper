from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            end_text += alphabet[position + shift_amount]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")


print(logo)

while True:
    # User specified variables
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    while shift > 26:
        shift = 26 % shift

    caesar(direction, text, shift)

    continues = input("Do you want to continue? Yes or No \n")

    if continues.capitalize() == "No":
        print('Good bye!')
        break
