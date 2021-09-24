


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


Calling a Function
To call a function, use the function name followed by parenthesis

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
   
    return foodPlate global
write microwave function

PULL CORRECTLY FROM GITHUB
dont forget to write stuff on paper if stuck and use python CMD

IF BROKEN RELOAD INCASE ERROR WITH visual studio
#KEYWORD  -- reserved words that canNOT be used as a variable name AKA statement makers(if, elif, and,return,etc)
-   XXX variables created inside functions belong to those functions only
- and can only be used inside the function it was created in UNLESS -- global -- keyword is used 
get element from list x ... x[0] for first x[1] for seccond and so on

Most comomn function flow
 pass an argument to a function, compute something in the function, save result,then return result 
   #y=random.choice(x)
    random.choice(menuDrink)
    print(random.choice(menuDrink))
    z=random.choice(menuDrink)
    
    
    for dish, recipeIngredients in riceCookerRecipes.items():
        print("***",dish, recipeIngredients,"***")

    *** cookedRice ['rawRice', 'smallWater', 'bowl'] ***
*** porridge ['rawRice', 'bigWater', 'bowl'] ***
*** chili ['beans', 'meat', 'smallWater', 'bowl'] ***





#XXX how to approach coding a new function
    0. review paper function thing 
        for now, re lable one coppy and compare it to master copy
    1. look at how the function is being callled
        for example. put the function call above the function def to remember what it is
    2. understand what the function arguments  REALLY  are reread function calls and defs before using them...
        see the args as they actually are. dont think.
        for ex, def each arg above funct. 
    3.before each component in the body write a comment describing what it will do. 
        for example.     # cook looks up order in cookbook to find recipe
    4. open python interpriter and look at components of code, then, try to access the part that is needed
        for ex, create temp file in myDiner, import temp to python interpreter (CMD), temp.getCookBook 
>           CB=temp.getCookBook()
            for x,y in CB.items():










    BOILER PLATE FUNCTION TEMPLATE
# gordon takes food request from customer(waiter) cooks then gives finished food( good or bad ) to waiter to bring out for customer
# Example function call; foodPlate=cooks.gordon( foodOrder,cookBook )
#   foodOrder is customer order
#   cookBook  is recipe
def gordon( foodOrder, cookBook ):
    
    
    >>> for x in temp.getCookBook():
...     print (x)
...
...
riceCooker
microwave
dessert
>>> for y in temp.getCookBook().items():
...     print (y)
...
('riceCooker', {'cookedRice': ['rawRice', 'smallWater'], 'porridge': ['rawRice', 'bigWater'], 'chili': ['beans', 'meat', 'smallWater']})
('microwave', {'bugsoup': ['bugs', 'bigWater'], 'tea': ['teaBag', 'smallWater'], 'bugs': ['bugs'], 'yesterdays special': ['teaBag', 'bugs', 'smallWater'], 'personal Pizza': ['bread', 'cheese', 'tomatoSauce']})
('dessert', {'iceCream': ['icecream'], 'chipIceCream': ['icecream', 'chips']})
>>>

#XXX SAT. 4

cups   = ["blue cup", "red cup", "green cup"]
dishes = ["small blue", "smaller blue", "smallest blue", "smallester blue"]
bowls  = ["tiny pewter", "giant ceramic"]
Careful - looks like google is playing with tabs in here.. 8*(


kitchen = [ cups, dishes, bowls ]

for container in kitchen:
    print( container )

for container in kitchen:
    print( container )
    for item in container:
    print( item )

for x in kitchen:
    print( x )
    # x will be set to       ["blue cup", "red cup", "green cup"]
    # then, x will be set to ["small blue", "smaller blue", "smallest blue", "smallester blue"]
    # then, x will be set to ["tiny pewter", "giant ceramic"]
    for y in x:
    print( y )


for y in cups:
    print(y)
    