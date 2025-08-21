# https://github.com/badprog/badprog_leetcode_python

######################################
##
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        hash_map = {}
        start = 0
        
        for index, element in enumerate(s):
            # print(f"index: {index}: {element}")
            
            position = hash_map.get(element)
            if position is not None:
                # print(f"This element '{element}' is already in the HasMap at position: {position}")
                if position >= start:
                    start = position + 1
            hash_map[element] = index
            max_length = max(max_length, index - start + 1)
            # tmp_max = index - start + 1
            # if tmp_max > max_length:
            #     max_length = tmp_max    
        # END for        
        
        return max_length