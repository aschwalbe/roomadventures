'''
Name: Austin Schwalbe
Date: 31 January 2020
Description: Timer
Reference: COSC 1351 - Fall 2020
'''

from time import time

# start a timer

def timer_start():
    global start
    start = time()


# stop the timer and return time elapsed
def timer_stop():
    stop = time()
    elapsed = stop - start
    return elapsed
