import sys

input = sys.stdin.readline

cs = int(input())


def solve():
  n = int(input())
  nums = list(map(int, input().split()))
  
  twos = 0 

  counts = []

  for val in nums:
    if val == 2:
      twos += 1
    
    counts.append(twos)
  total = counts[-1]
  
  # [1,1,2,2,3,3,4,5,5,5,5,5]

  # k = 4, then 2 and 3. doesnt work. keep going. arr[k] - arr[0] == arr[-1] - arr[k]
  
  for k in range(n-1):
    left_side = counts[k]
    right_side = total - counts[k]

    if left_side == right_side:
      print(k+1)
      return
  
  print(-1)
      

for _ in range(cs):
  solve()