# Python Interview Snippets

Fast, idiomatic Python for interviews. Reach for these instead of reinventing.

## Frequency map
```python
from collections import Counter, defaultdict

freq = Counter(nums)              # {val: count}
freq.most_common(k)               # k most common as [(val, count), ...]

freq = defaultdict(int)
for x in nums: freq[x] += 1       # no KeyError

# without imports:
freq[x] = freq.get(x, 0) + 1
```

## Enumerate / zip
```python
for i, val in enumerate(nums):
    ...
for a, b in zip(list1, list2):
    ...
```

## Sets
```python
seen = set()
seen.add(x); x in seen            # O(1)
unique = set(nums)
len(set(nums)) != len(nums)       # has duplicate?
```

## Heap (min-heap by default)
```python
import heapq
heap = []
heapq.heappush(heap, (priority, item))
priority, item = heapq.heappop(heap)
heapq.heapify(arr)                # in place, O(n)
heapq.nlargest(k, nums)           # top-k
# Max-heap: push negatives, negate on pop.
```

## Walrus (assign in condition) — clean one-pass
```python
if (comp := target - x) in seen:
    return [seen[comp], i]
```

## Canonical keys for grouping (MM1)
```python
key = tuple(sorted(s))            # anagram key, O(k log k)
cnt = [0] * 26                    # faster anagram key, O(k)
for c in s: cnt[ord(c) - 97] += 1
key = tuple(cnt)
```

## Misc
```python
float('inf'), float('-inf')       # sentinels for min/max
nums.sort()                       # in place; sorted(nums) returns new
a, b = b, a                       # swap, no temp
res[::-1]                         # reverse
divmod(a, b)                      # (a//b, a%b)
```
