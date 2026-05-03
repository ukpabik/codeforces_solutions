import sys

input = sys.stdin.readline

num_cases = int(input())

for _ in range(num_cases):
  n,m = list(map(int, input().split()))

  x = input().strip()
  s = input().strip()
  
  found = False
  ops = 0
  for _ in range(7):
    if s in x:
      found = True
      break
    x += x
    ops += 1
  if found:
    print(ops)
  else:
    print(-1)