# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:04:40 2020

@author: Sean

This is a Timer for Algorythims and Data Structure class

This is a Timer that allows you to interact with to start
 and then interact with a second time to stop.
 
Will then take the start and end times and find the difference
 resulting in the total time that the program was running.
"""

import time

# pauses the app until you interact to start the next line code
start = input("[Press enter to start the timer]")

# sets the current time as the start_time variable
start_time = time.time()

# pauses the app until you interact to start the next line of code
stop = input("[Press enter to stop the timer]")

# sets the current time as the end_time variable
end_time = time.time()

# math magic taking the end_time and subracts the start_time
total_time = int(end_time - start_time)

# prints the math results of you total time in seconds
print ("You waited [", total_time, "] seconds")