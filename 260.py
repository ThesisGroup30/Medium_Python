class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # XOR all numbers to get the XOR of the two single numbers
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        
        # Find the rightmost set bit in the XOR sum
        rightmost_set_bit = xor_sum & -xor_sum
        
        # Split the numbers into two groups based on the rightmost set bit
        group1 = 0
        group2 = 0
        for num in nums:
            if num & rightmost_set_bit:
                group1 ^= num
            else:
                group2 ^= num
        
        # Return the two single numbers
        return [group1, group2]
