import random

# List of words to choose from
word_list = ["python", "hangman", "challenge", "programming", "computer"]

# Function to display the hangman stages
def display_hangman(tries):
    stages = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   /
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |
           -
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |
           -
        ''',
        '''
           ------
           |    |
           |    O
           |
           |
           -
        ''',
        '''
           ------
           |    |
           |
           |
           |
           -
        '''
    ]
    return stages[tries]

# Main function to run the Hangman game
def hangman():
    word = random.choice(word_list).upper()  # Randomly select a word and convert to uppercase
    word_display = "_" * len(word)  # Displayed as underscores initially
    guessed = False
    guessed_letters = []  # Track guessed letters
    guessed_words = []    # Track guessed words (if the user guesses entire word)
    tries = 6             # Max number of tries
    
    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("Word to guess: " + " ".join(word_display))
    print("\n")
    
    # Main game loop
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        
        if len(guess) == 1 and guess.isalpha():  # Single letter guess
            if guess in guessed_letters:
                print(f"You already guessed the letter '{guess}'.")
            elif guess not in word:
                print(f"'{guess}' is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! '{guess}' is in the word!")
                guessed_letters.append(guess)
                # Reveal the guessed letter in the word display
                word_display = "".join([letter if letter == guess or letter in guessed_letters else "_" for letter in word])
                
        elif len(guess) == len(word) and guess.isalpha():  # Whole word guess
            if guess in guessed_words:
                print("You already guessed the word '{guess}'.")
            elif guess != word:
                print(f"'{guess}' is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_display = word
        
        else:
            print("Invalid input. Please enter a single letter or the whole word.")
        
        # Print current hangman state and guessed word
        print(display_hangman(tries))
        print("Word to guess: " + " ".join(word_display))
        print("\n")
        
        # Check if the player has guessed all letters
        if "_" not in word_display:
            guessed = True
    
    # End game message
    if guessed:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Sorry, you've run out of tries. The word was:", word)

# Run the game
# Uncomment the following line to play the game in your local Python environment
# hangman()
