import time, os
import threading as th
import multiprocessing as mp

NUMBERLIST = [2354, 9743, 2856, 1928, 4345, 3421]

def square_number(idx, number, results):
    pid = os.getpid()
    threadName = th.current_thread().name
    processName = mp.current_process().name
  
    #Print Starting Statement
    print(f"{pid} * {processName} * {threadName} ---> Starting....")

    #Multiply Numbers Together
    results[idx]=number*number

    #Waste time counting to a very large number ;)
    n=21880000
    while n>0:
        n -= 1

    #Print ending statement
    print(f"{pid} * {processName} * {threadName} ---> Finished. Square is: ", str(number * number))
  
if __name__=="__main__":
    
    #Start Timer
    start = time.time()

    #Create Empty Array For Results
    results = [0] * len(NUMBERLIST);

    #Calculate the Square of Each Number
    for idx, num in enumerate(NUMBERLIST):
        square_number(idx, num, results)

    #Output Sum of Squares
    print("Sum of Squares is: ", sum(results[:]))

    #Stop Timer    
    end = time.time()

    #Output Total Time
    print('Time taken in seconds -', end - start)
