# https://github.com/badprog/badprog_leetcode_python

# =============================================================================
#
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# =============================================================================
# 
class Solution:
    # =============================================================================
    # 
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # print("========== def addTwoNumbers")
        
        #
        # Var
        #
        # if l1 is None or l2 is None:
        #     return None
        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1
        
        head = ListNode(0)
        node = head
        current_1 = l1
        current_2 = l2
        number_total = 0
        number_1 = 0
        number_2 = 0
        
        # number = 0
        carry = 0
        
        #
        # loop
        #
        while (current_1 or current_2 or carry):
            number_1 = current_1.val if current_1 else 0
            number_2 = current_2.val if current_2 else 0
            
            number_total = number_1 + number_2 + carry
            
            carry = 0
            carry = number_total // 10 # //= -> no decimal
            number_total %= 10
            
            node.next = ListNode(number_total)
            node = node.next
        
            current_1 = current_1.next if current_1 else None
            current_2 = current_2.next if current_2 else None
            
        #
        # return
        #
        return head.next
    