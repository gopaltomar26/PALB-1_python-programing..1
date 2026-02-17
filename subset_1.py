class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      res=[]
      def back(start,route):
        res.append(route[:])
        for i in range(start,len(nums)):
                route.append(nums[i])
                back(i+1,route)
                route.pop()
        back(0,[])
        return res
