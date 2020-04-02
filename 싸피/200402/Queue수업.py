from queue import PriorityQueue
#from queue import Queue  <--- thread safe
import heapq

import time
from collections import deque
import collections

start = time.time()
Q = [0] * 1000000
f = r = -1

for i in range(100000):
    r += 1
    Q[r] = i

while f != r:
    f += 1

print(time.time() - start)

start = time.time()
Q = collections.deque()
for i in range(100000):
    Q.append(i)
while Q:
    Q.popleft()
print(time.time() - start)

start = time.time()
Q=[]
for i in range(100000):
    Q.append(i)
while Q:
    Q.pop(0)
print(time.time() - start)