class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # Create a dictionary to map each character in chars to its corresponding value in vals
        char_vals = {}
        for i in range(len(chars)):
            char_vals[chars[i]] = vals[i]
        
        # Initialize variables to keep track of maximum cost and current cost
        max_cost = 0
        cur_cost = 0
        
        # Initialize variables for sliding window technique
        left = 0
        right = 0
        
        # Iterate over string s using sliding window technique
        while right < len(s):
            # If the current character is in chars, add its value to the current cost
            if s[right] in char_vals:
                cur_cost += char_vals[s[right]]
            
            # If the current character is not in chars, add its index as its value to the current cost
            else:
                cur_cost += ord(s[right]) - 96
            
            # If the current substring has a negative cost, reset the current cost and move the left pointer
            if cur_cost < 0:
                cur_cost = 0
                left = right + 1
            
            # Update the maximum cost
            max_cost = max(max_cost, cur_cost)
            
            # Move the right pointer to expand the window
            right += 1
        
        return max_cost
