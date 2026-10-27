# Find a car by price in a list sorted by daily price.
def binary_search(cars, price):
    low = 0
    high = len(cars) - 1

    while low <= high:
        middle = (low + high) // 2
        current_price = cars[middle].daily_price

        if current_price == price:
            return cars[middle]
        elif current_price < price:
            low = middle + 1
        else:
            high = middle - 1

    return None