import random

def play():
    while True:
        to_play=input("Do you want to play rock, paper and scissor 'y' for yes or 'n' for No : ").upper()
        if to_play=="Y":
            user_input=input('Pick "r" for rock ,"p" for paper or "s" for scissor : ').upper()
            computer_pick = random.choice(["R", "P", "S"])
            if user_input==computer_pick:
                print("It was a Tie @@")
            elif find_winner(user_input,computer_pick):
                print("You Win !!")
            else:
                print("You Lose :/")
        else:
            break
def find_winner(user_input,computer_pick):
    if (computer_pick=="R" and user_input=="P") or (computer_pick=="P" and user_input=="S") or (computer_pick=="S" and user_input=="R"):
        return True
play()