import random

class Board:
    def __init__(self,dim_size,num_bombs):
        self.dim_size=dim_size
        self.num_bombs=num_bombs
        self.dug=set() # to store which places are already digged
        
        # let's create board
        self.board=self.create_board()
        self.assign_values_to_board()
        
    def create_board(self):
        board=[[None for i in range(self.dim_size)] for i in range(self.dim_size)]
        
        bombs_planted=0
        while bombs_planted<self.num_bombs:
            place=random.randint(0, self.dim_size*self.dim_size-1)
            row=place//self.dim_size
            col=place % self.dim_size
            if board[row][col]=="*":
                continue
            board[row][col]="*"
            bombs_planted+=1
        return board
    
    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c]=="*":
                    continue
                self.board[r][c]=self.get_neighbouring_bombs(r,c)
    
    def get_neighbouring_bombs(self,row,col):
        neighbouring_bombs=0
        for i in range(max(0,row-1),min(self.dim_size,row+2)):
            for j in range(max(0,col-1),min(self.dim_size,col+2)):
                if self.board[i][j]=="*":
                    neighbouring_bombs+=1
        return neighbouring_bombs

    def dig(self,row,col):
        self.dug.add((row,col))
        if self.board[row][col]=="*":
            return False
        elif self.board[row][col]>0:
            return True
        for r in range(max(0,row-1),min(self.dim_size,row+2)):
            for c in range(max(0,col-1),min(self.dim_size,col+2)):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)
        return True            
            
    def show(self):
        print()
        upper=[str(i) for i in range(self.dim_size)]
        print("  | "+" | ".join(upper)+" |")
        print((4*self.dim_size+4)*"-")
        new_board=[[" " for j in range(self.dim_size)] for i in range(self.dim_size)]
        for (row,col) in self.dug:
            new_board[row][col]=str(self.board[row][col])
        if len(self.dug)==self.dim_size**2-self.num_bombs:
            for i in range(self.dim_size):
                row=[str(i) for i in self.board[i]]
                print(f"{i} | "+" | ".join(row)+" |")
        else:
            for i in range(self.dim_size):
                row=new_board[i]
                print(f"{i} | "+" | ".join(row)+" |")
            print()
        
def play(dim_size=10,num_bombs=10):
    # step 1:  create board and plant bombs
    board=Board(dim_size, num_bombs)
    
    #step 2: show the board to user and ask where to dig
    #step 3 : dig according to user input
    #step 4 : repeat steps 2 and 3 until there are no places to dig
    
    safe=True
    while len(board.dug)<board.dim_size**2-num_bombs and safe==True:
        board.show()
        user_input=list(map(int,input("\nWhere Would You Like To Dig For Ex. 0,0 i.e.(row,column) : ").split(",")))
        row=user_input[0]
        col=user_input[1]
        if row<0 or row>board.dim_size-1 or col<0 or col>board.dim_size-1:
            print("Please Provide correct position to dig")
            continue
        if (row,col) in board.dug:
            print("It's already been digged")
            continue
        safe=board.dig(row, col)
    board.show()
    if safe:
        print("You Have Won The Game")
    else:
        print("You have Lose :/ ")
if __name__=="__main__":
    play(6,6)