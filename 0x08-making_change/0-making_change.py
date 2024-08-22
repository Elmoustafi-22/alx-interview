#!/usr/bin/python3
"""A function that determines the fewest number of coins needed
to meet a given amount of total"""

def makeChange(coins, total):
    """This function will take a list of coins and use it 
    to calculate the change the total will require
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= 1
        if total == 0:
            return counter
        return -1
