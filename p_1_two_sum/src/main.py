# https://github.com/badprog/badprog_leetcode_python

######################################
# import
import sys
import pathlib

# Adding the parent directory of this file to the sys.path
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from src.solution import Solution # from file import class

####################################
def hello(name: str) -> str:
  return f"Hello, {name}!"


######################################
# main
def main():
  print(hello("Python"))
  nums = [2, 7, 11, 15] # ----------------------------
  target = 17
  solution = Solution()

  result = solution.twoSum(nums, target)
  print(f"Index found: {result}")

######################################
# __name__
if __name__ == "__main__":
  main()

