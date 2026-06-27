"""
Longest Consecutive Sequence  —  Medium
LC: https://leetcode.com/problems/longest-consecutive-sequence/

Statement:
    Given an unsorted array, return the length of the longest run of
    consecutive integers (e.g. [100,4,200,1,3,2] -> 4 for [1,2,3,4]).
    Must be O(n) time (sorting it is the "better", not the optimal).

Constraints:
    0 <= len(nums) <= 1e5 ; -1e9 <= nums[i] <= 1e9

Pattern: Hash Set + sequence-start detection (Mental Model: Sequence Expansion)
    Only start counting a run from a number x where (x-1) is NOT in the set.

--- fill in as you solve (brief 7) ---
Brute force:
Better (sorting):
Optimal idea (why does start-detection keep it O(n) overall?):
Time / Space:
"""


def longest_consecutive_sequence(arr: []) -> int:
    n = len(arr)
    final_dict = {}
    for i in range(0, n):
        final_dict[arr[i]] = 0

    max_count = 0
    for key in final_dict.keys():
        count = 1
        if final_dict[key] == 0:
            final_dict[key] = 1
            look_up = key + 1
            while True:
                if look_up in final_dict:
                    final_dict[look_up] = 1
                    count = count + 1
                    max_count = max(count, max_count)
                    look_up = look_up + 1
                else:
                    break
    return max_count
    
    
if __name__ == "__main__":
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))   # 4
    print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
