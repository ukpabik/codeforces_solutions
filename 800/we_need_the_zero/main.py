import sys

input = sys.stdin.readline

cs = int(input())


def solve():
  n = int(input())
  nums = list(map(int, input().split()))
  
  xor_sum = 0
  
  for val in nums:
    xor_sum ^= val

  if len(nums) % 2 == 0:
    print(xor_sum) if xor_sum == 0 else print(-1)
  else:
    print(xor_sum)

for _ in range(cs):
  solve()