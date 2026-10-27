# Performance Analysis

## Measurement method

Sorting algorithms were tested with 25, 100 and 500 cars.
Inputs were random, sorted or in reverse price order.
All algorithms received the same input for each comparison.

Data preparation and correctness checks were outside the timed section.
Each algorithm was measured five times using perf_counter().
The reported time is the median, in milliseconds.

These measurements describe performance on the test computer.
They do not establish that one algorithm is always faster.

## Sorting complexity

Let n be the number of cars.

| Algorithm | Best time | Average time | Worst time | Extra space in our implementation |
|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(n) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |

Bubble Sort stops early when a pass makes no swaps.
Insertion Sort needs little work when the input is already sorted.
Merge Sort repeatedly divides the input and merges the sorted halves.

All three implementations preserve the original list.
Bubble Sort and Insertion Sort use O(n) extra space because they
copy the input. Their sorting steps alone need O(1) extra space.
Merge Sort uses additional lists and an O(log n) recursion stack.
Space complexity here is theoretical, not measured memory usage.
## Sorting results

Times are median milliseconds from five runs.

| Cars | Input order | Bubble Sort | Insertion Sort | Merge Sort |
|---|---|---|---|---|
| 25 | Random | 0.0262 | 0.0118 | 0.0566 |
| 25 | Sorted | 0.0037 | 0.0026 | 0.0205 |
| 25 | Reversed | 0.0311 | 0.0235 | 0.0224 |
| 100 | Random | 0.3617 | 0.1681 | 0.1284 |
| 100 | Sorted | 0.0129 | 0.0244 | 0.1069 |
| 100 | Reversed | 0.5680 | 0.4363 | 0.1217 |
| 500 | Random | 11.3631 | 5.2355 | 0.8288 |
| 500 | Sorted | 0.0738 | 0.1193 | 0.6026 |
| 500 | Reversed | 14.4887 | 10.0530 | 0.6210 |

Insertion Sort was fastest for 25 cars with random or sorted prices.
Merge Sort was fastest for random and reversed inputs at 100 and
500 cars. Bubble Sort was fastest for sorted inputs at those sizes
because it stopped after its first pass.

The results support choosing an algorithm according to input size
and order. Small timing differences should be interpreted cautiously.
## Tree traversal analysis

Balanced binary trees with 25, 100 and 500 nodes were tested.
Each traversal was measured in five batches of 100 calls.
Batch time was divided by 100, and the median was reported.
Tree construction and correctness checks were outside the timed section.

| Nodes | In-order (ms) | Pre-order (ms) | Post-order (ms) |
|---|---|---|---|
| 25 | 0.0038 | 0.0042 | 0.0042 |
| 100 | 0.0134 | 0.0139 | 0.0124 |
| 500 | 0.0704 | 0.0646 | 0.0648 |

All three traversals visit every node once, giving O(n) time.
No traversal was consistently fastest across the tested sizes.
Their main difference is the order in which nodes are visited.

The recursion stack uses O(h) space, where h is tree height:
O(log n) for a balanced tree and O(n) for a skewed tree.
Our implementations also return a list containing all n results,
so total extra space is O(n).

Only balanced trees were benchmarked. Results do not describe
performance on skewed trees.