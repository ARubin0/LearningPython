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
    #foodPlate needs to be set as x,y, and z but cant print all at the same time
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
                    foodPlate=appliances.riceCooker(ingredients,cookBook) 
                    print("****ricecooker******",foodPlate)


                elif appliance=="microwave":
                    foodPlate=appliances.microwave(ingredients,cookBook)
                    print("****microwave******",foodPlate)

                elif appliance=="dessert":
                    foodPlate=appliances.dessert(ingredients,cookBook)
                    print ("****dessert******",foodPlate)
                    
                    
    return foodPlate #("finished food")?