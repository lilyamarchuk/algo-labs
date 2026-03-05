def radix_sort(arr):
    if not arr:
        return arr

    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        exp *= 10
    return arr

def can_feed(S, hamsters, count):
    if count == 0:
        return True
    costs = []
    for h in hamsters:
        cost = h[0] + h[1] * (count - 1)
        costs.append(cost)
    costs = radix_sort(costs)
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