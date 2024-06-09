def caesar_cipher(text, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""

    for char in text:
        if char.isalpha():
            upper_case = char.isupper()
            index = (alphabet.index(char.upper()) + shift) % 26
            new_char = alphabet[index]
            output += new_char if upper_case else new_char.lower()
        else:
            output += char

    return output

def encrypt_text(input_text, shift_value):
    encrypted_text = caesar_cipher(input_text, shift_value)
    return encrypted_text
input_text = input("Enter the Text:")
shift_value = int(input("Enter the shift value:"))
encrypted_text = encrypt_text(input_text, shift_value)
print(encrypted_text)
