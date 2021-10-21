# -*- coding: utf-8 -*-
"""
Conditional Statements and Flow Control
Intro to Python Workshop
"""
# Comparison Operators
# We Boolean Expressions to help control flow
# In Python, here are you options use:
# <  Less than
# <= Less than or Equal to
# == Equal to (remember, '=' is used for assignment)
# >= Greater than or Equal to
# > Greater than
# != Not equal

# We often combine these with conditional statements
# These are based on one-way, two-way, and multi-way decisions

# if, else, and elif are used to operationalize these
# if you have two choices - use if/else

### Else ###
# in Python, 'else' is a bit of a 'catch all' for when condition is not met,
# but must be preceded by an 'if' test.  And can only be called once

## Elif ##
# shorthand for 'else if'. Used when choices > 2.  These are handy: they check
# if multiple conditions are true and executes a block of code once one of the
# conditions evaluates to true. And, you can call as many of these as you want

# Simple Flow Control
x = input('Enter your favorite number:')
if float(x) < 5:
    print ('Go bigger or go home')
elif float(x) < 7:
    print ('Good job!')
elif float(x) < 9:
    print ('Getting better')
else:
    print ('In double digits, nicely done')
    
#########
# Back to our example from previous section
# Definite Loop - Basic/Numeric
NVcounties = " Washoe, Clark, Lyon, Carson City, Pershing, Douglas, White Pine, Nye, Humboldt, Lincoln, Esmeralda, Mineral, Elko, Storey, Eureka, Churchill, Lander"
NVList = NVcounties.split(",")
NVList.sort()
for i in NVList:
    x = i.strip()
        # Recall the previous module, regarding the Carson City issue
    if i.find('City')== -1:
        print (x, 'County')
    else:
        print (x)
print ("That's Nevada!")

###########







