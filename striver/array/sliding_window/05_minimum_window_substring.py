"""
Minimum Window Substring  —  Hard  (stretch problem for the week)
LC: https://leetcode.com/problems/minimum-window-substring/

Statement:
    Given strings s and t, return the smallest substring of s that contains
    every character of t (including multiplicity). "" if none exists.

Constraints:
    1 <= len(s), len(t) <= 1e5 ; uppercase + lowercase English letters.

Pattern: Sliding Window + need/have counts (expand to satisfy, shrink to minimize)

--- fill in as you solve (brief 7) ---
Brute force:
Optimal idea (what "have == need" signal lets you shrink from the left?):
Time / Space:
"""


def min_window(s: str, t: str) -> str:
    pass


if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
    print(min_window("a", "a"))                # "a"
    print(min_window("a", "aa"))               # ""
