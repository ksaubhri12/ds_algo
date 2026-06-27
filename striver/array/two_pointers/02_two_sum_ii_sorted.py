"""
Two Sum II - Input Array Is Sorted  —  Medium
LC: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Statement:
    Given a 1-indexed SORTED array, return the 1-based indices of the two
    numbers that add up to target. Exactly one solution; O(1) extra space.

Constraints:
    2 <= len(numbers) <= 3e4 ; sorted non-decreasing ; one solution exists.

Pattern: Two Pointers (sorted -> move inward based on sum vs target)
    This is the "what if the array is sorted?" follow-up to Two Sum.

--- fill in as you solve (brief 7) ---
Brute force:
Optimal idea (why does sortedness remove the need for a hashmap?):
Time / Space:
"""


def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    pass


if __name__ == "__main__":
    print(two_sum_sorted([2, 7, 11, 15], 9))   # [1, 2]
    print(two_sum_sorted([2, 3, 4], 6))        # [1, 3]
