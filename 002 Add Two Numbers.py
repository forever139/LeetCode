#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
#  class ListNode(object):
   #  def __init__(self, x):
       #  self.val = x
       #  self.next = None

   #  def __repr__(self):
       #  return repr(self.val)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp_number = self.convertToNumber(l1) + self.convertToNumber(l2)

        temp_next = None
        for num_str in str(temp_number):
            temp_node = ListNode(int(num_str))
            temp_node.next = temp_next
            temp_next = temp_node
        return temp_node


    def convertToNumber(self, node):
        counter = 0
        number = 0

        while node:
            if counter == 0:
                number += node.val
            else:
                number += node.val * pow(10, counter)

            counter += 1
            node = node.next

        return number

if __name__ == "__main__":
    test = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(8)
    l2 = ListNode(0)
    print test.convertToNumber(l1)
    print test.convertToNumber(l2)

