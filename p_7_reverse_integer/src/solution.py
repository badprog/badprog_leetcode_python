# https://github.com/badprog/badprog_leetcode_python

############################
#
class Solution:
    ############################
    #
    def reverse(self, x: int) -> int:
        #
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        # 
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        # Reverse numbers
        reversed_x = 0
        while x > 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        
        # Apply the sign
        reversed_x *= sign
        
        # Check 32-bit limit
        if reversed_x > INT_MAX or reversed_x < INT_MIN:
            return 0
            
        return reversed_x
    