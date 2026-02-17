class Solution:
    def maxSubarraySum(self, arr):
      current_sum=arr[0]#2
      max_sum=arr[0]#2
      for i in range(1,len(arr)):#i=1 to 7
        current_sum=max(arr[i],current_sum+arr[i])#max(3,5)=5--> max(-8,-6),max(7,9)
        max_sum=max(current_sum,max_sum)#max(2,5)=5
      return max_sum
