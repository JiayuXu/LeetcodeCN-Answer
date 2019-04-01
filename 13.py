class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        flag=False
        for i,c in enumerate(s):
            if flag:
                flag=False
                continue
            if c=='I':
                if i+1<len(s) and s[i+1]=='V':
                    num=num+4
                    flag=True
                elif i+1<len(s) and s[i+1]=='X':
                    num=num+9  
                    flag=True
                else:
                    num=num+1
            if c=='X':
                if i+1<len(s) and s[i+1]=='L':
                    num=num+40
                    flag=True
                elif i+1<len(s) and s[i+1]=='C':
                    num=num+90  
                    flag=True
                else:
                    num=num+10
            if c=='C':
                if i+1<len(s) and s[i+1]=='D':
                    num=num+400
                    flag=True
                elif i+1<len(s) and s[i+1]=='M':
                    num=num+900  
                    flag=True
                else:
                    num=num+100
            if c=='M':
                num=num+1000 
            if c=='V':
                num=num+5  
            if c=='L':
                num=num+50 
            if c=='D':
                num=num+500  
        return num
