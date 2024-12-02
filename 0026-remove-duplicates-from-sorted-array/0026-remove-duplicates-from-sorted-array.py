class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=nums[0]
        index=1
        for  i in range(1,len(nums)):
            if nums[i]!=prev:
                nums[index]=nums[i]
                prev=nums[i]
                index+=1
        return index
        