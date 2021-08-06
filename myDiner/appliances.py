#!/usr/bin/env python

import sys
import time
import os
import logging
import random

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
# Give good raw ingredients, get good food back.
# example function call:   foodPlate = riceCooker( ["rawRice", "smallWater","bowl"], cookBook]   will return "cookedRice"
def riceCooker( rawIngredients, cookBook ):
    #print( cookBook )

    riceCookerRecipes = cookBook["riceCooker"]
    #print( riceCookerRecipes)

    # if raw ingredients don't match a "riceCooker" recipe, iiiick
    foodPlate = "brownMush"

    # run through riceCookerRecipes, look for rawIngredients that match a recipe, then get the food item.
    for dish, recipeIngredients in riceCookerRecipes.items():
        if recipeIngredients == rawIngredients:
            foodPlate = dish
            break
   
    return foodPlate, print("ricecooker printing test from appliances module")


def microwave( rawIngredients, cookBook ):
    #print( cookBook )

    microwaveRecipes = cookBook["microwave"]
    #print( microwaveRecipes)

    # if raw ingredients don't match a "microwave" recipe, iiiick
    foodPlate = "brownMush"

    # run through riceCookerRecipes, look for rawIngredients that match a recipe, then get the food item.
    for dish, recipeIngredients in microwaveRecipes.items():
        if recipeIngredients == rawIngredients:
            foodPlate = dish
            break
   
    return foodPlate

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