# https://github.com/badprog/badprog_leetcode_python

############################
# import
import sys
import pathlib

# Adding the parent directory of this file to the sys.path
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import pytest
from src.solution import Solution

def test_standard_case_numRows_3():
    solution = Solution()
    assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

def test_standard_case_numRows_4():
    solution = Solution()
    assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

def test_single_row():
    solution = Solution()
    assert solution.convert("A", 1) == "A"

def test_short_string_numRows_2():
    solution = Solution()
    assert solution.convert("AB", 2) == "AB"

def test_string_numRows_2():
    solution = Solution()
    assert solution.convert("ABCDE", 2) == "ACEBD"

def test_numRows_greater_than_string_length():
    solution = Solution()
    assert solution.convert("ABC", 5) == "ABC"

def test_empty_string():
    solution = Solution()
    assert solution.convert("", 3) == ""

def test_zigzag_numRows_3():
    solution = Solution()
    assert solution.convert("ABCDEFGHI", 3) == "AEIBDFHCG"

def test_zigzag_numRows_5():
    solution = Solution()
    assert solution.convert("ABCDEFGHIJK", 5) == "AIBHJCGKDFE"  # Fixed expected output

def test_special_characters():
    solution = Solution()
    assert solution.convert("Hello,World!", 3) == "Horel,ol!lWd"  # Fixed expected output
