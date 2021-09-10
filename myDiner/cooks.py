#!/usr/bin/env python

import sys
import time
import os
import logging
import random
import appliances

"""
    #examples of how to call appliances
    #variable z is being set to the call of appliances.ricecooker with arguments of (list) and cookbook
    z=appliances.riceCooker(["rawRice","smallWater"     ],cookBook)
    z=appliances.riceCooker(["beans","meat","smallWater"],cookBook)
    z=appliances.riceCooker(["rawRice","bigWater"       ],cookBook)
    #XXX microwave saved item functions
    y=appliances.microwave(["bugs","bigWater"              ],cookBook)
    y=appliances.microwave(["teaBag","smallWater"          ],cookBook)
    y=appliances.microwave(["bugs"                         ],cookBook)
    y=appliances.microwave(["teaBag","bugs","smallWater"   ],cookBook)
    y=appliances.microwave(["bread","cheese","tomatoSauce" ],cookBook)
    #XXX dessert not in appliances but doing this anyway for later incase of dessert code put in later
        #Now in appliances so "wrong icecream" can be made and sent out 
    w=appliances.dessert(["icecream"],cookBook)
    w=appliances.dessert(["icecream","chips"],cookBook)
    #print(z, "++++")
"""
"""
    for dish, recipeIngredients in riceCookerRecipes.items():
        print("***",dish, recipeIngredients,"***")
        if recipeIngredients == rawIngredients:
            riceFoodPlate = dish
            break
"""
    #XXX != is opposite of == 

# gordon takes food request from customer(waiter) cooks then gives finished food( good or bad ) to waiter to bring out for customer
# Example function call; foodPlate=cooks.gordon( foodOrder,cookBook )
#   foodOrder is customer order
#   cookBook  is recipe
"""
def gordon( foodOrder, cookBook ):
    #print( cookBook )
    for dish in cookBook.items():
        if foodOrder == :
            print("ready for the waiter")
        else: foodOrder !=
            print("iik...send it out to the customer anyway")
            
    
    # XXX cook looks up order in cookbook to find recipe
    # XXX use the cookbook to get the ingredients for the order, then
    # XXX use the cooking implement to make the food and return 
    
    foodPlate="brownMush"
    
    #XXX call the right appliance with the recipe. for example : 
    #    this goes here...z=appliances.riceCooker(["beans","meat","smallWater"],cookBook)
    #    the line above, cook feeds raw ingredients to appliance(s)
    
    #XXX  remember, cook needs to return food from appliance as a foodplate for the waiter 
    return foodPlate 
"""
def gordon (foodOrder,cookBook):
    for appliances, recipes in cookBook.items():
        print (appliances)
        for recipe,ingredients in recipes.items():
            print( recipe,ingredients )

"""
def gordon (foodOrder,cookBook):
    print(cookBook.items())
"""