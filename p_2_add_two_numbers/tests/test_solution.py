# https://github.com/badprog/badprog_leetcode_python

import pytest
from typing import List, Optional
from src.main import create_linked_list, display_linked_list
from src.solution import Solution, ListNode

class TestLinkedList:
    def setup_method(self):
        self.solution = Solution()

    def create_list_from_values(self, values: List[int]) -> Optional[ListNode]:
        """Helper to create a linked list from a Python list."""
        return create_linked_list(values)

    def list_to_values(self, head: Optional[ListNode]) -> List[int]:
        """Helper to convert a linked list to a Python list."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_create_linked_list_empty(self):
        """Test creating an empty linked list."""
        result = create_linked_list([])
        assert result is None, "Empty list should return None"

    def test_create_linked_list_single(self):
        """Test creating a linked list with one element."""
        result = create_linked_list([5])
        assert self.list_to_values(result) == [5], "List should be [5]"

    def test_create_linked_list_multiple(self):
        """Test creating a linked list with multiple elements."""
        result = create_linked_list([1, 2, 3])
        assert self.list_to_values(result) == [1, 2, 3], "List should be [1, 2, 3]"

    def test_add_two_numbers_equal_length(self):
        """Test adding two lists of equal length."""
        l1 = create_linked_list([2, 4, 3])  # 342
        l2 = create_linked_list([5, 6, 4])  # 465
        result = self.solution.addTwoNumbers(l1, l2)  # 807
        assert self.list_to_values(result) == [7, 0, 8], "342 + 465 = 807 -> [7, 0, 8]"

    def test_add_two_numbers_different_length(self):
        """Test adding two lists of different lengths."""
        l1 = create_linked_list([1, 8])  # 81
        l2 = create_linked_list([0])     # 0
        result = self.solution.addTwoNumbers(l1, l2)  # 81
        assert self.list_to_values(result) == [1, 8], "81 + 0 = 81 -> [1, 8]"

    def test_add_two_numbers_with_carry(self):
        """Test adding with carry."""
        l1 = create_linked_list([9, 9, 9])  # 999
        l2 = create_linked_list([1])        # 1
        result = self.solution.addTwoNumbers(l1, l2)  # 1000
        assert self.list_to_values(result) == [0, 0, 0, 1], "999 + 1 = 1000 -> [0, 0, 0, 1]"

    def test_add_two_numbers_empty_lists(self):
        """Test adding two empty lists."""
        l1 = create_linked_list([])
        l2 = create_linked_list([])
        result = self.solution.addTwoNumbers(l1, l2)
        assert self.list_to_values(result) == [], "[] + [] = []"

    def test_add_two_numbers_one_empty(self):
        """Test adding with one empty list."""
        l1 = create_linked_list([1, 2, 3])
        l2 = create_linked_list([])
        result = self.solution.addTwoNumbers(l1, l2)
        assert self.list_to_values(result) == [1, 2, 3], "[1, 2, 3] + [] = [1, 2, 3]"

    def test_display_linked_list(self):
        """Test display_linked_list runs without errors."""
        l1 = create_linked_list([1, 2, 3])
        try:
            display_linked_list(l1)
        except Exception as e:
            pytest.fail(f"display_linked_list raised an exception: {e}")
            
