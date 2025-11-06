nato_dict = {
    'A': 'Alpha',    'B': 'Bravo',     'C': 'Charlie',
    'D': 'Delta',    'E': 'Echo',      'F': 'Foxtrot',
    'G': 'Golf',     'H': 'Hotel',     'I': 'India',
    'J': 'Juliett',  'K': 'Kilo',      'L': 'Lima',
    'M': 'Mike',     'N': 'November',  'O': 'Oscar',
    'P': 'Papa',     'Q': 'Quebec',    'R': 'Romeo',
    'S': 'Sierra',   'T': 'Tango',     'U': 'Uniform',
    'V': 'Victor',   'W': 'Whiskey',   'X': 'X-ray',
    'Y': 'Yankee',   'Z': 'Zulu'
}

def convert_to_nato(text):
    return [
        nato_dict[char] if char in nato_dict else '[space]' if char == ' ' else f"[{char}]"
        for char in text.upper()
    ]

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a word or sentence: ")
    print("NATO Alphabet:")
    print(" ".join(convert_to_nato(user_input)))