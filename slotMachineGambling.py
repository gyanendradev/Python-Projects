import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_frequency = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 8, "B": 6, "C": 4, "D": 2}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, freq in symbols.items():
        for _ in range(freq):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            symbol = random.choice(current_symbols)
            current_symbols.remove(symbol)
            column.append(symbol)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    transposed = [[0 for _ in range(len(columns))]
                  for _ in range(len(columns[0]))]
    for i in range(len(columns)):
        for j in range(len(columns[0])):
            transposed[j][i] = columns[i][j]
    for i in range(len(transposed)):
        print(" | ".join(transposed[i]))


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings_line.append(line+1)
            winnings += bet*values[symbol]
    return (winnings, winnings_line)


def deposit():
    while True:
        amount = input("How much would you like to deposit ?  $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please deposit more than 0  ")
        else:
            print("Please give valid amount")
    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-"+str(MAX_LINES)+")  ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter valid number of lines.")
        else:
            print("Please give valid lines.")
    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line ?  ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount should be between {MIN_BET} ~ {MAX_BET}.")
        else:
            print("Please give valid number.")
    return amount


def game(balance):
    while True:
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(
                f"You don't have enough amount to place that bet, your current balance is: ${balance}")
        else:
            break
    print(
        f"You are betting ${bet} on ${lines} lines. Your total bet is ${lines*bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_frequency)
    print_slot_machine(slots)
    winnings, winnings_line = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines : ", *winnings_line)
    return winnings-total_bet


def main():
    balance = deposit()
    while True:
        if balance == 0:
            break
        print(f"Your current balance is ${balance}")
        spin = input("Press enter to play or 'q' to quit with your balance")
        if spin == "Q" or spin == "q":
            break
        balance += game(balance)
    print(f"You left with ${balance}")


main()
