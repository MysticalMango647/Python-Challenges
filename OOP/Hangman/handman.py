import random

#escape characters being weird, double slash on right arm and leg
HANGMAN_ART = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\\ ',
    '|       |',
    '|      / \\ '
]

WORDS = ['mango', 'python', 'lentils', 'apple', 'facebook', 'twitter']

class Hangman():
    def __init__(self, word_to_guess):
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list('_' * len(self.word_to_guess))

    def find_indexes(self, letter):
        return [i for i, char in enumerate(self.word_to_guess) if letter == char]

    def is_invalid_letter(self, input_):
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    def print_game_status(self):
        print('\n')
        print('\n'.join(HANGMAN_ART[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))

    def update_progress(self, letter, indexes):
        for index in indexes:
            self.game_progress[index] = letter

    def get_user_input(self):
        user_input = input('\n Please enter a letter: ').lower()
        return user_input

    def play(self):
        while self.failed_attempts < len(HANGMAN_ART):
            self.print_game_status()
            user_input = self.get_user_input()

            #validate user input
            if self.is_invalid_letter(user_input):
                print('Invalid letter. Please try again.')
                continue
            #check if letter is used before
            if user_input in self.game_progress:
                print('Letter has been guessed.')

            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                if self.game_progress.count('_') == 0:
                    print('You won!')
                    print(f'The word is: {self.word_to_guess}')
                    return
            else:
                self.failed_attempts += 1
        print('Womp Womp, somebody lost!')

if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = Hangman(word_to_guess)
    hangman.play()