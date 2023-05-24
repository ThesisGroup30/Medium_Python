class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array in ascending order
        n = len(nums)
        min_value = nums[0]
        max_value = nums[n - 1]
        result = max_value - min_value

        for i in range(n - 1):
            # Calculate the possible maximum and minimum values after modifying nums[i]
            possible_max = max(nums[i] + k, max_value - k)
            possible_min = min(nums[i + 1] - k, min_value + k)
            result = min(result, possible_max - possible_min)

        return result
