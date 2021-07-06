#!/usr/bin/env python

# TODO
# XXX * Need more townsfolk √ ADDED 10 more. if more are needed.https://www.name-generator.org.uk/?i=c
# XXX * makeCustomer function should roll the randInt for us
# XXX * add random events for when there are no customers (its a func)
# XXX * add random events for when there are customers (its the same func, different argument)
# XXX * add 2 cooking implements.   For example, riceCooker takes rawRice, returns cookedRice.  If input is not rawRice

# XXX add 1 cook
# XXX add ingredients + dish pairings that work on cooking implements.  e.g. ingredients: rawRice, makes: cookedRice
# XXX add days, 24 hours, Diner closes from 1AM to 6AM.  event loop is 1 tick per hour.
# XXX customers should only show up once, i.e. Bobby Smith does not have a clone
# XXX add waiters
# XXX add cooks
# XXX add cooking implements 
# XXX add tables
# XXX one waiter can serve 1 customer per hour.


import signal,sys               # to check for user abort
import random
import time                     # to sleep

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
###########################################################               XXX MENU/ Recipes            ################################################################################
#creates recipes and returns cookbook
def getCookBook():
    recipes = {}

    riceCookerRecipes = {}
    riceCookerRecipes["cookedRice"] = ["rawRice", "smallWater","bowl"]
    riceCookerRecipes["porridge"]   = ["rawRice", "bigWater","bowl"]
    riceCookerRecipes["chili"]      = ["beans", "meat","smallWater","bowl"]
    
    microwaveRecipes  = {}
    microwaveRecipes["bugsoup"]            = ["bugs", "bigWater","bowl"]
    microwaveRecipes["tea"]                = ["teaBag", "smallWater","mug"]
    microwaveRecipes["bugs"]               = ["bugs","plate"]
    microwaveRecipes["yesterdays special"] = ["teaBag", "bugs", "smallWater","mug"]
    microwaveRecipes["personal Pizza"] = ["bread", "cheese", "tomatosauce","plate"]

    recipes["riceCooker"] = riceCookerRecipes
    recipes["microwave"]  = microwaveRecipes
    return recipes

# Give good raw ingredients, get good food back.
# example function call:   foodPlate = riceCooker( ["rawRice", "smallWater","bowl"], cookBook]   will return "cookedRice"
def riceCooker( rawIngredients, cookBook ):
    #print( cookBook )

    riceCookerRecipes = cookBook["riceCooker"]
    #print( riceCookerRecipes)

    # if raw ingredients don't match a "riceCooker" recipe, iiiick
    foodPlate = "brownMush"

    # run through riceCookerRecipes, look for rawIngredients that match a recipe, then get the food item.
    for dish, recipeIngredients in riceCookerRecipes.items():
        if recipeIngredients == rawIngredients:
            foodPlate = dish
            break
   
    return foodPlate

def microwave( rawIngredients, cookBook ):
    #print( cookBook )

    microwaveRecipes = cookBook["microwave"]
    #print( microwaveRecipes)

    # if raw ingredients don't match a "microwave" recipe, iiiick
    foodPlate = "brownMush"

    # run through riceCookerRecipes, look for rawIngredients that match a recipe, then get the food item.
    for dish, recipeIngredients in microwaveRecipes.items():
        if recipeIngredients == rawIngredients:
            foodPlate = dish
            break
   
    return foodPlate
#customer chooses from menu 
def pickFromMenu( menu ):
    print ("randomwords")
    #XXX pick a random dish from the menu

#waiter brings one of two menues to customer MENU 1/2
def getMenu():
    options = ["cookedRice","porridge","chili","bugs","yesterdays special"]
    return options
    
#waiter brings one of two menues to customer MENU 2/2
def getVegMenu():
    options = ["","Bugsoup","tea"]
    return options
   
#this is the "cook" function that is the finished product ["cooked rice"] = ["rawRice", "smallWater"]
def riceCooker( rawIngredients ):
    foodPlate = "cooked rice"
    foodBowl  = "porridge"
    bowlFood  = "chili"
    # XXX if raw ingredients match a "riceCooker" recipe, set foodPlate to that.
   
    return [foodPlate, foodBowl, bowlFood]

#the other  "cook" function that is the finished product ->["bugs"] <- )) = ["rawRice", "smallWater"]
def microWave ( rawIngredients ):
    hotPlate    = "bugs"
    hotBowl     = "bugsoup"
    chunkyFood  = "yesterdays special"
    hotLiquid   = "tea"
    pizza       = "personal Pizza"

    # XXX if raw ingredients match a "riceCooker" recipe, set foodPlate to that.
   
    return [hotPlate, hotBowl, chunkyFood, hotLiquid,pizza]

# XXX down the road, different cooks will have different menus
def cookFood( cookBook, order ):
    print ("randomword")
    return "cupcake"
    # XXX use the cookbook to get the ingredients for the order, then
    # XXX use the cooking implement to make the food and return it.


    ##########################################################################  Menu/Recipe end       ##############################################################################################################

def bussBoy(Gary): #bussboy is the "accurate" term for table cleaner in resturaunt businesses
    print("cleaning table")
    #return dirty dishes to backroom 
    

def wait():
    print ("wait")

def clean():
    print("clean")

def ready():
    print("ready")

def dirty(dirtTable):
    while True:
        return random.randit (1,10)


roundtable =(wait,clean,ready)
x = roundtable
if   x   >= 6:
    print  + roundtable ("needs to be cleaned before another patron can be sat here")
    
elif x   == 3:
    print  + roundtable ("is currently being cleaned by the bussboy")
 
elif x   == 1:
    print  + roundtable ("is ready to be used")

def Table(tableOne,tableTwo):#table currently has one chair
    random.randit(1,2)
    print("table is open or closed")
 
def dish(bowl,plate,cup):
    print("FILLER")


def dishWash(dishwasher):
    while True:
        random.randit(1,5)
        x = dish
        if x <= 2:
            print ("dishes are being washed")
            time.sleep(1)
        if x == 1:
            print ("dishes are clean and ready")



def waiter(Guy,Anthony):
    random.randit(1,2)
    print("Blank Waiter will seat you now at a table")

"""
#XXX QUESTIONS
how would i leave specific dirty dishes on the table/ make the table un useable until the table is cleaned off

"""

def randCustEvent(maxNum):
    #Get Random Number 
    eventRandom = random.randint(0,maxNum)

    #based on random number choose random event
    if( eventRandom == 1 ):
        print( "Where are my customers??" )

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
            print( "What can I get for you " + serveCustomer + "we currently have replaceme1 and replaceme2 as our specials" )
            #
            order = pickFromMenu(menu)
            print ("thats a great dish!") #anyting else?")
            #time to make the food
            hotFood=cookFood(cookBook,order)
            print (hotFood)







            #XXX can another function be added ro randomly have the 
            # customer decide if they want to order anything else  i/e "wait no how about blank instead" and,  "ill also have this"
            
            # XXX deliver food from cook. 

            # XXX get customer feedback
def feedBack(0,20):
    #Get Random Number 
    eventRandom = random.randint(0,20)

        if   ( brownMush ) >=  10:
            print ("this is disgusting get me the cook")
        elif (brownMush) ==   9:
                print("this needed salt")
        elif ( foodPlate ) == 2:
            print ("this was the best food ive had in a while")
        elif ( foodPlate ) ==1:
                print("this needed salt") #add salt and pepper shaker when objects are added?
        elif ( foodPlate ) ==3:
                print("this was OK")
        elif ( foodPlate ) ==   4:
                print("this has WAY too much salt")
        # Wait for us slow humans
        print("" )
        time.sleep(3)

        
        
if __name__ == "__main__":
    main()