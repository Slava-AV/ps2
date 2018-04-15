import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in range(len(secret_word)+1):
        if secret_word[i] in letters_guessed:
            return True
        else:
            return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    i = 0
    outputStr = ""
    while i < len(secret_word):
        if secret_word[i] in letters_guessed:
            outputStr = outputStr + secret_word[i]
            i=i+1
        else:
            outputStr = outputStr + " _"
            i=i+1
    return outputStr


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    allLetters = string.ascii_lowercase
    outputStr = ""
    for i in range(len(allLetters)):
        if allLetters[i] not in letters_guessed:
            outputStr = outputStr + allLetters[i]
    return outputStr
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guessesLeft = 6
    print("I am thinking of a word that is " + str(len(secret_word)) + " long")
    letters_guessed = ""
    while guessesLeft > 0:
        print("_____________")
        print("You have " + str(guessesLeft) + " left")
        print("Available letters:" + get_available_letters(letters_guessed))
        newLetter = input("Guess a letter:")
        letters_guessed = letters_guessed + newLetter
        if newLetter in secret_word:
            if get_guessed_word(secret_word,letters_guessed) == secret_word:
                print("Congratulations, you won! My word was: " + secret_word)
                break
            else:
                letters_guessed = letters_guessed + newLetter
                print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
        guessesLeft = guessesLeft - 1

    if get_guessed_word(secret_word,letters_guessed) != secret_word:
        print("Sorry, you ran out of guesses. The word was: " + secret_word)




def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


if __name__ == "__main__":
    # secret_word = choose_word(wordlist)
    print("Welcome to the game Hangman!")
    secret_word = "apple"
    hangman(secret_word)
    # letters_guessed = ['y','j','l', 'i', 'k', 'p', 'r', 's']
    # print(secret_word)
    # print(is_word_guessed(secret_word, letters_guessed))
    # print(get_guessed_word(secret_word,letters_guessed))
    # print(get_available_letters(letters_guessed))
    #hangman_with_hints(secret_word)
