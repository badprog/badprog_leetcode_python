# https://github.com/badprog/badprog_leetcode_python


######################################
# import
import sys
import pathlib

# Adding the parent directory of this file to the sys.path
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from src.solution import Solution

######################################
# main
def main():
    print("Hello from Badprog, Python and Leetcode :D")
    s = "Héllo world"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(f"result = {result}")
    
    
######################################
# __name__p
if __name__ == "__main__":
    main() 
    
# EMD
