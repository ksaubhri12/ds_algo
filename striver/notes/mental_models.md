# Mental Models

The questions you ask *before* you've picked a pattern. These sit ABOVE patterns:
a mental model points you at a pattern; a pattern points you at a data structure.
In an interview, narrate the model out loud — it's how you show structured thinking.

---

## MM1 — Canonical Representation
> **How do I make equivalent objects look identical?**
- Sort the string; build a 26-length frequency vector; normalize email/case.
- Objects with the same signature go in the same bucket.
- **Used by:** Group Anagrams, Valid Anagram, Accounts Merge, email normalization.

## MM2 — Sequence Expansion
> **Does every element need to start a sequence, or is there a unique start?**
- Expand only from a true start (e.g. x is a start iff `x-1` not in the set).
- This is what turns O(n²) re-walks into a clean O(n).
- **Used by:** Longest Consecutive Sequence, Interval Merging, Graph Components.

## MM3 — Lookup Pattern
> **Can this become "have I already seen X?"**
- Two Sum → need `target - current`.
- Subarray Sum = K → need `currentPrefix - k`.
- The trick is naming *what* to look up; the hashmap does the rest in O(1).

## MM4 — Problem Transformation
> **Can I convert this into a simpler, known problem?**
- Top-K Frequent → count frequencies → "top-K of these counts" (heap/bucket).
- Subarray Sum = K → prefix sum → MM3 lookup pattern.
- **Habit:** name the subproblem first, THEN choose the data structure — never
  the reverse. Say it in the room: *"First I build a freq map; now it's 'find
  top-K of these counts,' which suggests a heap."*

---

> Add a new model the moment a problem teaches one. The recognition reflex you're
> building for interviews lives in this file more than in any single solution.
