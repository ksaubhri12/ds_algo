"""
Longest Substring Without Repeating Characters  —  Medium
LC: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Statement:
    Return the length of the longest substring of s with all distinct chars.

Constraints:
    0 <= len(s) <= 5e4 ; s has English letters, digits, symbols, spaces.

Pattern: Variable-size Sliding Window + HashMap/Set (shrink on duplicate)

--- fill in as you solve (brief 7) ---
Brute force:
Optimal idea (when a dup appears, where does left jump to?):
Time / Space:
"""


def length_of_longest_substring(s: str) -> int:
    pass


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))      # 1
    print(length_of_longest_substring("pwwkew"))     # 3
