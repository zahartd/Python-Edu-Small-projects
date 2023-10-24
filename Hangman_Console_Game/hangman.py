import random


class Hangman:

    def __init__(self, title: str = "H A N G M A N",
                 announcement: str = "The game will be available soon.",
                 guessed_words=None,
                 user_life: int = 8):
        if guessed_words is None:
            guessed_words = ["python", "java", "kotlin", "javascript"]
        self.title: str = title
        self.announcement: str = announcement
        self.guessed_words = guessed_words
        self.guessed_word: str = ""
        self.hint_word = []
        self.user_lives: int = user_life
        self.user_status: str = "hanged"
        self.used_letter = []

    def print_title(self):
        print(self.title)
        print()

    def print_announce(self):
        print(self.announcement)
        print()

    def print_hint(self):
        print("".join(self.hint_word))

    def print_end_game(self):
        if self.user_status == "win":
            print("You guessed the word!")
            print("You survived!")
        else:
            print("You are hanged!")
        print("Thanks for playing!")
        print("We'll see how well you did in the next stage")

    def make_guessed_word(self):
        self.guessed_word = random.choice(self.guessed_words)  # Random choice guessed word

    def generate_hint(self):
        self.hint_word = ["-" for _ in range(len(self.guessed_word))]  # Generate new hint word

    def update_hint(self, guess_letter: str):
        for i in range(len(self.guessed_word)):
            if self.guessed_word[i] is guess_letter:
                self.hint_word[i] = guess_letter

    def check_letter(self, guess_letter: str):
        global curr_life
        if guess_letter in self.used_letter:
            print("You already typed this letter")
        elif len(guess_letter) > 1:
            print("You should input a single letter")
        elif not guess_letter.isascii() or not guess_letter.islower():
            print("It is not an ASCII lowercase letter")
        elif guess_letter in self.guessed_word:
            self.update_hint(guess_letter)
        else:
            print("No such letter in the word")
            curr_life += 1

        self.used_letter.append(guess_letter)

    def check_word(self, word):
        return "".join(word) == self.guessed_word

    def start(self):
        self.print_title()
        self.make_guessed_word()
        self.generate_hint()


hangman = Hangman()
hangman.start()

curr_life: int = 1

while True:
    print()
    request = input('Type "play" to play the game, "exit" to quit: > ')
    print()
    if request == "exit":
        print("Goodbye!")
        break
    elif request == "play":
        while curr_life <= hangman.user_lives:
            hangman.print_hint()
            letter: str = input("Input a letter: > ")
            hangman.check_letter(letter)
            print()  # Prettify print
            if hangman.check_word(hangman.hint_word):
                hangman.user_status = "win"
                hangman.print_end_game()
                break

        else:
            hangman.print_end_game()
    else:
        print("Please input correct request!")
        print()
