def load_data(path):
    objects = []
    with open(path, "r") as f:
        n, m = map(int, f.readline().split(' '))
        reference = list(map(int, f.readline().split(' ')))
        for i in range(n):
            obj = list(map(int, f.readline().split(' ')))
            objects.append(obj)

    return objects, reference
