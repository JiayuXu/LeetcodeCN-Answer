class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        jin=1
        for  i in range(len(digits)-1,-1,-1):
            if jin!=0:
                digits[i]=digits[i]+1
                jin=0
                if digits[i]==10:
                    digits[i]=0
                    jin=1
            else:
                break
        if jin==1:
            digits.insert(0,1)
        return digits
