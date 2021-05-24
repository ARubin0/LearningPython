#!/usr/bin/env python


if __name__ == "__main__":

# List is a collection which is ordered and changeable. Allows duplicate members.
    #print("type your birthmonth here")
#x = input()
#thisListMonth = ["january", "february", "march", "april", "may","june", "july", "august","september","october", "november","december"]

#print(thisListMonth)
#thisList2 = ["January is a month","february is a short month","march is a decent month","april is a rainy month","may is a month of allergies","june is a month","july is the fourth","august is a month of days","september is a month","october is candy","nobember is a turkey","december is expensive"]
#print (thisList2)

#thisList3 = (thisListMonth + thisList2)

#print (thisList3)
#print(thisListMonth[0],thisList2[0])


    while True: 
        thisListMonth = ["january", "february", "march", "april", "may","june", "july", "august","september","october", "november","december"]
        thisList2 = ["January is a month","february is a short month","march is a decent month","april is a rainy month","may is a month of allergies","june is a month","july is the fourth","august is a month of days","september is a month","october is candy","nobember is a turkey","december is expensive"]
        print("Enter your birthmonth:")
        x = input()  #variable x is set to what the user writes as the input 
        print( x + "s horiscope")

        if x == "january":     
          print(thisListMonth[0],thisList2[0])
        elif x == "february":     
          print(thisListMonth[1],thisList2[1])
        elif x == "march":     
          print(thisListMonth[2],thisList2[2])
        elif x == "april":
          print(thisListMonth[3],thisList2[3])
        elif x == "may":
          print(thisListMonth[4],thisList2[4])
        elif x == "june":    
          print(thisListMonth[5],thisList2[5])
        elif x == "july":  
          print(thisListMonth[6],thisList2[6])
        elif x == "august":
          print(thisListMonth[7],thisList2[7])
        elif x == "september":
          print(thisListMonth[8],thisList2[8])
        elif x == "october":
          print(thisListMonth[9],thisList2[9])
        elif x == "november":
          print(thisListMonth[10],thisList2[10])
        elif x == "december":
          print(thisListMonth[11],thisList2[11])
        elif x == "stop":
          print("stopping")
          break 
        else: 
          print ("invalid input")


             #dont forget to break or will loop forever