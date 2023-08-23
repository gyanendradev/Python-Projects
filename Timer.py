import time


def start_timer(input_time):
    while input_time:
        min, sec = divmod(input_time, 60)
        print(f"{min}:{sec}", end="\r")
        time.sleep(1)
        input_time -= 1
    print("Timer is complete !!!")


t = int(input("Enter time in seconds to start timer : "))
start_timer(t)
