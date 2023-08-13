def find_it(seq):

    for i in seq:
        counter = seq.count(i)
        if not counter % 2 == 0:
            return i


print(find_it([0, 0, 1, 1, 1, 1, 5, 5, 5]))
