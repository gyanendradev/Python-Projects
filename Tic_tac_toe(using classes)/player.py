import math
import random

class player:
    def __init__(self,letter):
        self.letter=letter
        
    def get_move(self,game):
        pass

class randomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        position=random.choice(game.available_moves())
        return position
    
class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        validmove=False
        while validmove==False:
            value=input(self.letter + '\'s turn .Input from 0 to 8: ')
            try:
                value=int(value)
                if value not in game.available_moves():
                    raise ValueError
                validmove=True
            except:
                print("Enter valid position , Try again")
        return value
    
class GeniusComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        if len(game.available_moves())==9:
            best_move=random.choice(game.available_moves())
        else:
            # get position based on the minimax algorithm
            best_move=self.minimax(game,self.letter)["position"]
        return best_move
    
    def minimax(self,state,player):
        max_player=self.letter
        other_player="O" if player=="X" else "X"
        if state.currentWinner==other_player:
            # we should return position and score because we need to keep track of the score
            #  this is our base case
            return  {"position": None, "score": 1 * (state.empty_squares() + 1) if other_player == max_player else -1 *(
                        state.empty_squares() +1)}
        elif state.empty_squares()==0:
            return {"position":None,"score":0}
        
        # Initialise some dictionaries
        if player==max_player:
            best={"position":None,"score":-math.inf}  # each score should maximize (be larger)
        else:
            best={"position":None,"score":math.inf} # each score should minimize
            
        for possible_move in state.available_moves(): 
            
            # step 1:make a move and try that spot
            state.make_move(possible_move,player)
             
            # step 2: recure using minimax to simulatea game after making that move
            simulated_score=self.minimax(state,other_player)
            
            # step 3: undo the move
            state.board[possible_move]=" "
            state.currentWinner=None
            simulated_score["position"]=possible_move
            
            # step 4: update the dictionary if necessary
            if player==max_player: # we are trying to maximize the max_player 
                if simulated_score["score"]>best["score"]:
                    best=simulated_score 
            else: # trying to minimize the other player
                if simulated_score["score"]<best["score"]:
                    best=simulated_score
        return best