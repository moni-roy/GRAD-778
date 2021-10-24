import time, os
import threading as th
import multiprocessing as mp
import random

#Create 18 random numbers
NUMBEROFNUMBERS = 8

def square_number(idx, number, results):
    pid = os.getpid()
    threadName = th.current_thread().name
    processName = mp.current_process().name
  
    #Print Starting Statement
    print(f"{pid} * {processName} * {threadName} ---> Starting....")

    #Multiply Numbers Together
    results[idx]=number*number

    #Waste time counting to a very large number ;)
    n=5000000
    while n>0:
        n -= 1

    #Print ending statement
    print(f"{pid} * {processName} * {threadName} ---> Finished. Square is: ", str(number * number))
  
if __name__=="__main__":
    
    #Start Timer
    start = time.time()

    #Numebr List To Proces
    NUMBERLIST = []

    #Create random number to process
    for i in range(0,NUMBEROFNUMBERS):
        n = random.randint(1,10)
        NUMBERLIST.append(n)


    #Store details of each job ready to run
    jobs = []

    #Create Empty Array For Results
    results = mp.Array('i', len(NUMBERLIST))

    #Calculate the Square of Each Number
    for idx, num in enumerate(NUMBERLIST):
        p = mp.Process(target=square_number, args=(idx, num, results))
        p.start()
        jobs.append(p)
        
    #Wait for all processes to complete
    for p in jobs:
        p.join()  

    #Output Sum of Squares
    print("Sum of Squares is: ", sum(results[:]))

    #Stop Timer 
    end = time.time()

    #Output Total Time
    print('Time taken in seconds -', end - start)
