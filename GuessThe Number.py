import random
def guess(x):
    computer_will_pick=round(x*random.random())
    lowest=1
    highest=x
    print("\nComputer has guessed a number, now you have to find it.\n")
    user_pick=input(f"Pick A Number Between {lowest} and {highest} ")
    while not user_pick.isnumeric() or lowest>int(user_pick) or int(user_pick)>highest:
        print("Please pick a valid integer in range\n")
        user_pick=input(f"Pick A Number Between {lowest} and {highest} ")
    user_pick=int(user_pick)
    count=1
    while user_pick!=computer_will_pick:
        if user_pick<computer_will_pick:
            print("Your Pick Was Too low")
            lowest=user_pick
            user_pick=input(f"Again Pick A Number Between {lowest} and {highest} ")
            while not user_pick.isnumeric() or lowest>int(user_pick) or int(user_pick)>highest:
                print("Please pick a valid integer in range\n")
                user_pick=input(f"Pick A Number Between {lowest} and {highest} ")
            user_pick=int(user_pick)
        elif user_pick>computer_will_pick:
            highest=user_pick
            print("Your Pick Was Too High")
            user_pick=input(f"Again Pick A Number Between {lowest} and {highest} ")
            while not user_pick.isnumeric() or lowest>int(user_pick) or int(user_pick)>highest:
                print("Please pick a valid integer in range\n")
                user_pick=input(f"Pick A Number Between {lowest} and {highest} ")
            user_pick=int(user_pick)
        count+=1
    print(f"Hurray You have guessed {computer_will_pick} correctly in {count} attempts")

def computer_guess(x):
    print("\n Think of a Number")
    print("\n we will start finding the number which you are thinking \n")
    i=0
    j=x
    count=1
    while i<=j:
        num=random.randint(i, j)
        user_input=input(f"Is {num} is greater(G) or lower(l) or equal(e) to your number ")
        if user_input=="G" or user_input=="g":
            j=num-1
        elif user_input=="l" or user_input=="L":
            i=num+1
        elif user_input=="e" or user_input=="E":
            print(f"your number is founded in {count} attempts")
            break
        else:
            print("Please give correct input")
        count+=1
guess(100)