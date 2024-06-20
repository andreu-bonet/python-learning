def list_comprehension(expression, iterable, condition):
    result = []
    for item in iterable:
        if condition(item):
            result.append(expression(item))
    return result


def multiplica_per_dos(x):
    return x * 3


def filtra_parells(x):
    return x % 2 == 0


def filtra_imparells(x):
    return x % 2 == 1


llista = [1, 2, 3, 4, 5, 6]

newlistEven = list_comprehension(multiplica_per_dos, llista, filtra_parells)
newlistOdd = [multiplica_per_dos(item) for item in llista if filtra_imparells(item)]

print(newlistEven)
print(newlistOdd)

# Python - List Comprehension https://www.w3schools.com/python/python_lists_comprehension.asp
# newlist = [expression for item in iterable if condition == True]
newlistEvenPro = [item * 2 for item in llista if item % 2 == 0]  # [4, 8, 12]
print(newlistEvenPro)
