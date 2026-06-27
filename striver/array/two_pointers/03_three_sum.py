"""
3Sum  —  Medium
LC: https://leetcode.com/problems/3sum/

Statement:
    Return all UNIQUE triplets [a, b, c] such that a + b + c == 0.
    The solution set must not contain duplicate triplets.

Constraints:
    3 <= len(nums) <= 3000 ; -1e5 <= nums[i] <= 1e5

Pattern: Sort + Two Pointers (fix one, two-pointer the rest)
    The hard part is DEDUPING cleanly without a set of triplets.

--- fill in as you solve (brief 7) ---
Brute force:
Optimal idea (how do you skip duplicate fixed values AND duplicate pairs?):
Time / Space:
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    pass


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    print(three_sum([0, 0, 0]))              # [[0,0,0]]
