n=len(arr)
min_len=n+1
start=0
current_sum=0
for i in range(n):
  current_sum+=arr[start]
  while current_sum>x:
