class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        a=[]
        while x>0:
            a.append(x%10)
            x=int(x/10)
        for i in range(len(a)):
            if a[i] != a[-(i+1)]:
                return False
        return True
