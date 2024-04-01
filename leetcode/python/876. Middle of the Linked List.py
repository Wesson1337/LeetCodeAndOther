# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp_head = head
        while temp_head is not None:
            length += 1
            temp_head = temp_head.next

        count = length // 2
        while head is not None and count != 0:
            count -= 1
            head = head.next

        return head
