# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        pointer = result

        while l1 or l2 or carry:
            first_num = l1.val if l1 else 0
            second_num = l2.val if l2 else 0

            summation = first_num + second_num + carry

            num = summation % 10
            carry = summation // 10

            pointer.next = ListNode(num)

            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


def create_for_test(res_num: str):
    res = ListNode()
    next_node = res
    for i in range(len(res_num)):
        next_node.val = int(res_num[i])
        if i != len(res_num) - 1:
            next_node.next = ListNode()
            next_node = next_node.next
    return res


first = create_for_test("9999999")
second = create_for_test("9999")

res = Solution().addTwoNumbers(first, second)

while res is not None:
    print(res.val)
    res = res.next
# TODO
