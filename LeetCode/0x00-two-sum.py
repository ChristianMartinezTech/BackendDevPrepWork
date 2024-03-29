#!/usr/bin/env python3
"""
https://leetcode.com/problems/two-sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""


def twoSum(nums, target):
    """ With range(len we refence the index,
    by only ranging over nums we refence the value, not the index"""

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - \
                    nums[i]:  # Changed from i + j == target for running time
                return [i, j]


def main():
    response = twoSum([2, 7, 11, 15], 9)
    print(response)


if __name__ == '__main__':
    main()
