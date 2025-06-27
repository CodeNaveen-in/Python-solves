import random
print(r"""
   +---+
   |   |     ☠️ HANGMAN
   O   |     Guess or swing...
  /|\  |     
  / \  |     
       |
  =========
""")

word_list = ["tree", "rain", "branch", "forest", "ecosystem"]
chosen = random.choice(word_list)
lives = len(chosen)
display = '_' * len(chosen)
print("Hello Users, Welcome to HANGMAN! \n Not limited to 6 words")
print("The goal is to guess the coreect word.\t", display )
# print(chosen) ... testing done

while (lives != 0 and "_" in display):
    choice = input("Enter your selected alphabet:\t").lower()
    new_display = ""
    if (choice in chosen):
        for i in range(len(chosen)):
            if (choice == chosen[i]):
                new_display += choice
            else:
                new_display += display[i]
        display = new_display
    if (choice not in chosen):
        lives -= 1
        print(f"{choice} is not present. Life present {lives}")
    print(display)

if (lives == 0):
    print(f"You Lost the GAME.. Word was {chosen}")
elif ("_" not in display):
    print(f"You Won! You guessed it correctly!!! {chosen.capitalize()}")

# TODO 1- Prepare a list of words that the player might guess.
# TODO 2- Choose one word randomly from that list as the secret word.
# TODO 3- Initialize the game display with underscores representing each letter.
# TODO 4- Set the number of lives the player has (e.g., 6) and a way to track guessed letters.
# TODO 5- Display the initial game state and instructions to the player.
# TODO 6- Start the game loop that continues until the player wins or loses.
# TODO 7- Get the player's guess and check if it's already been guessed.
# TODO 8- Update the display if the guess is correct; if not, reduce a life.
# TODO 9- Repeat steps until the word is guessed or lives run out.
# TODO 10- Display the result: whether the player won or lost, and reveal the word.