def most_frequent(arr):
    if not arr:
        return None

    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    return max(frequency, key=frequency.get)