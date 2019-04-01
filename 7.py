class Solution:
    def reverse(self, x: int) -> int:
        result=0
        flag=True
        if x<0:
            x=-x
            flag=False
        while x>0:
            b=x%10
            x=int(x/10)
            result=result*10+b
        if not flag:
            result=-result
        if result >2147483647 or result<-2147483648:
            return 0
        return result
