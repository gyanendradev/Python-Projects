import random

def displayGame(gameValues):
    for i in range(0,9,3):
        print("|",end="")
        for j in range(i,i+3):
            print(f" {gameValues[j]}",end=" |")
        print()

def checkWin(gameValues,character):
    if (gameValues[0]==gameValues[1]==gameValues[2]==character) or (gameValues[3]==gameValues[4]==gameValues[5]==character) or (gameValues[6]==gameValues[7]==gameValues[8]==character) or (gameValues[0]==gameValues[3]==gameValues[6]==character) or (gameValues[1]==gameValues[4]==gameValues[7]==character) or (gameValues[2]==gameValues[5]==gameValues[8]==character) or (gameValues[0]==gameValues[4]==gameValues[8]==character) or (gameValues[2]==gameValues[4]==gameValues[6]==character):
        return True
    
def play_Tic_Tac_toe():
    gameValues=[" "," "," "," "," "," "," "," "," "]
    Not_filled_boxes=[0,1,2,3,4,5,6,7,8]
    for i in range(0,9,3):
        print("|",end="")
        for j in range(i,i+3):
            print(f" {j}",end=" |")
        print()
    number_of_moves=0
    while number_of_moves<9:
        if number_of_moves%2==0:
            user_input=int(input("X's turn. Input from 0 to 8 : "))
            if user_input in Not_filled_boxes:
                number_of_moves+=1
                print("\nX make a move to position",user_input)
                Not_filled_boxes.remove(user_input)
                gameValues[user_input]="X"
                displayGame(gameValues)
                if checkWin(gameValues,"X"):
                    return "X wins "
            else:
                print("Please Choose correct position !!")
                continue
        else:
            number_of_moves+=1
            computer_pick=random.choice(Not_filled_boxes)
            Not_filled_boxes.remove(computer_pick)
            gameValues[computer_pick]="O"
            print("\nO makes a move to position",computer_pick)
            displayGame(gameValues)
            if checkWin(gameValues,"O"):
                return "O wins "
print(play_Tic_Tac_toe())