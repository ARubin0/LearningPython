def heads_tails():
 print ("heads") or ("tails")
 print ("heads_tails")
 
 
 
 ###!/usr/bin/env python

import random
    

def printStuff() :
    print("Stuff")

def printStuffPrime() :
    print("Stuff Prime")
    
    
def main( cmd ):
    x = random.randint(1,2)

    if x == 1 :
        printStuff()
    else :
        printStuffPrime()
  
if __name__ == "__main__":
    main("")


    ###stackoverflow heads or tails
import random

flips = 1
heads = 0
tails= 0

while flips <= 100:
    coin = random.randint(1,2)
    flips +=1
    if coin == 1:
        print("Heads")
        heads += 1
    elif coin == 2:
        print("tails")
        tails += 1

print("You got " + str(heads) +  " heads and " + str(tails) + " tails!")
("Exit")
"""
take while function and move it 
"""