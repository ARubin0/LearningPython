#!/usr/bin/env python

import sys
import time
import os
import logging
import random

from appliances import dessert, microwave, riceCooker
import appliances

#cooks will be similar too cookbook
# (gordon is ricecooker and attributes as the recipe names /skilled appliances)(name. skill cook proficiency.with errror %)

# gordon takes food request from customer(waiter) cooks then gives finished food( good or bad ) to waiter to bring out for customer
#   foodOrder is customer order
#   cookBook  is recipe
def gordon (foodOrder,cookBook):
    foodPlate="brownMush"
    
    #use the cookbook to get the ingredients for the order
    #cook looks up order in cookbook to find CookItem 
    for appliance, recipes in cookBook.items():
        #(ricecooker, cookedRice in cookbook)
        #print (appliances)
        
        for cookItem,ingredients in recipes.items():    
            # cookItem, ingredients all combinations 
            
            if cookItem==foodOrder[0]:
                
                print ("gordon thinks to himself, now i can finish cooking this food" )
                print ("im going to use", ingredients, "in", appliance," to make a" ,cookItem)
                
                if appliance=="riceCooker":
                    foodPlate=appliances.riceCooker(ingredients,cookBook) 
                    print("****ricecooker******",foodPlate)
                elif appliance=="microwave":
                    foodPlate=appliances.microwave(ingredients,cookBook)
                    print("****microwave******",foodPlate)
                elif appliance=="dessert":
                    foodPlate=appliances.dessert(ingredients,cookBook)
                    print ("****dessert******",foodPlate)

    return foodPlate #("finished food")


def guy (foodOrder,cookBook):
    foodPlate="brownMush"
    
    #use the cookbook to get the ingredients for the order
    #cook looks up order in cookbook to find CookItem 
    for appliance, recipes in cookBook.items():
        #(ricecooker, cookedRice in cookbook)
        #print (appliances)
        
        for cookItem,ingredients in recipes.items():    
            # cookItem, ingredients all combinations 
            
            if cookItem==foodOrder[0]:
                
                print ("guy thinks to himself, now i can finish cooking this food" )
                print ("im going to use", ingredients, "in", appliance," to make a" ,cookItem) 
                
                if appliance=="riceCooker":
                    foodPlate=appliances.riceCooker(ingredients,cookBook) 
                    print("****ricecooker******",foodPlate)
                    
                elif appliance=="microwave":
                    foodPlate=appliances.microwave(ingredients,cookBook)
                    print("****microwave******",foodPlate)
                    
                elif appliance=="dessert":
                    foodPlate=appliances.dessert(ingredients,cookBook)
                    print ("****dessert******",foodPlate)

                    
    return foodPlate #("finished food")