# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    ' ': '/',      ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '!': '-.-.--'
}

# Function to convert text to Morse Code
def text_to_morse(text):
    text = text.upper()
    morse = ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)
    return morse

# Main Program
if __name__ == "__main__":
    user_input = input("Enter text to convert to Morse Code: ")
    morse_output = text_to_morse(user_input)
    print("\n🔔 Morse Code:")
    print(morse_output)