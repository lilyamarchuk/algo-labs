def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def can_feed(S, hamsters, count):
    if count == 0:
        return True
    costs = []
    for h in hamsters:
        cost = h[0] + h[1] * (count - 1)
        costs.append(cost)
    bubble_sort(costs)
    return sum(costs[:count]) <= S

def max_hamsters(S, C, hamsters):
    low = 0
    high = C
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if can_feed(S, hamsters, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result
