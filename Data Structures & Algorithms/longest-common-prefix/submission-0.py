class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pos=0
        result=""
        minm=9999
        for i in range(0,len(strs)):
            if(len(strs[i])<minm):
                minm=len(strs[i])


        for pos in range(0,minm):
            for i in range(0,len(strs)-1):
                if strs[i][pos] == strs[i+1][pos]:
                    continue
                else :
                    return result
            result+=(strs[i][pos])

        return result
            
