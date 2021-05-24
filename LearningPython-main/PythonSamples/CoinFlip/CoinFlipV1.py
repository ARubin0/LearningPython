#!/usr/bin/env python

import random #Library


#GetFlip returns a number from 0 to EdgeNum
def FlipCoin(HeadNum,TailNum, EdgeNum):
    #HeadNum and TailNum are Used later
    return random.randint(0,EdgeNum)


if __name__ == "__main__":  

    flips = 1 #initaializing flips
    heads = 0
    tails = 0
    edge = 0
    HeadNum=5
    TailNum=10
    EdgeNum=11
    while flips  <= 10:  
        
        # line 24 is correct. Variable 'Coin' is being set to the call to 'getflip'.
        coin = FlipCoin(HeadNum,TailNum,EdgeNum) 
        flips +=1 #incramenting
        if  coin   <= HeadNum :
            print("Heads")
            heads += 1
        elif coin  <= TailNum :
            print("tails")
            tails += 1
        elif coin == EdgeNum:
            print ("edge")
            edge +=1
        

    print("You got " + str(heads) +  " heads, " + str(tails) + " tails, and " + "on its edge " + str(edge))



("Exit")
