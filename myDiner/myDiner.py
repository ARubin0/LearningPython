#!/usr/bin/env python

import sys,os
import signal,sys               # to check for user abort
import random                   # to randomly select with the if/elif statements
import time

from appliances import riceCooker

#from myDiner import drinkMenu                     # to sleep
import appliances               # to do other things while keeping myDiner clean



# Abort handler
def signal_handling(signum,frame):
    print ("The Diner is closing for remodeling.")
    sys.exit()

sys.modules
signal.signal(signal.SIGINT,signal_handling)

#v0
# Our first customer function just returns the first name of the customer.
#def makeCustomer( firstName, lastName ):
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
    riceCookerRecipes["cookedRice"] = ["rawRice", "smallWater"]
    riceCookerRecipes["porridge"]   = ["rawRice", "bigWater"]
    riceCookerRecipes["chili"]      = ["beans", "meat","smallWater"]
    
    microwaveRecipes  = {}
    microwaveRecipes["bugsoup"]            = ["bugs", "bigWater"]
    microwaveRecipes["tea"]                = ["teaBag", "smallWater"]
    microwaveRecipes["bugs"]               = ["bugs"]
    microwaveRecipes["yesterdays special"] = ["teaBag", "bugs", "smallWater"]
    microwaveRecipes["personal Pizza"]     = ["bread", "cheese", "tomatosauce"]

    dessertRecipes  = {}
    dessertRecipes["iceCream"]             = ["icecream",]

    recipes ={}
    recipes["riceCooker"] = riceCookerRecipes
    recipes["microwave"]  = microwaveRecipes
    recipes["dessert"]    = dessertRecipes
    return recipes
    
#v1

"""
    random.choice(menuFood)
    print(random.choice(menuFood))
    y=random.choice(menuFood)
"""

#customer chooses a single food and drink from  menu
#anyTwoMenu is a food and a drink menu being chosen by customer 
def pickFromMenus( anyTwoMenu ):
    print ("this is the food and drink menu, take your time deciding,or dont")
    menuFood=anyTwoMenu [1]
    menuDrink=anyTwoMenu[0]
    
    aFood=random.choice(menuFood)
    #print(afood)

    aDrink=random.choice(menuDrink)
    #print(adrink)

    return aFood,aDrink
    
    #This returns a random entire menu
def getMenus():
    options = ["cookedRice","porridge","chili","bugs","yesterdays special"]
    drink=["oldFashoned",      "margarita",   "martini",       
            "mojito",           "whiskySour",  "darkandstormy",
            "bloodyMary",       "guinness",    "heineken",       
            "blueMoon",         "miller",      "millerLight",
            "coke",             "pepsi",       "sprite",         
            "creamSoda",        "mountainDew", "rootBeer"]
    drinksOnTap = []
    for x in range(9):
        #print("we  have " + random.choice(drink))
        d=drinksOnTap.append(random.choice(drink))
    return drinksOnTap,options

#d=drinksOnTap.append(random.choice(drink)) 
# above doesnt work.(d) cant be set to no list. also creates more errors

#XXX fixed 118-119 now (112-113) to look like 102 subtle bug prints twice doesnt save one 

# XXX down the road, different cooks will have different menus

def cookFood( cookBook, foodOrder ):
    print ("the food is cooking");time.sleep (1) 

    return "the food is done cooking " # + foodplate (if food doesnt match cookbood return brownMush instead)
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
        print( "a cold wind passes bye" )

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

    #drinkMenu = getDrinkMenu()
    #menu     = getMenu()
    maxNum    = 20 
    townsFolk = getTownsfolk()
    cookBook  = getCookBook()
    menu      = getMenus()

    # init customers with 2 random people
    firstCust = makeCustomer(townsFolk)
    secCust   = makeCustomer(townsFolk) 
    customers = [ firstCust, secCust ]

    #XXXRicecooker works. call it from a good place   
    #appliances.riceCooker(["rawRice"],cookBook)
    #cook will eventually take order and use "cookbook" to make food like code below
    #0.this belongs in event loop somewhere
    #1.waiter takes order from cust.
    #2. waiter gives order to cook
    #3. cook looks up order in cookbook to find recipe
    #3.5 this goes here...z=appliances.riceCooker(["beans","meat","smallWater"],cookBook)
    #                           print(z, "++++")
    #4.cook feeds raw ingredients to appliance(s) 
    #5.cook takes food from appliance and puts it on plate for waiter
    #6.cook rings bell telling waiter food is ready
    #7.waiter brings food to cust
    z=appliances.riceCooker(["beans","meat","smallWater"],cookBook)
    print(z, "++++")
    
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
            #foodOrder      = pickFromMenu(menu)
            #drinkOrder     = pickFromDrinkMenu(drinkMenu)
            tableOrder      = pickFromMenus(menu)
            #print (drinkOrder, foodOrder, + " thats a great dish!")
            print (tableOrder,"Great! we'll have them out for you shortly")
            #time to make the food
            #hotFood=cookFood(cookBook,foodOrder)
            hotFood=cookFood(cookBook,tableOrder,)
            print (hotFood)
    
        #wait
        print("")
        time.sleep(3)

if __name__ == "__main__":
    main()

    