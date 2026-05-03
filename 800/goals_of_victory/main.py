import sys

input = sys.stdin.readline

cases = int(input())


# e1 = 1vs2 + 1vs3 + 1vs4 - (2vs1 + 3vs1 + 4vs1)
# e2 = 2vs1 + 2vs3 + 2vs4 - (1vs2 + 3vs2 + 4vs2)
# e3 = 3vs1 + 3vs2 + 3vs4 - (1vs3 + 2vs3 + 4vs3)
# e4 = 4vs1 + 4vs2 + 4vs3 - (1vs4 + 2vs4 + 3vs4)


# e1 + e2 + e3 + e4 = 0, e4 = -(e1 + e2 + e3)

for _ in range(cases):
  n = int(input())
  
  efficiencies = list(map(int, input().split()))
  
  total = sum(efficiencies)
  
  print(-total)