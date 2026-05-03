import sys

input = sys.stdin.readline

cases = int(input())

for _ in range(cases):
  n = int(input())
  
  nums = list(map(int, input().split()))
  
  num_sum = sum(nums)
  
  if num_sum % 2 != 0:
    print("No")
  else:
    print("Yes")