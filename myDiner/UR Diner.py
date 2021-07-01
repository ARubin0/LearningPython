#!/usr/bin/env python

# TODO
# XXX * Need more townsfolk √ ADDED 10 more. if more are needed.https://www.name-generator.org.uk/?i=nmkp5u5
# XXX * makeCustomer function should roll the randInt for us
# XXX * add random events for when there are no customers (its a func)
# XXX * add random events for when there are customers (its the same func, different argument)
# XXX * add 2 cooking implements.   For example, riceCooker takes rawRice, returns cookedRice.  If input is not rawRice

# XXX add 1 cook
# XXX add ingredients + dish pairings that work on cooking implements.  e.g. ingredients: rawRice, makes: cookedRice
# XXX add days, 24 hours, Diner closes from 1AM to 6AM.  event loop is 1 tick per hour.
# XXX customers should only show up once, i.e. Bobby Smith does not have a clone
# XXX add waiters √   Guy Fieri / Anthony Bourdain
# XXX add cooks √ Gordon Ramsay
# XXX add cooking implements √ stovetop and microwave
# XXX add tables √ 1 / 2
# XXX one waiter can serve 1 customer per hour.


import signal,sys               # to check for user abort
import random
import time                     # to sleep

# Abort handler
def signal_handling(signum,frame):
    print 
    "The Diner is closing for remodeling."
    sys.exit()

signal.signal(signal.SIGINT,signal_handling)


# Our first customer function just returns the first name of the customer.
def makeCustomer( firstName, lastName ):
    return firstName



# The main event loop that drives myDiner.
def main():

    print( "Alfonso's Diner is open for business!" )

    townsFolk = [ ["Sally", "Jean"],
                  ["Billy", "Rae"],
                  ["Samantha", "Johnson"],
                  ["Jessica", "Wilson"],
                  ["Ashley", "Williams"],
                  ["Amber", "Moore"],
                  ["Albert", "Hodge"],
                  ["Benjamin", "Nash"],
                  ["Samuel", "White"],
                  ["James", "Torres"],
                  ["Megan", "Rodriguez"],
                  ["Lucky", "Miller"],
                  ["Georgia", "Brown"],
                  ["Charlotte", "Smith"],
                  ["George", "Michael"],
                  ["Carlos", "Santana"],
                  ["Goob", "Banner"],
                  ["Zack", "Felt"],
                  ["Bobby", "Smith"],
                  ["Sammi", "Jones"],
                  ]

    # init customers with 2 random people
    aCust     = random.randint(0, len( townsFolk ) - 1)
    firstCust = makeCustomer( townsFolk[aCust][0], townsFolk[aCust][1] )

    aCust   = random.randint(0, len( townsFolk ) - 1)
    secCust = makeCustomer( townsFolk[aCust][0], townsFolk[aCust][1] ) 

    customers = [ firstCust, secCust ]


    # Event loop.  The diner is always open.. loop forever
    while True:

        # Check if we have a new customer
        if( random.randint( 0, 10 ) < 3 ) :
            aCust   = random.randint(0, len( townsFolk ) - 1)
            newCust = makeCustomer( townsFolk[aCust][0], townsFolk[aCust][1] )
            print( newCust + " walks in." )
            print( "Hi " + newCust + ".  Be right with you." )
            customers.append( newCust )

        serveCustomer = "---"
        # Serve next customer in line, if there is one
        if( len( customers ) > 0 ): ###does this 0 get changed or does another function get added with randint
            serveCustomer = customers.pop(0)

        elif( serveCustomer == "---" ) == 1:
            print( "Where are my customers??" )

        elif( serveCustomer == "---" )== 2 :
            print( "a mouse scurries across the flo0r" )

        elif( serveCustomer == "---" ) == 3:
            print( " the lights flicker" )

        elif( serveCustomer == "---" ) == 4:
            print( "a car passes by the diner" )

        elif( serveCustomer == "---" ) == 5:
            print( "a car speeds by the diner" )

        elif( serveCustomer == "---" ) == 6:
            print( "somebody sneezes" )

        elif( serveCustomer == "---" ) == 7:
            print( "Gordon scratches his head" )

        elif( serveCustomer == "---" ) == 8:
            print( "somebody sneezes" )
            
        elif( serveCustomer == "---" ) == 9:
            print( "a cold wind passes bye" )
        

            # XXX add random event, like cook scratches his head
        else :
            # XXX Take an order based on cooking implements.
            print( "What can I get for you " + serveCustomer )
            
            #     For example, customer wants cooked rice
            order = "bugs"
            print( "Eeeew, " + serveCustomer + ", you want bugs again??!!" )

            # XXX place order to cook..  For example, if customer wants cookedRice, and we have rice cooker, tell cook cookedRice

            # XXX deliver food from cook. 

            # XXX get customer feedback
            
        # Wait for us slow humans
        print("" )
        time.sleep(5)

        
        
if __name__ == "__main__":
    main()