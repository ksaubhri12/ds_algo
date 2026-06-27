"""
Max Consecutive Ones III  —  Medium
LC: https://leetcode.com/problems/max-consecutive-ones-iii/
(Striver A2Z basic version: "Maximum Consecutive Ones" with no flips.)

Statement:
    Given a binary array and an integer k, return the length of the longest
    subarray of all 1s if you may flip at most k zeros.

Constraints:
    1 <= len(nums) <= 1e5 ; nums[i] in {0,1} ; 0 <= k <= len(nums)

Pattern: Sliding Window (shrink when zero-count in window exceeds k)

--- fill in as you solve (brief 7) ---
Brute force:
Optimal idea (what single counter decides when to shrink?):
Time / Space:
"""


def longest_ones(nums: list[int], k: int) -> int:
    pass


if __name__ == "__main__":
    print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))            # 6
    print(longest_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))  # 10
