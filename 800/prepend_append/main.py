import sys

input = sys.stdin.readline

cs = int(input())
def solve():
  
  n = int(input())
  
  s = input().strip()
  start, end = 0, len(s) - 1
  
  while start < end:
    if s[start] != s[end]:
      start += 1
      end -= 1 
    else:
      break
    
  print(end - start + 1)

for _ in range(cs):
  solve()