class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums) 
        s=set(nums)
        
        res=sum(nums)-sum(s)
        miss=n*(n+1)/2-sum(s)
        return[res,miss]
