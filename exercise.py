###CAESAR CIPHER
def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'        

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not encrypt:
        shift = -shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift, True)

def decrypt(text, shift):
    return caesar(text, shift, False)

# --- Interactive Section ---
print("--- Caesar Cipher Tool ---")
mode = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
message = input("Enter your message: ")

try:
    s = int(input("Enter shift number (1-25): "))
    
    if mode == 'e':
        print(f"Encrypted result: {encrypt(message, s)}")
    elif mode == 'd':
        print(f"Decrypted result: {decrypt(message, s)}")
    else:
        print("Invalid mode selected.")
        
except ValueError:
    print("Error: Shift must be a number.")
