# Sort cars by daily price using Bubble Sort.
def bubble_sort(cars):
    result = cars.copy()

    for i in range(len(result) - 1):
        swapped = False

        for j in range(len(result) - 1 - i):
            if result[j].daily_price > result[j + 1].daily_price:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:
            break

    return result

# Sort cars by daily price using Insertion Sort.
def insertion_sort(cars):
    result = cars.copy()

    for i in range(1, len(result)):
        current = result[i]
        j = i - 1

        while j >= 0 and result[j].daily_price > current.daily_price:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current

    return result
# Sort cars by daily price using Merge Sort.
def merge_sort(cars):
    if len(cars) <= 1:
        return cars.copy()

    middle = len(cars) // 2
    left = merge_sort(cars[:middle])
    right = merge_sort(cars[middle:])

    result = []
    i = 0
    j = 0

    # Merge the two sorted halves.
    while i < len(left) and j < len(right):
        if left[i].daily_price <= right[j].daily_price:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result