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