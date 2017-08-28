# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.head = None

    def addTwoNumbers(self, l1, l2):
        carry = 0
        sum = 0
        list = []

        while (l1 is not None and l2 is not None):

            sum = l1.val + l2.val + carry
            if sum > 9:
                sum = sum - 10
                carry = 1
            else:
                carry = 0

            list.append(sum)
            node = ListNode(sum)
            node.next = self.head
            self.head = node

            l1 = l1.next
            l2 = l2.next

        while (l1 is not None):
            sum = l1.val + carry
            if sum > 9:
                sum = sum - 10
                carry = 1
            else:
                carry = 0
            list.append(sum)
            if self.head is None:
                node = ListNode(sum)
                node.next = self.head
                self.head = node
            l1 = l1.next

        while (l2 is not None):
            sum = l2.val + carry
            if sum > 9:
                sum = sum - 10
                carry = 1
            else:
                carry = 0
            list.append(sum)
            if self.head is None:
                node = ListNode(sum)
                node.next = self.head
                self.head = node

            l2 = l2.next

        if carry == 1:
            list.append(carry)

        return list



