import sys

input = sys.stdin.readline


cases = int(input())

for _ in range(cases):
  n = int(input())
  nums_a = list(map(int, input().split()))
  
  b = []
  
  # n = 5, a = 1, 2, 4, 5, 3
  
  # 1 + ? <= 2 + ? <= 4 + ? <= 5 + ? <= 3 + ?

  for i in range(n):
    curr = nums_a[i]
    # 1 + what <= 4 + what, we can only use [1, 4], if we use 2, 3
    # the other permutation won't work

    """
    
    1 + ? <= 4 + ? <= 3 + ? <= 2 + ?
    
    1, 4, 3, 2
    2 <= 8 !<= 6 !<= 4    

    4, 1, 2, 3
    
    5 <= 5 <= 5 <= 5
    
    WORKS

    
    How can we calculate which number it is? The reverse.

    n = 4
    
    n - curr + 1 = index in the permutation

    """
    
    # 1, 4, 3, 2
    # 4, 1, 2, 3
    b.append((n - curr) + 1)

  print(" ".join([str(i) for i in b]))