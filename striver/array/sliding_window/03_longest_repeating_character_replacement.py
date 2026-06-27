"""
Longest Repeating Character Replacement  —  Medium
LC: https://leetcode.com/problems/longest-repeating-character-replacement/

Statement:
    Given s (uppercase letters) and k, you may replace up to k characters.
    Return the length of the longest substring of a single repeated letter
    achievable after at most k replacements.

Constraints:
    1 <= len(s) <= 1e5 ; uppercase English ; 0 <= k <= len(s)

Pattern: Sliding Window + frequency count
    Window is valid while (window_len - count_of_most_frequent_char) <= k.

--- fill in as you solve (brief 7) ---
Brute force:
Optimal idea (why is it OK to never shrink maxFreq?):
Time / Space:
"""


def character_replacement(s: str, k: int) -> int:
    pass


if __name__ == "__main__":
    print(character_replacement("ABAB", 2))      # 4
    print(character_replacement("AABABBA", 1))   # 4
