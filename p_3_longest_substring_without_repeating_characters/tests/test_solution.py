# https://github.com/badprog/badprog_leetcode_python

############################
# import
import sys
import pathlib

# Adding the parent directory of this file to the sys.path
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from src.solution import Solution 

class TestP3LongestSubstringWithoutRepeatingCharacters():
    def test_empty_string(self):
        solution = Solution()
        assert solution.lengthOfLongestSubstring("") == 0

    def test_single_character(self):
        solution = Solution()
        assert solution.lengthOfLongestSubstring("a") == 1

    def test_all_unique_characters(self):
        solution = Solution()
        assert solution.lengthOfLongestSubstring("abcde") == 5

    def test_all_same_characters(self):
        solution = Solution()
        assert solution.lengthOfLongestSubstring("aaaaa") == 1

    def test_repeating_characters(self):
        solution = Solution()
        assert solution.lengthOfLongestSubstring("abcabcbb") == 3

    def test_mixed_string(self):
        solution = Solution()
        assert solution.lengthOfLongestSubstring("pwwkew") == 3

    def test_long_string(self):
        solution = Solution()
        assert solution.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyz") == 26

    def test_string_with_spaces(self):
        solution = Solution()
        assert solution.lengthOfLongestSubstring("abc def") == 7

    def test_single_repeating_pair(self):
        solution = Solution()
        assert solution.lengthOfLongestSubstring("dvdf") == 3

    def test_complex_case(self):
        solution = Solution()
        assert solution.lengthOfLongestSubstring("tmmzuxt") == 5
    
# END
