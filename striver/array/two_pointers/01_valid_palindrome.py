"""
Valid Palindrome  —  Easy
LC: https://leetcode.com/problems/valid-palindrome/

Statement:
    Return True if the string is a palindrome considering only alphanumeric
    characters and ignoring case.

Constraints:
    1 <= len(s) <= 2e5 ; s contains printable ASCII.

Pattern: Two Pointers (converging from both ends)

--- fill in as you solve (brief 7) ---
Brute force:
Optimal idea (can you do it without building a cleaned copy -> O(1) space?):
Time / Space:
"""


def is_palindrome(s: str) -> bool:
    pass


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))                      # False
