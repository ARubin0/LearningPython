#!/usr/bin/env python

import sys
import time
import os
import logging
import random
#from typing import NoReturn

#from os import path

"""
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
"""

# example function call:   foodPlate = riceCooker( ["rawRice", "smallWater","bowl"], cookBook]   will return "cookedRice"
def riceCooker( rawIngredients, cookBook ):
    #print( cookBook )

    riceCookerRecipes = cookBook["riceCooker"]
    #print( riceCookerRecipes)

    # if raw ingredients don't match a "riceCooker" recipe, iiiick
    riceFoodPlate = "brownMush"
    oatFoodPlate  = "brownMush"
    chiliFoodPlate= "brownMush"
    # run through riceCookerRecipes, look for rawIngredients that match a recipe, then get the food item.
    for dish, recipeIngredients in riceCookerRecipes.items():
        print("***",dish, recipeIngredients,"***")
        if recipeIngredients == rawIngredients:
            riceFoodPlate = dish
            break
    return riceFoodPlate 


def microwave( rawIngredients, cookBook ):
    #print( cookBook )

    microwaveRecipes = cookBook["microwave"]
    #print( microwaveRecipes)

    # if raw ingredients don't match a "microwave" recipe, iiiick
    microFoodPlate = "brownMush"
    teaFoodPlate   = "brownMush"
    bugFoodPlate   = "brownMush"
    specFoodPlate  = "brownMush"
    pizzaFoodPlate = "brownMush"

    # run through riceCookerRecipes, look for rawIngredients that match a recipe, then get the food item.
    for dish, recipeIngredients in microwaveRecipes.items():
        if recipeIngredients == rawIngredients:
            microFoodPlate = dish
            break
    
    return microFoodPlate

def dessert( rawIngredients, cookBook ):
    #print( cookBook )

    dessertRecipes = cookBook["dessert"]
    #print( dessertRecipes)

    # if raw ingredients don't match a "dessert" recipe, its not "good" but not bad
    coldFoodPlate = "this isnt what the customer ordered"

    # run through riceCookerRecipes, look for rawIngredients that match a recipe, then get the food item.
    for dish, recipeIngredients in dessertRecipes.items():
        if recipeIngredients == rawIngredients:
            coldFoodPlate = dish
            chipFoodPlate = dish
            break
    
    return coldFoodPlate


def getTable():
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
"""
def dishWash(dishwasher):
#XXX this chunk needs to run only at "night" or when all of the dishes are used
    while True:
        random.randit(1,5)
        x = dish
        if x <= 2:
            print ("dishes are being washed")
            time.sleep(1)
        if x == 1:
            print ("dishes are clean and ready")
            return x
            
        """ 