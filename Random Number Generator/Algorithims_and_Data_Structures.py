# -*- coding: utf-8 -*-
"""
Program Name:   Random Number Generator and Factors of 3

Writen by:      Sean Mathews

Date:           11 September 2020

Synopsis:       This will take a set of random numbers between 1 and 1 million
                and put them in an array of 10 integers. Then will factor each
                integer in the array by 3 and if it is valid true, will add 
                them to a new array. It will also output the total time it
                took in seconds the program took to complete.
"""

import time

# Import library that for random numbers
import random

# sets the current time as the start_time variable
start_time = time.time()

"""
# sets int1 variable to random int between 1 and 1 million
int1 = random.randint(1, 1000000)

# Print a concatenated string with random generated variable
print("Random int between 1 and 1M:", int1)
"""

# Create array called randomInArray.
randomIntArray = []

# Sets array length to 10 integers.
for i in range(0, 100):
    
    # Any random numbers from 0 to 1M.
    randomIntArray.append(random.randint(0, 1000000))

# Print a concatenated string of the random integers in the array
print("Random Int Array values are:\n", randomIntArray, "\n")

# Creates array called factoredArray.
factoredArray = []
        
# loads each int in the array.
for n in randomIntArray:
    
    # Checks to see if the int from the array is factorable by 3.
    if n % 3 == 0:
        
        # Add each int that was factorable by 3 to a new array.
        factoredArray.append(n)

# print a concatenated string of the factored integers in the array
print ("The factored list is:\n", factoredArray, "\n")

# prints the number of random ints added to the randomIntArray
print("# of integers in randomIntArray is:", len(randomIntArray))

# prints to console the ints that were factors of 3 into factored Array
print("# of integers in factoredArray  is:", len(factoredArray), "\n")

# sets the current time as the end_time variable
end_time = time.time()

# math magic taking the end_time and subracts the start_time
total_time = float(end_time - start_time)

# prints the math results of you total time in seconds
print ("You waited [", total_time, "] seconds")