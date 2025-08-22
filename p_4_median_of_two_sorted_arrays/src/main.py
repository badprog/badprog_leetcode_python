# https://github.com/badprog/badprog_leetcode_python

################
# import
import sys
import pathlib

# Adding the parent directory of this file to the sys.path
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from src.solution import Solution
from typing import List

################
#
def main():
    print("Hello from Badprog, Leetcode challenge 4 and Rust :D")
    solution = Solution()
    # list1: List[int] = [1,2]
    list1: List[int] = [1,2,6,0,2,1,4,9]
    list2: List[int] = [4,5,6,8,9]
    list1.sort()
    list2.sort()
    result = solution.findMedianSortedArrays(list1, list2)
    print("result = {}", result)
    
################
#
if __name__ == "__main__":
    main()

