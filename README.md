# NeetCode — Algorithms & Data Structures for Beginners

My Python solutions to the [**Algorithms and Data Structures for Beginners**](https://neetcode.io/courses/dsa-for-beginners) course on NeetCode.

Each topic from the course has its own directory, numbered to follow the course order.

## Topics

| #  | Topic                  | Directory                  |
|----|------------------------|----------------------------|
| 01 | Arrays                 | [`01_arrays`](01_arrays)                         |
| 02 | Linked Lists           | [`02_linked_lists`](02_linked_lists)             |
| 03 | Recursion              | [`03_recursion`](03_recursion)                   |
| 04 | Sorting                | [`04_sorting`](04_sorting)                       |
| 05 | Binary Search          | [`05_binary_search`](05_binary_search)           |
| 06 | Trees                  | [`06_trees`](06_trees)                           |
| 07 | Backtracking           | [`07_backtracking`](07_backtracking)             |
| 08 | Heap / Priority Queue  | [`08_heap_priority_queue`](08_heap_priority_queue) |
| 09 | Hashing                | [`09_hashing`](09_hashing)                       |
| 10 | Graphs                 | [`10_graphs`](10_graphs)                         |
| 11 | Dynamic Programming    | [`11_dynamic_programming`](11_dynamic_programming) |
| 12 | Bit Manipulation       | [`12_bit_manipulation`](12_bit_manipulation)     |

## Structure

```
neetcode-dsa/
├── 01_arrays/
├── 02_linked_lists/
├── 03_recursion/
├── 04_sorting/
├── 05_binary_search/
├── 06_trees/
├── 07_backtracking/
├── 08_heap_priority_queue/
├── 09_hashing/
├── 10_graphs/
├── 11_dynamic_programming/
└── 12_bit_manipulation/
```

## Conventions

A few habits that keep the collection easy to navigate as it grows:

- **One problem per file**, named after the problem in `snake_case` — e.g. `two_sum.py`, `valid_palindrome.py`.
- **Document the approach at the top** of each file with a short docstring: the problem, a link, and the time/space complexity.

  ```python
  """
  Two Sum — https://leetcode.com/problems/two-sum/

  Given an array of integers, return indices of the two numbers
  that add up to a target.

  Time:  O(n)
  Space: O(n)
  """
  ```

- **Make files runnable** with a quick sanity check so you can verify a solution on the spot:

  ```python
  if __name__ == "__main__":
      assert two_sum([2, 7, 11, 15], 9) == [0, 1]
      print("ok")
  ```

## Running

```bash
python 01_arrays/two_sum.py
```

## Progress

- [x] Arrays
- [ ] Linked Lists
- [ ] Recursion
- [ ] Sorting
- [ ] Binary Search
- [ ] Trees
- [ ] Backtracking
- [ ] Heap / Priority Queue
- [ ] Hashing
- [ ] Graphs
- [ ] Dynamic Programming
- [ ] Bit Manipulation
