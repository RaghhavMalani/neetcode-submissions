class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i,char in enumerate(strs[0]):
            for rem_strs in strs[1:]:

                if i >= len(rem_strs) or char != rem_strs[i]:
                    return strs[0][:i]
                
        return strs[0]
        