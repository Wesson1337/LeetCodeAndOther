# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1, val2 = l1, l2
        num1, num2 = '', ''
        while val1 is not None:
            num1 += str(val1.val)
            val1 = val1.next

        while val2 is not None:
            num2 += str(val2.val)
            val2 = val2.next

        res_num = str(int(num1) + int(num2))

        res = ListNode()
        next_node = res

        for i in range(len(res_num)):
            next_node.val = int(res_num[i])
            if i != len(res_num) - 1:
                next_node.next = ListNode()

        return res


res_num = "932"
next_node = ListNode()
res = next_node
for i in range(len(res_num)):
    next_node.val = int(res_num[i])
    if i != len(res_num) - 1:
        next_node.next = ListNode()

while res.next is not None:
    print(res.val)
# TODO
