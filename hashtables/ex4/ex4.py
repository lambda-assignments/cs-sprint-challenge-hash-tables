
def has_negatives(a):
    pos = list()
    neg = list()
    arrays = [pos, neg]
    cache = dict()
    for i in a:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(abs(i))
    for a in arrays:
        for i in a:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
    return [i for i in cache if cache[i] == len(arrays)]

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
