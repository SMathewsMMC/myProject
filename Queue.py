# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:44:45 2020

@author: Sean
"""
import random

class Q:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Q()

for i in range(0, 10):
    i = (random.randint(0, 1000000))
    print ("stack value", i)

    q.enqueue(0)
    q.size()

print(q.size())
print(q.isEmpty())


for i in range(0,10):
    q.dequeue()
    print ("revStack value", i)

print(q.size())
print(q.isEmpty())

"""
for i in list(q):
    print(i, end=" ")
print("\nSize of the queue:")
print(q.qsize())
"""