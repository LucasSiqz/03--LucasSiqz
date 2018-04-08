import random
import string

WORDLIST_FILENAME = "words.txt"

def loadFile():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)

def printWelcomeMessage(secretWord, differentLetters):
    print '-------------'
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long with', differentLetters, 'differents letters.'
    print '-------------'

def CalcDifferentLetters(secretWord):
    differentLetters = 0
    for letter in string.ascii_lowercase:
        if letter in secretWord:
            differentLetters += 1
    return differentLetters

def ChooseWord(differentLetters, secretWord):
    if differentLetters > 8:
        choise = raw_input('Do you want to change the secret word? (Y to yes, N to no): ')
        if choise == 'Y':
            secretWord = loadFile().lower()
            differentLetters = CalcDifferentLetters(secretWord)
            printWelcomeMessage(secretWord, differentLetters)
            secretWord = ChooseWord(differentLetters, secretWord)
    return secretWord

def isWordGuessed(secretWord, lettersGuessed):

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():

     guessed = ''


     return guessed

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    return available


def hangman(secretWord):
    guesses = 8
    lettersGuessed = []

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print 'You have ', guesses, 'guesses left.'

        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


secretWord = loadFile().lower()
differentLetters = CalcDifferentLetters(secretWord)
printWelcomeMessage(secretWord, differentLetters)
hangman(ChooseWord(differentLetters, secretWord))
