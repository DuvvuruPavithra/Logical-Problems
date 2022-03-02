import math
import random

def gambler():
    stake = int(input("Enter Stack price : "))
    goal = int(input("Enter Stack Goal : "))
    betPrice = int(input("Enter Stack bet price : "))

    bets = 0
    wins = 0
    win_Percentage = 0
    loss_Percentage = 0

    for i in range(betPrice):
        cash = stake
        while cash > 0 and cash < goal:
            bets += 1
            if random.randrange(0, 1) == 0:
                cash += 1
            else:
                cash -= 1
        if cash == goal:
            wins += 1
    print('Number of times the gambler wins is ', wins)
    print('Number of times the gambler loss is ', bets)
    print('Winning Percentage is ', (100 * wins / betPrice),win_Percentage)
    print('Losing  Percentage is', (100 * bets / betPrice),loss_Percentage)
gambler()



