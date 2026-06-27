# Interview Follow-up Questions

Every follow-up we discuss, with the pattern it points to. Interviewers probe
with these to test depth — pre-loading them trains the recognition reflex.

---

## Two Sum
- **Return all pairs?** -> current code returns first only; need to keep
  scanning + handle duplicate pairs.
- **Array is sorted?** -> Two Pointers, O(1) extra space (vs O(n) map).
- **Streaming data?** -> Design + HashMap (add/find as numbers arrive).

## Group Anagrams
- **Key choice: sorted-string vs char-count tuple?** -> trade O(k log k) per
  word vs O(k); count-tuple wins for long words.
- **Unicode, not just a-z?** -> count-array of 26 breaks; use Counter/sorted.

## Top K Frequent
- **O(n) without a heap?** -> Bucket sort by frequency (freq in [1, n]).
- **k == 1?** -> single pass max; no heap needed.
- **k == #unique?** -> just return all keys; heap is wasted work.

## Longest Consecutive Sequence
- **Why is a visited set unnecessary?** -> only sequence-starts expand, so
  each number is walked at most once.
- **Can every element start a sequence?** -> no; only x with (x-1) absent.

## Sliding Window (general)
- **Why doesn't this work with negative numbers?** -> growing the window no
  longer monotonically increases the sum; use prefix-sum + hashmap.
- **At most k vs exactly k distinct?** -> exactly_k = atMost(k) - atMost(k-1).
