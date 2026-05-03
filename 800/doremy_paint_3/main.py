import sys
from collections import Counter
input = sys.stdin.readline

num_cases = int(input())
for _ in range(num_cases):
  n = int(input())
  nlist = list(map(int, input().split()))
  
  counts = Counter(nlist)
  distinct = list(counts.values())
  
  if len(counts) == 1:
    print("Yes")
  elif len(counts) == 2:
    v1, v2 = distinct
    
    if abs(v1 - v2) <= 1:
      print("Yes")
    else:
      print("No")
           
  else:
    print("No")