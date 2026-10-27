# Testing and Validation Report

## Method

Tests use Python assert statements to compare actual and expected results.
Expected errors are checked with try/except blocks.

Run all test files with:

python run_tests.py

The completed run reported: All 10 test files passed.
This counts test files, not individual assertions.

## Test coverage

| Test file | Scenarios checked | Result |
|---|---|---|
| test_car_array.py | Empty array, insertion, search, removal, shifting, capacity limit, reuse of space | PASS |
| test_sorting.py | Empty, single-item, random, sorted, reversed and repeated-price inputs; original order preserved | PASS |
| test_searching.py | Empty and single-item lists; first, middle and last prices; missing prices | PASS |
| test_rental_history.py | Empty history, first record, links between records, tail pointer, displayed output | PASS |
| test_action_stack.py | Empty stack, LIFO order, return to empty state | PASS |
| test_rental_queue.py | Empty queue, FIFO order, pointer reset, reuse | PASS |
| test_binary_tree.py | Three traversal orders and an empty tree | PASS |
| test_car_bst.py | Empty search, insertion positions, existing and missing plates, duplicate rejection, in-order traversal | PASS |
| test_car_avl.py | Four rotation cases, search, empty tree, duplicate rejection, balance and heights with 25 cars | PASS |
| test_car_hash_table.py | Empty search, collisions, existing and missing plates, duplicate rejection | PASS |

## Interpretation and limitations

All tested scenarios passed.
Performance scripts also checked their outputs outside the timed sections.

Passing these tests supports correctness for the tested scenarios.
It does not prove correctness for every possible input.
Validation of invalid prices, rental durations and customer details
is not covered by the current tests.