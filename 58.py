class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=0
        last=0
        for c in s:
            if c==" ":
                last=n if n>0 else last
                n=0
            else:
                n=n+1
        return n if n>0 else last
