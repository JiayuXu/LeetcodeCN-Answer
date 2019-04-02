class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0

        if len(nums)==0:
            return 0
        while (i<len(nums)):
            if val==nums[i]:
                nums.pop(i)
            else:
                t=nums[i]
                i=i+1
