#!/usr/bin/env python
if __name__ == "__main__":
#dictionary is a collection which is orderd and does not allow duplicates


    thisDict = { #curley brace defining dictionary from 7-18
"january":"January is a month",
"february": "february is a short month",
"march": "march is a decent month",
"april": "april is a rainy month",
"may": "may is a month of allergies",
"june":"june is a month",
"july": "july is the fourth",
"august": "august is a month of days",
"september":"september is a month",
"october":"october is candy",
"november": "november is a turkey",
"december":"december is expensive"} 
print("type your birthyear here ")

"""
print (thisDict["january"])
print (thisDict["february"])
print (thisDict["march"])
print (thisDict["april"])
print (thisDict["may"])
print (thisDict["june"])
print (thisDict["july"])
print (thisDict["august"])
print (thisDict["september"])
print (thisDict["october"])
print (thisDict["november"])
print (thisDict["december"])
"""
while True: 
    print("type your birthyear here ")
    x =input()

    if  x == "january":
        print(thisDict["january"])
    elif  x == "february":
        print(thisDict["february"])
    elif  x == "march":
        print(thisDict["march"])
    elif  x == "april":
        print(thisDict["april"])
    elif  x == "may":
        print(thisDict["may"])
    elif  x == "june":
        print(thisDict["june"])
    elif  x == "july":
        print(thisDict["july"])
    elif  x == "august":
        print(thisDict["august"])
    elif  x == "september":
        print(thisDict["september"])
    elif  x == "october":
        print(thisDict["october"])
    elif  x == "november":
        print(thisDict["november"])
    elif  x == "december":
        print(thisDict["december"])
    elif  x=="stop":
        print("stopping")
        break
    else: 
        print ("invalid input")