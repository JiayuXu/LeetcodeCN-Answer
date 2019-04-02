        i=0
        t=None
        if len(nums)==0:
            return 0
        while (i<len(nums)):
            if t==nums[i]:
                nums.pop(i)
            else:
                t=nums[i]
                i=i+1

        return i
