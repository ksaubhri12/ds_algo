# DSA Roadmap — Pattern Map

Companion to `../DSA_PREP.md` (the mentor brief). That file is the *method*;
this file is the *map*: where every problem lives, organized by **pattern**
(not difficulty), and which week we tackle it.

- Coding files: `striver/array/<pattern>/NN_problem.py` (docstring has the statement).
- Mistake notebook: one `NOTES.md` per pattern folder.
- Cross-week libraries: `striver/notes/{patterns,python_notes,interview_questions}.md`.

Rule: **one pattern per week.** Files get created the week we start the pattern,
so the repo never becomes a 50-item grind checklist.

---

## In scope now — Month 1 (files created)

### Week 1 — `array/arrays_hashing/`  (Hash Map / Set)
| # | Problem | LC | Diff |
|---|---------|----|------|
| 01 | Two Sum | 1 | Easy |
| 02 | Contains Duplicate | 217 | Easy |
| 03 | Group Anagrams | 49 | Medium |
| 04 | Top K Frequent Elements | 347 | Medium |
| 05 | Longest Consecutive Sequence | 128 | Medium |
| 06 | Subarray Sum Equals K | 560 | Medium |

### Week 2 — `array/two_pointers/`
| # | Problem | LC | Diff |
|---|---------|----|------|
| 01 | Valid Palindrome | 125 | Easy |
| 02 | Two Sum II (sorted) | 167 | Medium |
| 03 | 3Sum | 15 | Medium |
| 04 | Container With Most Water | 11 | Medium |
| 05 | Sort Colors (Dutch flag) | 75 | Medium |
| 06 | Trapping Rain Water | 42 | Hard (stretch) |

### Week 3 — `array/sliding_window/`
| # | Problem | LC | Diff |
|---|---------|----|------|
| 01 | Best Time to Buy and Sell Stock | 121 | Easy |
| 02 | Longest Substring Without Repeating | 3 | Medium |
| 03 | Longest Repeating Character Replacement | 424 | Medium |
| 04 | Max Consecutive Ones III | 1004 | Medium |
| 05 | Minimum Window Substring | 76 | Hard (stretch) |

### Week 4 — Review + first timed set (no new pattern)

---

## Full Striver A2Z "Array" sheet → pattern / when

The sheet is difficulty-sorted and spans Months 1–6. Mapped to our patterns:

| Striver problem | Our pattern | When |
|-----------------|-------------|------|
| Largest / Second Largest / Check sorted / Remove dup sorted / Move zeros / Linear search / Union of sorted / Leaders / Pascal's Triangle | array basics (warm-ups) | anytime |
| Left Rotate by One / by K places | array basics (reversal trick) | anytime |
| Two Sum | arrays_hashing | **Wk 1** |
| Longest Consecutive Sequence | arrays_hashing | **Wk 1** |
| Find missing number / Number appearing once (others twice) | arrays_hashing / bit (XOR) | **Wk 1** / M2 |
| Majority Element I & II | hashing → Moore's voting | **Wk 1** then M6 |
| Sort 0/1/2 (Dutch flag) | two_pointers | **Wk 2** |
| Rearrange array by sign | two_pointers | **Wk 2** |
| 3 Sum / 4 Sum | two_pointers | **Wk 2** |
| Merge two sorted arrays (no extra space) | two_pointers | **Wk 2** |
| Maximum Consecutive Ones | sliding_window | **Wk 3** |
| Longest subarray sum K (positives) | sliding_window | **Wk 3** |
| Stock Buy and Sell (one txn) | sliding_window / greedy | **Wk 3** |
| Longest subarray sum K (with negatives) | prefix_sum + hashmap | Month 2 |
| Count subarrays with given sum | prefix_sum + hashmap (= LC560) | Month 2 |
| Largest subarray with sum 0 | prefix_sum + hashmap | Month 2 |
| Count subarrays with given XOR K | prefix_sum (xor) + hashmap | Month 2 |
| Count Inversions / Reverse Pairs | merge-sort (divide & conquer) | Month 2 |
| Find repeating and missing number | math / hashing | Month 2 |
| Kadane's / Print max subarray / Maximum Product Subarray | DP (Kadane family) | Month 5 |
| Next Permutation | array manipulation (greedy) | Month 6 |
| Merge Overlapping Subintervals | intervals | Month 5 |
| Set Matrix Zeroes / Rotate 90° / Spiral matrix | matrix simulation | Month 6 |

---

## Later pattern folders (created the week we start them)

`prefix_sum/` · `binary_search/` · `linked_list/` · `stack_queue/` (+ monotonic) ·
`trees/` · `bst/` · `heap_top_k/` · (graphs & DP already exist) ·
`backtracking/` · `trie/` · `greedy/` · `intervals/` · `matrix/`.
