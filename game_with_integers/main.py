import sys
input = sys.stdin.readline

num_cases = int(input())


for _ in range(num_cases):
  n = int(input())

  if n % 3 == 0:
    print("Second")
  else:
    print("First")