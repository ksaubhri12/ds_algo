"""
Group Anagrams  —  Medium
LC: https://leetcode.com/problems/group-anagrams/

Statement:
    Given a list of strings, group the ones that are anagrams of each other.
    Order of groups and order within a group do not matter.

Constraints:
    1 <= len(strs) <= 1e4 ; 0 <= len(strs[i]) <= 100 ; lowercase English letters.

Pattern: Hash Map with a DERIVED / CANONICAL key
    (the whole problem = "what key makes all anagrams collide into one bucket?")

--- fill in as you solve (brief 7) ---
Brute force:
Optimal idea (think of TWO keys: one simpler, one O(n*k)):
Time / Space:
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    pass


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # e.g. [["eat","tea","ate"],["tan","nat"],["bat"]]
