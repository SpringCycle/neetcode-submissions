class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            dict1[s[i]]=dict1.get(s[i],0)+1
        for j in range(0,len(t)):
            dict2[t[j]]=dict2.get(t[j],0)+1
        # print(dict1, dict2)
        if dict1==dict2:
            return True
        else:
            return False
