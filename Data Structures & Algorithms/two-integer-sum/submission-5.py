class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(0,len(nums)):
            rem=target-nums[i]
            if rem in hash:
                return [hash[rem],i]
            hash[nums[i]]=i