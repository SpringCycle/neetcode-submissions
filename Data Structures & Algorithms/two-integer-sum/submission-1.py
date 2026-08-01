class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # O(n)^2
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        seen={}

        for i,num in enumerate(nums):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement],i]
            seen[num]=i