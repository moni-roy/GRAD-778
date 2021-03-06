# -*- coding: utf-8 -*-
"""
Looping Examples
Intro to Python Workshop
"""

## Iteration 1 - Iconic lyrics

n = 5
while n > 0:
    print ("Hello "*3)
    print ("How low")
print ("Entertain us!")

## Iteration 2 - Iconic lyrics

n = 0
while n > 0:
    print ("Hello"*3)
    print ("How low")
print ("Entertain us!")

# Using Breaks in Loops - Evaluating User Input
while True:
    line = input('>Enter something: ')
    if line == 'all done':
        break
    print (line)
print ('All Done!')


# Definite Loop - Basic/Numeric
# The 'i' character is called an iteration variable #
# It "iterates" through a sequence - an ordered set #
# Iteration variable moves through ALL values in that sequence#

NVPopulations2017 = [54745,24230,2204079,48309,52649,850,1961,16826,5693,5223,54122,4457,44202,6508,4006,460587,9592]
for i in NVPopulations2017:
    print (i)
print ("That's Nevada!")

# Definite Loop - Basic/Numeric
NVcounties = " Washoe, Clark, Lyon, Carson City, Pershing, Douglas, White Pine, Nye, Humboldt, Lincoln, Esmeralda, Mineral, Elko, Storey, Eureka, Churchill, Lander"
NVList = NVcounties.split(",")
NVList.sort()
for i in NVList:
    x = i.strip()
    print (x,"County")
    # What do we do about Carson City?? #
print ("That's Nevada!")

# Evaluating Values from an ordered set
# Find the largest population value! Looking at you, Vegas...#
largest_pop = -99
print ('Start', largest_pop)
for i in NVPopulations2017:
    if i > largest_pop:
        largest_pop = i
    print (largest_pop, i)
print ('End', largest_pop)

# Setting a counter #
county_count = 0
print ('Start the count!')
for i in NVPopulations2017:
    county_count = county_count + 1
    print (county_count, i)
print ("It's over!", county_count)

# Setting a counter and calculating incremental sums#
state_pop = 0
print ('Start the tabulating!')
for i in NVPopulations2017:
    state_pop = state_pop + i
    print (i, state_pop)
print ("It's over! Nevada's population is...", state_pop)

# To find the smallest number, run this code, and then edit to get meaningful answer #
smallest_pop = 300000000
print ('Start the tabulating!')
for i in NVPopulations2017:
    if i < smallest_pop:
        smallest_pop = i
    print (smallest_pop, i)
print ('End', smallest_pop)