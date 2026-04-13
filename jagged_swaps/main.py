import sys
input = sys.stdin.readline
  
  
num_cases = int(input())
for _ in range(num_cases):
  n = int(input())
  num_list = list(map(int, input().split())) 
  if num_list and num_list[0] != 1:
    print("NO")
  else:
    print("YES")