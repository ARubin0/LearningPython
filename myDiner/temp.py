#!/usr/bin/env python
"""
#% is basic comand shell 
<open cmd prompt>
% python 
>>> import temp #type name of file without the .py (extention)
>>> x=temp.getCookBook() #when calling funct add name of file otherwise wrong/wont work

"""
import pprint



from cooks import gordon, guy



    
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
"""
def kitchenCooks():
    gordon={}
    #gordon# gets gordon object
    gordon["firstName"]"# returns "gordon"
    gordon["lastName"]# returns "Ramsay"
    gordon["appliances"]# returns list of appliances gordon can cook with
    gordon["skillLevel"]# returns a Dictionary with numbers and appliances from 1-10 indicating cooking errors % wise
    gordon["skillLevel"]["riceCooker"]# returns a number from the above dictionary
    gordon["pizzazz"]# returns a number from 1-10 on if the food is super great or normal

    getOneCook= {}
    getOneCook =["Gordon"]
    getOneCook =["temp1"]
    return getOneCook
    """
"""
def kitchenCooks():
    applianceSkills={}
    applianceSkills["riceCooker"]= 1
    applianceSkills["microwave"] = 3
    applianceSkills["dessert"]   = 5
    
    gordon={}
    #gordon=getACook("Ramsay")# gets gordon object
    gordon["firstName"] ="Gordon"# returns "gordon"
    gordon["lastName"]  ="Ramsay"# returns "Ramsay"
    gordon["appliances"]= ["ricecooker","microwave","dessert"]# returns list of appliances gordon can cook with
    gordon["skillLevel"] = applianceSkills # returns a Dictionary with numbers and appliances from 1-10 indicating cooking errors % wise
    gordon["pizzazz"] = 6 #  returns a number from 1-10 on if the food is super great or normal
    #pprint.pp(gordon)
   

    gordon={}
    #gordon# gets gordon object
    gordon["firstName"]"# returns "gordon"
    gordon["lastName"]# returns "Ramsay"
    gordon["appliances"]# returns list of appliances gordon can cook with
    gordon["skillLevel"]# returns a Dictionary with numbers and appliances from 1-10 indicating cooking errors % wise
    gordon["skillLevel"]["riceCooker"]# returns a number from the above dictionary
    gordon["pizzazz"]# returns a number from 1-10 on if the food is super great or normal
    return guy,gordon


#what Cooks could look like when similar to the cookBook
def inStockCooks():#tempname 
    Gordon = {}
    Gordon["Skilled in using ricecooker"] = ["Percent of errors cooking and making mush 5% of 100%", "percent of Errors with equipment 9% of 100%"]
 
    
    Guy  = {}
    Guy["skillled in"]            = ["Cook Errors % of % ", "Equipment Errors % of %"]

    otherCook  = {}
    otherCook["ok with"]             = ["Cook Error % of % , Equipment Error % of % "]

    freeCooks ={}
    freeCooks["Gordon"]      = Gordon
    freeCooks["Guy"]         = Guy
    freeCooks["otherCook"]   = otherCook
    return freeCooks
"""

