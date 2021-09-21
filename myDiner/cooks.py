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

#XXX CALL IN MAIN

def gordon (foodOrder,cookBook):
    for appliances, recipes in cookBook.items():
        
        #print (appliances)
        # XXX use the cookbook to get the ingredients for the order
        # XXX cook looks up order in cookbook to find CookItem 
        # XXX use the cooking implement to make the food and return 
        # XXX use the cookbook to get the ingredients for the order
        for cookItem,ingredients in recipes.items():    
            #print( cookItem,ingredients )
            #appliances, cookItem, ingredients all combinations 
            appliances, cookItem, ingredients 
            if cookItem==foodOrder:
                print ("gordon thinks to himself, now i can finish cooking this food" )
                print ("im going to use", ingredients, "in", appliances," to make a" ,cookItem)
                # XXX use the cookbook to get the ingredients for the order
            
            # x=appliances.riceCooker(["beans","meat","smallWater"],cookBook) # XXX use the cooking implement to make the food and return 
            # y=appliances.microwave(["bugs"         , "bigWater"] ,cookBook)
            # z=appliances.dessert(["icecream"]                    ,cookBook)
            
            foodPlate="brownMush"
            
            return #("finished food")?
"""    
    
    #XXX call the right appliance with the recipe. for example : 
    #    this goes here...z=appliances.riceCooker(["beans","meat","smallWater"],cookBook)
    #    the line above, cook feeds raw ingredients to appliance(s)
    
    #XXX  remember, cook needs to return food from appliance as a foodplate for the waiter 
    return foodPlate 
"""