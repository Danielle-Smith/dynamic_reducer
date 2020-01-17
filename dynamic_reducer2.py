#changed import functools and called functools.reduce instead of - from functools import reduce and just calling reduce
import operator
import functools

def dynamic_reducer(collection, op):
    #dictionary to recall later
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    return functools.reduce((lambda total, element: operators[op](total, element)), collection)

print(dynamic_reducer([1, 2, 3], '+'))
print(dynamic_reducer([1, 2, 3], '-'))
print(dynamic_reducer([1, 2, 3], '*'))
print(dynamic_reducer([1, 2, 3], '/'))
