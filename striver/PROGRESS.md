# PROGRESS — Resume Anchor

> **This is the single source of truth for "where are we."** A new chat reads
> this first. Coach: on session start, read this file + `../DSA_PREP.md` (method)
> and resume from "Right now". Update the status table + changelog at the END of
> every session.

## How to resume (what I, the user, type in a fresh chat)
> "Continue DSA prep" — then the coach reads this file and `../DSA_PREP.md`,
> states where we are, and picks up at the current open problem. No re-explaining.

## Source-of-truth files
- `../DSA_PREP.md` — mentor brief / coaching rules (governing doc).
- `SPRINT_PLAN.md` — cadence: sprints → weeks → daily loop → Definition of Done.
- `ROADMAP.md` — pattern → problem map (incl. full Striver array sheet).
- `notes/patterns.md`, `notes/mental_models.md`, `notes/python_notes.md`,
  `notes/interview_questions.md` — cross-week libraries.
- `array/<pattern>/NOTES.md` — per-week mistake notebooks.

---

## Right now
- **Sprint 1 — Arrays & Hashing. Week 1 — `arrays_hashing`.** In progress.
- **Open problem:** `03_group_anagrams.py` (not started) + fix bug in
  `05_longest_consecutive_sequence.py`.
- **Next problem after that:** review `04_top_k_frequent_elements.py` (older code,
  not yet reviewed), then Week 1 wrap-up.

## Week 1 status — `array/arrays_hashing/`
| # | Problem | Status | Notes |
|---|---------|--------|-------|
| 01 | Two Sum | ✅ done | optimal one-pass map; reviewed |
| 02 | Contains Duplicate | ✅ skipped | trivial for user (`len(set)!=len`) |
| 03 | Group Anagrams | ⬜ open | **current live problem** |
| 04 | Top K Frequent Elements | 🟡 code exists | older code, needs review |
| 05 | Longest Consecutive Sequence | 🟡 has bug | len-1 runs return 0; also O(n²) worst case — switch to start-detection (MM2) |
| 06 | Subarray Sum Equals K | ✅ done | prefix-sum + count map; reviewed, correct |

Legend: ✅ done · 🟡 in progress/needs work · ⬜ not started

## Pending follow-ups owed by user (discuss when back)
- Subarray Sum K: (1) fold prefix array into running total → O(1) extra space?
  (2) why can't sliding window be used here? (negatives)
- Longest Consecutive: fix the max-update bug; then convert to start-detection
  ("x is a start iff x-1 not in set") and delete the visited-flag bookkeeping.

---

## Changelog (newest first)
- **2026-06-27** — Repo coaching system set up: `striver/` reorganized by pattern,
  Month-1 files created (arrays_hashing, two_pointers, sliding_window), global
  `notes/`, `ROADMAP.md`, `SPRINT_PLAN.md`, this `PROGRESS.md`. Retired external
  GPT plan — this repo + `DSA_PREP.md` are now the only sources. Week 1 started:
  Two Sum ✅, Subarray Sum K ✅, Longest Consecutive (bug pending), Group Anagrams next.
