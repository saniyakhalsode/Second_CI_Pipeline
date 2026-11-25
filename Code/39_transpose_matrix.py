def transpose_matrix(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result