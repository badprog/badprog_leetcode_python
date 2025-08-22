# https://github.com/badprog/badprog_leetcode_python

############################
# import
import sys
import pathlib

# Adding the parent directory of this file to the sys.path
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import pytest
from src.solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_two_sorted_arrays_equal_length(solution):
    assert solution.findMedianSortedArrays([1, 3], [2, 4]) == 2.5

def test_two_sorted_arrays_odd_total_length(solution):
    assert solution.findMedianSortedArrays([1, 3], [2]) == 2.0

def test_one_empty_array(solution):
    assert solution.findMedianSortedArrays([], [1]) == 1.0

def test_single_element_arrays(solution):
    assert solution.findMedianSortedArrays([1], [2]) == 1.5

def test_large_arrays(solution):
    assert solution.findMedianSortedArrays([1, 2, 3, 4], [5, 6, 7, 8]) == 4.5

def test_one_element_and_large_array(solution):
    assert solution.findMedianSortedArrays([1], [2, 3, 4]) == 2.5

def test_arrays_with_negative_numbers(solution):
    assert solution.findMedianSortedArrays([-5, -1], [2, 4]) == 0.5

def test_duplicate_elements(solution):
    assert solution.findMedianSortedArrays([1, 1], [1, 1]) == 1.0

def test_large_difference_in_sizes(solution):
    assert solution.findMedianSortedArrays([1, 2], [3, 4, 5, 6, 7]) == 4.0

def test_maximum_constraints(solution):
    nums1 = [1] * 1000
    nums2 = [2] * 1000
    assert solution.findMedianSortedArrays(nums1, nums2) == 1.5
    
    