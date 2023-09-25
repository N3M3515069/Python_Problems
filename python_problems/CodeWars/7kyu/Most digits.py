"""Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array."""


def find_longest(arr):
    counter = []
    for i in arr:
        if len(str(i)) == len(str(max(arr))):
            counter.append(str(i))
    return int(counter[0])
