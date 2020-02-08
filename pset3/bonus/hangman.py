# Hangman game
# with pseudographical progress info

import random
import gallows

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return set(secretWord) <= set(lettersGuessed)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return ''.join([c if c in lettersGuessed else '_ ' for c in secretWord])



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    ENGLISH_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([c for c in ENGLISH_LETTERS if c not in lettersGuessed])


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    SEP_LINE = '-------------'
    MAX_GUESSES = 8

    print('Welcome to the game, Hangman!')
    print(
        'I am thinking of a word that is {0} letters long.'.
        format(len(secretWord)))
    print(SEP_LINE)

    guesses = 8
    lettersGuessed = []
    winningGame = False

    while guesses > 0:
        print('You have {} guesses left.'.format(guesses))
        print('Available letters: {}'.
            format(getAvailableLetters(lettersGuessed)))

        letterGuessed = input('Please guess a letter: ')

        if letterGuessed in lettersGuessed:
            print('Oops! You\'ve already guessed that letter: ', end='')
        elif letterGuessed not in secretWord:
            print('Oops! That letter is not in my word: ', end='')
            guesses -= 1
        else:
            print('Good guess: ', end='')

        lettersGuessed.append(letterGuessed)
        print(getGuessedWord(secretWord, lettersGuessed))
        print(gallows.GALLOWS[MAX_GUESSES - guesses])
        print(SEP_LINE)

        if isWordGuessed(secretWord, lettersGuessed):
            winningGame = True
            break

    if winningGame:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was {}.'.
            format(secretWord.upper()))


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

