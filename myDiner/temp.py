#!/usr/bin/env python
"""
#% is basic comand shell 
<open cmd prompt>
% python 
>>> import temp #type name of file without the .py (extention)
>>> x=temp.getCookBook() #when calling funct add name of file otherwise wrong/wont work

"""
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



for x in temp.getCookBook():
    print (x)
        
        
for y in temp.getCookBook().items():
    print (y)

x=temp.getCookBook()
for y in x.items():
    print (y)


for cookBook,recipe in x.items():
    print (cookBook,recipe)