def main():
    class SimpleChattyBot:
        user_name: str = ""
        user_age: int = 0
        user_num: int = 0
        right_answer: str = "2"

        def __init__(self, bot_name: str, bot_birth_year: int):
            self.bot_name: str = bot_name
            self.bot_birth_year: int = bot_birth_year

        def __repr__(self):
            return f"Simple Chatty Bot, name: {self.bot_name}, {self.bot_birth_year}"

        def __str__(self):
            return f"The simple chatty bot {self.bot_name}, his birth year is {self.bot_birth_year}"

        def hello(self):
            print(f"Hello! My name is {self.bot_name} \n"
                  f"I was create in {self.bot_birth_year}")

        def greeting_user(self, user_name: str):
            SimpleChattyBot.user_name = user_name
            print(f"What a great name you have, {SimpleChattyBot.user_name}!")

        def guess_age(self, r3: int, r5: int, r7: int):
            SimpleChattyBot.user_age = (r3 * 70 + r5 * 21 + r7 * 15) % 105
            print(f"Your age is {SimpleChattyBot.user_age}; that's a good time to start programming!")

        def count_user_num(self, num: int):
            for i in range(num + 1):
                print(i, "!")
            print("Completed, have a nice day!")

        def check_quiz_ans(self, user_ans: str) -> bool:
            if user_ans == SimpleChattyBot.right_answer:
                return True
            return False

        def goodbye(self):
            print("Congratulations, have a nice day!")

    my_chatty_bot = SimpleChattyBot("Aid", 2020)

    my_chatty_bot.hello()

    name: str = input("Please, remind me your name. \n"
                      "> ")
    my_chatty_bot.greeting_user(name)

    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder_3: int = int(input("> "))
    remainder_5: int = int(input("> "))
    remainder_7: int = int(input("> "))
    my_chatty_bot.guess_age(remainder_3, remainder_5, remainder_7)

    print("Now I will prove to you that I can count to any number you want.")
    n: int = int(input("> "))
    my_chatty_bot.count_user_num(n)

    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    result: bool = False
    while not result:
        user_inp: str = input("> ")
        result = my_chatty_bot.check_quiz_ans(user_inp)
        if not result:
            print("Please, try again.")
    else:
        print("Completed, have a nice day!")

    my_chatty_bot.goodbye()


if __name__ == "__main__":
    main()
