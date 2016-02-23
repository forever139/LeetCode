#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        location = dict([(num, i) for i, num in enumerate(nums)])

        for i, num in enumerate(nums):
            other = target - num;
            if (other in nums) and location[other] != i:
                return [i, location[other]]


if __name__ == "__main__":
    test = Solution()
    print test.twoSum([0, 7, 11, 0], 0)
    print test.twoSum([3, 2, 4], 6)
    print test.twoSum([-9, -4, -5, -3], -8)
