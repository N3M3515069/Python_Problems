"""Your task is to write function factorial.

https://en.wikipedia.org/wiki/Factorial"""


def factorial(n):
    counter = 1
    for i in range(1, n + 1):
        counter = counter * i
    return counter
