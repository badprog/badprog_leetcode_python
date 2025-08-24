# https://github.com/badprog/badprog_leetcode_python

############################
# import
import sys
import pathlib

# Adding the parent directory of this file to the sys.path
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import pytest
from src.solution import Solution

@pytest.mark.parametrize("input_str, expected", [
    ("babad", {"bab", "aba"}),
    ("cbbd", {"bb"}),
    ("a", {"a"}),
    ("racecar", {"racecar"}),
    ("aaaa", {"aaaa"}),
    ("abc", {"a", "b", "c"}),
    ("", {""}),
    ("ababa", {"ababa"}),
    ("abcdedcba", {"abcdedcba"}),
    ("abbcccbba", {"abbcccbba"}),
])

def test_longest_palindrome(input_str, expected):
    solution = Solution()
    result = solution.longestPalindrome(input_str)
    assert result in expected, f"Failed for entry={input_str}, expected={expected}, current={result}"
    