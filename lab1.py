def zigzag_traversal(matrix):
    if not matrix or not matrix[0]:
        return []

    total_rows = len(matrix)
    total_cols = len(matrix[0])
    result = []

    for diagonal_sum in range(total_rows + total_cols - 1):
        if diagonal_sum % 2 != 0:
            if diagonal_sum < total_cols:
                row_index = 0
            else:
                row_index = diagonal_sum - total_cols + 1

            while row_index < total_rows and (diagonal_sum - row_index) >= 0:
                result.append(matrix[row_index][diagonal_sum - row_index])
                row_index += 1
        else:
            if diagonal_sum < total_rows:
                col_index = 0
            else:
                col_index = diagonal_sum - total_rows + 1

            while col_index < total_cols and (diagonal_sum - col_index) >= 0:
                result.append(matrix[diagonal_sum - col_index][col_index])
                col_index += 1

    return result