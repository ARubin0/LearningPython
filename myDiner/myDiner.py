#!/usr/bin/env python
#system libraries
import sys,os
import signal,sys               # to check for user abort
import random                   # to randomly select with the if/elif statements
import time

#local libraries 
import appliances               # to do other things while keeping myDiner clean
import cooks


# Abort handler
def signal_handling(signum,frame):
    print ("The Diner is closing for remodeling.")
    sys.exit()

sys.modules
signal.signal(signal.SIGINT,signal_handling)


def makeCustomer(townPeople):
    aCust=random.randint(0, len( townPeople ) - 1)
    Cust=townPeople[aCust][0]
    return Cust

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
    microwaveRecipes["personal Pizza"]     = ["bread", "cheese", "tomatoSauce"]

    dessertRecipes  = {}
    dessertRecipes["iceCream"]             = ["icecream"]
    dessertRecipes["chipIceCream"]         = ["icecream","chips"]

    recipes ={}
    recipes["riceCooker"] = riceCookerRecipes
    recipes["microwave"]  = microwaveRecipes
    recipes["dessert"]    = dessertRecipes
    return recipes


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
    
#make chair returns a (dict) chair that will either be occupied or not
def makeChair():
    chair     = {"occupied" : False}
    return chair
    
#get tables only returns tables/chairs for customers to sit at nothing else at this point
#-tableCount- the number of small tables is the argument tableCount is the NON fixed Number of tables in the resturaunt 
def getTables(tableCount):
    """Create a set number of  table and chairs that 
    the customers sit in and (occupy or dont)
    for every table have two chairs 
    known variables tableCount,
    """
    
    tablesInUse = []
    for  x in range(tableCount):
        table ={}
        table["chairOne"] = makeChair()
        table["chairTwo"] = makeChair()
        tablesInUse.append(table)

    return  tablesInUse


def getResturaunt():
    
    return 

    
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

# XXX down the road, different cooks will have different menus

def sendToKitchen( cookBook, foodOrder ):
    print ("the food is cooking");time.sleep (1) 

    #XXX randomly choose cook 
    cooks=["Gordon","Guy"]
    cook=random.choice(cooks)
    print ("****",cook)
    
    foodPlate="bronwMush"
    
    #send food order to chosen cook
    if( cook=="Gordon" ):
        foodPlate=cooks.gordon( foodOrder,cookBook )
        print ("gordon is cooking")
    elif( cook=="Guy" ):
        foodPlate=cooks.guy( foodOrder,cookBook )
        print ("guy is cooking")
        
    print("returning",foodPlate)
    return foodPlate

def waiter(Anthony):
    x=random.choice(waiter)
    
    a=Anthony
    return a


def randCustEvent(maxNum):
    #Get Random Number 
    eventRandom = random.randint(0,maxNum)

    #based on random number choose random event
    if( eventRandom == 1 ):
        print( "Where is everyone??" ) 

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
#XXX clean up the constants MaxNum-tables 
def main():
    
    print( "Alfonso's Diner is open for business!" )
    #(Initializing variables)
    #XXX drinkMenu = getDrinkMenu()
    maxNum    = 20 
    townsFolk = getTownsfolk()
    cookBook  = getCookBook()
    menu      = getMenus()
    tables    = getTables(10)

    # init customers with 2 random people
    firstCust = makeCustomer(townsFolk)
    secCust   = makeCustomer(townsFolk) 
    customers = [ firstCust, secCust ]

    #cook will eventually take order and use "cookbook" to make food like code below

    #3. cook looks up order in cookbook to find recipe
    #3.5 this goes here...z=appliances.riceCooker(["beans","meat","smallWater"],cookBook)
    #                           print(z, "++++")
    #4.cook feeds raw ingredients to appliance(s) 
    #5.cook takes food from appliance and puts it on plate for waiter
    #6.cook rings bell telling waiter food is ready



    # Event loop.  The diner is always open.. loop forever
    while True:
        #
        # Check if we have a new customer
        if( random.randint( 0, 10 ) < 7 ) :

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
            #hotFood=cookFood(cookBook,foodOrder)
            hotFood=sendToKitchen(cookBook,tableOrder)
            print (hotFood)
    
        #wait
        print("")
        time.sleep(3)

if __name__ == "__main__":
    main()

