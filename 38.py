class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            result=""
            s=self.countAndSay(n-1)
            count=0
            t=-1
            for c in s:
                if int(c)!=t:
                    if t!=-1:
                        result=result+str(count)+str(t)
                    count=1
                    t=int(c)
                else:
                    count=count+1
            result=result+str(count)+str(t)
            return result
