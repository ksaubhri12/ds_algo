"""
Sort Colors (Dutch National Flag)  —  Medium
LC: https://leetcode.com/problems/sort-colors/
Striver A2Z: "Sort an array of 0's, 1's and 2's"

Statement:
    Sort an array containing only 0, 1, 2 IN PLACE, in a single pass,
    without using a library sort.

Constraints:
    1 <= len(nums) <= 300 ; nums[i] in {0, 1, 2}

Pattern: Two/Three Pointers (low, mid, high partitioning)

--- fill in as you solve (brief 7) ---
Brute force (counting sort is the "better"):
Optimal idea (one pass: what do low/mid/high invariants mean?):
Time / Space:
"""


def sort_colors(nums: list[int]) -> None:
    pass


if __name__ == "__main__":
    a = [2, 0, 2, 1, 1, 0]
    sort_colors(a)
    print(a)   # [0, 0, 1, 1, 2, 2]
