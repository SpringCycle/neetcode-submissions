class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist={}
        for num in nums:
            newlist[num]=newlist.get(num,0)+1
        for k in newlist:
            if newlist[k]>1:
                return True
        return False