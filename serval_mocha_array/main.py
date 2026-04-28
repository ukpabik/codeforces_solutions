import sys
import math

input = sys.stdin.readline

cs = int(input())
def solve():
  
  n = int(input())
  
  arr = list(map(int,input().split()))
  
  for i in range(n):
    for j in range(i+1, n):
      if math.gcd(arr[i],  arr[j]) <= 2:
        print("Yes")
        return

  print("No")

for _ in range(cs):
  solve()