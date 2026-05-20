def build_transition_table(needle):
    m = len(needle)
    alphabet = set(needle)
    table = [{} for _ in range(m + 1)]

    for state in range(m + 1):
        for char in alphabet:
            k = min(m, state + 1)
            while k > 0:
                if (needle[:state] + char).endswith(needle[:k]):
                    break
                k -= 1
            table[state][char] = k

    return table


def fa_search(haystack, needle):
    if not needle:
        return []

    m = len(needle)
    n = len(haystack)
    table = build_transition_table(needle)
    state = 0
    indices = []

    for i in range(n):
        char = haystack[i]
        state = table[state].get(char, 0)
        if state == m:
            indices.append(i - m + 1)

    return indices
