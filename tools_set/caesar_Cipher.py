#TODO: 1. Setting all the set of characters
print(r"""
   _______________________
  |                       |
  |   🏛️ CAESAR CIPHER     |
  |   Shift: +13          |
  |   Message: Encrypted  |
  |_______________________|
      Decode the ancient!
""")
#Characters
lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
digits = [str(i) for i in range(10)]
symbols = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~")
all_chars = lowercase_letters + uppercase_letters + digits + symbols

#TODO: 2. Asking for the functioning details 
direction = input("What action you want to perform? encrypt or decrypt? :\t")
text = input("Enter your message for the program:\t ")
shift = int(input("Give the SHIFT NUMBER for the program:\t"))

#TODO: 3. Defining encrypt and decrypt functions
def encrypt(text, shift):
    new_mess = ''
    for i in text:
        ind=all_chars.index(i)
        new_ind = (ind + shift) % len(all_chars)
        new_mess += all_chars[new_ind]
    print(f"Encrypted Message is {new_mess}")

def decrypt(text, shift):
    new_mess =''
    for i in text:
        ind=all_chars.index(i)
        new_ind = (ind - shift) % len(all_chars)
        new_mess += all_chars[new_ind]
    print(f"Decrypted Message is {new_mess}")

#TODO: 4. Calling the functions and using accordingly
if (direction == "encrypt"):
    encrypt(text, shift)
elif (direction == "decrypt"):
    decrypt(text, shift)