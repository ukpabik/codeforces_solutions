import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp(): # int input
    return(int(input()))
def inlt(): # list inputs
    return(list(map(int,input().split())))
def insr(): # string inputs
    return input().strip()
def invr(): # space separated int inputs
    return(map(int,input().split()))
   
num_cases = inp()
for _ in range(num_cases):
  n, k = invr()
  values = inlt()
  
  # check if values are already sorted
  is_sorted = True 
  for i in range(n-1):
    if values[i] > values[i+1]:
      is_sorted = False 

  if k < 2:
    if is_sorted:
      print("YES")
    else:
      print("NO")
  else:
    print("YES")
  

  # if k < 2 and input is not already sorted, NO
  # if k > 2 --> YES 