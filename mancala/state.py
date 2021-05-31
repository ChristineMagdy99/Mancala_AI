from copy import deepcopy

START_STATE = ([4]*6 + [0])*2


class PocketName:
    num_pockets = 14

    p0_mancala = 6
    p1_mancala = 13

    p0_pockets = list(range(6))
    p1_pockets = list(range(12,6,-1))


class GameState:
    def __init__(self, init_state=START_STATE, player_turn=0, stealing=True):
        self.state = init_state
        self.player_turn = player_turn
        self.stealing = stealing
        self.winner = None

    def show(self):
        print()
        print("Player {}'s turn:".format(self.player_turn))
        print("      5   4   3   2   1   0")
        print("[{:2}]({:2})({:2})({:2})({:2})({:2})({:2})[  ]".format(*self.state[-1:6:-1]))
        print("[  ]({:2})({:2})({:2})({:2})({:2})({:2})[{:2}]".format(*self.state[:7]))
        print("      0   1   2   3   4   5")

    def show_winning_message(self):
        print(f"Player {self.winner} Won!")

    def is_terminal(self):
        if self.winner is not None:
            return True
        return False

    def children(self):
        for move in self.possible_moves():
            new_state = self.make_move(move)
            yield move, new_state

    def possible_moves(self):
        if self.player_turn == 0:
            for i in PocketName.p0_pockets:
                if self.state[i] != 0:
                    yield i
        else:
            for i in PocketName.p1_pockets:
                if self.state[i] != 0:
                    yield i
            

if __name__ == "__main__":
    game_state = GameState()
    game_state.show()