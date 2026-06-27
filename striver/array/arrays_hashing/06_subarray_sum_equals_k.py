"""
Subarray Sum Equals K  —  Medium
LC: https://leetcode.com/problems/subarray-sum-equals-k/

Statement:
    Return the total number of contiguous subarrays whose elements sum to k.
    NOTE: nums can contain negatives, so sliding window does NOT work here.

Constraints:
    1 <= len(nums) <= 2e4 ; -1000 <= nums[i] <= 1000 ; -1e7 <= k <= 1e7

Pattern: Prefix-sum + HashMap of prefix-sum counts
    (bridges Week 1 hashing into the Month-2 prefix-sum pattern)
    Key: count how many earlier prefix sums equal (current_prefix - k).

--- fill in as you solve (brief 7) ---
Brute force: get all the sub array
Optimal idea (why seed the map with {0: 1}?):
The sum of element between i and j can be computed easily by prefix sum
sum(i..j) = prefix(j) - prefix(i-1
sum(i..j) = k
prefix(j) - prefix(i-1) = k
at any index , we need to see what is the prefix sum
after  that, we need to see have we seen any other element for which the prefix sum is k - prefix()
if yes, then it means a sub array exists
We have added zero because for ex = [1, -1, 2], and k = 2
the last index prefix sum is 2 so we need to know have we seen 0 and we have seen 0 two times, one if we don't have anything
which is the starting and the second is prefix sum at index 1
Time / Space:
"""


def subarray_sum(nums: list[int], k: int) -> int:
    n = len(nums)
    count_map = {0: 1}
    prefix_sum = [nums[0]] * n
    for i in range(1, n):
        prefix_sum[i] = nums[i] + prefix_sum[i - 1]
    total_count = 0
    for element in prefix_sum:
        other_element = element - k
        if other_element in count_map:
            total_count += count_map[other_element]

        count_map[element] = count_map.get(element, 0) + 1
    return total_count


if __name__ == "__main__":
    print(subarray_sum([1, 1, 1], 2))  # 2
    print(subarray_sum([1, 2, 3], 3))  # 2
