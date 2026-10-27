# Car Rental Data Structures and Algorithms

## Purpose

This educational project implements data structures and algorithms
using a car rental scenario.

It demonstrates storing cars, searching by plate or price,
sorting daily prices, recording rental history, managing actions
and handling requests in arrival order.

The modules demonstrate individual operations.
They are not yet an integrated booking application.

## Data structures

| Module | Structure | Role |
|---|---|---|
| car.py | Car class | Plate, brand, model, daily price and availability |
| car_array.py | Fixed-capacity array | Store up to 25 cars by default |
| rental_history.py | Singly linked list | Append and display rental records |
| action_stack.py | Stack | Store actions in LIFO order |
| rental_queue.py | Linked queue | Handle requests in FIFO order |
| binary_tree.py | Binary tree | Represent sample car categories |
| car_bst.py | Binary search tree | Insert and search cars by plate |
| car_avl.py | AVL tree | Insert and search cars with automatic balancing |
| car_hash_table.py | Hash table | Store cars by plate using separate chaining |

## Algorithms

sorting.py implements Bubble Sort, Insertion Sort and Merge Sort.
All three return a new list sorted by daily price.

searching.py implements Binary Search by daily price.
Its input must already be sorted in ascending price order.

CarArray implements Linear Search by plate.
CategoryTree provides in-order, pre-order and post-order traversals.
CarBST provides in-order traversal sorted by plate.
## Running the project

Python 3 is required. No third-party packages are needed.
Open a terminal in the project folder and run:

```bash
python main.py
```

Run all test files:

```bash
python run_tests.py
```

Run the performance comparisons:

```bash
python performance.py
python performance_tree.py
```

## Usage example

```python
from car import Car
from car_array import CarArray
from sorting import merge_sort

fleet = CarArray()
fleet.add(Car("ABC-123", "Toyota", "Yaris", 40))
fleet.add(Car("DEF-456", "Ford", "Focus", 50))

found = fleet.linear_search("ABC-123")
if found is not None:
    print(found.brand, found.model)

# Pass only occupied positions to the sorting algorithm.
cars = fleet.cars[:fleet.size]
ordered = merge_sort(cars)

for car in ordered:
    print(car.plate, car.daily_price)
```

## Reports

analysis.md contains complexity analysis and measured performance.
validation.md describes test coverage and results.

## Limitations

Data is held in memory and is lost when the program ends.
The project does not yet manage booking dates or prevent
overlapping reservations.

Car availability initially defaults to True; rental history records
do not automatically change availability.

BST, AVL and hash table insertion reject duplicate plates.
CarArray currently does not enforce unique plates.
## Design principles

Each structure is implemented in a separate module so it can be
tested and used independently. main.py demonstrates their use.

CarArray uses a Python list as fixed-capacity storage.
Insertion fills the next free position. Removal shifts later
elements left and clears the unused final position.

RentalHistory links records through next pointers.
A tail pointer allows records to be appended in O(1) time.

ActionStack uses append and pop at the end of a Python list.
RentalQueue uses linked nodes with front and rear pointers.

CategoryTree allows up to two children per node.
It has no ordering rule. CarBST instead orders nodes by plate.

CarAVL follows the BST ordering rule and stores node heights.
Single or double rotations restore balance after insertion.

CarHashTable adds character codes and takes the remainder modulo 25.
Colliding plates share a bucket, which is searched sequentially.

The sorting algorithms return new lists and preserve input order
in the original list. Binary Search repeatedly halves its search
range and therefore requires input sorted by daily price.