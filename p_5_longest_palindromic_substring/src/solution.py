# https://github.com/badprog/badprog_leetcode_python

############################
#
class Solution:
    ############################
    #
    def longestPalindrome(self, s: str) -> str:
        # 1
        special_char = '#'
        str_ready = special_char.join(s)
        str_ready = special_char + str_ready + special_char
        
        # 2
        str_len = len(str_ready)
        vec_palindrom = [0] * str_len
        # print(f"str_len: {str_len}, vec_palindrom:{vec_palindrom}")
        palindrom_center = 0
        palindrom_right = 0
        
        # 3
        for (index, element) in enumerate(str_ready):
            # print(f"index: {index}, element: {element}")
            if index < palindrom_right:
                vec_palindrom[index] = min(palindrom_right - index, vec_palindrom[2 * palindrom_center - index])
            else:
                vec_palindrom[index] = 0
                
            # 4
            while   (index + vec_palindrom[index] + 1 < str_len and 
                    index - vec_palindrom[index] -1 >= 0 and 
                    str_ready[index - vec_palindrom[index] - 1] == 
                    str_ready[index + vec_palindrom[index] + 1]):
                vec_palindrom[index] += 1
                
            # 5
            if index + vec_palindrom[index] > palindrom_right:
                palindrom_center = index
                palindrom_right = index + vec_palindrom[index]
            
        # 6
        # max_center = max(int(char) for char in vec_palindrom if char.isdigit())
        max_center = max(vec_palindrom)
        max_index = vec_palindrom.index(max_center)
        # print(f"vec_palindrom: {vec_palindrom}")
        # print(f"max_center: {max_center}")
        # print(f"max_index: {max_index}")
        start = (max_index - max_center) // 2
        # print(f"start: {start}")
        end = start + max_center
        
        str_to_return = s[start:end]
        # print(f"str_to_return: {str_to_return}")

        # return        
        return str_to_return
    