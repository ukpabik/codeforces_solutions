import sys

input = sys.stdin.readline

cases = int(input())

for _ in range(cases):
  x, k = list(map(int, input().split()))
  
  if x % k != 0:
    print(1)
    print(x)
  else:
    print(2)
    print(f"{x - 1} {1}")