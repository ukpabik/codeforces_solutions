import sys

input = sys.stdin.readline

cases = int(input())

for _ in range(cases):
  n, k = list(map(int, input().split()))
  
  values = list(map(int, input().split()))
  
  if k in values:
    print("YES")
  else:
    print("NO")