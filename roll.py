#!/usr/bin/env python3

import random
import time

def d_roll(di):
       return random.randint(1,di) + random.randint(1,di)

def error_msg():
    time.sleep(0.2)
    print("\nPlease enter only values 6 or 8...\n")
    time.sleep(0.3)

# This should be generalized
dist6 = [" 2: ", " 3: ", " 4: ", " 5: ", " 6: ", " 7: ", " 8: ", " 9: ", "10: ", "11: ", "12: "]
dist8 = [" 2: ", " 3: ", " 4: ", " 5: ", " 6: ", " 7: ", " 8: ", " 9: ", "10: ", "11: ", "12: ", "13: ", "14: ", "15: ", "16: "]

def loop(dis, d):
    while True:
        time.sleep(0.1)
        dis[d_roll(d) - 2] += "|"
        print()
        print("="*79)
        print("Showing dice roll distribution of two %s sided dice:" % number)
        print("="*79)
        for i in range(len(dis)):
            print(dis[i])
        print("="*79)
        print("Use Ctrl+c in order to quit...")
        print("="*79)

while True: # After generalizing distrobutions, optimize if/elif statements
    try:
        number = int(input("Choose 6 or 8 sided dice: "))
        if number == 6:
            dist_gen = dist6
            break
        elif number == 8:
            dist_gen = dist8
            break
        else:
            error_msg()
    except ValueError:
        error_msg()

loop(dist_gen, number)
