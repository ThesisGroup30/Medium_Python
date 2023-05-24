class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s3 = float('-inf')  # Initialize s3 to negative infinity
        
        # Iterate the array in reverse order
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < s3:
                return True  # Found a 132 pattern
            
            # Update s3 with the greater element from the stack
            while stack and nums[i] > stack[-1]:
                s3 = stack.pop()
            
            # Push the current element into the stack
            stack.append(nums[i])
        
        return False  # No 132 pattern found
