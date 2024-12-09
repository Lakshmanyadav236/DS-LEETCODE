class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum=0
        n=len(nums)
        mpp={}
        cnt=0
        for i in range(n):
            pref_sum+=nums[i]
            if pref_sum==k:
                cnt+=1
            remove=pref_sum-k
            if remove in mpp:
                cnt+=mpp[remove]
            if pref_sum in mpp:
                mpp[pref_sum]+=1
            else:
                mpp[pref_sum]=1
        return cnt