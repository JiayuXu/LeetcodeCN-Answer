class Solution:
    def isValid(self, s: str) -> bool:
        l=["{","[","("]
        r=["}","]",")"]
        stack=[]
        for k in s:
            if k in l:
                stack.append(k)
            elif k in r:
                if len(stack)==0:
                    return False
                elif l[r.index(k)]==stack.pop():
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
