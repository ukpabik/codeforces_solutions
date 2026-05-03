import sys

input = sys.stdin.readline

cs = int(input())

def solve():
  """
  conditions:

  common prefix length of p and q == a
  common suffix length of p and q == b
  
  p and q length == n
  
  [1,2,3,4]
  
  
  n - (a + b) > 1

  a=2, b=1
  
  
  [1,2,3,4]
  [1,2,4,3]
  n - (2+1) = 4 - 3 = 1. 

  NOT POSSIBLE
  """
  n,a,b = list(map(int, input().split()))
  
  leftover = n - (a + b)
  
  if leftover > 1 or (n == a == b):
    print("Yes")
  else:
    print("No")
  
  pass

for _ in range(cs):
  solve()