# https://github.com/badprog/badprog_leetcode_python

from typing import List
import pytest
from src.solution import Solution

@pytest.fixture
def solution():
    return Solution()

# +============================================================================
#
def test_twoSum_standard_case(solution):
    nums = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(nums, target) == [0, 1], "Should return indices [0, 1] for nums=[2, 7, 11, 15] and target=9"

# +============================================================================
#
def test_twoSum_no_solution(solution):
    nums = [1, 2, 3]
    target = 10
    assert solution.twoSum(nums, target) == [], "Should return empty list if no solution exists"

# +============================================================================
#
def test_twoSum_duplicate_numbers(solution):
    nums = [3, 3]
    target = 6
    assert solution.twoSum(nums, target) == [0, 1], "Should return indices [0, 1] for nums=[3, 3] and target=6"

# +============================================================================
#
def test_twoSum_negative_numbers(solution):
    nums = [-1, -2, -3, -4]
    target = -5
    assert solution.twoSum(nums, target) == [1, 2], "Should return indices [1, 2] for nums=[-1, -2, -3, -4] and target=-5"

# +============================================================================
#
def test_twoSum_empty_list(solution):
    nums = []
    target = 5
    assert solution.twoSum(nums, target) == [], "Should return empty list for empty input"

# +============================================================================
#
def test_twoSum_single_element(solution):
    nums = [5]
    target = 5
    assert solution.twoSum(nums, target) == [], "Should return empty list for single-element list"
