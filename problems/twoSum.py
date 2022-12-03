"""
题目：输入一个递增排序的数组和一个值k
，请问如何在数组中找出两个和为k
的数字并返回它们的下标？假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。
例如，输入数组[1，2，4，6，10]，k
的值为8，数组中的数字2与6的和为8，它们的下标分别为1与3
"""
import unittest


def twoSum(nums: list[int], k: int) -> list[int]:
    right_p = 0
    left_p = len(nums) - 1
    while nums[right_p]+nums[left_p] != k and right_p < left_p:
        if nums[right_p]+nums[left_p] > k:
            left_p -= 1
        else:
            right_p += 1
    return [right_p, left_p]


class TestTwoSum(unittest.TestCase):

    def test_two_sum(self):
        self.assertEqual([1, 3], twoSum([1, 2, 4, 6, 10], 8))


