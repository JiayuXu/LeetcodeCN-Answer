class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        if strs[0]=="":
            return ""
        for i,a in enumerate(strs[0]):
            flag=True
            for s in strs:
                if i>=len(s) or a!=s[i]:
                    flag=False
                    break
            if not flag:
                return strs[0][:i]
