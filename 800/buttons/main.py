import sys

input = sys.stdin.readline

cases = int(input())

for _ in range(cases):
  a,b,c = list(map(int, input().split()))

  if c % 2 != 0:
    a += 1
  
  print("First") if a > b else print("Second")

