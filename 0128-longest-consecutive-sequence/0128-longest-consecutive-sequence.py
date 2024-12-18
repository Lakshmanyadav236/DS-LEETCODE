class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        longest=1
        cnt=0
        if n==0:
            return 0
        st=set()
        for i in range(n):
            st.add(nums[i])
        for it in st:
            if it-1 not in st:
                cnt=1
                x=it
                while x+1 in st:
                    cnt+=1
                    x+=1
                longest=max(longest,cnt)
        return longest
