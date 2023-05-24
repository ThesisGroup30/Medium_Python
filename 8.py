class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Read in and ignore any leading whitespace
        s = s.lstrip()
        
        # Step 2: Check if the next character is '-' or '+'
        sign = 1
        if s and (s[0] == '-' or s[0] == '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        # Step 3: Read in next characters until next non-digit or end of input
        num_str = ''
        for char in s:
            if char.isdigit():
                num_str += char
            else:
                break
        
        # Step 4: Convert digits into integer and change sign if necessary
        if num_str:
            num = sign * int(num_str)
        else:
            num = 0
        
        # Step 5: Clamp integer to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        else:
            return num
