# https://github.com/badprog/badprog_leetcode_python

############################
# import
import sys
import pathlib

# Adding the parent directory of this file to the sys.path
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import pytest
from src.solution import Solution
def test_reverse_positive():
    assert Solution().reverse(123) == 321

def test_reverse_negative():
    assert Solution().reverse(-123) == -321

def test_reverse_zero():
    assert Solution().reverse(0) == 0

def test_reverse_trailing_zero():
    assert Solution().reverse(100) == 1

def test_reverse_single_digit():
    assert Solution().reverse(7) == 7

def test_reverse_negative_single_digit():
    assert Solution().reverse(-5) == -5

def test_reverse_two_digits():
    assert Solution().reverse(45) == 54

def test_reverse_negative_with_zeros():
    assert Solution().reverse(-130300) == -3031

def test_reverse_large_positive():
    assert Solution().reverse(123456) == 654321

def test_reverse_large_negative():
    assert Solution().reverse(-654321) == -123456
