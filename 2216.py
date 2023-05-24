class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deletions = 0
        
        # Check if nums length is even
        if len(nums) % 2 != 0:
            deletions += 1
        
        # Check beauty conditions
        for i in range(0, len(nums)-1, 2):
            if nums[i] == nums[i+1]:
                deletions += 1
        
        return deletions
