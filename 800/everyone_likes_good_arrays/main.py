import sys

input = sys.stdin.readline

cs = int(input())


def solve():
  n = int(input())
  nums = list(map(int, input().split()))
  
  """
  good if adjacent elements all have different parity (n % 2 == 0 and n % 2 != 0)

  even odd even odd.
  or
  odd even odd even.
  
  [1, 7, 11, 2, 13]
  
  [7, 11, 2, 13]
  
  [77, 2, 13]
  
  odd * even = even
  odd * odd = odd
  even * even = even
  
  
  [1, 1, 1, 2, 2, 3]
  [1, 1, 2, 2, 3]
  [1, 2, 2, 3]
  [1, 4, 3]
  
  
  
  curr
  
  if curr % 2 == nums[i] % 2:
    curr *= nums[i]
  else:
    curr = nums[i]
    
  """

  curr = nums[0]
  ops = 0
  
  for num in nums[1:]:
    if curr % 2 == num % 2:
      curr *= num
      ops += 1
    else:
      curr = num

  print(ops)
  

for _ in range(cs):
  solve()