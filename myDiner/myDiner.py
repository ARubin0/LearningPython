#!/usr/bin/env python
#system libraries
import sys,os
import signal,sys               # to check for user abort
import random                   # to randomly select with the if/elif statements
import time

#local libraries 
import appliances               # to do other things while keeping myDiner clean
import cooks
import pprint

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
    #print(aFood)

    aDrink=random.choice(menuDrink)
    #print(aFrink)

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
"""
# TODO XXX down the road, different cooks will have different menus
# sendToKitchen chooses a cook randomly to make food
def sendToKitchen( cookBook, foodOrder, availCooks ):
    print( "the food is co000000000000000000000000000000000000000000000oking" )
    time.sleep(1) 

    # randomly choose cook 
    #cook=random.choice(availCooks)
    cook = random.choice(list(availCooks.values()))
    foodPlate="bronwMush"
    # cook dictionary
    if(  cook["firstName"] =="Gordon" ): 
        print(  ["firstName"],"is----------- cooking"  )
        foodPlate=cooks.gordon( foodOrder, cookBook )
    if( cook["firstName"] == "Guy" ): 
        print( "is----------- cooking"  )
        foodPlate=cooks.gordon( foodOrder, cookBook )
    if( cook["firstName"] =="Paula" ): 
        print( "is----------- cooking"  )
        foodPlate=cooks.gordon( foodOrder, cookBook )
    if(cook["firstName"] =="Jamie" ): 
        print("is----------- cooking"  )
        foodPlate=cooks.gordon( foodOrder, cookBook )
    if( cook["firstName"] =="Rachel" ): 
        print( "is----------- cooking"  )
        foodPlate=cooks.gordon( foodOrder, cookBook )
    if( cook["firstName"]=="Bobby" ): 
        print( "is----------- cooking" )
        foodPlate=cooks.gordon( foodOrder, cookBook )
    print ("SEND BACK FROM KITCHEN/*/*/*/*/*/*/*/*/*/*/*")
    return 
"""




# sendToKitchen chooses a cook randomly to make food and returns a foodPlate
# foodOrder is pickFromMenu aFOod+aDrink ("cookedRice","Coke")
def sendToKitchen( cookBook, foodOrder, availCooks ):
    print( "the food is co000000000000000000000000000000000000000000000oking" )
    time.sleep(1) 

    # randomly choose cook 
    #cook=random.choice(availCooks)
    cook = random.choice(list(availCooks.values()))
    foodPlate="bronwMush"
    # cook dictionary
    if(  cook["firstName"] =="Gordon" ): 
        print(  "Gordon is cooking"  )
        foodPlate=cooks.theCooks( foodOrder, cookBook,cook )
    if( cook["firstName"] == "Guy" ): 
        print( " Guy is cooking"  )
        foodPlate=cooks.theCooks( foodOrder, cookBook,cook )
    if( cook["firstName"] =="Paula" ): 
        print( " Paula is cooking"  )
        foodPlate=cooks.theCooks( foodOrder, cookBook,cook )
    if(cook["firstName"] =="Jamie" ): 
        print(" Jamie is cooking"  )
        foodPlate=cooks.theCooks( foodOrder, cookBook,cook )
    if( cook["firstName"] =="Rachel" ): 
        print( " Rachel is cooking"  )
        foodPlate=cooks.theCooks( foodOrder, cookBook,cook )
    if( cook["firstName"]=="Bobby" ): 
        print( " Bobby is cooking" )
        foodPlate=cooks.theCooks( foodOrder, cookBook,cook )
    print ("SEND BACK FROM KITCHEN/*/*/*/*/*/*/*/*/*/*/*")
    return foodPlate


#XXX waiter can trip and lose the food 
def waiter(Anthony):
    x=random.choice(waiter)
    
    a=Anthony
    return a
# XXX Next, use  COoks Wisely 

 
def randCustEvent():

    r= ["Where is everyone??",
                "a mouse scurries across the floor",
                "a cold wind passes bye",       
                "a car passes by the diner",           
                "Gordon coughs",
                "Guy coughs"
                "Gordon scratches his head",
                "Guy scratches his head",       
                "Gordon sneezes",      
                "Guy sneezes"
                "the jukebox skips a beat",
                "the lights flicker",]
    randEvent=(random.choice(r))
    return randEvent

def getTownsfolk(): # Currently 20 TOWNSFOLK
    x =[ ["Sally", "Jean"]      ,["Billy", "Rae"],
        ["Samantha", "Johnson"] ,["Jessica", "Wilson"],
        ["Ashley", "Williams"]  ,["Amber", "Moore"],
        ["Albert", "Hodge"]     ,["Benjamin", "Nash"],
        ["Samuel", "White"]     ,["James", "Torres"],
        ["Megan", "Rodriguez"]  ,["Lucky", "Miller"],
        ["Georgia","Brown"]     ,["Charlotte", "Smith"],
        ["George", "Michael"]   ,["Carlos", "Santana"],
        ["Goob", "Banner"]      ,["Zack", "Felt"],
        ["Bobby", "Smith"]      ,["Sammi", "Jones"],
        ["Josephine", "Goodman"],["Poppy, Trejo"],
        ["Cooper,", "Luna"]     ,["Angelo, Ward"],
        ["Eileen", "Gardiner"]  ,["Milena" ,"Walmsley"],
        ["Marcelina", "Mccall"] ,["Daniella" ,"Pemberton"],
        ["Whitney", "Hooper"]   ,["Ezra","Hickman"],
        ["Colleen", "Wilson"]   ,["Rae"," Lawson"],
        ["Mylie", "Zimmerman"]  ,["Tye","Larson"],
        ["Merryn", "Andrade"]   ,["Lacey"," Ellison"],
        ["Kiri"," Burn"]        ,["Felicity","Bain"],
        ["Taybah", "Norton"]    ,["Sean","Rivers"],
        ["Paisley", "Goulding"] ,["Tahlia Russo"],
        ["Lucy"," Garner"]      ,["Stuart","Faulkner"],
        ["Alissia ", "Lennon"]  ,["Amy"," Mills"],
        ["Brendan"," Mcgill"]   ,["Summer","Kirkland"],
        ["Zach"," Davie"]       ,["Zack","Bautista"],
        ["Mason"," Prince"]     ,["Jonah","Tanner"],
        ["Aidan"," Newman"]     ,["Gracie","Mill"],
        ["Carmen ", "Mccallum"] ,["Macsen","Snider"],
        ["Momina"," Feeney"]    ,["Rick","Vang"],
        ["Tristan ", "Dowling"] ,["David","Lamb"],
        ["Alexander", "Aguilar"],["Dru","Weston"],
        ["Kaitlin ", "Robins"]  ,["Fay","Peralta"],
        ["Yasin ", "Davila"]    ,["Giselle ","Armita"],
        ["Grace"," Baldwin"]    ,["Rafe","Perkins"],
        ["Dean"," Dudley"]      ,["Naomi","Bate"],
        ["Eduard ","Finch"]     ,["Patric","Schneider"]]


    return x



# TODO setup cooks using cooks.set* interface
# retuns a dictionary of cooks
def getCooks():# currently 6
    x ={}
    
    Gordon=cooks.makeCook()
    cooks.setFirstName(Gordon,"Gordon")
    cooks.setLastName(Gordon,"Ramsay")
    cooks.setPizzazz(Gordon,3)
    cooks.setSkillLevel(Gordon,"riceCooker",5)
    cooks.setSkillLevel(Gordon,"microwave",5)
    cooks.setSkillLevel(Gordon,"dessert",5)
    x["Gordon"]= Gordon
    
    
    Bobby=cooks.makeCook()
    cooks.setFirstName(Bobby,"Bobby")
    cooks.setLastName(Bobby,"Flay")
    x["Bobby"]= Bobby
    
    Guy=cooks.makeCook()
    cooks.setFirstName(Guy,"Guy")
    cooks.setLastName(Guy,"Fieri")
    x["Guy"]=Guy
    
    Jamie= {}
    Jamie=cooks.makeCook()
    cooks.setFirstName(Jamie,"Jamie")
    cooks.setLastName(Jamie,"Oliver")
    x["Jamie"]= Jamie
    
    Rachel= {}
    Rachel=cooks.makeCook()
    cooks.setFirstName(Rachel,"Rachel")
    cooks.setLastName(Rachel,"Ray")
    x["Rachel"]=Rachel
    
    Paula = {}
    Paula=cooks.makeCook()
    cooks.setFirstName(Paula,"Paula")
    cooks.setLastName(Paula,"Deen")
    x["Paula"]=Paula
    
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
    availableCooks = getCooks()
    townsFolk      = getTownsfolk()
    cookBook       = getCookBook()
    menu           = getMenus()
    tables         = getTables(10)
    
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
        # Check if we have a new customer the normal number should be set to 4 (<4)
        if( random.randint( 0, 10 ) < 1 ) :

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
            # add random event, like cook scratches his head
            randEvent = randCustEvent()
            print ( randEvent )
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
            hotFood=sendToKitchen(cookBook,tableOrder,availableCooks)
            print (hotFood)
    
        #wait
        print("")
        time.sleep(3)

if __name__ == "__main__":
    main()
#