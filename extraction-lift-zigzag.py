def evacuation_elevator():
    try:
        r_count = int(input("enter rows: "))
        c_count = int(input("enter columns: "))
    except ValueError:
        return

    matrix = []
    for i in range(r_count):
        row = list(map(int, input(f"elements of row {i + 1}: ").split()))
        matrix.append(row)

    total_rows = len(matrix)
    total_cols = len(matrix[0])

    scan_step = 0
    total_evacuated = 0

    for d_sum in range(total_rows + total_cols - 1):
        if d_sum % 2 != 0:
            row_i = 0 if d_sum < total_cols else d_sum - total_cols + 1
            while row_i < total_rows and (d_sum - row_i) >= 0:
                people = matrix[row_i][d_sum - row_i]
                scan_step += 1
                total_evacuated += people
                print(f"step {scan_step}: picked up {people} people (total: {total_evacuated})")
                row_i += 1
        else:
            col_i = 0 if d_sum < total_rows else d_sum - total_rows + 1
            while col_i < total_cols and (d_sum - col_i) >= 0:
                people = matrix[d_sum - col_i][col_i]
                scan_step += 1
                total_evacuated += people
                print(f"step {scan_step}: picked up {people} people (total: {total_evacuated})")
                col_i += 1

    print(f"\nevacuation finished. total people: {total_evacuated} in {scan_step} steps.")

if __name__ == "__main__":
    evacuation_elevator()
