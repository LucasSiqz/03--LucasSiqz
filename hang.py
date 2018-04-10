import random
import string

WORDLIST_FILENAME = "teste.txt"

class File():

    def open_file(self, file):
        return open(file, 'r', 0)

    def read_file(self, inFIle):
        return inFile.readline()


class Word():

    def create_word_list(self, line):
        return string.split(line)

    def calc_different_letters(self, secretWord):
        self.differentLetters = 0
        for letter in string.ascii_lowercase:
            if letter in secretWord:
                self.differentLetters += 1

        return self.differentLetters

    def choose_word(self, differentLetters, secretWord, wordList):
        if differentLetters > 8:
            choise = raw_input('Do you want to change the secret word? (Y to yes): ')
            if choise == 'Y' or choise == 'y':
                secretWord = random.choice(wordList)
                differentLetters = self.calc_different_letters(secretWord)
                game = Game()
                game.print_welcome_message(secretWord, differentLetters)
                secretWord = self.choose_word(differentLetters, secretWord, wordList)

        return secretWord


class Game():

    def print_welcome_message(self, secretWord, differentLetters):
            print '-------------'
            print 'Welcome to the game, Hangam!'
            print 'I am thinking of a word that is', len(secretWord), 'letters long with', differentLetters, 'differents letters.'
            print '-------------'

    def is_word_guessed(self, secretWord, lettersGuessed):
        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False

        return True

    def get_guessed_word(self):
         self.guessed = ''

         return self.guessed

    def get_available_letters(self):
        # 'abcdefghijklmnopqrstuvwxyz'
        self.available = string.ascii_lowercase

        return self.available

    def hangman(self, secretWord):
        self.guesses = 8
        self.lettersGuessed = []

        while  self.is_word_guessed(secretWord, self.lettersGuessed) == False and self.guesses >0:
            print 'You have ', self.guesses, 'guesses left.'

            self.available = self.get_available_letters()
            for letter in self.available:
                if letter in self.lettersGuessed:
                    self.vailable = self.available.replace(letter, '')

            print 'Available letters', self.available
            letter = raw_input('Please guess a letter: ')
            if letter in self.lettersGuessed:

                self.guessed = self.get_guessed_word()
                for letter in secretWord:
                    if letter in self.lettersGuessed:
                        self.guessed += letter
                    else:
                        self.guessed += '_ '

                print 'Oops! You have already guessed that letter: ', self.guessed
            elif letter in secretWord:
                self.lettersGuessed.append(letter)

                self.guessed = self.get_guessed_word()
                for letter in secretWord:
                    if letter in self.lettersGuessed:
                        self.guessed += letter
                    else:
                        self.guessed += '_ '

                print 'Good Guess: ', self.guessed
            else:
                self.guesses -=1
                self.lettersGuessed.append(letter)

                self.guessed = self.get_guessed_word()
                for letter in secretWord:
                    if letter in self.lettersGuessed:
                        self.guessed += letter
                    else:
                        self.guessed += '_ '

                print 'Oops! That letter is not in my word: ',  self.guessed
            print '------------'

        else:
            if self.is_word_guessed(secretWord, self.lettersGuessed) == True:
                print 'Congratulations, you won!'
            else:
                print 'Sorry, you ran out of guesses. The word was', secretWord, '.'

file = File()
inFile = file.open_file(WORDLIST_FILENAME)
line = file.read_file(inFile)

word = Word()
wordList = word.create_word_list(line)
secretWord = random.choice(wordList)
differentLetters = word.calc_different_letters(secretWord)

game = Game()
game.print_welcome_message(secretWord, differentLetters)
game.hangman(word.choose_word(differentLetters, secretWord, wordList))
