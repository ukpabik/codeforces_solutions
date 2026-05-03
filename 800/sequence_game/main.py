import sys

input = sys.stdin.readline

cases = int(input())


for _ in range(cases):
  
  n = int(input())
  
  numsb = list(map(int, input().split()))
  
  result = [numsb[0]]
  
  for i in range(1, n):
    if numsb[i - 1] > numsb[i]:
      result.append(numsb[i])
    result.append(numsb[i])
    
  print(len(result))
  print(" ".join(str(i) for i in result))