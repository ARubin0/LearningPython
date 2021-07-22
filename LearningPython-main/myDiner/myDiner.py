#!/usr/bin/env python

# TODO
# XXX * if more townsfolk needed.https://www.name-generator.org.uk/?i=c
# XXX add days, 24 hours, Diner closes from 1AM to 6AM.  event loop is 1 tick per hour.
# XXX add cooks √
# XXX add cooking implements 
# XXX one waiter can serve 1 customer per hour.
# XXX IDEAS III/ Questions QQQ/ ZZZ later code things

# QQQ can another function be added to randomly have the  
#   customer decide if they want to order anything else  i/e "wait no how about blank instead" and,  "ill also have this"
# QQQ Line 76-86 r menu. want to be able to "remove drinks" from menu with append as if the tap runs dry
#  CTRL G is shortcut to type to the line of code you want to go to
# ZZZ   FOR LATER
#   physical objects being salt and pepper shaker for food
#   monetary values for food  on the menu and tipping for service
#   dirty dishes on the table/ make the table un useable until the table is cleaned off
#   use input command before/after code to add townsfolk but not allow for duplicants or random letters?

import sys,os

import signal,sys               # to check for user abort
import random
import time                     # to sleep
import appliances

# Abort handler
def signal_handling(signum,frame):
    print ("The Diner is closing for remodeling.")
    sys.exit()


signal.signal(signal.SIGINT,signal_handling)

#v0
# Our first customer function just returns the first name of the customer.
#ef makeCustomer( firstName, lastName ):
    #return firstName
    
#v1
#Picking a random townsfolk and returning the first name

def makeCustomer(townPeople):
    aCust=random.randint(0, len( townPeople ) - 1)
    Cust=townPeople[aCust][0]
    return Cust

#############################################              XXX MENU/ Recipes 
#creates recipes and returns cookbook


def getCookBook():
    riceCookerRecipes = {}
    riceCookerRecipes["cookedRice"] = ["rawRice", "smallWater","bowl"]
    riceCookerRecipes["porridge"]   = ["rawRice", "bigWater","bowl"]
    riceCookerRecipes["chili"]      = ["beans", "meat","smallWater","bowl"]
    
    microwaveRecipes  = {}
    microwaveRecipes["bugsoup"]            = ["bugs", "bigWater","bowl"]
    microwaveRecipes["tea"]                = ["teaBag", "smallWater","mug"]
    microwaveRecipes["bugs"]               = ["bugs","plate"]
    microwaveRecipes["yesterdays special"] = ["teaBag", "bugs", "smallWater","mug"]
    microwaveRecipes["personal Pizza"]     = ["bread", "cheese", "tomatosauce","plate"]

    dessertRecipes  = {}
    dessertRecipes["iceCream"]            = ["icecream","bowl"]

    recipes ={}
    recipes["riceCooker"] = riceCookerRecipes
    recipes["microwave"]  = microwaveRecipes
    recipes["dessert"]    = dessertRecipes
    return recipes
    
    #XXX Drinks
#def drinkStock
#v1

#customer chooses from menu
# IN 
def pickFromMenu( menu ):
    print ("randomwords")
    #XXX pick a random dish from the menu

#XXX drink menu commented out for now
"""
1. one way to build drinks-in-stock list would be;
        *have a for loop
        *in it randomly pick member from list x
        *append it to drinks in stock
        *return drinks in stock
2. figure out appliances ricecooker and microwave and how to call them 
"""
 
"""
2. what am i returning below.
3. do drink menu similar to line 215
4. add pick from drink menu near line 81
5. make pick from menu and pick from drink menu do something real

"""
def drinkMenu(): 
   
    drink=["oldFashoned",      "margarita",   "martini",       
           "mojito",           "whiskySour",  "darkandstormy",
           "bloodyMary",       "guinness",    "heineken",       
           "blueMoon",         "miller",      "millerLight",
           "coke",             "pepsi",       "sprite",         
           "creamSoda",        "mountainDew", "rootBeer"]
    drinkStock = []
    for x in range(9):
        print("ill have " + random.choice(drink))
        drinkStock.append(random.choice(drink))
    return #XXX 
    #

#return list at end of for loop

#waiter brings one of two menues to customer MENU 1/2

def getMenu():
    options = ["cookedRice","porridge","chili","bugs","yesterdays special"]
    return options


# XXX down the road, different cooks will have different menus

def cookFood( cookBook, order ):
    print ("randomword")
    return "cupcake"
    # XXX use the cookbook to get the ingredients for the order, then
    # XXX use the cooking implement to make the food and return it.


    #########################################  Menu/Recipe end


def randCustEvent(maxNum):
    #Get Random Number 
    eventRandom = random.randint(0,maxNum)

    #based on random number choose random event
    if( eventRandom == 1 ):
        print( "Where is everyone??" ) #use to be. where are my customers??

    elif( eventRandom == 2 ):
        print( "a mouse scurries across the floor" )

    elif( eventRandom == 3 ):
        print( " a cold wind passes bye" )

    elif( eventRandom == 4 ):
        print( "a car passes by the diner" )

    elif( eventRandom == 5 ):
        print( "a car speeds by the diner" )

    elif( eventRandom == 6 ):
        print( "Gordon coughs" )

    elif( eventRandom == 7 ):
        print( "Gordon scratches his head" )

    elif( eventRandom == 8 ):
       print( "Gordon coughs" )
            
    elif( eventRandom == 9 ):
       print( "Gordon sneezes"  )

    elif( eventRandom == 10 ):
        print( "the jukebox changes songs" )

    elif( eventRandom >=11 ):
        print( "the lights flicker" )
    
    

def getTownsfolk(): # Currently 20 TOWNSFOLK
    x =[ ["Sally", "Jean"],
        ["Billy", "Rae"],
        ["Samantha", "Johnson"],
        ["Jessica", "Wilson"],
        ["Ashley", "Williams"],
        ["Amber", "Moore"],
        ["Albert", "Hodge"],
        ["Benjamin", "Nash"],
        ["Samuel", "White"],
        ["James", "Torres"],
        ["Megan", "Rodriguez"],
        ["Lucky", "Miller"],
        ["Georgia", "Brown"],
        ["Charlotte", "Smith"],
        ["George", "Michael"],
        ["Carlos", "Santana"],
        ["Goob", "Banner"],
        ["Zack", "Felt"],
        ["Bobby", "Smith"],
        ["Sammi", "Jones"],
        ]
    return x

# XXX deliver food from cook. 
# XXX get customer feedback
# XXX customer feedback 


# The main event loop that drives myDiner.
def main():
   
    
    print( "Alfonso's Diner is open for business!" )

    maxNum    = 20 
    townsFolk = getTownsfolk()
    cookBook  = getCookBook()
    menu      = getMenu()

    # init customers with 2 random people
    firstCust = makeCustomer(townsFolk)
    secCust   = makeCustomer(townsFolk) 
    customers = [ firstCust, secCust ]

   
    # Event loop.  The diner is always open.. loop forever
    while True:
        
        # Check if we have a new customer
        if( random.randint( 0, 10 ) < 3 ) :

            newCust =makeCustomer(townsFolk)
            print( newCust + " walks in." )
            print( "Hi " + newCust + ".  Be right with you." )
            customers.append( newCust )

        serveCustomer = "---"
        # Serve next customer in line, if there is one
        if( len( customers ) > 0 ):
            serveCustomer = customers.pop(0)

        if( serveCustomer == "---" ) :
            print( "Where are my customers??" )
            # XXX add random event, like cook scratches his head
            randCustEvent(maxNum)
        else :
            # XXX Take an order based on cooking implements.
            print( "What can I get for you " + serveCustomer + " we currently have replaceme1 and replaceme2 as our specials" )
            #
            order = pickFromMenu(menu)
            drinkOrder = drinkMenu()
            print("so you would like "+drinkOrder)
            print ("thats a great dish!") #anyting else?")
            #time to make the food
            hotFood=cookFood(cookBook,order)
            print (hotFood)
    
        #wait
        print("")
        time.sleep(3)
          

if __name__ == "__main__":
    main()