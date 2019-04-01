class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k=0
        for n in nums:
            if target>n:
                k=k+1
            else :
                return k
        return len(nums)
