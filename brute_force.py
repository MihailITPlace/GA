import utils

objects, reference = utils.load_data("input.txt")
n = len(objects)


def bitfield(i):
    return [int(digit) for digit in bin(i)[2:]]


def target_function(chromosome):
    error = 0
    for i, gen in enumerate(chromosome):
        if gen == 0:
            continue

        for j, o in enumerate(objects[i]):
            error += (abs(o - reference[j]))

    return error / 10


res = []
for i in range(1, 2**n+1):
    bits = bitfield(i)
    arr = [0] * (n - len(bits)) + bits
    res.append(arr)

arg_min = None
min = 10000
for i in res:
    if min > target_function(i):
        min = target_function(i)
        arg_min = i

print(arg_min, min)