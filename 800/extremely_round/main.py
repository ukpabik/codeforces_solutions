import sys

input = sys.stdin.readline

cs = int(input())

"""
0-9

if num < 10:
  round_in = num
else:
  
  
1-9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100-900, 1000-9000, 10000-90000, 

27 + 5 = 32

1-9, 10-90, 100-900, 1000-5000

"""



def solve():
  n = int(input())
  
  total = 0 
  while n > 10:
    total += 9
    n /= 10
  total += int(n)

  
  print(total)

for _ in range(cs):
  solve()