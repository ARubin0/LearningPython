#!/usr/bin/env python

# TODO
# XXX Need more townsfolk
# XXX makeCustomer function should roll the randInt for us
# XXX add random events for when there are no customers
# XXX add random events for when there are customers
# XXX add 2 cooking implement.   For example, riceCooker takes rawRice, returns cookedRice.  If input is not rawRice
# XXX add 1 cook
# XXX add ingredients + dish pairings that work on cooking implements.  e.g. ingredients: rawRice, makes: cookedRice

# XXX add days, 24 hours, Diner closes from 1AM to 6AM.  event loop is 1 tick per hour.
# XXX customers should only show up once, i.e. Bobby Smith does not have a clone
# XXX add waiters
# XXX add cooks
# XXX add cooking implements 
# XXX add tables
# XXX one waiter can serve 1 customer per hour.
# XXX check for user abort and end nicely


import signal,sys               # to check for user abort
import random
import time                     # to sleep

# Abort handler
def signal_handling(signum,frame):
    print "The Diner is closing for remodeling."
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
        if( len( customers ) > 0 ):
            serveCustomer = customers.pop(0)

        if( serveCustomer == "---" ) :
            print( "Where are my customers??" )
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

