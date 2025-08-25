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
    print("Hello from Badprog, Leetcode challenge 7 and Python :D")
    number = -130300
    solution = Solution()
    result = solution.reverse(number)
    print(f"result = {result}")
    
################
#
if __name__ == "__main__":
    main()

