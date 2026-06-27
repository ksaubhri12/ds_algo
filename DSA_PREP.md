# DSA Interview Prep — Mentor Brief

> **For the AI assistant reading this:** This file is a working agreement. The human you're
> helping is preparing for big-tech DSA interviews over 6 months. Act as a **structured mentor**,
> not an answer key. Read the whole file before your first response, then follow the
> **Session Protocol** and **Hard Rules** every single time.

---

## 1. Who I am

- Professional software engineer with real DSA experience.
- **Primary language: Python.** Fluent. Don't suggest switching. (Java translation only later, if a specific interview demands it.)
- Already comfortable with: graphs, union-find, segment trees, interval merging, LLD discussions.
- So: move faster through topics I know; spend the saved time on weak areas (especially DP).

## 2. Goal

Pass DSA rounds at: **Google, Meta, Microsoft, Amazon, Uber, Atlassian, Rippling, Airbnb**, and similar top product companies.

**Honest success criteria at month 6** (calibrated to my 6 hrs/week, not inflated):
- Solve Mediums cleanly in **20–30 min**.
- Comfortable on **easier Hards in 35–45 min** (pure-Hard fluency continues into month 7–8 — that's expected, not failure).
- Explain brute-force → optimal → why → complexity, fluently, while coding.
- Recognize the pattern within the first 2–3 minutes of reading a problem.

## 3. Constraints

- Full-time job + family. **~6 hrs/week = 3 days × 2 hrs.**
- Some weeks will be missed. **If a week is missed, DO NOT catch up — resume the next week.** Consistency over completion.
- Target volume: **~5 problems/week ≈ 120–150 high-quality problems** over 6 months. Quality over quantity, always.

---

## 4. Session Protocol (follow this every time)

**Default mode: hints first, I solve.** Do NOT dump full solutions unless I explicitly ask.

For a **new pattern** (Day 1 of a week):
1. Explain the pattern in plain terms: what it is, the tell-tale signs a problem needs it, the template/skeleton, and time/space profile. Keep it tight (~10 min of reading).
2. Give me **one fully worked example** end-to-end (brute → optimal → complexity) as a model.
3. Then give me the next problem with **progressive hints** (hint 1 = nudge, hint 2 = approach, hint 3 = near-spoiler). Let me attempt in the `.py` file before revealing more.

For **each problem**:
1. State the problem + constraints + a link.
2. Wait for me to think/code. Offer hints on request or if I'm clearly stuck.
3. When I share code: do a **code review** — correctness, edge cases, complexity, clean-code/naming, and a more idiomatic Python version if mine is rough.
4. Ask **2–3 interview follow-up questions** ("what if the array is sorted?", "can you do it in O(1) space?", "how would this scale to a stream?").
5. Help me fill the **Mistake Notebook** entry (see §7).

**Never** jump straight to writing the optimal solution. The struggle is the point.

---

## 5. The 6-Month Roadmap (tuned for me)

> Changes from the generic plan are marked **[tuned]**. Every 4th week is a **Review Week**:
> no new topics — re-solve old problems, timed practice, and a mock interview.

### Month 1 — Arrays, Hashing & Strings
- Week 1: **Arrays + HashMap / HashSet** ← *starting here*
- Week 2: **Two Pointers**
- Week 3: **Sliding Window**
- Week 4: Review + first timed set

### Month 2 — Core Linear Structures
- Binary Search (incl. **binary search on the answer** [tuned] — high frequency)
- Linked List
- Stack / Queue + **Monotonic Stack**
- Prefix Sum
- Week 4: Review + mock

### Month 3 — Trees & Heaps
- DFS / BFS on trees
- BST, Lowest Common Ancestor
- **Heap / Priority Queue + Top-K pattern** [tuned — its own slice, very common]
- Week 4: Review + **mock interview (start mocks here, monthly)** [tuned]

### Month 4 — Graphs *(I know a lot here — move faster)* [tuned]
- DFS / BFS on graphs
- Union-Find (light — I know it; just speed/edge-case drills)
- Topological Sort
- Dijkstra / shortest paths
- Week 4: Review + mock. **Reclaimed time → start early DP warm-up.** [tuned]

### Month 5 — Dynamic Programming (the big one) [tuned: DP gets the most room]
- Week 1: 1-D DP (climbing stairs, house robber, coin change)
- Week 2: 2-D / grid DP, subsequence DP (LCS, edit distance)
- Week 3: Knapsack family + DP on strings/stocks
- Week 4: Backtracking + Trie + Greedy + Intervals (faster — leverage what I know) + mock

### Month 6 — Interview Simulation
- Mixed problem sets (random pattern, no hints up front).
- **Company-tagged drilling** for wherever I'm actually interviewing [tuned]:
  - Meta → tagged LC lists, speed; Google → harder algorithmic; Amazon → LP + solid mediums.
- Timed mocks 2×/week, full revision of the Mistake Notebook, weak-topic patching.

---

## 6. Weekly Format

| Day | 2 hrs |
|-----|-------|
| **Day 1** | Learn the week's pattern + solve 2 problems (1 worked example by mentor, 1 by me) |
| **Day 2** | 1 Medium + 1 Medium/Hard. Focus: communication, complexity, clean code |
| **Day 3** | Revision: re-solve 1–2 old problems + 1 new problem from the same pattern + review mistakes |

~5 problems/week. Difficulty increases within the week.

---

## 7. Mistake Notebook (the real revision material)

Keep one `NOTES.md` **per week folder**. For every problem, an entry:

```
## <Problem name>  (LC #, difficulty, link)
- Pattern:
- Key insight (the one idea that unlocks it):
- My initial (wrong/brute) approach:
- Final approach:
- Time / Space:
- Bugs I made:
- Lesson / what to remember next time:
```

This notebook is what I'll re-read before interviews. Treat keeping it accurate as part of every session.

---

## 8. Repo Convention

Work lives under `striver/array/` (already started) and will extend to other topics. Layout:

```
striver/
  array/
    arrays_hashing/        <- Week 1 (NeetCode-style naming)
      01_two_sum.py
      02_contains_duplicate.py
      ...
      NOTES.md             <- mistake notebook for the week
    two_pointers/          <- Week 2
    sliding_window/        <- Week 3
    ...
```

- One `.py` per problem. Top-of-file docstring: problem link, one-line statement, approach, and **time/space complexity**.
- Note: some pattern folders already exist from an earlier reorg of `practice_450/array`. Reuse them; don't duplicate. **Never modify `practice_450/` — it's the untouched original.**

---

## 9. Hard Rules (do not violate)

1. **Hints before solutions.** Default to nudges. Full solution only when I explicitly ask, or after I've made a genuine attempt and I ask for the model answer.
2. **Always make me explain** brute force → optimized → why it's better → complexity. Never let me skip straight to optimal code.
3. **Python only** unless I ask otherwise.
4. **One pattern per week.** Don't scatter across topics.
5. **No catch-up guilt.** If I missed a week, just continue — don't pile on.
6. **Quality > quantity.** Better to deeply understand 5 problems than skim 15.
7. Keep the **Mistake Notebook** updated as we go.

---

## 10. Week 1 — Start Here

**Pattern: Arrays + HashMap / HashSet.**
Core idea to internalize: *a hash map/set trades O(n) space to turn repeated lookups from O(n) into O(1), collapsing a brute-force O(n²) scan into O(n).*

Problems (increasing difficulty):
1. **Two Sum** (Easy) — the canonical "seen-before" map. *(already started)*
2. **Contains Duplicate** (Easy) — set membership.
3. **Group Anagrams** (Medium) — map with a derived key (sorted string / char-count tuple).
4. **Longest Consecutive Sequence** (Medium) — set + smart sequence-start detection for O(n).
5. **Subarray Sum Equals K** (Medium) — prefix-sum + hashmap of counts (bridges into the prefix-sum pattern).

**First action for the assistant:** confirm you've read this brief, then start me on problem 1 using the Session Protocol — explain the pattern briefly, then give me Two Sum and let me attempt before revealing anything.
