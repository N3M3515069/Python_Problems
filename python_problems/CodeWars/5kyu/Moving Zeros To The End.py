'''Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.'''

def move_zeros(lst):
    
    counter = []
    for i in lst:
        if i != 0:
            counter.append(i)   
    for j in lst:
        if j == 0:
            counter.append(j)
    return counter