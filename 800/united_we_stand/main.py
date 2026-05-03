import sys

input = sys.stdin.readline

cases = int(input())


for _ in range(cases):
  n = int(input())
  
  nums = list(map(int, input().split()))
  nums.sort()
  
  if nums[-1] == nums[0]:
    print(-1)
    continue
  b, c = [], []
  
  # b_i % c_i, if == 0, problem
  max_val = nums[-1]
  for val in nums:
    if val == max_val:
      c.append(max_val)
    else:
      b.append(val)
  print(f"{len(b)} {len(c)}")
  print(" ".join(str(i) for i in b))
  print(" ".join(str(i) for i in c))
