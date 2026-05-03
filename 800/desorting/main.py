import sys

input = sys.stdin.readline

cases = int(input())

for _ in range(cases):
  n = int(input())
  nums = list(map(int, input().split()))
  

  is_sorted = True
  min_diff = float('inf')
  for i in range(n - 1):
    if nums[i+1] < nums[i]:
      is_sorted = False
    
    min_diff = min(min_diff, nums[i+1] - nums[i])
      
  if not is_sorted:
    print(0)
  else:
    print((min_diff // 2) + 1)