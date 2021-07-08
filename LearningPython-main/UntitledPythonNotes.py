


Difference between  # A and B is 8 and 13 heads tabbed in when it shouldnt be otherwise it "breaks" the code otherwise code continues to print 
coin without looking at if function. in A heads is only incramented if less than 5 , in b it is incramented every time

#A
    if coin   <= 5 :
        print("Heads")
    	  heads += 1
 
#B
    if coin   <= 5 :
        print("Heads")
    heads += 1

 #   Boolean logic… basically means and or not and combos of them.
#   example
   if( coin >= 6 and coin <= 10 )    #means
   if( (coin >= 6) and (coin <= 10) )  #which evaluates to
   if( true and true )  # which evaluates to 
   If ( true )
#  a List is a collection which is ordered and changeable. Allows duplicate members-
    ( members are words/numbers in the list [ie] Number (1),(1) or names/words [ie] (james),(james) 



###Function V Function Call
 # line 30 is correct. Variable 'Coin' is being set to the call to 'getflip'.
    coin = GetFlip(HeadNum,TailNum,EdgeNum) 
    #line 32 is Wrong. variable 'coin' is being set to the  GetFlip Funciton. (which is just a function. not the call to the function)
    #coin = GetFlip 
  

make another function more complicated than coinflip 3 numbers less than or = heads greater than or = tails greater than or equal to the third number it is edge




### Correct Layout For Python Code File name is  CoinFlip3GetFlipFunction.py
"""
#!/usr/bin/env python

import random #Library


#GetFlip returns a number from 0 to EdgeNum
def GetFlip(HeadNum,TailNum, EdgeNum):
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
        
        # line below is correct. Variable 'Coin' is being set to the call to 'getflip'.
        coin = GetFlip(HeadNum,TailNum,EdgeNum) 
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
"""
XXX 0443148 Kahoot pin 

double check UR diner and get all code out that i want to keep and put it into myDIner then delete UR diner
Check myDiner into MyGithub Branch 
commit to main branch 
FOR THURSDAY 
ADD MORE FUNCTIONS
DO KAHOOT THING WITH SLIDE
SWITCH CASE 
XXX
Function  (   anything   ) #


# method 1 for returning a list
def hiDad():
    x = [["a", "b"], ["c", "d"]]
    return x

FOr thursday add 5 lines of comments 
move order stuff into a function
try to use rice cooker function



FOR MONDAY
EXPLAIN RICE COOKER FUNCTION
# Give good raw ingredients, get good food back.
# example function call:   foodPlate = riceCooker( ["rawRice", "smallWater","bowl"], cookBook]   will return "cookedRice"
def riceCooker( rawIngredients, cookBook ):
    #print( cookBook )

    #variable ricecooker recipes is beeing set to what is in cookbook
    riceCookerRecipes = cookBook["riceCooker"]
    #print( riceCookerRecipes)
    # if raw ingredients don't match a "riceCooker" recipe, iiiick
    foodPlate = "brownMush"

    #iterating through riceCookerRecipes for when recipe ingredients = raw incredients sets foodplate to dish
    # run through riceCookerRecipes, look for rawIngredients that match a recipe, then get the food item.
    for dish, recipeIngredients in riceCookerRecipes.items():
        if recipeIngredients == rawIngredients:
            foodPlate = dish
            break
   
    return foodPlate
write microwave function

PULL CORRECTLY FROM GITHUB
dont forget to write stuff on paper if stuck and use python CMD