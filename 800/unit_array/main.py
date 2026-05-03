import sys

input = sys.stdin.readline

cases = int(input())

for _ in range(cases):
  n = int(input())
  
  nums = list(map(int, input().split())) 

  neg = nums.count(-1)
  pos = nums.count(1)

  ans = 0 
  
  while neg > pos:
    pos += 1
    neg -= 1
    ans += 1
  
  if neg % 2 != 0:
    ans += 1
  
  print(ans)