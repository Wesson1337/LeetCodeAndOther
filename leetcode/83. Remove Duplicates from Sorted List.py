# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        current_num = head.val
        current_head = head
        first_head = head

        while head is not None:
            if head.next is None and current_num == head.val:
                current_head.next = None
                break
            if current_num != head.val:
                current_head.next = head
                current_head = head
                current_num = head.val
            head = head.next
        return first_head
