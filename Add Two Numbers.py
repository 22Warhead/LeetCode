"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans = ListNode()
        temp = ans
        carry = 0
        while (l1 is not None) or (l2 is not None):
            temp.next = ListNode()
            temp = temp.next
            addition = l1.val + l2.val + carry
            carry = addition // 10
            value = addition % 10
            temp.val = value
            l1 = l1.next
            l2 = l2.next


        while l1 is not None:
            temp.next = ListNode()
            temp = temp.next
            addition = l1.val + carry
            carry = addition // 10
            value = addition % 10
            temp.val = value
            l1 = l1.next

        while l2 is not None:
            temp.next = ListNode()
            temp = temp.next
            addition = l2.val + carry
            carry = addition // 10
            value = addition % 10
            temp.val = value
            l2 = l2.next

        if carry > 0:
            temp.next = ListNode()
            temp.next.val = carry

        return ans.next