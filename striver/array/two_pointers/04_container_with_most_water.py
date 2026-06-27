"""
Container With Most Water  —  Medium
LC: https://leetcode.com/problems/container-with-most-water/

Statement:
    Given heights[], pick two lines that together with the x-axis form a
    container holding the most water. Return the max area.

Constraints:
    2 <= len(height) <= 1e5 ; 0 <= height[i] <= 1e4

Pattern: Two Pointers (greedy shrink from the wider, shorter side)

--- fill in as you solve (brief 7) ---
Brute force:
Optimal idea (why is it always safe to move the SHORTER line inward?):
Time / Space:
"""


def max_area(height: list[int]) -> int:
    pass


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(max_area([1, 1]))                        # 1
