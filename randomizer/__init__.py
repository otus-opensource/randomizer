import random


def choose(items, seed, max_count=None, rounds=64):
    random.seed(seed)
    count = len(items)

    temp = [None for _ in range(count)]

    for _ in range(rounds):
        for i in range(count):
            j = random.randint(0, i)
            temp[i] = temp[j]
            temp[j] = items[i]

        items = list(temp)
        temp = [None for _ in range(count)]

    if max_count is not None:
        return items[:max_count]

    return items
