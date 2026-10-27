import random
from statistics import median
from time import perf_counter

from car import Car
from sorting import bubble_sort, insertion_sort, merge_sort


# Create repeatable sample cars for performance measurements.
def create_cars(count):
    generator = random.Random(42)

    return [
        Car(
            f"CAR-{i:05d}",
            "Toyota",
            "Yaris",
            generator.randint(20, 150),
        )
        for i in range(count)
    ]


# Compare three input orders at each size.
for count in [25, 100, 500]:
    original = create_cars(count)

    cases = {
        "Random": original,
        "Sorted": sorted(original, key=lambda car: car.daily_price),
        "Reversed": sorted(
            original, key=lambda car: car.daily_price, reverse=True
        ),
    }

    for label, cars in cases.items():
        expected = sorted(car.daily_price for car in cars)
        print(f"\nCars: {count} | Order: {label}")

        for algorithm in [bubble_sort, insertion_sort, merge_sort]:
            times = []

            # Measure five runs on the same input.
            for repeat in range(5):
                start = perf_counter()
                result = algorithm(cars)
                elapsed = perf_counter() - start

                # Check correctness outside the timed section.
                assert [car.daily_price for car in result] == expected
                times.append(elapsed)

            milliseconds = median(times) * 1000
            print(f"{algorithm.__name__}: {milliseconds:.4f} ms")