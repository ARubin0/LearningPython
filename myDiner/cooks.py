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
    #use the cookbook to get the ingredients for the order
    #cook looks up order in cookbook to find CookItem 
    for appliance, recipes in cookBook.items():
        #(ricecooker, cookedRice in cookbook)
        #print (appliances)
        
        for cookItem,ingredients in recipes.items():    
            #print( cookItem,ingredients )
            #appliances, cookItem, ingredients all combinations 
            
            if cookItem==foodOrder[0]:          
                
                print ("gordon thinks to himself, now i can finish cooking this food" )
                print ("im going to use", ingredients, "in", appliance," to make a" ,cookItem)
            
                # XXX use the cooking implement to make the food and return 
                if appliance[0]:
                    x=appliance.riceCooker(["beans","meat","smallWater"],cookBook) 
                elif appliance[1]:
                    y=appliance.microwave(["bugs"         , "bigWater"] ,cookBook)
                elif appliance.dessert[2]:
                    z=appliance.dessert(["icecream"]                    ,cookBook)
            
            foodPlate="brownMush"
            
            return #("finished food")?
"""    
    
    #XXX call the right appliance with the recipe. for example : 
    #    this goes here...z=appliances.riceCooker(["beans","meat","smallWater"],cookBook)
    #    the line above, cook feeds raw ingredients to appliance(s)
    
    #XXX  remember, cook needs to return food from appliance as a foodplate for the waiter 
    return foodPlate 
"""