class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_list={}
        for i in range(0,len(nums)):
            hash_list[nums[i]]=hash_list.get(nums[i],0)+1
            if hash_list.get(nums[i])>1:
                return True
        return False

        