#!/usr/bin/env python

import sys,os
import signal,sys               # to check for user abort
import random                   # to randomly select with the if/elif statements
import time


#from myDiner import drinkMenu                     # to sleep
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
    microwaveRecipes["personal Pizza"]     = ["bread", "cheese", "tomatoSauce"]

    dessertRecipes  = {}
    dessertRecipes["iceCream"]             = ["icecream"]
    dessertRecipes["chipIceCream"]         = ["icecream","chips"]

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
    
#make chair returns a (dict) chair that will either be occupied or not
def makeChair():
    chair     = {"occupied" : False}
    return chair
    
#get tables only returns tables/chairs for customers to sit at nothing else at this point
def getTables():
    table=["tableOne","tableTwo"]
    chair=["chairOne","chairTwo,""chairThree","chairFour","chairFive","chairSix","chairSeven","chairEight",\
           "chairNine","chairTen","chairEleven","chairTwelve","chairThirteen","chairFourteen","chairFifteen",\
            "chairSixteen, chairSeventeen,chairEighteen"]
    resturaunt = {table,chair}
    a=makeChair() 
    b=makeChair()
    c=makeChair()
    d=makeChair()
    e=makeChair()
    #5 chairs
    f=makeChair()
    g=makeChair()
    h=makeChair()
    i=makeChair()
    j=makeChair()
    #5 more chairs
    k=makeChair()
    l=makeChair()
    m=makeChair()
    n=makeChair()
    o=makeChair()
    #5 more chairs...
    p=makeChair()
    q=makeChair()
    r=makeChair()
    #last 3 chairs that makes 18 
    return resturaunt
    
    #20 current customers-so 10 tables+2 chairs per table= a perfect amount of seats (want less so wait time,8 tables+2 chairs=16 of 20 )
    # Deuce – A table with only two seating spaces. For example, “Seat this deuce at Table 
    #deuce["tableOne"] = ["tableOne","chairOne" ,"chairTwo"]
        #tableOne is made up of table One and two chairs and so on
def getResturaunt():
    deuce= {}
    
    deuce["tableOne"]    = ["tableOne"  , "chairOne"       ,      "chairTwo"]
    deuce["tableTwo"]    = ["tableTwo"  , "chairThree"     ,     "chairFour"]
    deuce["tableThree"]  = ["tableThree", "chairFive"      ,      "chairSix"]
    deuce["tableFour"]   = ["tableFour" , "chairSeven"     ,    "chairEight"]
    deuce["tableFive"]   = ["tableFive" , "chairNine"      ,      "chairTen"]
    deuce["tableSix"]    = ["tableSix"  , "chairEleven"    ,   "chairTwelve"]
    deuce["tableSeven"]  = ["tableSeven", "chairThirteen"  , "chairFourteen"]
    deuce["tableEight"]  = ["tableEight", "chairFifteen"   ,  "chairSixteen"]
    deuce["tableNine"]   = ["tableNine" , "chairSeventeen" , "chairEighteen"]

    biggerTables  = {}
    
    biggerTables["bigTableOne"] = ["tableOne,tableTwo"     , "chairOne"  , "chairTwo","chairThree","chairFour"]
    biggerTables["bigTableTwo"] = ["tableThree,tableFour"  , "chairFive" , "chairSix","chairSeven","chairEight"]
    
    singleBigTable ={}
    
    singleBigTable ["annoyinglybigGroupOfPeople"]    = ["tableFive","tableSix","tableSeven","tableEight" , "chairNine","chairTen","chairEleven","chairTwelve",
                                                        ,"chairThirteen","chairFourteen","chairFifteen","chairSixteen","chairSeventeen","chairEighteen"]
    
    

    seating ={}
    seating["table"] = deuce
    seating["a bigger table"]  = biggerTables
    seating["a biggest table"]= singleBigTable
   
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

def sendToKitchen( cookBook, foodOrder ):
    print ("the food is cooking");time.sleep (1) 

    #XXX randomly choose cook 
    cook="Gordon"
    
    foodPlate="bronwMush"
    
    #send food order to chosen cook
    if( cook=="Gordon" ):
        foodPlate=cooks.gordon( foodOrder,cookBook )

    return foodPlate

#XXX
def waiter(Guy,Anthony):
    x=random.choice(waiter)
    g=Guy
    a=Anthony
    return g,a
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
    #(Initializing variables)
    #drinkMenu = getDrinkMenu()
    #menu     = getMenu()
    maxNum    = 20 
    townsFolk = getTownsfolk()
    cookBook  = getCookBook()
    menu      = getMenus()
    tables    = getTables()

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
            hotFood=sendToKitchen(cookBook,tableOrder)
            print (hotFood)
    
        #wait
        print("")
        time.sleep(3)

"""
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
"""
if __name__ == "__main__":
    main()

