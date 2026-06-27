# Master Pattern Library

The reusable, cross-week reference. Each time we finish a pattern we append:
recognition clues, mental model, template, complexity, example problems.

Mistakes go in each week's `NOTES.md`; durable *ideas* go here.

---

## Mental Models

Angle-of-attack questions that sit *above* patterns live in their own file:
see **`mental_models.md`** (MM1 Canonical Representation, MM2 Sequence Expansion,
MM3 Lookup Pattern, MM4 Problem Transformation). Patterns below reference them.

---

## Pattern: Hash Map / Hash Set        [Week 1]

### Recognition clues
- You want a nested loop to find a partner / complement / duplicate.
- Question is about membership ("exists?"), counting ("how many?"), or
  grouping ("which share a key?"). Order doesn't matter; identity does.

### Templates
```python
# 1. "Seen before": value -> info (often index)
seen = {}
for i, x in enumerate(arr):
    if needed(x) in seen:
        ...
    seen[x] = i

# 2. Group by a derived/canonical key (MM1)
from collections import defaultdict
groups = defaultdict(list)
for x in arr:
    groups[key(x)].append(x)
```

### Complexity
O(n) time, O(n) space (amortized O(1) lookup/insert).

### Example problems
Two Sum, Contains Duplicate, Group Anagrams, Top-K Frequent,
Longest Consecutive Sequence, Subarray Sum = K (prefix-sum + map).

---

## Pattern: Two Pointers              [Week 2]

### Recognition clues
- Array is sorted (or sorting is harmless); looking for a pair/triplet by sum.
- "In-place", "O(1) space", "without extra array".
- Palindrome / converging-from-both-ends checks.

### Templates
```python
# Converging
l, r = 0, len(a) - 1
while l < r:
    s = a[l] + a[r]
    if s == target: ...
    elif s < target: l += 1
    else: r -= 1

# Fast/slow or same-direction (partitioning, dedupe in place)
```

### Complexity
O(n) (after an O(n log n) sort if needed); usually O(1) extra space.

### Example problems
Valid Palindrome, Two Sum II, 3Sum/4Sum, Container With Most Water,
Sort Colors (Dutch flag), Trapping Rain Water.

---

## Pattern: Sliding Window            [Week 3]

### Recognition clues
- "longest/shortest/contains" over a CONTIGUOUS subarray/substring.
- A constraint that monotonically breaks as the window grows
  (distinct chars, at-most-k zeros, sum >= target with non-negatives).
- TRAP: needs non-negative contributions. "Subarray sum = k" with negatives
  is prefix-sum + hashmap, NOT a window.

### Template
```python
left = 0
for right in range(len(a)):
    include(a[right])
    while window_invalid():
        exclude(a[left]); left += 1
    best = max(best, right - left + 1)
```

### Complexity
O(n) (each index enters and leaves the window at most once).

### Example problems
Best Time to Buy/Sell Stock, Longest Substring Without Repeating,
Longest Repeating Character Replacement, Max Consecutive Ones III,
Minimum Window Substring.
