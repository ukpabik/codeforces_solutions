import sys

input = sys.stdin.readline

cases = int(input())

for _ in range(cases):
  
  points = 0
  for r in range(10):
    line = input().strip()
    
    for c in range(10):
      if line[c] == "X":
        points += min(r, c, 9-r, 9-c) + 1
  
  print(points)
      