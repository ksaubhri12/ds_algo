# Week 3 — Sliding Window — Mistake Notebook

> Core idea: a window [left, right] over a contiguous range; expand right to
> include, shrink left to restore a constraint. Each index enters/leaves the
> window once -> O(n). Watch the trap: needs NON-NEGATIVE contributions (so
> "subarray sum = k" with negatives is prefix-sum, not window).

One entry per problem.

---

## Best Time to Buy and Sell Stock  (LC #121, Easy)
- Pattern: Running minimum / degenerate window
- Key insight:
- My initial approach:
- Final approach:
- Time / Space:
- Bugs I made:
- Lesson:

## Longest Substring Without Repeating Characters  (LC #3, Medium)
- Pattern: Variable window + last-seen map
- Key insight:
- My initial approach:
- Final approach:
- Time / Space:
- Bugs I made:
- Lesson:

## Longest Repeating Character Replacement  (LC #424, Medium)
- Pattern: Window + freq count, valid while len - maxFreq <= k
- Key insight:
- My initial approach:
- Final approach:
- Time / Space:
- Bugs I made:
- Lesson:

## Max Consecutive Ones III  (LC #1004, Medium)
- Pattern: Window with bounded zero-count
- Key insight:
- My initial approach:
- Final approach:
- Time / Space:
- Bugs I made:
- Lesson:

## Minimum Window Substring  (LC #76, Hard)
- Pattern: Window + need/have counts
- Key insight:
- My initial approach:
- Final approach:
- Time / Space:
- Bugs I made:
- Lesson:
