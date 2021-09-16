


#XXX definitions/chunks taken out of myDiner for later use

#MENU
#TABLE CLEANER
#TABLE
#Waiter 1/2
#waiter 2/2
#food
#food feedback
#deliver food from cook






""" XXX MENU
#waiter brings one of two menues to customer MENU 2/2
def getVegMenu():
    options = ["","Bugsoup","tea"]
    return options
"""
"""XXX TABLE CLEANER
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

XXX TABLE
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


XXX Waiter 1/2
def waiter(Guy,Anthony):
    random.randit(1,2)
    print("Blank Waiter will seat you now at a table")
"""
"""
# XXX deliver food from cook. XXX Waiter 2/2
def tableOne():
    print("TABLE FILLER")

def tableTwo():
    print("TABLE FILLER")

    if waiter ( tableOne ):
        print ("here is BLANK food for" )+ (tableOne)

    if waiter ( tableTwo ):
        print ("here is BLANK food for" )+ (tableTwo)
"""
""" XXX Food 
def brownMush ():
    print ("BAD food")

def foodPlate ():
    print ("GOOD food")

def feedBack(): XXX food Feedback

    #Get Random Number 
    eventRandom = random.randint(0,20)

    if    ( brownMush ) >=  10:
        print ("this is disgusting get me the cook")
    elif  ( brownMush )   ==  9:
        print("this needed salt")
    elif  ( foodPlate ) ==  2:
        print ("this was the best food ive had in a while")
    elif  ( foodPlate ) ==  1:
        print("this needed salt") #add salt and pepper shaker when objects are added?
    elif  ( foodPlate ) ==  3:
        print("this was OK")
    elif  ( foodPlate ) ==  4:
        print("this has WAY too much salt i need to get a replacement")


    
# XXX deliver food from cook. 
def tableOne():
    print("TABLE FILLER")

def tableTwo():
    print("TABLE FILLER")
    

    if waiter ( tableOne ):
        print ("here is BLANK food for" )+ (tableOne)

    if waiter ( tableTwo ):
        print ("here is BLANK food for" )+ (tableTwo)
"""




#XXX WORKING CODE TAKEN OUT OF MYDINER FOR BETTER/OTHER CODE
#XXX Drinkmenu 
def getDrinkMenu(): 

    drink=[ "oldFashoned",      "margarita",   "martini",       
            "mojito",           "whiskySour",  "darkandstormy",
            "bloodyMary",       "guinness",    "heineken",       
            "blueMoon",         "miller",      "millerLight",
            "coke",             "pepsi",       "sprite",         
            "creamSoda",        "mountainDew", "rootBeer"]
    drinksOnTap = []
    for x in range(9):
        print("we  have " + random.choice(drink))
        drinksOnTap.append(random.choice(drink))
    return drinksOnTap
#waiter brings one of two menues to customer MENU 1/2 is getMenu 2/2 is getVegMenu

def getMenu():
    options = ["cookedRice","porridge","chili","bugs","yesterdays special"]
    return options


def pickFromMenu( anyMenu ):
    print ("this is the menu, what would you like?")
    return (random.choice(anyMenu))

#customer chooses from drink menu

def pickFromDrinkMenu( anyDrinkMenu ):
    print ("this is the drink menu, what would you like?")
    print(anyDrinkMenu)
    return(random.choice(anyDrinkMenu))




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
    
    singleBigTable ["annoyinglybigGroupOfPeople"]    = ["tableFive","tableSix","tableSeven","tableEight" , 
                                                        "chairNine","chairTen","chairEleven","chairTwelve",
                                                        "chairThirteen","chairFourteen","chairFifteen"
                                                        ,"chairSixteen","chairSeventeen","chairEighteen"]
    
    

    seating ={}
    seating["table"] = deuce
    seating["a bigger table"]  = biggerTables
    seating["a biggest table"]= singleBigTable
    