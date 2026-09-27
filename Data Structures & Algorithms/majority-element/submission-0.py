class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        for i in range(0,len(nums)):
            dict1[nums[i]]=dict1.get(nums[i],0)+1

        for i in dict1:
            if dict1[i]>(len(nums)//2):
                return i