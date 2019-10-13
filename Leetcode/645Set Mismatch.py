class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums) 
        s=set(nums) 
        mis=n*(n+1)/2-sum(s)
        res=sum(nums)-sum(s)
        return[res,mis]
