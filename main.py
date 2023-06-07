import random


HANGMAN = (
    """
        -----------
        |        
        |
        |
        |
        |
        |
        |
    ----------------
    """,
    """
    -----------
    |        |   
    |        0 |
    |
    |
    |
    |
    |
    |
    ----------------
    """,
    """
     -----------
     |        |   
     |        0 | -+-
     |
     |
     |
     |
     |
     |
     ----------------
     """,
    """
     -----------
     |        |   
     |        0 | -+-
     |
     |
     |
     |
     |
     |
     ----------------
     """,
    """
     -----------
     |        |   
     |        0 | /-+-
     |
     |
     |
     |
     |
     |
     ----------------
     """,
    """
     -----------
     |        |   
     |        0 | /-+-/
     |
     |
     |
     |
     |
     |
     ----------------
     """,
    """
     -----------
     |        |   
     |        0 | /-+-/
     |        |  
     |
     |
     |
     |
     |
     ----------------
     """,
    """
     -----------
     |        |   
     |        0 | /-+-/
     |        |  
     |        |
     |       |
     |       |
     |
     |
     ----------------
     """,
    """
     -----------
     |        |   
     |        0 | /-+-/
     |        |  
     |        |
     |       | |
     |       | |
     |
     |
     ----------------
     """
)

# The number of errors allowed to the player
MAX_WRONG = len(HANGMAN) - 1

# words in game
WORDS = ["VODKA", "ABYSS", "GUAM", "TAFFETA", "PYTHON", "WAVY", "PEEKABOO", "BLIZZARD", "NYMPH"]
word = random.choice(WORDS)
so_far = '-' * len(word)
wrong = 0
used = []

print('Welcome to the gallows game!')

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print('\n', f"You try this letters: {used}"'\n')
    print('\n' f"Word looks like this: {so_far}"'\n')
    guess = input('\n'"Write letters: "'\n')
    guess = guess.upper()
    # if letters already used
    while guess in used:
        print('\n''You already suggested this letter''\n')
        guess = input('\n'"Write letters: "'\n')
        guess = guess.upper()
    used.append(guess)

    # If user is right
    if guess in word:
        print('\n''Yes! This letter is right!''\n')
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    # letters not in word
    else:
        print('\n'f"Uhhh... letter {guess} isn't in the word."'\n')
        wrong += 1
# finish
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print('\n'"you were hanged"'\n')
else:
    print('\n''You right!''\n')
print('\n'f"It's was {word}"'\n')
input('\n''Press Enter for exit''\n')
