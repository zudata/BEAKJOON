# 11279
import sys
import heapq
inputs = sys.stdin.readline
n = int(inputs())
heap = []
for i in range(n):
    x = int(inputs())
    x = -1 * x
    if x < 0:
        heapq.heappush(heap, x)
    elif x == 0 and len(heap) > 0:
        print(heap[0] * -1)
        heapq.heappop(heap)
    elif x == 0 and len(heap) == 0:
        print(0)

# 1927
import sys, heapq
inputs = sys.stdin.readline
n = int(inputs())
heap = []
for _ in range(n):
    cmd = int(inputs())
    if not cmd:
        if heap: print(heapq.heappop(heap))
        else: print(0)
    else: heapq.heappush(heap, cmd)