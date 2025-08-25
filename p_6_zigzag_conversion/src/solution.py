# https://github.com/badprog/badprog_leetcode_python

from typing import List

############################
#
class Solution:
    ############################
    #
    def convert(self, s: str, numRows: int) -> str:
        #
        if numRows == 1:
            return s
        
        #
        vec_row: List[str] = [""] * numRows
        step = 0
        cur_row = 0
        
        for index, element in enumerate(s):
            # print(f"index: {index}, element: {element}")
            vec_row[cur_row] += element
            
            if cur_row == 0:
                step = 1
            elif cur_row == numRows - 1:
                step = -1
        
            cur_row += step
            
        #
        # print(f"vec_row: {vec_row}")
        final_str = ''.join(vec_row)
        
        #
        return final_str
    