def josephus(items, k):
    if not items:
        return []

    result = []
    idx = 0

    while items:
        idx = (idx + k - 1) % len(items)
        result.append(items.pop(idx))

    return result