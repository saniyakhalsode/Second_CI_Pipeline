def find_missing_number(arr):
    n = len(arr)
    result = 0

    for i in range(n + 1):
        result ^= i

    for num in arr:
        result ^= num

    return result