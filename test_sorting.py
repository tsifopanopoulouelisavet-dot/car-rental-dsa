from car import Car
from sorting import bubble_sort, insertion_sort, merge_sort

# Test different price lists with all three algorithms.
cases = [
    [],
    [40],
    [50, 35, 40],
    [35, 40, 50],
    [50, 40, 35],
    [40, 35, 40, 35],
]

for algorithm in [bubble_sort, insertion_sort, merge_sort]:
    for prices in cases:
        cars = [
            Car(f"CAR-{i}", "Toyota", "Yaris", price)
            for i, price in enumerate(prices)
        ]

        result = algorithm(cars)

        assert [car.daily_price for car in result] == sorted(prices)
        assert [car.daily_price for car in cars] == prices

    print(algorithm.__name__, "tests: PASS")