#!/usr/bin/env python
"""
#% is basic comand shell 
<open cmd prompt>
% python 
>>> import temp #type name of file without the .py (extention)
>>> x=temp.getCookBook() #when calling funct add name of file otherwise wrong/wont work

"""

from appliances import riceCooker


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

cookBook=getCookBook()
for appliance, recipes in cookBook.items():
    for recipe,ingredients in recipes.items():
        print( recipe,ingredients )


def gordon (foodOrder,cookBook):
    for appliances, recipes in cookBook.items():
        print (appliances)
        for recipe,ingredients in recipes.items():
            print( recipe,ingredients )
"""
        # XXX cook looks up order in cookbook to find recipe
            for appliances, recipes in cookBook.items():
        # XXX use the cookbook to get the ingredients for the order, then
            for recipe,ingredients in recipes.items():
        # XXX use the cooking implement to make the food and return 
            in appliances.riceCooker
                if recipeIngredients == rawIngredients:
                    print ("foodplate")
        # XXX call the right appliance with the recipe. for example :  foodPlate = appliances.riceCooker(["beans","meat","smallWater"],cookBook)
            z=appliances.riceCooker(["rawRice","smallWater"     ],cookBook)
    
        # XXX  remember, cook needs to return food from appliance as a foodplate for the waiter 

"""
"""
cookBook=temp.getCookBook()
for appliance, recipes in cookBook.items():
    for recipe in recipes:
        print( recipe )






for x in temp.getCookBook():
    print (x)

***riceCooker
    microwave
    dessert***
 

for y in temp.getCookBook().items():
    print (y)



***('riceCooker', {'cookedRice': ['rawRice', 'smallWater'], 'porridge': ['rawRice', 'bigWater'], 'chili': ['beans', 'meat', 'smallWater']})
('microwave', {'bugsoup': ['bugs', 'bigWater'], 'tea': ['teaBag', 'smallWater'], 'bugs': ['bugs'], 'yesterdays special': ['teaBag', 'bugs', 'smallWater'], 'personal Pizza': ['bread', 'cheese', 'tomatoSauce']})
('dessert', {'iceCream': ['icecream'], 'chipIceCream': ['icecream', 'chips']})***

x=temp.getCookBook()
for y in x.items():
    print (y)

***('riceCooker', {'cookedRice': ['rawRice', 'smallWater'], 'porridge': ['rawRice', 'bigWater'], 'chili': ['beans', 'meat', 'smallWater']})
('microwave', {'bugsoup': ['bugs', 'bigWater'], 'tea': ['teaBag', 'smallWater'], 'bugs': ['bugs'], 'yesterdays special': ['teaBag', 'bugs', 'smallWater'], 'personal Pizza': ['bread', 'cheese', 'tomatoSauce']})
('dessert', {'iceCream': ['icecream'], 'chipIceCream': ['icecream', 'chips']})***


for cookBook,recipe in x.items():
    print (cookBook,recipe)

***riceCooker {'cookedRice': ['rawRice', 'smallWater'], 'porridge': ['rawRice', 'bigWater'], 'chili': ['beans', 'meat', 'smallWater']}
microwave {'bugsoup': ['bugs', 'bigWater'], 'tea': ['teaBag', 'smallWater'], 'bugs': ['bugs'], 'yesterdays special': ['teaBag', 'bugs', 'smallWater'], 'personal Pizza': ['bread', 'cheese', 'tomatoSauce']}
dessert {'iceCream': ['icecream'], 'chipIceCream': ['icecream', 'chips']}***



"""