# https://github.com/badprog/badprog_leetcode_python

######################################
# import
from solution import Solution # from file import class

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




