class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        cp=nums[:]
        nums=sorted(nums)
        s=-1
        end=len(nums)
        for i,n in enumerate(nums):
            if n==cp[i]:
                s=i
            else:
                break
        for i in range(len(nums)-1,0,-1):
            if nums[i]==cp[i]:
                end=i
            else:
                break
        s=s+1
        end=len(nums)-end
        if(s+end)>=len(nums):
            return 0
        return len(nums)-(s+end)
