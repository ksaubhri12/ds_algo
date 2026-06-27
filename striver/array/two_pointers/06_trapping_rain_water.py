"""
Trapping Rain Water  —  Hard  (stretch problem for the week)
LC: https://leetcode.com/problems/trapping-rain-water/

Statement:
    Given non-negative heights representing an elevation map (width 1 each),
    compute how much rain water it can trap.

Constraints:
    1 <= len(height) <= 2e4 ; 0 <= height[i] <= 1e5

Pattern: Two Pointers (left/right with running max walls)
    Worth knowing the prefix-max/suffix-max version first, then the O(1)-space
    two-pointer version.

--- fill in as you solve (brief 7) ---
Brute force (per index: min(maxLeft, maxRight) - h):
Better (precompute prefix-max & suffix-max arrays):
Optimal idea (two pointers, why move the side with the smaller wall?):
Time / Space:
"""


def trap(height: list[int]) -> int:
    pass


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(trap([4, 2, 0, 3, 2, 5]))                     # 9
