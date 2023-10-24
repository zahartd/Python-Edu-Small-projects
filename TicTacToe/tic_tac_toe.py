class TicTacToe:
    def __init__(self):
        self.curr_state: list = [["_", "_", "_"] for _ in range(0, 3)]
        self.win_count: int = 0
        self.winner: str = ""
        self.is_possible: bool = True
        self.is_draw: bool = True
        self.game_status: bool = False
        self.curr_symbol: str = "X"
        self.curr_step: int = 0

    def __repr__(self):
        return "Console game +-+-+-+TicTacToe+-+-+-+: \n" \
               f"Current state: {self.curr_state} \n" \
               f"Count of win: {self.win_count} \n" \
               f"Winner: {self.winner} \n" \
               f"Is possible: {self.is_possible} \n" \
               f"Is draw: {self.is_draw} \n" \
               f"Game status is {int(self.game_status)} \n" \
               f"Current symbol is {self.curr_symbol}"

    def __str__(self):
        return f"TicTacToe(curr_state: {self.curr_state}, " \
               f"win_count: {self.win_count}, " \
               f"winner: {self.winner}, " \
               f"is_possible: {self.is_possible}, " \
               f"is_draw: {self.is_draw}, " \
               f"game_status: {self.game_status}, " \
               f"curr_symbol: {self.curr_symbol})"

    def check_horizontal_win(self):
        for i in range(0, 3):
            if "".join(self.curr_state[i]) == "XXX":
                self.winner = "X"
                self.win_count += 1
            elif "".join(self.curr_state[i]) == "OOO":
                self.winner = "O"
                self.win_count += 1

    def check_vertical_win(self):
        for i in range(0, 3):
            if self.curr_state[0][i] + self.curr_state[1][i] + self.curr_state[2][i] == "XXX":
                self.winner = "X"
                self.win_count += 1
            elif self.curr_state[0][i] + self.curr_state[1][i] + self.curr_state[2][i] == "OOO":
                self.winner = "O"
                self.win_count += 1

    def check_dioganally_win(self):
        if self.curr_state[0][0] + self.curr_state[1][1] + self.curr_state[2][2] == "XXX" \
                or self.curr_state[0][2] + self.curr_state[1][1] + self.curr_state[2][0] == "XXX":
            self.winner = "X"
            self.win_count += 1
        elif self.curr_state[0][0] + self.curr_state[1][1] + self.curr_state[2][2] == "OOO" \
                or self.curr_state[0][2] + self.curr_state[1][1] + self.curr_state[2][0] == "OOO":
            self.winner = "O"
            self.win_count += 1

    def check_win(self):
        self.check_horizontal_win()
        self.check_vertical_win()
        self.check_dioganally_win()

    def check_draw(self):
        self.is_draw = self.curr_step == 9 and self.win_count == 0

    @staticmethod
    def print_border():
        print("---------")

    def print_curr_state(self):
        self.print_border()

        curr_row = 1
        curr_symbol = 0
        for j in range(2, -1, -1):
            for i in range(0, 3):
                elem = self.curr_state[i][j]
                curr_symbol += 1
                if curr_symbol % 3 == 0:
                    print(elem + " ", end="")
                    print("|")
                    curr_row += 1
                elif (curr_symbol - 1) % 3 == 0:
                    print("| ", end="")
                if curr_symbol % 3 > 0:
                    print(elem + " ", end="")

        self.print_border()

    def player_move(self):
        correct_inp: bool = False
        self.curr_step += 1
        while not correct_inp:
            coord: list = input("Enter the coordinates: > ").split()
            if len(coord) < 2 or not (coord[0].isdigit() and coord[1].isdigit()):
                print("You should enter numbers!")
            elif int(coord[0]) > 3 or int(coord[1]) > 3:
                print("Coordinates should be from 1 to 3!")
            elif self.curr_state[int(coord[0]) - 1][int(coord[1]) - 1] != "_":
                print("This cell is occupied! Choose another one!")
            else:  # always is correct
                self.curr_state[int(coord[0]) - 1][int(coord[1]) - 1] = self.curr_symbol
                correct_inp = True

    def start(self):
        self.game_status = True
        self.print_curr_state()
        while self.game_status:
            self.player_move()
            self.print_curr_state()
            self.check_win()
            self.check_draw()
            if self.is_draw:
                print("Draw")
                self.game_status = False
            elif self.win_count == 1:
                print(f"{self.winner} wins")
                self.game_status = False

            if self.curr_symbol == "X":
                self.curr_symbol = "O"
            else:
                self.curr_symbol = "X"


def main():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()


if __name__ == "__main__":
    main()
