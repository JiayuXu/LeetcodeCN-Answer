class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}

        for i,n in enumerate(nums):
            d_n=target-n
            if d_n in d:
                return [d[d_n],i]
            d[n]=i
        return [None,None]
