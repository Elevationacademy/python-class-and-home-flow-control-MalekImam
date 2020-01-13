def sum(a, b):
    return a + b


def my_reduce(operation, l_reduce):
    if not l_reduce:
        return None
    result = l_reduce[0]
    for i in range(1, len(l_reduce)):
        result = operation(result, l_reduce[i])
    return result


list_reduce = [1, 2, 3, 4, 5]
print(my_reduce(sum, list_reduce))

# example of lambda
# ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
# print(sorted(ids, key=lambda x: int(x[2:])))
