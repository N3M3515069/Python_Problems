def move_zeros(lst):
    
    counter = []
    for i in lst:
        if i != 0:
            counter.append(i)   
    for j in lst:
        if j == 0:
            counter.append(j)
    return counter


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))