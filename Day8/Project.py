alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            encrypted_text += alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
        else:
            encrypted_text += letter
    print(f"The encoded text is {encrypted_text}")

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:
            decrypted_text += alphabet[(alphabet.index(letter) - shift) % len(alphabet)]
        else:
            decrypted_text += letter
    print(f"The decoded text is {decrypted_text}")
true_false = True

def caesar(direction, text, shift):
    text1 = ""
    for letter in text:
        if direction == "encode":
            if letter in alphabet:
                text1 += alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
            else:
                text1 += letter
        elif direction == "decode":
            if letter in alphabet:
                text1 += alphabet[(alphabet.index(letter) - shift) % len(alphabet)]
            else:
                text1 += letter
    print(f"The {direction}d text is {text1}")

while true_false:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)
    
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if go_again == "no":
        true_false = False
    else:
        true_false = True

