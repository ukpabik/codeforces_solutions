import sys
input = sys.stdin.readline

num_cases = int(input())

for _ in range(num_cases):
  n, x = map(int, input().split())
  stations = list(map(int, input().split()))

  min_val = stations[0]
  for i in range(n - 1):
    diff = stations[i + 1] - stations[i]
    min_val = max(min_val, diff)
  
  diff = (x - stations[-1]) * 2
  min_val = max(min_val, diff)
  print(min_val)