class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i=1
        prefix=strs[0]
        while i < len(strs):
            while not strs[i].startswith(prefix):
                prefix= prefix[:-1]
            i+=1
        return prefix

        