import sys
input = sys.stdin.readline


num_cases = int(input())

for _ in range(num_cases):
  _ = int(input())
  input_str = input().strip() 

  actions = 0
  dots = 0
  for ch in input_str:
    if ch == ".":
      dots += 1
  
  if "..." in input_str:
    print(2)
  else:
    print(dots)