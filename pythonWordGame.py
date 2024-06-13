import random

stages = [r'''
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

quit_game = False
end_of_game = False
lives = 6
word_list = ["algorithm", "arrays", "dictionary", "programming",
                "coding", "python", "strings"]

chosen_word=random.choice(word_list)

word_length = len(chosen_word)

display=[]
for i in range(word_length):
    display += "_"


answer=input("Would you like to play? Type Y/y for yes, N/n for no ")

while not quit_game:
    
    if answer.lower()=="y":

        guess = input("Guess a letter: ").lower()
        if guess not in display:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
            if guess not in chosen_word:
                lives-=1
                
            print(f"{''.join(display)}")
            if "_" not in display:
                end_of_game == True
                print("You win.")
            print (stages[lives])
            if lives == 0:
                print("You lose. :(")
                end_of_game == True
                quit_choice=input("Do you want to play again Y/y or N/n?")
                if quit_choice.lower() == "n":
                    quit_game==True
                elif quit_choice.lower() == "y":
                    quit_game==False
    elif answer.lower()=="n":
        quit_game==True

