# -*- coding: utf-8 -*-
"""
Program Name:   Stack.py

Writen by:      Sean Mathews

Date:           11 October 2020

Synopsis:       This program will create a Queue with varibles, and display them as they are added. It will then give you the total in the queue.  It will also verify that the queue is not empty before deQueueing and then repeat the check the number of varialbes in the Queue and test that its empty.
"""

import random

class Q:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(10,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Q()

for i in range(0, 10):
    i = (random.randint(0, 1000000))
    print ("stack value", i)
    q.enqueue(i)
    q.size()

print(q.size())
print(q.isEmpty())

for i in range(0,10):
    q.dequeue()
    print ("revStack value", i)

print(q.size())
print(q.isEmpty())

for i in list(q):
    print(i, end=" ")
print("\nSize of the queue:")
print(q.qsize())


