### Correct Layout For Python Code File name is  fileName.py

# XXX  dont forget to save the result of the function x=hello()
    even if a list is set to a name. set it to anothe name for it to work 
    
    
    def example():

    e= ["1",
                "2",
                "3",       
                "4",           
                ]
    cammelExample=(random.choice(e))
    return cammelExample # return what is on the left side of the = and dont forget to import random 
    

# XXX incramenting code
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

# XXX Boolean logic… basically means and or not and combos of them.

    if( coin >= 6 and coin <= 10 )    #means
    if( (coin >= 6) and (coin <= 10) )  #which evaluates to
    if( true and true )  # which evaluates to 
    If ( true )
 

# XXX a List
    # -is a collection which is ordered and changeable. Allows duplicate members-
        ( members are words/numbers in the list [ie] Number (1),(1) or names/words [ie] (james),(james) 


#XXX CALLING A FUNCTION
    To call a function, use the function name followed by parenthesis

###Function V Function Call
 # line 30 is correct. Variable 'Coin' is being set to the call to 'getflip'.
    coin = GetFlip(HeadNum,TailNum,EdgeNum) 
    #line 32 is Wrong. variable 'coin' is being set to the  GetFlip Funciton. (which is just a function. not the call to the function)
    #coin = GetFlip 



Function  (   anything   ) #


# XXX method 1 for returning a list
def hiDad():
    x = [["a", "b"], ["c", "d"]]
    return x

# XXX KEYWORD  -- reserved words that canNOT be used as a variable name AKA statement makers(if, elif, and,return,etc)
    #XXX variables created inside functions belong to those functions only
    and can only be used inside the function it was created in UNLESS -- global -- keyword is used 
    get element from list x ... x[0] for first x[1] for seccond and so on

# XXX Most comomn function flow
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
            CB=temp.getCookBook()
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


# XXX Square Brackets
    square brackets alone make a list ; [1,2] ,[a,b]
    square brackets next to a name means a modifier gordon["FirstName"] This is not a list
                                                        ^defintion   ^word
        meaning get the value of the first name of gordon 
        a normal  non code dictionary has a word then definition 
        a python dictionary also has a word then definition 
        word: "firstName" 
        a word is a "Key" in python
        get the Definition:gordon["FirstName"]

    
# XXX DICT 
        # everything within square brackets has to evaluate to be a string
        cheese="firstName"
        gordon[cheese]      # works because cheese evaluates to become string firstname  
        gordon["firstName"] # works because string evaluates to be a string
        cheese=1            #
        gordon[cheese]      # does not work because it does not evaluate to be a string


# XXX DICT CONTINUED
    # defined x to be Guy cook 
    >>> pprint.pp (x)
    {'firstName': 'Guy',
     'lastName': 'Fieri',
     'appliances': ['::ricecooker::', '::microwave::', '::dessert::'],
     'skillLevel': {'riceCooker': 1, 'microwave': 3, 'dessert': 5},
     'pizzazz': 1}
    
    # how can i check if x is Guy Fieri???
    #  check the firstname / down the road if two cooks have the same firstname Check last name aswell
     x["firstName"]=="Guy"


# XXX Code Speaking
    #code speak : getting the entry firstName in the gordon dictionary 
    gordon["firstName"]

    # code speak : setting the first name entry in gordon, to john
    gordon["firstName"] ="john"

    # code speak : we set gordon to makeCook 
    gordon = makeCook()

    get riceCooker skillLevel of Cook
    >>> cook["skillLevel"]
    {'riceCooker': 1, 'microwave': 3, 'dessert': 5, 'appliance': 1}
    >>> cook["skillLevel"]["riceCooker"]
    1

#?IM STUCK SIMPLIFIED
    1. Write down exactly what you want to do


    2: Write down what you know


    3: Divide & Conquer: Break the problem into smaller pieces

    4. use Python Interpreter 


# XXX MODULES...
    import temp # imports temp module
    # cookbook is defined in temp. if using cookbook where imported temp as a module, as above, do this;
    temp.cookBook # cookbook is the name inside of temp. temp.cookBook is the FULL name outside of temp

    # below imports one function from myDiner and gives it the name getCooks, so myDiner.getCooks is not needed 
    from myDiner import getCooks # 
