# -*- coding: utf-8 -*-
"""
Program Name:   Slow_Sort_Random_Int.py

Writen by:      Sean Mathews

Date:           18 October 2020

Synopsis:       This will make a list of random ints and then sort them by comparing the next value in teh index and then move it to the order that it should be in.  It repeats this process until the entire list is sorted. The greated the list of values, the longer it takes to iterate through all the values.
"""

import random

stack = []


for i in range(0, 1000):
    i = (random.randint(0, 1000000))
    print ("stack value", i)
    stack.append(i)


"""
sorted_list = sorted(stack)
print (sorted_list)
"""

def slow_sort(array):

    n = len(array)

    for i in range(n):
        already_sorted = True
        
        for j in range(n - i - 1):
            
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
                print (j)
        if already_sorted:
            break
        
    return array
    

newstack = slow_sort(stack)




"""
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
"""