#!/usr/bin/env python

import sys
import time
import os
import logging
import random

# TODO XXX move to config later
RICE_COOKER_BREAK_RATE=.05 #5%


"""
#XXX TODO
i want to
        “break” an appliance so it doesn’t work for a IE, return brown mush always
            later, remove appliance from list of appliances
        randomly break the appliance then
                “set” period of time when a
                wrong recipe
                or a random time happens.

"""
# example function call:   foodPlate = riceCooker( ["rawRice", "smallWater","bowl"], cookBook]   will return "cookedRice"
def riceCooker( rawIngredients, cookBook ):
    #print( cookBook )

    riceCookerRecipes = cookBook["riceCooker"]
    #print( riceCookerRecipes)

    # if raw ingredients don't match a "riceCooker" recipe, iiiick
    foodPlate= "brownMush"
    # run through riceCookerRecipes, look for rawIngredients that match a recipe, then get the food item.
    for dish, recipeIngredients in riceCookerRecipes.items():
        print("***",dish, recipeIngredients,"***")
        
        if recipeIngredients == rawIngredients:
            foodPlate = dish    
            # XXX change this to use RC_break_rate             
            badFood=random.randint(0,1) 
            if badFood == 0:
                print ("--------------------------------------------goodfood-")
            elif badFood == 1:            
                foodPlate = "brownMush"
                print ("-badfoo000000000000000000000000000000000000000000000000000000000000d-")
            break
    return foodPlate 


def microwave( rawIngredients, cookBook ):
    #print( cookBook )

    microwaveRecipes = cookBook["microwave"]
    #print( microwaveRecipes)

    # if raw ingredients don't match a "microwave" recipe, iiiick
    foodPlate = "brownMush"

    # run through microwaverecipes, look for rawIngredients that match a recipe, then get the food item.
    for dish, recipeIngredients in microwaveRecipes.items():
        if recipeIngredients == rawIngredients:
            foodPlate = dish
            break
    
    return foodPlate

def dessert( rawIngredients, cookBook ):
    #print( cookBook )

    dessertRecipes = cookBook["dessert"]
    #print( dessertRecipes)



    # run through riceCookerRecipes, look for rawIngredients that match a recipe, then get the food item.
    for dish, recipeIngredients in dessertRecipes.items():
        if recipeIngredients == rawIngredients:
            foodPlate = dish

            break
    
    return foodPlate





"""
def dishWash(dishwasher):
#XXX this chunk needs to run only at "night" or when all of the dishes are used

""" 