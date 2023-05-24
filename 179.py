class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            # Concatenate the numbers in both orders and compare them
            return int(str(y) + str(x)) - int(str(x) + str(y))
        
        # Sort the numbers using the custom comparison function
        nums.sort(key=functools.cmp_to_key(compare))
        
        # Concatenate the sorted numbers and return the result
        return str(int(''.join(map(str, nums))))
