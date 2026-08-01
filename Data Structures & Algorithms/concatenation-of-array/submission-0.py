class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newlist=[]
        for i in range(0,len(nums)):
            newlist.append(nums[i])
        return (newlist+nums)