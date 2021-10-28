#!/usr/bin/env python

import sys
import time
import os
import logging
import random

from myDiner import getCooks

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

# 

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
                    

# change TheCOOks int the IF STATEment
# theCooks takes food request from customer(stoKitchen) - then returns finished food( good or bad )
# foodOrder is pickFromMenu aFOod+aDrink ("cookedRice","Coke")
# cookBook  is recipes                   {{'riceCooker': { 'cookedRice': ["rawRice", "smallWater"] },... }
#* availCooks is the dictionary of cooks with the skill level *AKA MakeCook* 
def theCooks (foodOrder,cookBook,cook):
    foodPlate="brownMush"
    #use the cookbook to get the ingredients for the order
    #cook looks up order in cookbook to find CookItem 
    for appliance, recipes in cookBook.items():
        #(ricecooker, cookedRice in cookbook)
        #print (appliances)
        
        for cookItem,ingredients in recipes.items():    
            # cookItem, ingredients all combinations 
            
            if cookItem==foodOrder[0]:
                if( cook["firstName"] =="Gordon" ): 
                    foodPlate=theCooks (foodOrder,cookBook,cook)
                    
                if( cook["firstName"] == "Guy" ): 
                    foodPlate=theCooks (foodOrder,cookBook,cook)
                    
                if( cook["firstName"] =="Paula" ): 
                    foodPlate=theCooks (foodOrder,cookBook,cook)
                    
                if(cook["firstName"] =="Jamie" ): 
                    foodPlate=theCooks (foodOrder,cookBook,cook)
                    
                if( cook["firstName"] =="Rachel" ): 
                    foodPlate=theCooks (foodOrder,cookBook,cook)
                    
                if( cook["firstName"]=="Bobby" ): 
                    foodPlate=theCooks (foodOrder,cookBook,cook)
                    
                    #print statements need to be seperate from the if(cook) statements as to allow them to work for each one.
                print (cook["firstName"]," thinks to themselves, now i can finish cooking this food" ) # *cook["firstName"] will not work find another way to call specific cook
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
    print("*******************WORKING*****************")
    


#1 is worst 10 is best
def makeCook():
    applianceSkills={}
    applianceSkills["riceCooker"]= 3
    applianceSkills["microwave"] = 6
    applianceSkills["dessert"]   = 8
    
    aCook={}# to be changed later
    #gordon=getACook("Ramsay")# gets gordon object
    aCook["firstName"] ="aCook"# returns "gordon"
    aCook["lastName"]  ="aCook"# returns "Ramsay"
    aCook["appliances"]= ["::ricecooker::","::microwave::","::dessert::"]# returns list of appliances gordon can cook with
    aCook["skillLevel"] = applianceSkills # returns a Dictionary with numbers and appliances from 1-10 indicating cooking errors % wise
    aCook["pizzazz"] = 1 #  returns a number from 1-10 on if the food is super great or normal
    #pprint.pp(aCook)
    return aCook


def setFirstName(aCook,aName):
    aCook["firstName"] = aName
    return


def setLastName(aCook,lName):
    aCook["lastName"] = lName
    return

# cook is makeCook() / ricecooker(appliance)/ pizzazz number 
# cooks.setSkilllevel(x["Ramsay"],"riceCooker",7 ) 
# XXX TODO fix appliance if not in appliance to not do anything and return -1...or  Assert instead
def setSkillLevel(cook,appliance,num):
    cook["skillLevel"][appliance]=num
    return  


def setPizzazz(aCook,num):
    # code speak : setting the pizzazz entry in aCook, to num
    aCook["pizzazz"]=num
    return
