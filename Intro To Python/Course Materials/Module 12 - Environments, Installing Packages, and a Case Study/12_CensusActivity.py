# -*- coding: utf-8 -*-
"""
Census Activity
"""

# This module requires finding, installing, and loading a package that is 
# not included in the original download of the Anaconda Distribution
# By the time you start working on this activity, you'll have set up two new
# environments, each of which should have the census package installed,
# along with matplotlib. You also installed Spyder for each envionrment.

pip install census

from census import Census

Washoe = '031'

# This is my US Census API key
# You can get your own and replace in the code by going here and filling out
# this simple form: https://api.census.gov/data/key_signup.html
c = Census("7e8401ce249220dcba1ef497a3903ced266c772f")

#Question - what does the 'E' stand for in the table name
WashoeTractBike = c.acs.state_county_tract('B08006_014E', 32, Washoe, Census.ALL)
WashoeTractWalk = c.acs.state_county_tract('B08006_015E', 32, Washoe, Census.ALL)

# These data are just a sample of what can be extracted from census data
# for full documentation and look-up values, go here:
# https://api.census.gov/data.html

def WalkTotalByTract(walkdata):
    WashoeWalk = []
    for i in walkdata:
        z = list(i.items())
        WalkByTract = z[0][1]
        WashoeWalk.append(WalkByTract)
    return WashoeWalk

def BikeTotalByTract(bikedata):
    WashoeBike = []
    for i in bikedata:
        z = list(i.items())
        BikeByTract = z[0][1]
        WashoeBike.append(BikeByTract)
    return WashoeBike

Walk=WalkTotalByTract(WashoeTractWalk)
Bike=BikeTotalByTract(WashoeTractBike)

print ("The total sum (by tract) of those who walk to work in Washoe County is:", sum(Walk))
print ("The total sum (by tract) of those who bike to work in Washoe County is:", sum(Bike))

import matplotlib.pyplot as plt

n, bins, patches = plt.hist(Walk,10,density=0,facecolor='blue',alpha=0.75)
plt.xlabel('# Commuters')
plt.ylabel('Count - Census Tracts')
plt.title('Frequency Distribution of Commuters')
plt.grid(True)





    
    
