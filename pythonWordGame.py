import random

stages = [
    r"""
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]


end_of_game = False
lives = 6
word_list = [
    "algorithm",
    "arrays",
    "dictionary",
    "programming",
    "coding",
    "python",
    "strings",
]


def generate_random_word():
    return random.choice(word_list)


chosen_word = generate_random_word()


def create_display():
    word_length = len(chosen_word)
    display = []
    for _ in range(word_length):
        display += "_"
    return display


def random_word_arrray():
    word_length = len(chosen_word)
    letters = []
    for i in range(word_length):
        letters += chosen_word[i]
    return letters


answer = input("Would you like to play? Type Y/y for yes, N/n for no ")
letter_array = random_word_arrray()
display_underscores = create_display()

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess not in display_underscores:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display_underscores[position] = letter
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose. :(")

        print(f"{' '.join(display_underscores)}")

        if "_" not in display_underscores:
            end_of_game == True
            print("You win.")

        print(stages[lives])
