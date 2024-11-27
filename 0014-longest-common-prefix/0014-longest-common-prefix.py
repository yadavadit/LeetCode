class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        word = strs[0]
        for i in range(len(word)):
            for s in strs:
                if i >= len(s) or s[i] != word[i]:
                    return prefix
            prefix += word[i]
        return prefix
            
        
            