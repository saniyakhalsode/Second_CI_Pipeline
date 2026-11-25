def move_zeros(arr):
    non_zeros = [num for num in arr if num != 0]
    zeros = [num for num in arr if num == 0]
    return non_zeros + zeros