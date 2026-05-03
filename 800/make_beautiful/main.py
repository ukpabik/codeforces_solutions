import sys

input = sys.stdin.readline

cs = int(input())


def solve():
  n = int(input())
  nums = list(map(int, input().split()))
  
  if max(nums) == min(nums):
    print("NO")
  else:
    print("YES")
    nums.sort(reverse=True)
    if nums[1] == nums[0]:
      nums[1], nums[-1] = nums[-1], nums[1]
    separated = " ".join(map(str, nums))
    print(separated)
    
  
      
"""
[6,3,9,6]

[9,6,6,3]

0 != 9, 6 != 9, 15 != 6, 21 != 3

if all elements are equal, impossible.
otherwise, we can.

[largest, others, smallest]

[2,6,5,4]

[6,5,4,2]

"""


for _ in range(cs):
  solve()