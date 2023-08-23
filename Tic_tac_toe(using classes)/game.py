import player
import time

class Tic_Tac_toe:
    def __init__(self):
        self.board=self.make_board()
        self.currentWinner=None
        
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
        
    def print_board(self):
        for i in range(0,9,3):
            print("|",end="")
            for j in range(i,i+3):
                print(f" {self.board[j]}",end=" |")
            print()
    
    @staticmethod
    def print_board_indexes():
        board=[j for i in range(0,9,3) for j in range(i,i+3)]
        for i in range(0,9,3):
            print("|",end="")
            for j in range(i,i+3):
                print(f" {board[j]}",end=" |")
            print()
            
    def make_move(self,square,letter):
        if self.board[square]==" ":
            self.board[square]=letter
            if self.check_winner(self.board,letter):
                self.currentWinner=letter
            return True
        return False
    
    def check_winner(self,gameValues,character):
        if (gameValues[0]==gameValues[1]==gameValues[2]==character) or (gameValues[3]==gameValues[4]==gameValues[5]==character) or (gameValues[6]==gameValues[7]==gameValues[8]==character) or (gameValues[0]==gameValues[3]==gameValues[6]==character) or (gameValues[1]==gameValues[4]==gameValues[7]==character) or (gameValues[2]==gameValues[5]==gameValues[8]==character) or (gameValues[0]==gameValues[4]==gameValues[8]==character) or (gameValues[2]==gameValues[4]==gameValues[6]==character):
            return True
                
    def available_moves(self):
        return [i for i in range(9) if self.board[i]==" "]
    
    def empty_squares(self):
        return self.board.count(" ")
        
def play(game,x_player,o_player,print_game=True):
    if print_game:
        game.print_board_indexes()
    letter="X"
    while game.empty_squares():
        if letter=="O":
            square=o_player.get_move(game)
        else:
            square=x_player.get_move(game)
        if game.make_move(square,letter):
            if print_game:
                print(letter+f" makes a move to square {square}")
                game.print_board()
                print()
            if game.currentWinner:
                if print_game:
                    print(letter," Wins!!")
                return letter
            letter="O" if letter=="X" else "X"
        #Read this out ,It is new 
        if print_game:
            time.sleep(2)
    if print_game:
        print("  It's A Tie ")
if __name__=="__main__":
    x=player.HumanPlayer("X")
    o=player.randomComputerPlayer("O")
    play(Tic_Tac_toe(), x,o,print_game=True)