class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N=len(nums)
        total_sum=N*(N+1)//2
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
        return total_sum-sum