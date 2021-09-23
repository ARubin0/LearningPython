#!/usr/bin/env python

import sys
import time
import os
import logging
import random

from appliances import dessert, microwave, riceCooker
import appliances



# gordon takes food request from customer(waiter) cooks then gives finished food( good or bad ) to waiter to bring out for customer
# Example function call; foodPlate=cooks.gordon( foodOrder,cookBook )
#   foodOrder is customer order
#   cookBook  is recipe

#XXX CALL IN MAIN

def gordon (foodOrder,cookBook):
    foodPlate="brownMush"
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
                #appliance might equal a string
                    #if the appliance equals ricecooker 
                if appliance=="riceCooker":
                    x=appliances.riceCooker(["beans","meat","smallWater"],cookBook) 
                    print(x)
                    #print ("****ricecooker*******")
                elif appliance=="microwave":
                    y=appliances.microwave(["bugs"         , "bigWater"] ,cookBook)
                    print(y)
                    #print ("*****microwave******")
                elif appliance=="dessert":
                    z=appliances.dessert(["icecream"]                    ,cookBook)
                    print (z)
                    #print ("****dessert*******")
            
    return foodPlate #("finished food")?
        
"""
    
    #XXX call the right appliance with the recipe. for example : 
    #    this goes here...z=appliances.riceCooker(["beans","meat","smallWater"],cookBook)
    #    the line above, cook feeds raw ingredients to appliance(s)
    
    #XXX  remember, cook needs to return food from appliance as a foodplate for the waiter 
    return foodPlate 
"""