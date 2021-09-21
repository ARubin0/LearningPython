#!/usr/bin/env python

import sys
import time
import os
import logging
import random
import appliances



# gordon takes food request from customer(waiter) cooks then gives finished food( good or bad ) to waiter to bring out for customer
# Example function call; foodPlate=cooks.gordon( foodOrder,cookBook )
#   foodOrder is customer order
#   cookBook  is recipe

def gordon (foodOrder,cookBook):
    for appliances, recipes in cookBook.items():
        print (appliances)
        for recipe,ingredients in recipes.items():
            print( recipe,ingredients )

"""    
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