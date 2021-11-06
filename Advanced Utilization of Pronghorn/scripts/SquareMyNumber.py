import time, os
import random
import sys

#Start Timer
start = time.time()

#Create Empty Array For Results
number = int(sys.argv[1])

#Calculate the Square of Number
result = number * number

#Waste time counting to a very large number ;)
n=2500000
while n>0:
    n -= 1

#Stop Timer    
end = time.time()

#Print Squre of Number and Time Taken
print(f"Square is: ", str(result), " Time taken is: ", end-start)
